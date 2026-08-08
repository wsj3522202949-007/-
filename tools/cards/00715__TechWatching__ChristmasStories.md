---
id: tool-00715
type: tool
area: 库
status: active
tags: [C#, 协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: ChristmasStories
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/techwatching/christmasstories
created: 2026-07-18
updated: 2026-07-18
no: 715
category: 二、网文 / 长篇 AI 写作系统 库
repo: TechWatching/ChristmasStories
stars: 1
url: https://github.com/techwatching/christmasstories
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: ff1e0f7319803018
  - methods/最强写作方法论_全球最强综合版.md
---

# TechWatching/ChristmasStories

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/techwatching/christmasstories
- **Stars**：1
- **语言**：C#
- **License**：MIT
- **Topics**：aspire, blazor, dotnet, github-models, minimal-api
- **GitHub 描述**：🎄 AI-powered Christmas story generator for children. Create personalized, heartwarming bedtime stories with customizable characters, settings, and objects. Built with .NET Aspire, Blazor, and GitHub Models.
- **本地描述**：🎄 AI-powered Christmas story generator for children. Create personalized, heartwarming bedtime stories with customizable characters, settings, and objects. Built with .NET Aspire, Blazor, and GitHub Models.
- **拉取时间**：2026-07-23 22:59:53

---

# 🎄 Christmas Story Generator

Create magical, personalized Christmas stories for young children using AI.

[![.NET](https://img.shields.io/badge/.NET-10.0-512BD4?style=flat-square&logo=dotnet)](https://dotnet.microsoft.com/)
[![Aspire](https://img.shields.io/badge/Aspire-13.1-512BD4?style=flat-square)](https://learn.microsoft.com/dotnet/aspire/)
[![Blazor](https://img.shields.io/badge/Blazor-Server-512BD4?style=flat-square)](https://dotnet.microsoft.com/apps/aspnet/web-apps/blazor)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

[Features](#features) • [Getting Started](#getting-started) • [Run the App](#run-the-app) • [Architecture](#architecture) • [Resources](#resources)

![Christmas Story Generator](https://img.shields.io/badge/AI_Powered-GPT--4o_mini-10a37f?style=for-the-badge&logo=openai&logoColor=white)

</div>

A delightful web application that generates personalized Christmas stories for 5-year-old children. Parents and caregivers can select or customize story elements—characters, settings, objects, and actions—then let AI create a unique, heartwarming tale perfect for bedtime reading.

## Features

- **Curated Story Elements** - Choose from pre-selected characters (curious penguin, brave little girl, friendly snowman), settings (Santa's workshop, cozy cabin, enchanted forest), objects (glowing star, magic cookies, golden sleigh bell), and optional actions
- **Custom Input** - Add your own story elements for a truly personalized experience (child's name, favorite toy, family traditions)
- **Age-Appropriate Content** - Stories are crafted for 5-year-olds with simple vocabulary, positive themes, and gentle lessons about kindness and friendship
- **Perfect Reading Length** - Each story is 750-1500 words (5-10 minutes reading time)
- **Real-time Generation** - Watch the magic happen with AI-powered story creation

![Christmas Story Generator website](https://github.com/TechWatching/ChristmasStories/blob/main/docs/website_01.png)

## Getting Started

### Prerequisites

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0)
- [GitHub account](https://github.com/) with a [Personal Access Token](https://github.com/settings/tokens) for GitHub Models
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (optional, for containerized dependencies)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ChristmasStories.git
   cd ChristmasStories
   ```

2. **Configure GitHub Models API Key**
   
   The application uses GitHub Models for AI story generation. You need to configure your GitHub token:
   
   ```bash
   # Set as user secret for the AppHost project
   cd ChristmasStories.AppHost
   dotnet user-secrets set "Parameters:chat-gh-apikey" "your-github-token"
   ```

   > [!TIP]
   > Get your GitHub token from [GitHub Settings > Developer Settings > Personal Access Tokens](https://github.com/settings/tokens). The token needs access to GitHub Models.

## Run the App

This project uses [.NET Aspire](https://learn.microsoft.com/dotnet/aspire/) to orchestrate all services.

```bash
# From the repository root
aspire run
```

The Aspire dashboard will open automatically, showing all running services:
- **Web Frontend** - The Blazor web application at `https://localhost:7134`
- **API Service** - The story generation API at `https://localhost:7312`
- **Dev Tunnel** - For sharing your app externally (optional)

> [!NOTE]
> The first story generation may take 10-30 seconds as the AI model processes your request. Subsequent requests are typically faster.

### Development

To run use `aspire run` in the root of the repository.

```bash
aspire run
```

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     .NET Aspire AppHost                      │
│                    (Orchestration Layer)                     │
└─────────────────────────────────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│   Web Frontend  │  │   API Service   │  │  GitHub Models  │
│    (Blazor)     │──│   (Minimal API) │──│   (GPT-4o-mini) │
│                 │  │                 │  │                 │
│ • Story Builder │  │ • /api/story/*  │  │ • AI Generation │
│ • Story Display │  │ • Story Service │  │ • Chat API      │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

### Projects

| Project | Description |
|---------|-------------|
| `ChristmasStories.AppHost` | Aspire orchestration - configures and runs all services |
| `ChristmasStories.Web` | Blazor Server frontend with interactive story builder |
| `ChristmasStories.ApiService` | Minimal API backend with story generation endpoints |
| `ChristmasStories.ServiceDefaults` | Shared service configurations (telemetry, health checks) |

### Key Technologies

- **.NET 10** - Latest .NET runtime and SDK
- **.NET Aspire** - Cloud-native orchestration and observability
- **Blazor Server** - Interactive web UI with server-side rendering
- **Microsoft.Extensions.AI** - Unified AI abstraction layer
- **GitHub Models** - AI model hosting (GPT-4o-mini)

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|----------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| `GET` | `/api/story/presets` | Get available story element presets |
| `POST` | `/api/story/generate` | Generate a new Christmas story |
| `GET` | `/health` | Health check endpoint |

### Generate Story Request

```json
{
  "character": "A curious penguin named Pip",
  "setting": "Santa's workshop at the North Pole",
  "object": "A mysterious gift box that won't open",
  "action": "Helping someone in need"
}
```

## Resources

- [.NET Aspire Documentation](https://learn.microsoft.com/dotnet/aspire/)
- [Blazor Documentation](https://learn.microsoft.com/aspnet/core/blazor/)
- [Microsoft.Extensions.AI](https://devblogs.microsoft.com/dotnet/introducing-microsoft-extensions-ai-preview/)
- [GitHub Models](https://docs.github.com/en/github-models)
