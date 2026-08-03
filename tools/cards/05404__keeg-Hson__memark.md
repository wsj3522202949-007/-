---
id: tool-05404
type: tool
area: 库
status: active
tags: [去AI味, JavaScript, 协议宽松, 需API密钥, 英文文档]
title: memark
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/keeg-hson/memark
created: 2026-07-18
updated: 2026-07-18
no: 5404
category: 一、去 AI 味 / Humanizer 库
repo: keeg-Hson/memark
stars: 0
url: https://github.com/keeg-hson/memark
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# keeg-Hson/memark

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/keeg-hson/memark
- **Stars**：0
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：LLM text humanizer that will take user input (personal data files), and seed findings into LLM providers (Claude, ChatGPT) in order to word outputs in the very cadence of the end user.
- **本地描述**：LLM text humanizer that will take user input (personal data files), and seed findings into LLM providers (Claude, ChatGPT) in order to word outputs in the very cadence of the end user.
- **拉取时间**：2026-07-25 18:17:19

---

# memark
Paste samples of your writing. Get a system prompt that makes any LLM sound exactly like you.

<img width="1223" height="734" alt="Screen Shot 2026-03-11 at 1 50 13 AM" src="https://github.com/user-attachments/assets/f5032a58-6440-4e45-9f1d-52005aaee077" />


## Quick Start

### 1. Backend
```bash
cd backend
cp .env.example .env
# Open .env and add your ANTHROPIC_API_KEY
npm install
npm run dev
```

### 2. Frontend (new terminal)
```bash
cd frontend
npm install
npm run dev
```

### 3. Open http://localhost:5173

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## What you need
- Node.js 18+
- An Anthropic API key → https://console.anthropic.com

## How it works
1. Paste 1–5 samples of your own writing (emails, essays, messages, etc)
2. Memark sends them to Claude (or OpenAI) with a style analysis meta-prompt
3. Claude returns a structured style fingerprint
4. A second pass converts the fingerprint into a ready-to-use system prompt + style guide
5. Drop the system prompt into ChatGPT custom instructions, a Claude Project, or any LLM

## Project structure
```
memark/
├── backend/
│   ├── server.js
│   ├── routes/         analyze.js, generate.js
│   ├── services/       styleAnalysis.js, promptGenerator.js
│   └── prompts/        styleAnalysis.js  ← meta-prompts live here
└── frontend/
    └── src/
        ├── pages/      SeedPage.jsx, OutputPage.jsx
        ├── hooks/      useGhostwriter.js
        └── lib/        api.js
```
