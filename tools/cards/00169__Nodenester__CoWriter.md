---
id: tool-00169
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: CoWriter
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/nodenester/cowriter
created: 2026-07-18
updated: 2026-07-18
no: 169
category: 二、网文 / 长篇 AI 写作系统 库
repo: Nodenester/CoWriter
stars: 0
url: https://github.com/nodenester/cowriter
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
  - "⚠️ 仓库疑似停更/归档，bug 不会修、依赖可能过期"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Nodenester/CoWriter

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/nodenester/cowriter
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI writing copilot — API + Chrome extension + Google Docs extension (Jan-Feb 2023)
- **本地描述**：AI writing copilot — API + Chrome extension + Google Docs extension (Jan-Feb 2023)
- **拉取时间**：2026-07-23 22:43:56

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# CoWriter

> **Archived** -- This project is no longer maintained.

Built January--February 2023.

An AI-powered writing copilot that suggests sentence completions as you type in any text field on the web. One of the earliest AI writing assistants, built when the OpenAI API had just become widely accessible.

## What it does

- **Chrome Extension** injects into any webpage, detects the active text input (standard inputs, textareas, and contentEditable elements), and displays ghost-text completion suggestions inline -- triggered via keyboard shortcut (Ctrl+B)
- **Backend API** (C#/.NET 7) receives partial text and optional context, calls the OpenAI Completions API (GPT-3.5 Turbo), and returns the suggested continuation
- **Google Extension** variant adds Firebase Authentication (Google sign-in) so usage could be tied to user accounts

The extension wraps the active input element in a container and uses CSS pseudo-element overlays (`::after` with `data-placeholder`) to render suggestion text that visually continues from the cursor position without modifying the actual input value.

## Project structure

```
CoWriterApi/              C#/.NET 7 Web API -- sentence completion endpoint using OpenAI
CoWriter-Extention1.0/    Chrome extension with Firebase Auth (login flow)
CoWriter-GoogleExtention/  Chrome extension variant with Firebase + Google Docs support
CoWriterTextEditor/       Core text editor extension -- inline ghost-text suggestions
JustTextModifier/         Minimal standalone text modifier extension (early prototype)
Test-GoogleExtention/     Test version of the extension
test-4-FirebasAuth/       Firebase Auth integration test
```

## Tech stack

- **API**: C# / .NET 7, ASP.NET Core Web API, Swagger/OpenAPI
- **AI**: OpenAI GPT-3.5 Turbo (Completions API)
- **Extensions**: Chrome Manifest V3, vanilla JavaScript
- **Auth**: Firebase Authentication, Google OAuth2
- **Frontend**: HTML/CSS/JS (no frameworks)

## Setup

1. Add your OpenAI API key in `CoWriterApi/CoWriterApi/Controllers/SACController.cs`
2. Add your Firebase config in the extension `background.js` / `firebase.js` files
3. Load the extension in Chrome via `chrome://extensions` (Developer Mode > Load unpacked)
4. Run the API with `dotnet run` in the `CoWriterApi/CoWriterApi/` directory

## License

MIT
