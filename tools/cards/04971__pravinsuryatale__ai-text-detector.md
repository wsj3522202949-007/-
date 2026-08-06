---
id: tool-04971
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 英文文档, 去AI味]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/pravinsuryatale/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 4971
category: 一、去 AI 味 / Humanizer 库
repo: pravinsuryatale/ai-text-detector
stars: 0
url: https://github.com/pravinsuryatale/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# pravinsuryatale/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/pravinsuryatale/ai-text-detector
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：pravinsuryatale/ai-text-detector
- **拉取时间**：2026-07-25 18:01:24

---

# Verascript — AI Text Detection Tool

A full-stack web application that analyses text for AI-generated content, with sentence-level probability scoring and an inline rewrite interface.

**Live:** https://verascript.com](https://ai-text-detector-sigma.vercel.app

---

## What it does

Paste any text and Verascript returns:

- An overall AI likelihood score with a colour-coded progress bar
- Sentence-by-sentence breakdown (high / medium / low / human)
- A plain-English verdict summary
- Inline rewrite suggestions for flagged sentences

Built as a personal project to explore full-stack AI application development and production deployment patterns.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend & API routes | Next.js 14 (App Router) |
| AI detection & rewrites | Anthropic Claude API |
| Authentication | Supabase Auth (OTP, passwordless) |
| Database | Supabase Postgres |
| Styling | Tailwind CSS |
| Deployment | Vercel (CI/CD via GitHub) |

---

## Access Model

| Tier | Analyses | Price |
|---|---|---|
| Free | 5 / month | $0 |
| Pro | Unlimited | $12 / month |

---

## Project Structure

```
app/
  ├── page.js              # Main analysis UI
  ├── layout.js            # Root layout
  ├── globals.css          # Global styles
  └── api/
      └── detect/
          └── route.js     # Claude API endpoint
```

---

## Local Setup

See [SETUP.md](https://github.com/pravinsuryatale/ai-text-detector/blob/main/SETUP.md) for full instructions.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## License

MIT
