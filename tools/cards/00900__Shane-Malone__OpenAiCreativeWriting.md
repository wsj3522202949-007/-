---
id: tool-00900
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: OpenAiCreativeWriting
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/shane-malone/openaicreativewriting
created: 2026-07-18
updated: 2026-07-18
no: 900
category: 二、网文 / 长篇 AI 写作系统 库
repo: Shane-Malone/OpenAiCreativeWriting
stars: 0
url: https://github.com/shane-malone/openaicreativewriting
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Shane-Malone/OpenAiCreativeWriting

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/shane-malone/openaicreativewriting
- **Stars**：0
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Node.js web app based on OpenAI quickstart repo to generate creative writing prompts based on given topics.
- **本地描述**：Node.js web app based on OpenAI quickstart repo to generate creative writing prompts based on given topics.
- **拉取时间**：2026-07-23 23:05:18

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# OpenAI API Creative Writing

This is a creative writing prompt generator app. It uses the [Next.js](https://nextjs.org/) framework with [React](https://reactjs.org/). Check out the tutorial or follow the instructions below to get set up.

## Setup

1. If you don’t have Node.js installed, [install it from here](https://nodejs.org/en/) (Node.js version >= 14.6.0 required)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd OpenAiCreativeWriting
   ```

4. Install the requirements

   ```bash
   $ npm install
   ```

5. Make a copy of the example environment variables file

   On Linux systems: 
   ```bash
   $ cp .env.example .env
   ```
   On Windows:
   ```powershell
   $ copy .env.example .env
   ```
6. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

7. Run the app

   ```bash
   $ npm run dev
   ```

You should now be able to access the app at [http://localhost:3000](http://localhost:3000)!
