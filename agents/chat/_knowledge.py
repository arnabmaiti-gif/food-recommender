"""Embedded knowledge base for TasteBud.

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

EMBEDDED: dict[str, str] = {
    'profile.json': r'''
{
  "user": {
    "name": "Arnab",
    "neighborhood": "Maple District",
    "work": "4th & Pine, Maple District"
  },
  "preset_requirements": {
    "allergies": ["peanut"],
    "allergy_policy": "Never suggest items containing peanut. A place may still be recommended for its safe items, but always name what to avoid there.",
    "dietary_rules": [],
    "app_settings": {
      "max_walk_minutes": 20,
      "price_ceiling": "$$$",
      "min_rating_hint": 4.2
    }
  }
}
''',
    'restaurants.json': r'''
{
  "note": "Synthetic catalog for the TasteBud demo. All places are within walking distance of the user's Maple District home/office.",
  "restaurants": [
    {
      "id": "amber-rye",
      "name": "Amber & Rye Patisserie",
      "type": "small cafe / patisserie",
      "size": "small",
      "categories": ["dessert", "coffee", "pastry"],
      "rating": 4.7,
      "price": "$$",
      "walk_minutes": 8,
      "ambience": { "noise": "quiet", "seats": 18, "laptop_friendly": true, "wifi": true, "outlets": "several" },
      "good_for": ["solo-work", "relax", "reading"],
      "pickup": true,
      "signature_items": [
        { "name": "rye honey madeleines", "sweetness": "low", "allergens": [] },
        { "name": "black sesame mille-feuille", "sweetness": "low", "allergens": [] },
        { "name": "lemon tart", "sweetness": "medium", "allergens": [] }
      ],
      "notes": "Corner tables by the window; staff famously never rush laptop campers."
    },
    {
      "id": "matcha-ya",
      "name": "Matcha-ya Tea House",
      "type": "tiny tea house",
      "size": "small",
      "categories": ["dessert", "tea"],
      "rating": 4.8,
      "price": "$$",
      "walk_minutes": 12,
      "ambience": { "noise": "very quiet", "seats": 12, "laptop_friendly": true, "wifi": true, "outlets": "few" },
      "good_for": ["solo-work", "relax"],
      "pickup": false,
      "signature_items": [
        { "name": "matcha kakigori", "sweetness": "low", "allergens": [] },
        { "name": "hojicha pudding", "sweetness": "low", "allergens": [] },
        { "name": "yuzu cheesecake", "sweetness": "medium", "allergens": [] }
      ],
      "notes": "Soft music only; feels like a library that serves dessert."
    },
    {
      "id": "molten",
      "name": "Molten Dessert Bar",
      "type": "dessert bar",
      "size": "large",
      "categories": ["dessert", "drinks"],
      "rating": 4.5,
      "price": "$$$",
      "walk_minutes": 14,
      "ambience": { "noise": "lively", "seats": 60, "laptop_friendly": false, "wifi": false, "outlets": "none" },
      "good_for": ["groups", "date", "celebration"],
      "pickup": false,
      "signature_items": [
        { "name": "tableside chocolate souffle", "sweetness": "high", "allergens": [] },
        { "name": "praline tasting flight", "sweetness": "high", "allergens": ["peanut"] },
        { "name": "smores board for two", "sweetness": "high", "allergens": [] }
      ],
      "notes": "Theatrical plating, loud on weekends; reservations recommended after 7pm."
    },
    {
      "id": "sugar-rush",
      "name": "Sugar Rush Bakehouse",
      "type": "bakery counter",
      "size": "small",
      "categories": ["dessert", "pastry"],
      "rating": 4.6,
      "price": "$",
      "walk_minutes": 6,
      "ambience": { "noise": "crowded", "seats": 0, "laptop_friendly": false, "wifi": false, "outlets": "none" },
      "good_for": ["quick-treat"],
      "pickup": true,
      "signature_items": [
        { "name": "cinnamon roll with cream-cheese frosting", "sweetness": "high", "allergens": [] },
        { "name": "funfetti layer cake", "sweetness": "high", "allergens": [] },
        { "name": "peanut butter brownie", "sweetness": "high", "allergens": ["peanut"] }
      ],
      "notes": "Counter-service only, permanent line out the door."
    },
    {
      "id": "cielo",
      "name": "Cielo Gelato",
      "type": "gelato bar",
      "size": "small",
      "categories": ["dessert"],
      "rating": 4.4,
      "price": "$",
      "walk_minutes": 5,
      "ambience": { "noise": "moderate", "seats": 6, "laptop_friendly": false, "wifi": false, "outlets": "none" },
      "good_for": ["quick-treat", "walk-and-eat"],
      "pickup": true,
      "signature_items": [
        { "name": "dark chocolate sorbetto", "sweetness": "low", "allergens": [] },
        { "name": "pistachio gelato", "sweetness": "medium", "allergens": ["tree nut"] },
        { "name": "peanut butter swirl", "sweetness": "high", "allergens": ["peanut"] }
      ],
      "notes": "Scoops use a shared case — staff will grab a clean scoop from the back on request."
    },
    {
      "id": "copper-kettle",
      "name": "The Copper Kettle",
      "type": "large dessert cafe",
      "size": "large",
      "categories": ["dessert", "coffee", "brunch"],
      "rating": 4.3,
      "price": "$$",
      "walk_minutes": 10,
      "ambience": { "noise": "moderate", "seats": 80, "laptop_friendly": true, "wifi": true, "outlets": "some" },
      "good_for": ["relax", "groups", "long-sits"],
      "pickup": true,
      "signature_items": [
        { "name": "warm apple pie", "sweetness": "medium", "allergens": [] },
        { "name": "bread pudding", "sweetness": "medium", "allergens": [] }
      ],
      "notes": "Deep booths; open until midnight."
    },
    {
      "id": "fern-filament",
      "name": "Fern & Filament",
      "type": "specialty coffee bar",
      "size": "small",
      "categories": ["coffee", "dessert", "pastry"],
      "rating": 4.7,
      "price": "$$",
      "walk_minutes": 7,
      "ambience": { "noise": "quiet", "seats": 24, "laptop_friendly": true, "wifi": true, "outlets": "every table" },
      "good_for": ["solo-work", "meetings-for-two"],
      "pickup": true,
      "signature_items": [
        { "name": "canele", "sweetness": "low", "allergens": [] },
        { "name": "oat milk latte", "sweetness": "low", "allergens": [] }
      ],
      "notes": "Mezzanine upstairs is the quiet zone; plugs at every table."
    },
    {
      "id": "verde-bowls",
      "name": "Verde Bowls",
      "type": "fast-casual bowls",
      "size": "small",
      "categories": ["lunch"],
      "rating": 4.5,
      "price": "$$",
      "walk_minutes": 3,
      "ambience": { "noise": "moderate", "seats": 14, "laptop_friendly": false, "wifi": false, "outlets": "none" },
      "good_for": ["quick-lunch", "pickup"],
      "pickup": true,
      "signature_items": [
        { "name": "harissa chicken bowl", "sweetness": null, "allergens": [] },
        { "name": "gado-gado bowl", "sweetness": null, "allergens": ["peanut"] }
      ],
      "notes": "Online ordering; happily swaps peanut sauce for tahini."
    },
    {
      "id": "bo-bao",
      "name": "Bo & Bao",
      "type": "casual counter",
      "size": "small",
      "categories": ["lunch", "snack"],
      "rating": 4.2,
      "price": "$",
      "walk_minutes": 4,
      "ambience": { "noise": "moderate", "seats": 10, "laptop_friendly": false, "wifi": false, "outlets": "none" },
      "good_for": ["quick-lunch", "pickup"],
      "pickup": true,
      "signature_items": [
        { "name": "braised pork bao (3pc)", "sweetness": null, "allergens": [] },
        { "name": "salted egg custard bao", "sweetness": "medium", "allergens": [] }
      ],
      "notes": "Fastest pickup on the block — under five minutes at noon."
    },
    {
      "id": "nonna-lucia",
      "name": "Nonna Lucia",
      "type": "large Italian restaurant",
      "size": "large",
      "categories": ["dinner", "dessert"],
      "rating": 4.6,
      "price": "$$$",
      "walk_minutes": 18,
      "ambience": { "noise": "warm buzz", "seats": 90, "laptop_friendly": false, "wifi": false, "outlets": "none" },
      "good_for": ["date", "groups", "celebration"],
      "pickup": false,
      "signature_items": [
        { "name": "tagliatelle al ragu", "sweetness": null, "allergens": [] },
        { "name": "tiramisu", "sweetness": "medium-high", "allergens": [] }
      ],
      "notes": "Candlelit back room; book ahead on weekends."
    },
    {
      "id": "han-river",
      "name": "Han River BBQ",
      "type": "large Korean BBQ",
      "size": "large",
      "categories": ["dinner"],
      "rating": 4.4,
      "price": "$$$",
      "walk_minutes": 15,
      "ambience": { "noise": "lively", "seats": 110, "laptop_friendly": false, "wifi": false, "outlets": "none" },
      "good_for": ["groups", "celebration"],
      "pickup": false,
      "signature_items": [
        { "name": "galbi set for the table", "sweetness": null, "allergens": [] },
        { "name": "kimchi jjigae", "sweetness": null, "allergens": [] }
      ],
      "notes": "Grill-at-the-table; great for loud groups."
    },
    {
      "id": "luna-diner",
      "name": "Luna Diner",
      "type": "24h diner",
      "size": "large",
      "categories": ["dessert", "breakfast", "late-night"],
      "rating": 4.1,
      "price": "$$",
      "walk_minutes": 9,
      "ambience": { "noise": "moderate", "seats": 70, "laptop_friendly": true, "wifi": true, "outlets": "some" },
      "good_for": ["late-night", "long-sits"],
      "pickup": true,
      "signature_items": [
        { "name": "buttermilk pancake stack", "sweetness": "high", "allergens": [] },
        { "name": "black-and-white milkshake", "sweetness": "high", "allergens": [] }
      ],
      "notes": "Open 24 hours; roomy booths."
    }
  ]
}
''',
    'order_history.json': r'''
{
  "note": "Synthetic order history for the TasteBud demo. Each session: what the user asked, which options the app showed, what they chose, and the context that emerged.",
  "sessions": [
    {
      "date": "2026-04-04",
      "day": "Saturday evening",
      "request": "somewhere fun for dessert with friends tonight",
      "context": { "company": "friends (3)", "mode": "dine-in", "intent": "celebrate" },
      "options_shown": ["molten", "copper-kettle", "luna-diner"],
      "chose": "molten",
      "item_ordered": "tableside chocolate souffle (shared)",
      "note": "Asked staff about peanuts in the praline flight and skipped it."
    },
    {
      "date": "2026-04-12",
      "day": "Sunday afternoon",
      "request": "dessert",
      "context": { "company": "solo", "mode": "dine-in", "intent": "work on laptop" },
      "options_shown": ["sugar-rush", "amber-rye", "cielo"],
      "chose": "amber-rye",
      "item_ordered": "black sesame mille-feuille + pour-over",
      "note": "Stayed about two hours working."
    },
    {
      "date": "2026-04-18",
      "day": "Friday noon",
      "request": "quick lunch near the office",
      "context": { "company": "solo", "mode": "pickup", "intent": "quick" },
      "options_shown": ["verde-bowls", "bo-bao"],
      "chose": "verde-bowls",
      "item_ordered": "harissa chicken bowl",
      "note": "Confirmed no peanut cross-contact before ordering."
    },
    {
      "date": "2026-04-25",
      "day": "Saturday morning",
      "request": "coffee shop to get some work done",
      "context": { "company": "solo", "mode": "dine-in", "intent": "work on laptop" },
      "options_shown": ["fern-filament", "copper-kettle"],
      "chose": "fern-filament",
      "item_ordered": "oat milk latte + canele"
    },
    {
      "date": "2026-05-02",
      "day": "Saturday afternoon",
      "request": "dessert, somewhere calm",
      "context": { "company": "solo", "mode": "dine-in", "intent": "relax" },
      "options_shown": ["matcha-ya", "copper-kettle", "molten"],
      "chose": "matcha-ya",
      "item_ordered": "hojicha pudding"
    },
    {
      "date": "2026-05-09",
      "day": "Saturday evening",
      "request": "dinner with college friends, five of us",
      "context": { "company": "friends (5)", "mode": "dine-in", "intent": "social" },
      "options_shown": ["han-river", "nonna-lucia"],
      "chose": "han-river",
      "item_ordered": "galbi set for the table"
    },
    {
      "date": "2026-05-16",
      "day": "Saturday afternoon",
      "request": "dessert",
      "context": { "company": "solo", "mode": "dine-in", "intent": "work on laptop" },
      "options_shown": ["copper-kettle", "matcha-ya", "sugar-rush"],
      "chose": "matcha-ya",
      "item_ordered": "matcha kakigori",
      "note": "Said the kakigori was 'exactly the right amount of sweet'."
    },
    {
      "date": "2026-05-23",
      "day": "Saturday noon",
      "request": "lunch",
      "context": { "company": "solo", "mode": "pickup", "intent": "quick" },
      "options_shown": ["bo-bao", "verde-bowls"],
      "chose": "bo-bao",
      "item_ordered": "braised pork bao (3pc)"
    },
    {
      "date": "2026-05-31",
      "day": "Sunday afternoon",
      "request": "dessert somewhere I can sit for a while",
      "context": { "company": "solo", "mode": "dine-in", "intent": "work on laptop" },
      "options_shown": ["amber-rye", "luna-diner", "copper-kettle"],
      "chose": "amber-rye",
      "item_ordered": "rye honey madeleines + pour-over"
    },
    {
      "date": "2026-06-06",
      "day": "Saturday evening",
      "request": "date-night dinner",
      "context": { "company": "partner", "mode": "dine-in", "intent": "date" },
      "options_shown": ["nonna-lucia", "han-river"],
      "chose": "nonna-lucia",
      "item_ordered": "tagliatelle al ragu, shared tiramisu after"
    },
    {
      "date": "2026-06-13",
      "day": "Saturday morning",
      "request": "coffee",
      "context": { "company": "solo", "mode": "dine-in", "intent": "work on laptop" },
      "options_shown": ["fern-filament"],
      "chose": "fern-filament",
      "item_ordered": "oat milk latte"
    },
    {
      "date": "2026-06-21",
      "day": "Sunday afternoon",
      "request": "dessert",
      "context": { "company": "solo", "mode": "dine-in", "intent": "quick treat" },
      "options_shown": ["cielo", "amber-rye", "luna-diner"],
      "chose": "cielo",
      "item_ordered": "dark chocolate sorbetto",
      "note": "Picked the least sweet flavor in the case."
    }
  ]
}
''',
    'feedback.json': r'''
{
  "note": "Synthetic post-visit feedback for the TasteBud demo. Verbatim comments the user left after visits.",
  "feedback": [
    {
      "place": "sugar-rush",
      "date": "2026-03-14",
      "rating": 2,
      "comment": "Cinnamon roll frosting was way too sweet — left half of it. Nowhere to sit either.",
      "tags": ["too_sweet", "no_seating"]
    },
    {
      "place": "amber-rye",
      "date": "2026-04-12",
      "rating": 5,
      "comment": "Quiet corner table and nobody rushed me for two hours. The mille-feuille is barely sweet — perfect.",
      "tags": ["low_sugar", "work_friendly", "quiet"]
    },
    {
      "place": "molten",
      "date": "2026-04-05",
      "rating": 4,
      "comment": "So much fun with friends, but way too loud to go alone. Skipped the praline flight because of my peanut allergy — staff handled it well.",
      "tags": ["lively", "group_fun", "peanut_risk"]
    },
    {
      "place": "matcha-ya",
      "date": "2026-05-17",
      "rating": 5,
      "comment": "Calmest room in the city. The kakigori is the right kind of sweet — subtle.",
      "tags": ["quiet", "low_sugar"]
    },
    {
      "place": "verde-bowls",
      "date": "2026-04-18",
      "rating": 4,
      "comment": "They swapped the peanut sauce for tahini without making it weird. Pickup was ready in five minutes.",
      "tags": ["allergy_accommodating", "fast_pickup"]
    },
    {
      "place": "luna-diner",
      "date": "2026-02-21",
      "rating": 3,
      "comment": "Pancakes drowned in syrup and the coffee was thin. Roomy booths though.",
      "tags": ["too_sweet", "spacious"]
    },
    {
      "place": "fern-filament",
      "date": "2026-06-13",
      "rating": 5,
      "comment": "Plugs at every table and the canele is not too sweet. My default work spot.",
      "tags": ["work_friendly", "low_sugar"]
    },
    {
      "place": "han-river",
      "date": "2026-05-09",
      "rating": 5,
      "comment": "Perfect for a loud group of five. Galbi set is the move.",
      "tags": ["group_fun"]
    },
    {
      "place": "nonna-lucia",
      "date": "2026-06-06",
      "rating": 4,
      "comment": "Lovely dinner. The tiramisu was good but sweeter than I like — half was enough.",
      "tags": ["slightly_too_sweet", "date_spot"]
    }
  ]
}
''',
}


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
        sections.append(f"### {name}\n```json\n{text.strip()}\n```")
    block = (
        "## KNOWLEDGE BASE (verbatim ground truth — never invent beyond it)\n\n"
        + "\n\n".join(sections)
    )
    return block, sources
