---
id: tool-00432
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: HiStory
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/rei-x/history
created: 2026-07-18
updated: 2026-07-18
no: 432
category: 二、网文 / 长篇 AI 写作系统 库
repo: Rei-x/HiStory
stars: 1
url: https://github.com/rei-x/history
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
content_hash: 1134e5f0a642a9f8
  - methods/最强写作方法论_全球最强综合版.md
---

# Rei-x/HiStory

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/rei-x/history
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：ai, chakra-ui, firebase, generator, gpt-3, hackathon, hackyeah, mvp, react
- **GitHub 描述**：AI quiz generator for resources from IPN database
- **本地描述**：AI quiz generator for resources from IPN database
- **拉取时间**：2026-07-23 22:51:42

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<p align="center">
  <img src="https://user-images.githubusercontent.com/38581479/203157467-63fbd218-c41d-4abd-a507-87297169e945.gif" alt="Hero" />
</p>

# HiStory                             

HiStory is a web application that allows you to easily generate quizzes (using artificial intelligence) based on historical articles from the Institute of National Memory database. It is intended to serve as a teaching aid in conveying knowledge.

This app won second place in the quiz generator category at Hackyeah 2022

Presentation of the product:
https://www.canva.com/design/DAFSZ0oMjxg/loEnpZpBDWJbTfxvVTcUqw/view

## How to run it?

1. Create .env.local file based on .env.example and add your OpenAI api token.
2. `pnpm i`
3. `pnpm dev`
