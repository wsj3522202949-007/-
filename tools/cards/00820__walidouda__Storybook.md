---
id: tool-00820
type: tool
area: 库
status: active
tags: [TTS, TypeScript, 协议未明, 需API密钥, 英文文档]
title: Storybook
summary: 小说转语音/有声书
source: https://github.com/walidouda/storybook
created: 2026-07-18
updated: 2026-07-18
no: 820
category: 二、网文 / 长篇 AI 写作系统 库
repo: walidouda/Storybook
stars: 0
url: https://github.com/walidouda/storybook
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# walidouda/Storybook

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/walidouda/storybook
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI Storybook generator 
- **本地描述**：AI Storybook generator
- **拉取时间**：2026-07-23 23:02:57

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Storybook AI

This repository contains a Next.js application that can turn a short prompt
into a complete ten‑page storybook.  It uses OpenAI's generative models to
produce narrative text, page illustrations, and narration audio.  The app
provides a simple web interface where you can:

* Input a prompt and generate a structured story (title plus exactly ten pages).
* Generate images for each page using the latest image model (`gpt-image-1`).
* Generate narration audio per page via the text‑to‑speech model (`gpt-4o-mini-tts`).
* Preview the pages side‑by‑side with their illustrations.
* Re‑roll individual page images or text passages if you're not satisfied.
* Save generated stories to local storage and reload them later.
* Export your storybook to PDF for printing or sharing.
* Export a narrated MP4 video with page‑turn sound effects and configurable
  fade/hold times.

## Getting started

1. Install dependencies and run the development server:

   ```bash
   npm install
   npm run dev
   ```

2. Create a `.env.local` file in the project root with your OpenAI API key:

   ```
   OPENAI_API_KEY=sk‑...
   ```

3. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Notes

* This project uses experimental OpenAI models (`gpt-4o-mini`, `gpt-image-1`,
  `gpt-4o-mini-tts`) via the official SDK.  You must have access to these
  models on your account for the endpoints to work.
* Video export is implemented entirely client‑side using FFmpeg compiled to
  WebAssembly.  As a result it can be slow and memory intensive.  Adjust
  the hold and fade times to balance quality and performance.
* The code provided here is intended as a starting point.  Feel free to
  customise the UI, add additional styles or themes, and extend the API.

## License

This project is provided under the MIT license.
