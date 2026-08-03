---
id: tool-01191
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: rook-ai-expo
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/alwaysahmedansari/rook-ai-expo
created: 2026-07-18
updated: 2026-07-18
no: 1191
category: 二、网文 / 长篇 AI 写作系统 库
repo: alwaysahmedansari/rook-ai-expo
stars: 1
url: https://github.com/alwaysahmedansari/rook-ai-expo
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# alwaysahmedansari/rook-ai-expo

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/alwaysahmedansari/rook-ai-expo
- **Stars**：1
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A premium AI assistant built with React Native (Expo) and Gemini API, featuring context-aware intelligence, writing tools, and a human-like response system.
- **本地描述**：A premium AI assistant built with React Native (Expo) and Gemini API, featuring context-aware intelligence, writing tools, and a human-like response system.
- **拉取时间**：2026-07-23 23:13:47

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Rook AI

Rook AI is a premium AI assistant built with Expo (React Native).

Quick start

1. Copy .env.example to .env and fill in your Supabase and Gemini credentials.
2. Install dependencies:
   npm install
3. Start Expo:
   npm run start

Notes

- Do NOT commit real secrets. Use .env (local) and .env.example for reference.
- The project uses @supabase/supabase-js for Supabase integration.
- Gemini API key should be provided via GEMINI_API_KEY environment variable.
