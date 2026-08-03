---
id: tool-01057
type: tool
area: 库
status: active
tags: [TTS, TypeScript, 协议未明, 需API密钥, 英文文档]
title: lullo
summary: 小说转语音/有声书
source: https://github.com/morganthen/lullo
created: 2026-07-18
updated: 2026-07-18
no: 1057
category: 二、网文 / 长篇 AI 写作系统 库
repo: morganthen/lullo
stars: 1
url: https://github.com/morganthen/lullo
tier: "B"
use_case: "小说转语音/有声书"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# morganthen/lullo

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/morganthen/lullo
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered personalised bedtime story generator with text-to-speech narration. Built with Next.js, Supabase, Claude API, and ElevenLabs.
- **本地描述**：AI-powered personalised bedtime story generator with text-to-speech narration. Built with Next.js, Supabase, Claude API, and ElevenLabs.
- **拉取时间**：2026-07-23 23:09:49

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Lullo – AI Bedtime Story Generator

Lullo generates personalised, AI-voiced bedtime stories for children. A parent fills in a short form and gets back a fully narrated story in under a minute.

## How it works

1. Parent fills in child's name, age, theme, and an optional feeling to explore
2. Claude generates a custom bedtime story
3. ElevenLabs voices it with a curated narrator
4. Story plays automatically with a built-in audio player
5. Plus users can save stories to their personal library

## Tech Stack

- **Frontend** – Next.js 16, TypeScript, Tailwind CSS, Shadcn
- **Backend** – Next.js API Routes
- **Database & Auth** – Supabase (Postgres, Storage, OAuth)
- **AI** – Claude Haiku (Anthropic)
- **Text-to-Speech** – ElevenLabs
- **Payments** – Stripe (coming soon)

## Features

- Google OAuth authentication
- AI story generation via Claude API
- Text-to-speech narration via ElevenLabs
- Free tier: 3 stories per month
- Plus tier: unlimited stories + save to library
- Story library with playback and delete

## Getting Started

1. Clone the repo
2. Install dependencies: `npm install`
3. Copy `.env.local.example` to `.env.local` and fill in your keys
4. Run the dev server: `npm run dev`

## Environment Variables

NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=
SUPABASE_SERVICE_ROLE_KEY=
ANTHROPIC_API_KEY=
ELEVENLABS_API_KEY=
NEXT_PUBLIC_SITE_URL=

## Status

Active development. Core generation flow complete. Stripe integration and UI polish in progress.
