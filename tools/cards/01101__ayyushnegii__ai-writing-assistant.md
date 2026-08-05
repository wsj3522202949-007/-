---
id: tool-01101
type: tool
area: 库
status: active
tags: [TypeScript, 协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: ai-writing-assistant
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/ayyushnegii/ai-writing-assistant
created: 2026-07-18
updated: 2026-07-18
no: 1101
category: 二、网文 / 长篇 AI 写作系统 库
repo: ayyushnegii/ai-writing-assistant
stars: 0
url: https://github.com/ayyushnegii/ai-writing-assistant
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# ayyushnegii/ai-writing-assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ayyushnegii/ai-writing-assistant
- **Stars**：0
- **语言**：TypeScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI-powered writing assistant with prompt building capabilities
- **本地描述**：AI-powered writing assistant with prompt building capabilities
- **拉取时间**：2026-07-23 23:11:08

---

# AI Writing Assistant

An AI-powered productivity tool built with Next.js, TypeScript, and Tailwind CSS. Features include an AI Prompt Builder and Writing Assistant to help you create better content faster.

![GitHub stars](https://img.shields.io/github/stars/ayyushnegii/ai-writing-assistant?style=social)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

## 🚀 Features

### AI Prompt Builder
- Generate optimized prompts for any task
- Select from multiple AI models (OpenRouter supported)
- Choose output formats (Markdown, JSON, Plain Text)
- Copy prompts to clipboard with one click

### AI Writing Assistant
- Grammar & spelling correction
- Style improvement suggestions
- Content expansion and shortening
- Tone adjustment for professional communication
- Real-time AI-powered feedback

## 🛠️ Tech Stack

- **Framework**: Next.js 15 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS (Dark Neon Theme)
- **AI Provider**: OpenRouter (supports 200+ models)
- **Deployment**: Vercel-ready

## 📦 Setup Instructions

### 1. Prerequisites
- Node.js 18+ (you have v22.22.2 installed)
- OpenRouter API key ([get one free here](https://openrouter.ai/keys))

### 2. Clone the repo
```bash
git clone https://github.com/ayyushnegii/ai-writing-assistant.git
cd ai-writing-assistant
```

### 3. Install dependencies (when you have good internet)
```bash
npm install
```

### 4. Configure environment variables
```bash
cp .env.example .env.local
```
Then edit `.env.local` and add your OpenRouter API key:
```
OPENROUTER_API_KEY=your_actual_api_key_here
```

### 5. Run locally
```bash
npm run dev
```
Open [http://localhost:3000](http://localhost:3000) in your browser.

## 🌐 Deployment

This project is ready to deploy on Vercel:

1. Push your changes to GitHub
2. Go to [Vercel](https://vercel.com)
3. Import your `ai-writing-assistant` repository
4. Add the `OPENROUTER_API_KEY` environment variable
5. Deploy!

## 📝 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENROUTER_API_KEY` | Yes | Your OpenRouter API key for AI model access |

## 🤝 Contributing

Contributions welcome! Feel free to open issues or pull requests.

## 📄 License

MIT License - see `[LICENSE](LICENSE)` file for details.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

Built by [Ayush Negi](https://github.com/ayyushnegii) as part of his portfolio demonstrating AI workflow integration.
