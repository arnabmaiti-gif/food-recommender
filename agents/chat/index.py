"""
Claude Agent SDK chat handler — EdgeOne Makers agent-python format.

Route: POST /chat
Response: SSE stream (text/event-stream)

SSE event protocol:
  event: text_delta  data: {"delta": "..."}
  event: tool_called data: {"tool": "ToolName"}
  event: image       data: {"imageId": "...", "base64": "...", "mimeType": "...", "size": ...}
  event: ping        data: {"ts": 1710000000000}
  event: error       data: {"message": "..."}
  event: done        data: {"stopped": false}

Session persistence:
  Uses ctx.store to save user/assistant messages for /history recovery.

Tools:
  EdgeOne platform sandbox tools (commands/files/code_interpreter/browser)
  bridged via Claude SDK's MCP Server mechanism.
"""

from __future__ import annotations

import asyncio
import os
import time
from typing import Any, AsyncGenerator
from uuid import UUID

from dotenv import load_dotenv

load_dotenv()

try:
    from claude_agent_sdk import (
        ClaudeAgentOptions,
        create_sdk_mcp_server,
        query,
    )
    _SDK_AVAILABLE = True
except ImportError:
    _SDK_AVAILABLE = False

from .._model import collect_gateway_env, resolve_model_name
from .._logger import create_logger
from ._stream import (
    StreamState,
    iter_query_messages,
    sanitize_assistant_text,
    sdk_message_to_sse,
    sse_event,
)


logger = create_logger("chat")
HEARTBEAT_INTERVAL_S = 5
MCP_SERVER_NAME = "edgeone"

SYSTEM_PROMPT = """\
You are TasteBud — a personal food concierge built with the Claude Agent SDK (Python) on EdgeOne Makers.
You help ONE regular user decide where to eat by combining (a) what they are asking for right now, \
(b) their preset requirements, and (c) the patterns hidden in their past orders and feedback.

## Your knowledge base (the food-concierge project skill)
Everything you know about this user lives in `.claude/skills/food-concierge/`:
- SKILL.md                      — the recommendation method to follow
- references/profile.json       — preset requirements: allergies, hard rules, app settings
- references/restaurants.json   — the ONLY places you may recommend
- references/order_history.json — past requests, options shown, what they chose, and in what context
- references/feedback.json      — post-visit ratings and comments

On the FIRST food request of a conversation: load the `food-concierge` skill, then Read all four
reference files before answering. On later turns, reuse what you already read instead of re-reading.

## Recommending (per SKILL.md, in short)
1. Hard filters first — allergy conflicts (item-level: a place can stay if it has safe items, but
   name what to avoid), category actually served, preset rules from profile.json.
2. Mine the history for THIS category — sweetness of past picks, the ratings they accept, small
   quiet cafe vs large lively spot, solo-work vs social, dine-in vs pickup, repeat-favorite vs explorer.
3. Apply feedback — bad reviews exclude or penalize (quote them), loved places get a boost.
4. Answer with 2-3 options, best first. For each: one line `**Name** — type · rating · walk · price`,
   then a 1-2 sentence "Why:" citing concrete evidence from their history or feedback (counts, quotes,
   dates). No generic praise like "great food and cozy vibes".
5. Close by naming anything notable you filtered out and why (e.g. a peanut conflict), then invite
   refinement in one short line.

## If they are not satisfied
Ask at most 2-3 sharp clarifying questions — and PREDICT the likely answer from their history so they
can just confirm (e.g. "Solo with the laptop like most of your dessert runs, or a social one?").
Typical axes: alone vs with someone, dine-in vs pickup, work/relax vs quick treat, budget, distance.
Then re-rank and say what changed in the ranking and why.

## When they choose an option
Confirm in one short line (address or landmark + one practical tip drawn from the data). Then persist
the decision so future sessions learn: use the `files` tool — read `taste-memory.json` if it exists,
append {date, request, chosen, context}, write it back — and tell them you will remember it.

## Rules
- Never invent places, menu items, history entries, or reviews that are not in the reference files.
  If a file cannot be read, say so plainly instead of improvising.
- Never recommend anything that conflicts with a listed allergy. This overrides everything else.
- Keep answers compact and chat-friendly: short paragraphs, bold names, no raw JSON dumps, no tables.
- Tools: use Skill + Read for the knowledge base, and `files` only to persist a chosen option.
  Do not use commands, code_interpreter, or browser for food requests.
- If asked something unrelated to food, answer briefly and steer back to what you can do.
- When introducing yourself, say you are a food-concierge demo built with the Claude Agent SDK
  (Python) on EdgeOne Makers that learns from order history, feedback, and preset requirements.
"""


def _normalize_uuid(value: str) -> str | None:
    """Return canonical UUID string, or None if value is not a valid UUID."""
    try:
        return str(UUID(value))
    except (TypeError, ValueError):
        return None


