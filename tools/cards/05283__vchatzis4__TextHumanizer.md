---
id: tool-05283
type: tool
area: 库
status: active
tags: [去AI味, C#, 协议未明, 需API密钥, 英文文档]
title: TextHumanizer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/vchatzis4/texthumanizer
created: 2026-07-18
updated: 2026-07-18
no: 5283
category: 一、去 AI 味 / Humanizer 库
repo: vchatzis4/TextHumanizer
stars: 1
url: https://github.com/vchatzis4/texthumanizer
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: f5f5fcb429fe37d0
  - methods/改稿润色指令库.md
---

# vchatzis4/TextHumanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/vchatzis4/texthumanizer
- **Stars**：1
- **语言**：C#
- **License**：None
- **Topics**：—
- **GitHub 描述**：A full-stack .NET 8 app that humanizes AI-generated text and detects AI-written content using LLM providers (Groq/LmStudio).
- **本地描述**：A full-stack .NET 8 app that humanizes AI-generated text and detects AI-written content using LLM providers (Groq/LmStudio).
- **拉取时间**：2026-07-25 18:12:51

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# TextHumanizer

A web application that humanizes AI-generated text and detects AI-written content.

## Features

- **Humanize Text** - Transform robotic AI-generated text into natural, human-sounding prose
- **Detect AI Text** - Analyze text to determine the probability it was written by AI

Supports **English** and **Greek** languages.

## Tech Stack

- **Backend:** ASP.NET Core 8 Web API
- **Frontend:** Blazor WebAssembly
- **LLM Provider:** Groq (llama-3.3-70b-versatile)

## Live Demo

- **App:** https://texthumanizer.up.railway.app
- **API:** https://texthumanizerapi-production.up.railway.app

## Local Development

### Prerequisites

- .NET 8 SDK
- Groq API key ([get one here](https://console.groq.com))

### Setup

1. Clone the repository
   ```bash
   git clone https://github.com/vchatzis4/TextHumanizer.git
   cd TextHumanizer
   ```

2. Copy the template config
   ```bash
   cp appsettings.template.json appsettings.json
   ```

3. Add your Groq API key to `appsettings.json`

4. Run the API
   ```bash
   dotnet run
   ```

5. Run the UI (in a separate terminal)
   ```bash
   cd TextHumanizer.UI
   dotnet run
   ```

6. Open http://localhost:5054 (API) and the Blazor UI port

## Deployment

Deployed on Railway with Docker. See `Dockerfile` and `TextHumanizer.UI/Dockerfile`.

Environment variables needed:
- `ASPNETCORE_ENVIRONMENT=Production`
- `GROQ_API_KEY=your_api_key`

## License

MIT
