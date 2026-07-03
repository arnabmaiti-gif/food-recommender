# TasteBud 🍨 — a food concierge that remembers how you eat

A conversational food-recommendation agent built with the **Claude Agent SDK (Python)** on
**Tencent EdgeOne Makers**. Ask it for dessert, lunch, coffee, or dinner and it returns 2–3
curated places — each with a *why* traced to your own order history, your past feedback, and
your preset requirements (like a peanut allergy).

Built on the [claude-agent-starter-python](https://github.com/TencentEdgeOne/claude-agent-starter-python)
EdgeOne Makers template (SSE streaming chat, sandbox tools via MCP, conversation persistence).

[![Deploy to EdgeOne Makers](https://cdnstatic.tencentcs.com/edgeone/pages/deploy.svg)](https://edgeone.ai/makers/new?template=claude-agent-starter-python&from=within&fromAgent=1&agentLang=python)

## What it does

1. **You ask for food** — "I'm craving dessert."
2. **It applies hard filters first** — the peanut allergy from your profile is non-negotiable;
   item-level: a place can survive with safe items, but the agent names what to avoid there.
3. **It mines your history for patterns** — for *this* category: do you pick low-sugar options?
   What's your rating floor? Small quiet café or big lively spot? Do you go to work on your
   laptop, to relax, or to socialize? Solo or with friends? Dine-in or pickup?
4. **It applies your past feedback** — the bakery you rated 2★ ("frosting way too sweet") gets
   skipped, and the agent quotes your own review to explain why.
5. **It answers with 2–3 options**, best first, each with a one-line why built from real
   evidence: *"low-sugar picks in 5 of your 6 dessert runs"*.
6. **Not satisfied?** It asks 2–3 sharp questions — pre-filled with the answer your history
   predicts ("solo with the laptop like usual, or a social one?") — then re-ranks.
7. **When you choose**, it records the decision to `taste-memory.json` in the sandbox so future
   sessions keep learning.

## Where the "brain" lives

| Piece | Path |
|---|---|
| Concierge behavior (system prompt) | `agents/chat/index.py` |
| Recommendation method | `agents/chat/knowledge/SKILL.md` |
| Preset requirements (allergies, settings) | `agents/chat/knowledge/references/profile.json` |
| Restaurant catalog (12 synthetic places) | `agents/chat/knowledge/references/restaurants.json` |
| Order history (12 synthetic sessions) | `agents/chat/knowledge/references/order_history.json` |
| Post-visit feedback (9 synthetic reviews) | `agents/chat/knowledge/references/feedback.json` |

The synthetic data is crafted so real patterns emerge: a peanut allergy, a strong low-sugar
dessert habit, a preference for quiet small cafés with wifi (dessert = solo work sessions),
one social exception (dessert bar with friends), a 2★ grudge against a too-sweet bakery, and a
rating floor of ~4.4.

The agent reads these files through the Claude Agent SDK's project-skill mechanism (`Skill` +
`Read`, scoped to `.claude/skills/**`) — you can watch the reads happen live in the app's
Trace panel. The canonical copy lives in `agents/chat/knowledge/` (deploy bundles reliably
ship files next to the handler, but not dot-directories) and is materialized into
`{cwd}/.claude/skills/food-concierge/` at cold start.

## Demo

Follow [`DEMO_SCRIPT.md`](./DEMO_SCRIPT.md) for a 5-minute walkthrough (happy path → refinement
→ choice memory → allergy handling in another category). The original product spec is in
[`docs/PRD.md`](./docs/PRD.md), and there's an 8-slide overview deck in
[`slides/`](./slides/) ([PDF](./slides/TasteBud-slides.pdf) · [Marp source](./slides/SLIDES.md)).

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `AI_GATEWAY_API_KEY` | Yes | Model gateway API key. Use your Makers Models API Key, or any compatible provider key. |
| `AI_GATEWAY_BASE_URL` | Yes | Gateway base URL. For Makers Models, use `https://ai-gateway.edgeone.link/v1`. |
| `AI_GATEWAY_MODEL` | No | Model ID. Defaults to `@makers/deepseek-v4-flash` (free built-in model). |

`agents/_model.py` also reads `ANTHROPIC_API_KEY` / `ANTHROPIC_BASE_URL` directly if you prefer
calling the Anthropic API without a gateway. To get an `AI_GATEWAY_API_KEY`: open the
[Makers Console](https://console.tencentcloud.com/edgeone/makers) → **Models → API Key**.

## Local Development

Prerequisites: Node.js ≥ 18, Python ≥ 3.10, and the EdgeOne CLI (`npm i -g edgeone`).

```bash
npm install
pip install -r agents/requirements.txt
cp .env.example .env       # fill in AI_GATEWAY_API_KEY / AI_GATEWAY_BASE_URL
edgeone makers dev
```

Local agent metrics & traces: `http://localhost:8080/agent-metrics`.

## Project Structure

```text
food-recommender/
├── agents/                          # Stateful EdgeOne Makers Agent Functions (Python)
│   ├── chat/index.py               # POST /chat — SSE streaming; TasteBud system prompt
│   ├── chat/knowledge/             # Recommendation method + synthetic taste data
│   │   ├── SKILL.md               #   (materialized to .claude/skills/ at cold start)
│   │   └── references/{profile,restaurants,order_history,feedback}.json
│   └── stop/index.py               # POST /stop — abort active agent run
├── cloud-functions/                 # Stateless CRUD: history, conversations, delete, clear
├── src/                             # React + Vite + TypeScript chat frontend
├── DEMO_SCRIPT.md                   # 5-minute demo walkthrough
├── docs/PRD.md                      # Product requirements
└── edgeone.json                     # EdgeOne deployment config
```

## Roadmap (post-MVP)

- Real user accounts: per-user profile/history instead of synthetic files
- Write chosen options back into the order history (full learning loop)
- Live restaurant data (maps/reviews APIs) instead of a static catalog
- Structured option cards in the UI (choose buttons, photos) on top of the markdown chat

## License

MIT.
