const zh = {
  // Header
  "app.title": "TasteBud 味蕾管家",
  "app.subtitle": "记得你怎么吃的美食推荐助手 —— 过敏、口味、习惯都记在心里",

  // Empty state
  "empty.title": "今天想吃点什么？",
  "empty.hint": "我是 TasteBud。我了解你的点单历史、你的评价、还有你的花生过敏 —— 想吃甜品、午餐、咖啡或晚餐，直接说，我会挑 2–3 家并解释为什么适合你。",
  "empty.features": "2–3 个精选推荐 · 理由来自你自己的历史 · 过敏安全",

  // Chat input
  "chat.placeholder": "想吃点什么？  ⏎ 发送 · Shift+⏎ 换行",
  "chat.hint": "TasteBud 演示 · Claude Agent SDK + EdgeOne Makers · 合成口味数据",

  // Preset questions
  "preset.dessert": "我想吃甜品",
  "preset.lunch": "在公司附近能快速自取的午餐",
  "preset.coffee": "找个能安静工作几小时的咖啡馆",

  // Tool indicators
  "tool.commands": "终端命令",
  "tool.files": "口味记忆",
  "tool.codeRunner": "代码解释器",
  "tool.browser": "浏览器",

  // Web search activity (in-bubble chip)
  "webSearch.error.wsaMissing": "搜索不可用，需配置 {0} API Key",
  "webSearch.error.wsaCta": "获取 Key",

  // Skill indicators
  "skill.foodConcierge": "美食管家",

  // Debug panel
  "debug.title": "传输流",
  "debug.events": "事件",
  "debug.clear": "清除",
  "debug.empty": "等待 SSE 事件...",
  "debug.emptyHint": "发送消息后，可以在这里看到 Agent 读取你的口味数据的全过程。",

  // Status & errors
  "status.error": "⚠️ 请求失败，请检查后端服务是否启动。",
  "status.stopped": "⏹ *已停止生成*",
  "status.backendError": "⚠️ 后端中断请求失败，服务端可能仍在运行。",

  // Language toggle
  "lang.switch": "English",

  // Sidebar
  "sidebar.label": "会话列表",
  "sidebar.title": "想吃的",
  "sidebar.newChat": "新的想法",
  "sidebar.loading": "正在加载会话...",
  "sidebar.loadMore": "加载更多",
  "sidebar.loadingMore": "加载中...",
  "sidebar.emptyTitle": "暂无会话",
  "sidebar.emptyHint": "点击「新的想法」，告诉我你想吃什么。",
  "sidebar.delete": "删除会话",
  "sidebar.deleteConfirm": "确定要永久删除这个会话吗？此操作不可恢复。",

  // Aria labels (button hover/screen-reader)
  "aria.send": "发送",
  "aria.clearHistory": "清除历史",
  "aria.stopGeneration": "停止生成",

  // ─── Floating bottom-right action badges ─────────────────────────────
  "floatingLink.deploy": "一键部署",
  "floatingLink.github": "GitHub",
} as const;

export default zh;