async def resolve_claude_session_binding(
    session_store: Any,
    conversation_id: str,
) -> tuple[str | None, str | None]:
    """
    Bind Claude SDK session to frontend conversation_id.

    First request for a conversation uses session_id=<conversation_id> to create
    a deterministic SDK session. Later requests use resume=<conversation_id>
    when that transcript already exists in session_store.
    """
    session_id = _normalize_uuid(conversation_id)
    if not session_id:
        logger.log(f"[session] skip SDK session binding: invalid conversation_id={conversation_id!r}")
        return None, None

    try:
        from claude_agent_sdk._internal.sessions import project_key_for_directory

        # project_key is load-bearing: EdgeOne ClaudeSessionStore.load() uses it
        # as a namespace prefix on blob keys. Drop it and load() returns None.
        project_key = project_key_for_directory(os.getcwd())
        entries = await session_store.load({"project_key": project_key, "session_id": session_id})
        if entries:
            logger.log(f"[session] resume Claude SDK session_id={session_id}, entries={len(entries)}")
            return None, session_id
        logger.log(f"[session] create Claude SDK session_id={session_id}")
    except Exception as e:
        logger.error(f"[session] failed to inspect session_store for resume: {e}")

    return session_id, None


def build_agent_options(
    session_store=None,
    mcp_server=None,
    mcp_server_name: str = MCP_SERVER_NAME,
    allowed_tools: list[str] | None = None,
    session_id: str | None = None,
    resume: str | None = None,
) -> "ClaudeAgentOptions":
    """Build Claude Agent SDK options. EdgeOne tools come from MCP."""
    cwd = os.getcwd()
    skill_read_allow_rules = [
        "Read(.claude/skills/**)",
        f"Read({cwd}/.claude/skills/**)",
    ]
    # Merge incoming MCP tool names with the built-in Read scoping rules.
    # The Python SDK's `settings` field only accepts a JSON-file path
    # (str | None), unlike the TS SDK which also accepts an inline Settings
    # dict. Trying to pass a dict raises CLIConnectionError("Failed to start
    # Claude Code: expected str, bytes or os.PathLike object, not dict") at
    # subprocess launch. So we route the same `permissions.allow` intent
    # through `allowed_tools` instead — the CLI treats both as auto-allow
    # rules with identical syntax.
    merged_allowed_tools = list(
        dict.fromkeys((allowed_tools or []) + skill_read_allow_rules)
    )
    opts = ClaudeAgentOptions(
        model=resolve_model_name(),
        system_prompt=SYSTEM_PROMPT,
        cwd=cwd,
        # Keep Claude Code's built-in tools narrowly scoped: Skill loads
        # project skills, and Read may only access .claude/skills resources.
        # EdgeOne sandbox tools are exposed separately through MCP below.
        tools=["Skill", "Read"],
        allowed_tools=merged_allowed_tools,
        setting_sources=["project"],
        skills="all",
        permission_mode="dontAsk",
        # Enough turns for: skill load + 4 data-file reads + taste-memory
        # persistence + the final answer, even when the model doesn't batch.
        max_turns=12,
        env=collect_gateway_env(),
        include_partial_messages=True,
        max_buffer_size=20 * 1024 * 1024,  # 20MB — enough for browser screenshots
        session_id=session_id,
        resume=resume,
    )
    if session_store is not None:
        opts.session_store = session_store
    if mcp_server is not None:
        opts.mcp_servers = {mcp_server_name: mcp_server}
    return opts


