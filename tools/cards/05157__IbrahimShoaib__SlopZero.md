---
id: tool-05157
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 去AI味]
title: SlopZero
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/ibrahimshoaib/slopzero
created: 2026-07-18
updated: 2026-07-18
no: 5157
category: 一、去 AI 味 / Humanizer 库
repo: IbrahimShoaib/SlopZero
stars: 0
url: https://github.com/ibrahimshoaib/slopzero
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 45702f0a3cabf4c6
  - methods/改稿润色指令库.md
---

# IbrahimShoaib/SlopZero

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ibrahimshoaib/slopzero
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A minimalist AI text detector
- **本地描述**：A minimalist AI text detector
- **拉取时间**：2026-07-25 18:08:13

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# SlopZero

Detect the unnatural. SlopZero is a minimalist AI text detector built with Next.js and powered by Google Gemini 3. It helps writers identify and remove robotic language, overused words, and hallmark LLM patterns from their work.

## Features
- **Pattern Recognition**: Identifies common "slop" patterns (e.g., "In the ever-evolving landscape", "Not X. Not Y. Just Z.").
- **Slop Score**: Get an uncertainty score from 0-100% indicating whether the text is human or AI-generated.
- **Detailed Reasoning**: Markdown-rendered, detailed explanation behind why a block of text was flagged or cleared.

## Tech Stack
- Frontend: Next.js (App Router), React, Tailwind CSS v4, Motion (Framer Motion)
- Backend API: Next.js Serverless API Routes
- AI Model: Google Gemini via `@google/genai`

## Getting Started

1. Copy `.env.local.example` to `.env.local` and add your Gemini API Key:
   ```bash
   GEMINI_API_KEY=your_api_key_here
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.
