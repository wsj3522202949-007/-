---
id: tool-00223
type: tool
area: 库
status: active
tags: [去AI味, HTML, 协议未明, 需API密钥, 英文文档]
title: AI-Writing-Ratio-Reducer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/xingjiantian/ai-writing-ratio-reducer
created: 2026-07-18
updated: 2026-07-18
no: 223
category: 二、网文 / 长篇 AI 写作系统 库
repo: XingjianTian/AI-Writing-Ratio-Reducer
stars: 0
url: https://github.com/xingjiantian/ai-writing-ratio-reducer
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# XingjianTian/AI-Writing-Ratio-Reducer

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/xingjiantian/ai-writing-ratio-reducer
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：A 4 stage AI-Writing-Ratio-Reducer（Original->AI prompt rewrite->EN2CH->CH2EN）
- **本地描述**：A 4 stage AI-Writing-Ratio-Reducer（Original->AI prompt rewrite->EN2CH->CH2EN）
- **拉取时间**：2026-07-23 22:45:35

---

# AI Writing Ratio Reducer

A specialized tool to reduce AI writing detection scores through advanced LLM rewriting and back-translation logic. Optimized for high-speed streaming and human-like output.

## Key Features

-   **Gemini 1.5 Flash Stream**: Real-time rewriting with high-speed streaming feedback.
-   **Back-Translation Logic**: English <-> Chinese multi-stage humanization using Baidu Translation API.
-   **Vercel Optimized**: Ready-to-deploy serverless architecture with robust routing.
-   **Real-time Metrics**: Word and character counts for precise API management.

## Deployment & Configuration

### Required Environment Variables

Set these in your Vercel Dashboard or local `.env` file:

| Variable | Description |
| :--- | :related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
--- |
| `GOOGLE_API_KEY` | Your Google Gemini API Key |
| `BAIDU_APP_ID` | Your Baidu Translation App ID |
| `BAIDU_SECRET_KEY` | Your Baidu Translation Secret Key |
| `GEMINI_PROMPT_BASE` | The system prompt base for the rewriting task |

### Vercel Deployment

This project is configured for Vercel Serverless Functions. Simply push to GitHub and link your project, or use the Vercel CLI:

```bash
vercel --prod
```

### Local Development

1. Install [Bun](https://bun.sh/).
2. `bun install`
3. Create a `.env` file with the required variables.
4. `bun dev`
5. Open `http://localhost:3000`.

## Tech Stack

-   **Backend**: Bun, Express, TypeScript
-   **Frontend**: Tailwind CSS, Vanilla JS
-   **Infrastructure**: Vercel Serverless Functions
-   **APIs**: Google Gemini AI, Baidu Translation
