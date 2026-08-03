---
id: tool-01581
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: autopipe
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/mauriciogirardi/autopipe
created: 2026-07-18
updated: 2026-07-18
no: 1581
category: 二、网文 / 长篇 AI 写作系统 库
repo: mauriciogirardi/autopipe
stars: 0
url: https://github.com/mauriciogirardi/autopipe
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# mauriciogirardi/autopipe

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/mauriciogirardi/autopipe
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Autopipe is a visual workflow automation platform that lets you connect your favorite apps and automate repetitive tasks — without writing a single line of code.
- **本地描述**：Autopipe is a visual workflow automation platform that lets you connect your favorite apps and automate repetitive tasks — without writing a single line of code.
- **拉取时间**：2026-07-23 23:25:11

---

<div align="center">
  <img src=".github/autopipe-logo.svg" width="600"/>
</div>


### What is Autopipe?
**Autopipe** is a visual workflow automation platform that lets you connect your favorite apps and automate repetitive tasks — without writing a single line of code.

Built around an intuitive drag-and-drop canvas, Autopipe lets you create automation pipelines by linking triggers, actions, and integrations. Need more power? Drop in AI steps powered by OpenAI or Claude and let intelligence handle the logic.

Think of it as your own automation layer — faster and more affordable than Zapier, more approachable than n8n.

</br>
</br>
</br>

### Features
 
- 🎨 **Visual canvas** — drag-and-drop workflow builder with real-time preview
- ⚡ **Multiple triggers** — webhooks, schedules, form submissions, and app events
- 🤖 **AI-powered steps** — native integrations with OpenAI and Claude
- 🔌 **App integrations** — Gmail, Slack, Notion, Stripe, Google Sheets, and more
- 🔁 **Background execution** — robust job queue system for reliable workflow runs
- 📊 **Real-time monitoring** — execution logs, error tracking, and status dashboard
- 🔐 **Authentication** — secure user accounts with role-based access
- 💳 **Subscription plans** — Free, Pro, and Team tiers powered by Stripe
- 🚧 **Paywalls & usage limits** — built-in billing gates per plan

 
</br>
</br>
</br>

### Tech Stack
 
| Layer | Technology |
|---|related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| Framework | Next.js  (App Router) |
| Language | TypeScript |
| Database | PostgreSQL + Prisma ORM |
| Auth | Clerk |
| Payments | Stripe |
| Job Queue | Inngest |
| AI | OpenAI SDK / Anthropic SDK |
| Styling | Tailwind CSS |
| Error Tracking | Sentry |
| Deployment | Vercel |
 
</br>
</br>
</br>

### Roadmap
 
- [x] Project setup & authentication
- [x] Visual canvas (drag-and-drop)
- [x] Workflow triggers & actions
- [x] AI integrations (OpenAI / Claude)
- [x] Background job execution
- [x] Subscription & billing (Stripe)
- [ ] More app integrations
- [ ] Team workspaces
- [ ] Workflow templates marketplace
- [ ] Analytics dashboard
