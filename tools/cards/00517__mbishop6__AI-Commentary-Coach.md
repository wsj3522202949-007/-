---
id: tool-00517
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: AI-Commentary-Coach
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/mbishop6/ai-commentary-coach
created: 2026-07-18
updated: 2026-07-18
no: 517
category: 二、网文 / 长篇 AI 写作系统 库
repo: mbishop6/AI-Commentary-Coach
stars: 1
url: https://github.com/mbishop6/ai-commentary-coach
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# mbishop6/AI-Commentary-Coach

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/mbishop6/ai-commentary-coach
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A game designed to help students master the art of writing effective commentary for rhetorical synthesis essays. Users write commentary based on a provided prompt and evidence, and an AI-powered coach provides instant, actionable feedback.
- **本地描述**：A game designed to help students master the art of writing effective commentary for rhetorical synthesis essays. Users write commentary based on a provided prompt and evidence, and an AI-powered coach provides instant, actionable feedback.
- **拉取时间**：2026-07-23 22:54:07

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<div align="center">
<img width="1200" height="475" alt="GHBanner" src="https://github.com/user-attachments/assets/0aa67016-6eaf-458a-adb2-6e31a0763ed6" />
</div>

# Run and deploy your AI Studio app

This contains everything you need to run your app locally.

View your app in AI Studio: https://ai.studio/apps/drive/1F5TmXGYQ3BDUFWruy1k2GsSYZkZYZmIG

## Run Locally

**Prerequisites:**  Node.js


1. Install dependencies:
   `npm install`
2. Set the `GEMINI_API_KEY` in [.env.local](https://github.com/mbishop6/AI-Commentary-Coach/tree/main/.env.local) to your Gemini API key
3. Run the app:
   `npm run dev`