async def handler(ctx: Any) -> AsyncGenerator[str, None]:
    """EdgeOne Makers entry point (async generator streaming)."""
    cid = ctx.conversation_id or ""
    logger.log(f"[chat] entered with cid={cid!r}")

    body = ctx.request.body
    user_message: str = body.get("message", "") if isinstance(body, dict) else ""
    if not user_message.strip():
        yield sse_event("error", {"message": "'message' is required"})
        yield sse_event("done", {"stopped": False})
        return

    # Extract frontend-generated message IDs for history alignment
    user_msg_id: str = body.get("userMsgId", "") if isinstance(body, dict) else ""
    bot_msg_id: str = body.get("botMsgId", "") if isinstance(body, dict) else ""

    # Extract user ID for store scoping
    raw_user_id = body.get("userId") or body.get("user_id") or "" if isinstance(body, dict) else ""
    user_id = str(raw_user_id).strip() or None

    if not _SDK_AVAILABLE:
        yield sse_event("error", {"message": "claude_agent_sdk is not installed"})
        yield sse_event("done", {"stopped": False})
        return

    cancel_signal = ctx.request.signal
    store_adapter = ctx.store

    # Get Claude session store for transcript persistence (matches TS reference).
    # This gives the SDK multi-turn context, preventing chaotic/repeated tool calls.
    try:
        raw_session_store = store_adapter.claude_session_store()
        logger.log(f"[session_store] enabled, type={type(raw_session_store).__name__}, value={raw_session_store is not None}")
    except Exception as e:
        raw_session_store = None
        logger.error(f"[session_store] failed to get claude_session_store: {e}")
    session_store = raw_session_store

    # Save user message (with frontend-generated ID if available)
    if cid:
        # === DEBUG: dump all store messages for this conversation ===
        try:
            all_msgs = await store_adapter.get_messages(conversation_id=cid, limit=100, order="asc")
            logger.log(f"[debug_store] conversation={cid}, total_messages={len(all_msgs)}")
            for m in all_msgs:
                role = getattr(m, "role", "?")
                msg_id = getattr(m, "message_id", "?")
                content = getattr(m, "content", "")
                preview = str(content)[:200] if content else ""
                created_at = getattr(m, "created_at", 0)
                logger.log(f"[debug_store]   [{role}] id={msg_id} ts={created_at} content={preview}")
        except Exception as e:
            logger.error(f"[debug_store] failed to dump: {e}")
        # === END DEBUG ===

        try:
            # append_message accepts only: conversation_id, role, content, metadata, user_id.
            # message_id is not supported (the SDK auto-generates one).
            await store_adapter.append_message(
                conversation_id=cid,
                role="user",
                content=user_message,
                user_id=user_id,
            )
        except Exception as e:
            logger.error(f"[store] failed to save user message: {e}")

    # Build EdgeOne platform tools → Claude Agent SDK MCP server
    raw_tools = ctx.tools
    if not hasattr(raw_tools, "to_claude_mcp_server"):
        yield sse_event("error", {"message": "context.tools.to_claude_mcp_server is unavailable."})
        yield sse_event("done", {"stopped": False})
        return

    edgeone_mcp = raw_tools.to_claude_mcp_server(MCP_SERVER_NAME, {"always_load": True})
    logger.log("[tool_debug][mcp_server]", {
        "name": getattr(edgeone_mcp, "name", None),
        "allowed_tools": getattr(edgeone_mcp, "allowed_tools", None),
        "tools": [
            {
                "name": getattr(tool, "name", None) if not isinstance(tool, dict) else tool.get("name"),
                "description": getattr(tool, "description", None) if not isinstance(tool, dict) else tool.get("description"),
                "input_schema": getattr(tool, "input_schema", None) if not isinstance(tool, dict) else tool.get("input_schema"),
            }
            for tool in (getattr(edgeone_mcp, "tools", None) or [])
        ],
    })
    mcp_server = create_sdk_mcp_server(
        name=edgeone_mcp.name,
        tools=edgeone_mcp.tools,
    )

    sdk_session_id, sdk_resume = await resolve_claude_session_binding(session_store, cid)
    options = build_agent_options(
        session_store=session_store,
        mcp_server=mcp_server,
        mcp_server_name=edgeone_mcp.name,
        allowed_tools=edgeone_mcp.allowed_tools,
        session_id=sdk_session_id,
        resume=sdk_resume,
    )

    stopped = False
    stream_state = StreamState(bot_msg_id=bot_msg_id)

    try:
        response_iter = query(prompt=user_message, options=options).__aiter__()
        async for item_type, msg in iter_query_messages(response_iter, cancel_signal, HEARTBEAT_INTERVAL_S):
            if item_type == "cancelled":
                logger.log(f"[cancel] cancel_signal observed, stopping stream cid={cid!r}")
                stopped = True
                break
            if item_type == "finished":
                break
            if item_type == "ping":
                yield sse_event("ping", {"ts": int(time.time() * 1000)})
                continue

            events, should_stop = sdk_message_to_sse(msg, stream_state, logger)
            for event in events:
                yield event
            if should_stop:
                break

    except Exception as e:  # noqa: BLE001
        logger.error(f"[error] {e}")
        yield sse_event("error", {
            "message": str(e),
            "errorType": type(e).__name__,
            "detail": repr(e),
        })

    # Save assistant response (with frontend-generated ID if available)
    # Save even if text is empty but images were sent (use placeholder)
    assistant_content = sanitize_assistant_text(stream_state.full_assistant_text).strip()
    if not assistant_content and stream_state.has_images:
        assistant_content = "[image]"

    if store_adapter and cid and assistant_content:
        try:
            # append_message accepts only: conversation_id, role, content, metadata, user_id.
            await store_adapter.append_message(
                conversation_id=cid,
                role="assistant",
                content=assistant_content,
                user_id=user_id,
            )
        except Exception as e:
            logger.error(f"[store] failed to save assistant response: {e}")

    yield sse_event("done", {"stopped": stopped})
