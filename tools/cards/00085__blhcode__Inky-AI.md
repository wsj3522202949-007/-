---
id: tool-00085
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Inky-AI
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/blhcode/inky-ai
created: 2026-07-18
updated: 2026-07-18
no: 85
category: 二、网文 / 长篇 AI 写作系统 库
repo: blhcode/Inky-AI
stars: 0
url: https://github.com/blhcode/inky-ai
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: ac761d8ec4ab8fb1
  - methods/最强写作方法论_全球最强综合版.md
---

# blhcode/Inky-AI

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/blhcode/inky-ai
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：An AI writing assistant that helps you with writing. Features include editing, expansion, story ideas and free chat. This is a powerful tool that can help increase writing speed and eficency.
- **本地描述**：An AI writing assistant that helps you with writing. Features include editing, expansion, story ideas and free chat. This is a powerful tool that can help increase writing speed and eficency.
- **拉取时间**：2026-07-23 22:41:20

---

# Inky AI — Writer Assistant

A local web app for writers, powered by [Ollama](https://ollama.com) and DuckDuckGo search.

## Features

| Mode | What it does |
|------|----------------|
| **Free Chat** | General writing coach — craft, structure, motivation |
| **Expand** | Deepen a chapter with richer detail |
| **Ideas** | Brainstorm hooks, characters, conflicts, and twists |
| **Research** | Search the web and synthesize facts with cited sources |
| **Edit Story** | Upload a manuscript for full rewrite or editorial notes |

## Prerequisites

- Python 3.10+
- Node.js 18+
- [Ollama](https://ollama.com) running locally or on another machine on your network

```bash
ollama pull llama3.1:8b
```

## Configuration

Copy the example config and set your Ollama URL:

```bash
cp inky.config.env.example inky.config.env
```

Edit **`inky.config.env`**:

```ini
OLLAMA_URL=http://127.0.0.1:11434/api/chat
OLLAMA_MODEL=llama3.1:8b
INKY_PORT=8084
```

For Ollama on another PC, use that machine's IP instead of `127.0.0.1`.

**Never commit `inky.config.env` or anything under `data/stories/`** — those hold your settings and uploaded manuscripts.

## Quick start

### Linux

```bash
chmod +x scripts/run.sh scripts/stop.sh
./scripts/stop.sh all
./scripts/run.sh
```

Open **http://127.0.0.1:8084**

Dev mode (hot reload): `./scripts/dev.sh` → **http://127.0.0.1:5173**

### Windows

```bat
scripts\run.bat
```

Or: `.\scripts\run.ps1`

## What stays private

| Path | Why |
|------|--related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| `inky.config.env` | Your Ollama IP, model, ports |
| `data/stories/` | Uploaded manuscripts (original + edited) |

This repo includes only source code and `inky.config.env.example`.

## Project structure

```
backend/               FastAPI server, Ollama proxy, research
frontend/              React + Vite UI
scripts/               Run/dev/stop scripts (Linux + Windows)
inky.config.env.example  Config template — copy to inky.config.env
data/stories/          Created at runtime for uploads (gitignored)
```

## License

MIT — see [LICENSE](https://github.com/blhcode/Inky-AI/blob/main/LICENSE).
