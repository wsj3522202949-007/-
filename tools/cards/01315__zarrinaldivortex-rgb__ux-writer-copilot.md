---
id: tool-01315
type: tool
area: 库
status: active
tags: [TTS, Claude插件, TypeScript, 协议未明, 需API密钥, 英文文档]
title: ux-writer-copilot
summary: 小说转语音/有声书
source: https://github.com/zarrinaldivortex-rgb/ux-writer-copilot
created: 2026-07-18
updated: 2026-07-18
no: 1315
category: 二、网文 / 长篇 AI 写作系统 库
repo: zarrinaldivortex-rgb/ux-writer-copilot
stars: 0
url: https://github.com/zarrinaldivortex-rgb/ux-writer-copilot
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

# zarrinaldivortex-rgb/ux-writer-copilot

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/zarrinaldivortex-rgb/ux-writer-copilot
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered UX writing assistant for consistent, data-driven copy — Figma plugin
- **本地描述**：AI-powered UX writing assistant for consistent, data-driven copy — Figma plugin
- **拉取时间**：2026-07-23 23:17:27

---

# UX Writer Copilot

AI-powered UX writing assistant for consistent, data-driven copy — a Figma plugin.

## Features

- **Generate** — AI-powered copy suggestions for selected text layers, grounded in your brand voice and writing principles
- **Analyze** — 8-dimension UX writing audit (Brand Voice, Principles, CTA Clarity, Accessibility, Reading Level, Localization, Terminology, Product Consistency)
- **Brainstorm** — Multi-session AI chat with full product context loaded
- **Contexts** — Define brand voice, tone, vocabulary rules, PRD docs, personas, and writing principles per product
- **Agents** — Supports Groq, Ollama, OpenRouter, DeepSeek, Mistral, OpenAI, Anthropic, Gemini, Together AI, and custom endpoints

## Files

| File | Description |
|------|-------------|
| `manifest.json` | Plugin manifest (name, id, editor type, relaunch buttons) |
| `code.ts` | Plugin sandbox code — Figma API calls, text layer detection, font loading |
| `ui.html` | Plugin UI panel — all tabs, AI calls, context/brainstorm/analyze |
| `icon.svg` | Plugin icon |

> **Note:** `ui.html` is the main UI file (~180KB). To get the full source, pull directly from Figma:
> ```
> figma plugin pull d97113ef-c6a0-4b61-b0c3-c64c0824de4f
> ```
> This requires the [Figma CLI](https://www.figma.com/developers/api) with appropriate credentials.

## Setup

1. Open the plugin in Figma
2. Go to the **Contexts** tab and create a Product Context with your brand voice, tone, and writing principles
3. Go to the **Agents** tab and select your AI provider + enter your API key (session-only, never stored)
4. Select text layers or a frame, then use **Generate** to get AI copy suggestions

## Security

API keys are **session-only** — they are never stored between sessions. The plugin source is stored inside the Figma file, so no credentials are ever embedded in the code.

## Supported AI Providers

| Provider | Free Tier | Notes |
|----------|-----------|----related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| Groq | Yes | Llama 3.3 70B, DeepSeek R1, Llama 4 Scout |
| Ollama | Local | 100% private, offline |
| OpenRouter | Yes | Dozens of free models |
| DeepSeek | Yes | V3 & R1 — near-zero cost |
| Mistral AI | Yes | Small, Large, Codestral |
| OpenAI | Paid | GPT-4.1 Mini, GPT-4.1, GPT-4o |
| Anthropic | Paid | Claude Haiku, Sonnet, Opus |
| Gemini | Yes | 2.0 Flash, 2.5 Flash |
| Together AI | Yes | Free credits |
| Custom | — | Any OpenAI-compatible endpoint |

## Plugin ID

`d97113ef-c6a0-4b61-b0c3-c64c0824de4f`
