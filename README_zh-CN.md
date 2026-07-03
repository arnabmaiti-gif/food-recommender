# TasteBud 🍨 味蕾管家 — 记得你怎么吃的美食推荐 Agent

基于 **Claude Agent SDK（Python）** 与 **腾讯 EdgeOne Makers** 构建的对话式美食推荐应用。
告诉它你想吃甜品、午餐、咖啡或晚餐，它会结合你的**点单历史**、**过往评价**和**预设要求**
（例如花生过敏），给出 2–3 个精选推荐，每个都附上可追溯到数据的推荐理由。

基于 EdgeOne Makers 模板
[claude-agent-starter-python](https://github.com/TencentEdgeOne/claude-agent-starter-python)
改造（SSE 流式对话、MCP 沙箱工具、会话持久化）。

## 核心能力

1. **硬性过滤优先** —— 档案中的花生过敏不可妥协；精确到单品：某家店可以因为有安全单品而保留，但 Agent 会点名提醒避开哪道。
2. **历史模式挖掘** —— 针对当前品类：偏好低糖？个人评分底线？安静小店还是热闹大店？独自带电脑工作还是社交聚会？堂食还是自取？
3. **个人评价修正** —— 用户给过 2 星（“糖霜甜得发齁”）的店，即使大众评分 4.6 也会被跳过，并引用用户自己的原话解释。
4. **2–3 个选项 + 理由** —— 每条理由都来自真实证据：“你最近 6 次甜品有 5 次选了低糖”。
5. **不满意就追问** —— 最多 2–3 个问题，并根据历史**预测你会怎么答**（“照旧一个人带电脑，还是这次是社交局？”），确认后重新排序。
6. **记住你的选择** —— 选定后写入沙箱 `taste-memory.json`，供后续会话继续学习。

## “大脑”在哪里

| 组件 | 路径 |
|---|---|
| 管家行为（系统提示词） | `agents/chat/index.py` |
| 推荐方法论 | `agents/chat/knowledge/SKILL.md` |
| 预设要求（过敏、设置） | `agents/chat/knowledge/references/profile.json` |
| 餐厅目录（12 家合成数据） | `agents/chat/knowledge/references/restaurants.json` |
| 点单历史（12 次会话） | `agents/chat/knowledge/references/order_history.json` |
| 用后评价（9 条） | `agents/chat/knowledge/references/feedback.json` |

> 数据的规范副本放在 `agents/chat/knowledge/`（部署打包一定会带上 handler 旁边的文件，
> 但不一定带 dot 目录），冷启动时自动物化到 `{cwd}/.claude/skills/food-concierge/`。

## 环境变量

| 变量 | 必填 | 说明 |
|------|------|------|
| `AI_GATEWAY_API_KEY` | 是 | 模型网关 Key（Makers Models API Key 或兼容服务商） |
| `AI_GATEWAY_BASE_URL` | 是 | 网关地址，Makers Models 用 `https://ai-gateway.edgeone.link/v1` |
| `AI_GATEWAY_MODEL` | 否 | 模型 ID，默认 `@makers/deepseek-v4-flash`（免费内置） |

## 本地开发

```bash
npm install
pip install -r agents/requirements.txt
cp .env.example .env       # 填入 AI_GATEWAY_API_KEY / AI_GATEWAY_BASE_URL
edgeone makers dev
```

演示流程见 [`DEMO_SCRIPT.md`](./DEMO_SCRIPT.md)，产品需求见 [`docs/PRD.md`](./docs/PRD.md)。

## License

MIT.
