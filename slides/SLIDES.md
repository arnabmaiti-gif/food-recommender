---
marp: true
paginate: true
title: TasteBud — a food concierge that remembers how you eat
style: |
  :root {
    --espresso: #120d0b;
    --cream: #f7efe4;
    --berry: #ff6b93;
    --caramel: #e8a04c;
    --muted: #b39a87;
  }
  section {
    background: var(--espresso);
    color: var(--cream);
    font-family: Georgia, 'Times New Roman', serif;
    padding: 56px 64px;
  }
  h1, h2 { color: var(--cream); }
  h1 strong, h2 strong, em { color: var(--berry); font-style: normal; }
  a { color: var(--caramel); }
  code { background: #211814; color: var(--caramel); padding: 2px 6px; border-radius: 4px; }
  pre { background: #1b1310; border: 1px solid #3a2b22; border-radius: 8px; }
  pre code { display: block; padding: 14px; line-height: 1.45; background: transparent; }
  blockquote { border-left: 4px solid var(--berry); color: var(--muted); padding-left: 16px; }
  table { font-size: 0.85em; }
  th, td { border: 1px solid #3a2b22 !important; background: #1b1310 !important; color: var(--cream) !important; }
  thead th { background: #211814 !important; color: var(--caramel) !important; }
  section::after { color: var(--muted); }
  ul { line-height: 1.55; }
---

# 🍨 **TasteBud**

## A food concierge that *remembers how you eat*

Conversational food recommendations powered by your own history —
allergies, taste, habits.

**Claude Agent SDK (Python) · Tencent EdgeOne Makers**

[github.com/arnabmaiti-gif/food-recommender](https://github.com/arnabmaiti-gif/food-recommender)

---

# The problem

- Choosing where to eat is a **repeated decision made with zero memory**
- Every app asks the same questions and shows the same crowd-ranked lists
- The strongest signal is the least used: **your own record** —
  what you chose, what you said afterwards, what you're allergic to

> A 4.6★ bakery is the wrong answer if *you* rated it 2★ — "frosting way too sweet."

---

# The core loop

1. **You ask** — "I'm craving dessert"
2. **Hard filters first** — peanut allergy is non-negotiable, item-level
3. **Pattern mining** — low-sugar habit? rating floor? quiet café or lively bar? solo-work or social? dine-in or pickup?
4. **Your feedback beats crowd ratings** — quoted back to you as evidence
5. **2–3 options**, each with a *why* traced to real data
6. **Not satisfied?** It asks 2–3 questions — *pre-filled with the answers your history predicts* — then re-ranks
7. **Your choice is remembered** for next time

---

# What a recommendation looks like

> **Amber & Rye Patisserie** — small café · 4.7★ · 8 min · $$
> *Why:* low-sugar picks in **5 of your 6** dessert runs, and your own 5★ review: "nobody rushed me for two hours."
>
> **Matcha-ya Tea House** — tiny tea house · 4.8★ · 12 min · $$
> *Why:* your dessert runs are usually **solo work sessions** — this is the calmest room in the city.
>
> ⛔ Skipped **Sugar Rush Bakehouse** (4.6★ crowd) — you rated it 2★: *"frosting way too sweet."*

Context flips it: "a friend is visiting, we want something fun" →
**Molten Dessert Bar** rises — with a warning to skip the peanut praline flight.

---

# Architecture

```text
React + Vite chat (SSE stream, tool lamps, trace panel)
        │  POST /chat
        ▼
EdgeOne Makers agent function (Python, Claude Agent SDK)
        │  Skill + Read (scoped to .claude/skills/**)
        ▼
food-concierge skill = the entire "brain"
  ├─ SKILL.md ................ recommendation method
  ├─ profile.json ............ allergies, preset rules
  ├─ restaurants.json ........ 12-place catalog
  ├─ order_history.json ...... 12 past sessions + context
  └─ feedback.json ........... 9 post-visit reviews
        │  files tool (sandbox)
        ▼
taste-memory.json ← chosen options written back
```

---

# The logic is *data*, not code

- **SKILL.md** holds the method; **JSON files** hold the user's world;
  the system prompt holds the guardrails
- Zero hardcoded scoring rules in the app — change the user by changing the data
- Synthetic persona crafted so patterns *pop* in a demo:
  peanut allergy · low-sugar habit · quiet laptop-friendly cafés ·
  one social exception · a 2★ grudge
- **Watch it think**: the trace panel shows the skill load and every
  data-file read, live

---

# Built on the EdgeOne Makers stack

| From the template | Added for TasteBud |
|---|---|
| SSE streaming chat loop | Concierge system prompt (PRD flow) |
| Sandbox tools via MCP | `food-concierge` skill + synthetic dataset |
| Conversation persistence | Choice write-back (`taste-memory.json`) |
| React chat UI | Rebrand: palette, type, preset chips, en/中文 copy |

- Model-agnostic: free built-in `@makers/deepseek-v4-flash`, or BYOK (Anthropic API)
- One-click deploy to EdgeOne Makers

---

# Try it in 5 minutes

- **Demo**: follow [`DEMO_SCRIPT.md`](../DEMO_SCRIPT.md) — happy path →
  refinement → choice memory → allergy handling at lunch
- **Run it**: `npm install` · `pip install -r agents/requirements.txt` ·
  set `AI_GATEWAY_API_KEY` · `edgeone makers dev`
- **Spec**: [`docs/PRD.md`](../docs/PRD.md)

### Roadmap
Real accounts → live restaurant data → structured option cards →
full learning loop into canonical history

**github.com/arnabmaiti-gif/food-recommender** 🍨
