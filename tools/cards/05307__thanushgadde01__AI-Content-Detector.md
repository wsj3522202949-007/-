---
id: tool-05307
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 英文文档, 去AI味]
title: AI-Content-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/thanushgadde01/ai-content-detector
created: 2026-07-18
updated: 2026-07-18
no: 5307
category: 一、去 AI 味 / Humanizer 库
repo: thanushgadde01/AI-Content-Detector
stars: 1
url: https://github.com/thanushgadde01/ai-content-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# thanushgadde01/AI-Content-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/thanushgadde01/ai-content-detector
- **Stars**：1
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：10. The AI Content Detective (Text, Image, & Video)  ● The Problem: As AI content becomes more realistic, it is increasingly difficult to tel if a  video, image, or article was made by a human or a machine. Single-model detectors often  fail because they only look at one thing (like text style).  ● The Goal: Build a unified system that can take any
- **本地描述**：10. The AI Content Detective (Text, Image, & Video)  ● The Problem: As AI content becomes more realistic, it is increasingly difficult to tel if a  video, image, or article was made by a human or a machine. Single-model detectors often  fail because they only look at one thing (like text style).  ● The Goal: Build a unified system that can take any
- **拉取时间**：2026-07-25 18:13:45

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

<div align="center">
<img width="1200" height="475" alt="GHBanner" src="https://github.com/user-attachments/assets/0aa67016-6eaf-458a-adb2-6e31a0763ed6" />
</div>

# Run and deploy your AI Studio app

This contains everything you need to run your app locally.

View your app in AI Studio: https://ai.studio/apps/c6203bf7-e611-4c1e-97b3-8a9d50933e19

## Run Locally

**Prerequisites:**  Node.js


1. Install dependencies:
   `npm install`
2. Set the `GEMINI_API_KEY` in `[.env.local](.env.local)` to your Gemini API key
3. Run the app:
   `npm run dev`
