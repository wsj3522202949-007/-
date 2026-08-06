---
id: tool-00965
type: tool
area: 库
status: active
tags: [TTS, TypeScript, 协议未明, 需API密钥, 英文文档]
title: Voicebox
summary: 小说转语音/有声书
source: https://github.com/abhaydv77/voicebox
created: 2026-07-18
updated: 2026-07-18
no: 965
category: 二、网文 / 长篇 AI 写作系统 库
repo: abhaydv77/Voicebox
stars: 0
url: https://github.com/abhaydv77/voicebox
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# abhaydv77/Voicebox

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/abhaydv77/voicebox
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：ai-chatbot, database, javascript, nextauth, nextjs, react, typescript, vercel-deployment
- **GitHub 描述**：Voicebox is an AI-powered writing assistant Most AI tools leave a clear footprint they use overly balanced sentences, predictable rhythms, and a ton of generic hedge phrases. Voicebox is a writing assistant designed specifically to strip away those generic "AI tells" for social media posts. Instead of sounding like a robot 
- **本地描述**：🚧Voicebox is an AI-powered writing assistant Most AI tools leave a clear footprint they use overly balanced sentences, predictable rhythms, and a ton of generic hedge phrases. Voicebox is a writing assistant designed specifically to strip away those generic "AI tells" for social media posts. Instead of sounding like a robot
- **拉取时间**：2026-07-23 23:07:11

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# VoiceBox

AI writing has a "tell" — overly balanced sentences, generic hedge phrases,
uniform rhythm. VoiceBox exists to fix that for people who use AI to help
draft social posts (LinkedIn, X, etc.) but don't want the output to sound
like everyone else's AI-assisted post.

You create named **Voices** — style profiles built either from your own
past writing samples, or from a well-known writer's stylistic traits
(described abstractly, never reproducing their actual text). When you
write something new, VoiceBox rewrites it through that Voice, so the
output sounds like you — not like generic AI.

## How it works

1. Create a Voice from your own writing samples (or a writer's style)
2. Write a rough idea/draft of what you want to say
3. VoiceBox drafts the content, then rewrites it through your Voice's
   style profile — actively avoiding common AI-writing tells

## Tech stack

- Next.js (App Router) + TypeScript
- NextAuth v5 (Credentials provider)
- Prisma + SQLite (dev) — migrating to Postgres before production
- Gemini API (Flash model, free tier)

## Getting started

```bash
npm install
cp .env.local.example .env.local   # fill in GEMINI_API_KEY, NEXTAUTH_SECRET, etc.
npx prisma migrate dev
npm run dev
```

Visit `http://localhost:3000/voicebox`.

## Project docs

This repo is built spec-by-spec, CEO-instructs-developer style. See:

- [`VISION.md`](https://github.com/abhaydv77/Voicebox/blob/main/VISION.md) — what we're building and why
- [`CURRENTSTATE.md`](https://github.com/abhaydv77/Voicebox/blob/main/CURRENTSTATE.md) — what's actually built right now
- [`TODO.md`](https://github.com/abhaydv77/Voicebox/blob/main/TODO.md) — what's next
- [`.voicebox/README.md`](https://github.com/abhaydv77/Voicebox/blob/main/.voicebox/README.md) — how specs work
- [`.voicebox/specs/`](https://github.com/abhaydv77/Voicebox/tree/main/.voicebox/specs/) — the actual instruction history
