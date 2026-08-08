---
id: tool-00540
type: tool
area: 库
status: active
tags: [TTS, TypeScript, 协议未明, 需API密钥, 英文文档]
title: Granny-AI
summary: 小说转语音/有声书
source: https://github.com/amalkrishnaas/granny-ai
created: 2026-07-18
updated: 2026-07-18
no: 540
category: 二、网文 / 长篇 AI 写作系统 库
repo: AmalkrishnaAS/Granny-AI
stars: 1
url: https://github.com/amalkrishnaas/granny-ai
tier: "B"
use_case: "小说转语音/有声书"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: dcf848a573157473
  - methods/最强写作方法论_全球最强综合版.md
---

# AmalkrishnaAS/Granny-AI

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/amalkrishnaas/granny-ai
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI Bedtime story generator with Gemini 2.0 and stable diffusion
- **本地描述**：AI Bedtime story generator with Gemini 2.0 and stable diffusion
- **拉取时间**：2026-07-23 22:54:47

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Granny-AI

AI Bedtime story generator using Gemini 2.0 and Stable diffusion

## Tech Stack

- Next JS 14 - App Router
- shadcn/ui (UI components)
- Convex (Database / Backend)
- Gemini 2.0 (Content Generation)
- CompVis/stable-diffusion-v1-4 (Image Generation)
- React Icons (Icons)
- Tailwind CSS (Styling)
- Clerk (Authentication and User Management)

## Features

- [x] Authentication
- [x] CRUD Operations
- [x] Content Generation
- [x] Cover Image Generation
- [ ] Fork Story
- [ ] Customise Prompts from existing stories to generate new ones
- [ ] Dark Mode
- [ ] Vector Similarity based Recomendations
- [ ] Text to Speech

## Environment Variables

Set the following variables in your `.env` file

```python
NEXT_PUBLIC_GEMINI_API_KEY=
NEXT_PUBLIC_HUGGINGFACE_API_KEY=

# Deployment used by `npx convex dev`
CONVEX_DEPLOYMENT=d
NEXT_PUBLIC_CONVEX_URL=
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=
CLERK_SECRET_KEY=

NEXT_PUBLIC_CLERK_SIGN_IN_URL=
NEXT_PUBLIC_CLERK_SIGN_UP_URL=
CLERK_WEBHOOK_SECRET
```

## Run in Local

### Frontend

```bash
bun install
```

### Backend (Convex)

```bash
bunx convex dev
bunx convex dashboard #to open the WebUI
```
