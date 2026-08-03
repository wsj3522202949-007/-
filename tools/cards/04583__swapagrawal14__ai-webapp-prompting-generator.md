---
id: tool-04583
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档]
title: ai-webapp-prompting-generator
summary: 本地优先、隐私可控的写作工作台
source: https://github.com/swapagrawal14/ai-webapp-prompting-generator
created: 2026-07-18
updated: 2026-07-18
no: 4583
category: 五、写作 IDE / 本地优先工作台 库
repo: swapagrawal14/ai-webapp-prompting-generator
stars: 1
url: https://github.com/swapagrawal14/ai-webapp-prompting-generator
tier: "B"
use_case: "本地优先、隐私可控的写作工作台"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# swapagrawal14/ai-webapp-prompting-generator

- **分类**：五、写作 IDE / 本地优先工作台 库
- **链接**：https://github.com/swapagrawal14/ai-webapp-prompting-generator
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Uses AI to expand a simple app idea into a detailed development prompt, complete with user stories, technical recommendations, and more. Try it now for FREE here! 👇
- **本地描述**：Uses AI to expand a simple app idea into a detailed development prompt, complete with user stories, technical recommendations, and more. Try it now for FREE here! 👇
- **拉取时间**：2026-07-25 17:49:17

related:
  - methods/QUICK_START.md
---

# Run and deploy your AI Studio app

This contains everything you need to run your app locally.

## Run Locally

**Prerequisites:**  Node.js


1. Install dependencies:
   `npm install`
2. Set the `GEMINI_API_KEY` in [.env.local](.env.local) to your Gemini API key
3. Run the app:
   `npm run dev`
