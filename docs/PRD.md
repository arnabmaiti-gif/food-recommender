# PRD — TasteBud, a personal food recommendation app

## Problem

Choosing where to eat is a repeated decision made with zero memory: every app asks the same
questions and shows the same crowd-ranked lists. A person's own history — what they actually
chose, what they said afterwards, what they're allergic to — is the strongest signal and the
least used.

## Core flow

1. The user comes in with a food request (e.g. **"dessert"**).
2. The app holds a **history of past recommendation requests** and which suggestion the user
   chose each time.
3. The app first presents **2–3 options** that satisfy the stated requirement, ranked by
   **patterns mined from past orders**, such as:
   - desserts with certain traits (e.g. **less sugar**),
   - **restaurants with high ratings** (the user's personal rating floor),
   - **variety** of desserts vs a specific kind,
   - **small cafés vs large restaurants** (ambience/comfort),
   - whether dessert requests are really about **going somewhere to relax or work**.
4. The app uses the user's **past feedback** on places they visited to curate better
   recommendations (their own 2★ beats a crowd 4.6★).
5. The app respects **preset requirements** — allergies (hard constraint) and other standing
   rules (max walk distance, price ceiling).

Each option comes with a **brief explanation of why it was suggested**, traced to concrete
evidence (counts from history, quotes from the user's feedback).

If the user is not satisfied, the app **asks what they're looking for** — and uses past
patterns to **predict the answers** it expects (going alone or with a friend? pickup or
eating there? working, relaxing, or a quick treat?), so the user can just confirm or correct.

When the user chooses an option, the app **records the decision** so future recommendations
keep learning.

## MVP scope (this repo)

| Requirement | Implementation |
|---|---|
| Conversational request intake | Chat UI (React + SSE streaming) |
| Past request/choice history | `references/order_history.json` (12 synthetic sessions) |
| Pattern mining + 2–3 explained options | Claude Agent SDK + `food-concierge` skill method |
| Past feedback curation | `references/feedback.json` (9 synthetic reviews) |
| Preset requirements / allergies | `references/profile.json` (peanut allergy, app settings) |
| Refinement with predicted context | Skill step 5 (predicted clarifying questions) |
| Choice recording | `taste-memory.json` via sandbox `files` tool |

## Out of scope for MVP (iteration 2+)

- Real accounts and per-user data storage
- Live restaurant data (maps/review APIs), photos, booking links
- Structured option cards with one-tap "choose" buttons
- Writing choices back into the canonical order history automatically
- Multi-city support, time-of-day awareness from real clocks
