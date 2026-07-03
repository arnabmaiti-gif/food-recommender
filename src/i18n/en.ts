const en = {
  // Header
  "app.title": "TasteBud",
  "app.subtitle": "A food concierge that remembers how you eat — allergies, taste, habits",

  // Empty state
  "empty.title": "What are you craving?",
  "empty.hint": "I'm TasteBud. I know your order history, your feedback, and your peanut allergy — ask me for dessert, lunch, coffee or dinner and I'll pick 2–3 places and tell you exactly why each one fits you.",
  "empty.features": "2–3 curated picks · reasons from your own history · allergy-aware",

  // Chat input
  "chat.placeholder": "What are you craving?  ⏎ Send · Shift+⏎ Newline",
  "chat.hint": "TasteBud demo · Claude Agent SDK on EdgeOne Makers · synthetic taste data",

  // Preset questions
  "preset.dessert": "I'm craving dessert",
  "preset.lunch": "Quick lunch I can pick up near the office",
  "preset.coffee": "Find me a coffee spot where I can work for a few hours",

  // Tool indicators
  "tool.commands": "Commands",
  "tool.files": "Taste Memory",
  "tool.codeRunner": "Code Runner",
  "tool.browser": "Browser",

  // Web search activity (in-bubble chip)
  "webSearch.error.wsaMissing": "Web search unavailable — needs a {0} API key",
  "webSearch.error.wsaCta": "Get a key",

  // Skill indicators
  "skill.foodConcierge": "Food Concierge",

  // Debug panel
  "debug.title": "Trace",
  "debug.events": "events",
  "debug.clear": "Clear",
  "debug.empty": "Waiting for SSE events...",
  "debug.emptyHint": "After sending a message, you can watch the agent read your taste data here.",

  // Status & errors
  "status.error": "Request failed. Please check if the backend service is running.",
  "status.stopped": "⏹ *Generation stopped*",
  "status.backendError": "Backend abort request failed. The server may still be running.",

  // Language toggle
  "lang.switch": "中文",

  // Sidebar
  "sidebar.label": "Conversation list",
  "sidebar.title": "Cravings",
  "sidebar.newChat": "New craving",
  "sidebar.loading": "Loading conversations...",
  "sidebar.loadMore": "Load more",
  "sidebar.loadingMore": "Loading...",
  "sidebar.emptyTitle": "No conversations yet",
  "sidebar.emptyHint": "Click \"New craving\" and tell me what you feel like eating.",
  "sidebar.delete": "Delete conversation",
  "sidebar.deleteConfirm": "Permanently delete this conversation? This cannot be undone.",

  // Aria labels (button hover/screen-reader)
  "aria.send": "Send",
  "aria.clearHistory": "Clear history",
  "aria.stopGeneration": "Stop generation",

  // ─── Floating bottom-right action badges ─────────────────────────────
  "floatingLink.deploy": "Deploy",
  "floatingLink.github": "GitHub",
} as const;

export default en;
