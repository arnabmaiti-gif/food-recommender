# TasteBud — 5-Minute Demo Script

A word-for-word walkthrough for demoing TasteBud. The synthetic persona: **Arnab**, peanut
allergy, likes low-sugar desserts in quiet cafés where he can work, rating floor ~4.4, one
social exception in his history (dessert bar with friends).

## Before the demo

1. Deploy on EdgeOne Makers (or run `edgeone makers dev` locally) with `AI_GATEWAY_API_KEY`
   and `AI_GATEWAY_BASE_URL` set. Open the app.
2. Click **New craving** in the sidebar so you start from a clean conversation.
3. Make sure the language toggle (top right) is on the language you'll present in.
4. Optional dry run: send one message so the sandbox is warm — the first request of a fresh
   deployment is the slowest (skill load + four data reads).

> **Stage directions** are in blockquotes. Lines to type are in `code`.

---

## Act 1 — The happy path (≈90s)

> Point at the empty state: "This is TasteBud — a food concierge that already knows this
> user: their order history, their post-visit reviews, and their preset requirements,
> including a peanut allergy."

Type (or click the first preset chip):

```
I'm craving dessert
```

> While it streams, point at the **Trace panel** on the right: "Watch what it's doing — it
> loads a 'food-concierge' skill and reads four files: my profile, the restaurant catalog,
> my order history, my feedback. This is the Claude Agent SDK's project-skill mechanism —
> the recommendation logic is data, not hardcoded rules."

**Expect:** 2–3 options led by the quiet low-sugar cafés (Amber & Rye Patisserie and/or
Matcha-ya Tea House), each with an evidence-based *why* — something like "5 of your 6 dessert
picks were low-sugar" or a quote from the user's own 5★ review. It should also mention what
it *skipped*: Sugar Rush Bakehouse despite its 4.6★ crowd rating, because *the user* rated it
2★ — "frosting way too sweet".

> Talking points, counting on fingers:
> 1. "It didn't just match 'dessert' — it noticed I pick **low-sugar** desserts."
> 2. "It knows my dessert runs are usually **solo work sessions**, so it favored quiet,
>    laptop-friendly cafés."
> 3. "It **overrode the crowd rating** with my own 2★ review — my feedback beats the average."
> 4. "And everything with peanuts is filtered or flagged before ranking even starts."

## Act 2 — Refinement with predicted context (≈90s)

Type:

```
Not feeling these today, show me something different
```

**Expect:** instead of blindly reshuffling, it asks 2–3 clarifying questions with the
predicted answers built in — e.g. "Solo with the laptop like most of your dessert runs, or
a social one this time? Dine-in as usual?"

> "This is the part I love — it doesn't interrogate me with a blank form. It *predicts* my
> answers from history and I just confirm or correct."

Type:

```
Actually a friend is visiting tonight, we want something fun
```

**Expect:** the ranking flips to the social cluster — **Molten Dessert Bar** on top ("the one
time you brought friends, you went here and rated it 4★"), with an explicit warning to skip
the praline tasting flight because it contains peanuts, and a note on what changed in the
ranking and why.

> "Same data, new context — and the allergy warning travels with the recommendation."

## Act 3 — Choosing and remembering (≈45s)

Type:

```
Molten it is
```

**Expect:** a one-line confirmation with a practical tip (e.g. book after 7pm on weekends),
and then the agent writes the decision to `taste-memory.json` — the **Taste Memory** lamp in
the header lights up when the `files` tool fires.

> "The choice is persisted. Next session, this decision is part of the history it learns
> from — that's the recommendation loop closing."

## Act 4 — Breadth beyond dessert (≈45s, optional)

Click **New craving**, then type (or click the second preset chip):

```
Quick lunch I can pick up near the office
```

**Expect:** Verde Bowls first (3-min walk, pickup, 4.5★) with the allergy nuance: their
gado-gado bowl uses peanut sauce, but the agent knows from past feedback that "they swap the
peanut sauce for tahini without making it weird".

> "Different category, same brain: it knows my lunches are pickup, near the office, and it
> even remembers which places handle my allergy gracefully."

---

## Recovery lines (if things go sideways)

- **First response is slow** → narrate the Trace panel: the reads you see are real.
- **Only shows 1–2 options or no 'why'** → nudge: `Give me the top 3 with the reasons from my history.`
- **It asks questions in Act 1 instead of recommending** → say: `Just pick for me based on my history.`
- **Model hallucinates a place** → point out the rule exists, then: `Only use places from my restaurant catalog.`
  (Worth mentioning: the free gateway model is swappable — `AI_GATEWAY_MODEL` — and a stronger
  model follows the skill more faithfully.)

## Q&A crib sheet

- **Where do recommendations come from?** A project skill: `SKILL.md` (method) + four JSON
  reference files (profile, catalog, history, feedback). No hardcoded rules in the app.
- **How would this scale to real users?** Swap the synthetic JSON for per-user records in
  EdgeOne storage; the choice-recording path (`taste-memory.json`) already sketches the
  write-back loop.
- **Why an agent instead of a scoring function?** The refinement dialogue ("predict what I'd
  answer") and evidence-quoting explanations are language-native tasks; the hard constraints
  (allergy filter) stay in the prompt/skill as non-negotiable rules.
- **Stack?** React + Vite frontend, Python Claude Agent SDK backend on EdgeOne Makers agent
  functions, SSE streaming, conversation persistence via `context.store`.
