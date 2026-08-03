---
id: tool-01230
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: Story-Generator-and-Translator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/misbah7172/story-generator-and-translator
created: 2026-07-18
updated: 2026-07-18
no: 1230
category: 二、网文 / 长篇 AI 写作系统 库
repo: misbah7172/Story-Generator-and-Translator
stars: 3
url: https://github.com/misbah7172/story-generator-and-translator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# misbah7172/Story-Generator-and-Translator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/misbah7172/story-generator-and-translator
- **Stars**：3
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：This an AI story generator and translator app.
- **本地描述**：This an AI story generator and translator app.
- **拉取时间**：2026-07-23 23:14:58

---

# Word Weaver

A modern web application built with Next.js and Tailwind CSS that offers an interactive writing experience. The application leverages AI capabilities and provides a rich text editing environment.

## Features
- Built with Next.js 13+ App Router
- Styled using Tailwind CSS for responsive design
- AI integration capabilities using Google Gemini
- Server and client components architecture
- TypeScript for type safety

## Setup

1. Install dependencies:
```bash
npm install
```

2. Create a `.env` file in the root directory and add your Google Gemini API key:
```properties
GEMINI_API_KEY=your_gemini_api_key_here
```

3. Run development server:
```bash
npx next build
npm run dev
```

## Project Structure
```
src/
  ai/         # AI integration related code
  app/        # Next.js app router pages
  components/ # React components
  hooks/      # Custom React hooks
  lib/        # Shared utilities and libraries
```

## Environment Variables

Make sure to set up the following environment variables in your `.env` file:

| Variable | Description |
|----------|----------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| GEMINI_API_KEY | Your Google Gemini API key |

> **Note**: You'll need to obtain a Google Gemini API key from the Google AI Studio to use the AI features. Never commit your API key to version control.

## License

MIT License
