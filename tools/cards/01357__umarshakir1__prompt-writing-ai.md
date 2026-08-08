---
id: tool-01357
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: prompt-writing-ai
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/umarshakir1/prompt-writing-ai
created: 2026-07-18
updated: 2026-07-18
no: 1357
category: 二、网文 / 长篇 AI 写作系统 库
repo: umarshakir1/prompt-writing-ai
stars: 0
url: https://github.com/umarshakir1/prompt-writing-ai
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 2d7c4de4eaa56e09
  - methods/最强写作方法论_全球最强综合版.md
---

# umarshakir1/prompt-writing-ai

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/umarshakir1/prompt-writing-ai
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：umarshakir1/prompt-writing-ai
- **拉取时间**：2026-07-23 23:18:41

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Prompt Writer AI

A single-page AI-powered prompt writing tool built with HTML + PHP, using the [OpenRouter](https://openrouter.ai) API.

## Features

- **Write Prompt** — Describe an idea and get a fully crafted AI prompt
- **Analyze URL** — Paste any website URL and generate a prompt capturing its style, tone, and purpose
- **Analyze Image** — Upload an image and get a regeneration prompt for Midjourney / DALL-E / Stable Diffusion

## Setup

1. Clone the repo into your XAMPP `htdocs` folder:
   ```bash
   git clone https://github.com/umarshakir1/prompt-writing-ai.git
   ```
2. Start Apache in XAMPP
3. Open `http://localhost/prompt-writing-ai` in your browser

## Configuration

Edit `api.php` and replace the `$OPENROUTER_API_KEY` value with your own key from [openrouter.ai/keys](https://openrouter.ai/keys).

## Tech Stack

- Frontend: HTML, TailwindCSS (CDN), Vanilla JS
- Backend: PHP (XAMPP)
- AI: OpenRouter API (free models)
