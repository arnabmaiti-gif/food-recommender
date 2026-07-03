#!/usr/bin/env python3
"""Regenerate agents/chat/_knowledge.py from agents/chat/knowledge/.

The knowledge/ directory is the human-editable source of truth. The generated
module embeds the same data as Python constants so the deployed agent never
depends on data files surviving deployment packaging. Run after editing any
file under knowledge/:

    python3 scripts/embed_knowledge.py
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = ROOT / "agents" / "chat" / "knowledge"
OUT = ROOT / "agents" / "chat" / "_knowledge.py"

DATA_FILES = [
    "profile.json",
    "restaurants.json",
    "order_history.json",
    "feedback.json",
]

HEADER = '''"""Embedded knowledge base for TasteBud.

AUTO-GENERATED from agents/chat/knowledge/ by scripts/embed_knowledge.py —
edit the files there and re-run the script; do not edit this module by hand.

The embedded constants make the knowledge base part of the code bundle, so
recommendations work no matter what deployment packaging does to data files.
When the live knowledge/ directory is present (local dev, faithful bundles),
its files win so edits show up without regeneration.
"""
from __future__ import annotations

import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_LIVE_DIR = os.path.join(_HERE, "knowledge", "references")

'''

FOOTER = '''

def _load(name: str) -> tuple[str, str]:
    """Return (content, source) for a data file — live file if present, else embedded."""
    path = os.path.join(_LIVE_DIR, name)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read(), "file"
    except OSError:
        return EMBEDDED[name], "embedded"


def knowledge_block() -> tuple[str, dict[str, str]]:
    """Build the verbatim knowledge block appended to the system prompt.

    Returns (block, sources) where sources maps file name -> "file"/"embedded"
    for cold-start logging.
    """
    sections: list[str] = []
    sources: dict[str, str] = {}
    for name in EMBEDDED:
        text, src = _load(name)
        sources[name] = src
        sections.append(f"### {name}\\n```json\\n{text.strip()}\\n```")
    block = (
        "## KNOWLEDGE BASE (verbatim ground truth — never invent beyond it)\\n\\n"
        + "\\n\\n".join(sections)
    )
    return block, sources
'''


def main() -> None:
    parts = [HEADER, "EMBEDDED: dict[str, str] = {\n"]
    for name in DATA_FILES:
        text = (KNOWLEDGE_DIR / "references" / name).read_text(encoding="utf-8")
        if "'''" in text:
            raise SystemExit(f"{name} contains ''' — adjust the data or this generator")
        parts.append(f"    {name!r}: r'''\n{text}''',\n")
    parts.append("}\n")
    parts.append(FOOTER)
    OUT.write_text("".join(parts), encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
