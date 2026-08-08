---
id: tool-01679
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: ai-story-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/armacintosh/ai-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1679
category: 二、网文 / 长篇 AI 写作系统 库
repo: armacintosh/ai-story-generator
stars: 1
url: https://github.com/armacintosh/ai-story-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 4b31b68ff059def6
  - methods/最强写作方法论_全球最强综合版.md
---

# armacintosh/ai-story-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/armacintosh/ai-story-generator
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：turn what happend today into a bedtime story
- **本地描述**：turn what happend today into a bedtime story
- **拉取时间**：2026-07-23 23:28:00

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI Story Generator

Try it here https://bedtimestorygenerator.netlify.app/

This project is an AI-powered story generator that creates unique children's stories based on user input. It uses React, TypeScript, and the Google Generative AI API to generate story content and images.

## Features

- Generate unique stories based on user input
- AI-generated images for each story page
- Speech recognition for story input
- Responsive design with Tailwind CSS

## Getting Started

1. Clone the repository
2. Install dependencies: `npm install`
3. Create a `.env` file in the root directory and add your Google API key:
   ```
   VITE_GOOGLE_API_KEY=your_google_api_key_here
   ```
4. Run the development server: `npm run dev`

## Building for Production

To build the project for production, run:

```
npm run build
```

This will create a `dist` folder with the compiled assets.

## Technologies Used

- React
- TypeScript
- Vite
- Tailwind CSS
- Google Generative AI
- Lucide React (for icons)

## License

This project is open source and available under the MIT License.
