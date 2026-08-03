---
id: tool-00637
type: tool
area: 库
status: active
tags: [TTS, Python, 协议宽松, 需API密钥, 英文文档]
title: echo-scribe-agent
summary: 小说转语音/有声书
source: https://github.com/1pio/echo-scribe-agent
created: 2026-07-18
updated: 2026-07-18
no: 637
category: 二、网文 / 长篇 AI 写作系统 库
repo: 1Pio/echo-scribe-agent
stars: 0
url: https://github.com/1pio/echo-scribe-agent
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 1Pio/echo-scribe-agent

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/1pio/echo-scribe-agent
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：It is a local-first, tool-augmented LiveKit voice assistant platform that already handles conversational help and personal workflow actions and is evolving toward a dedicated dictation mode with LLM-based real-time transcription cleanup, autocorrection, and writing enrichment.
- **本地描述**：It is a local-first, tool-augmented LiveKit voice assistant platform that already handles conversational help and personal workflow actions and is evolving toward a dedicated dictation mode with LLM-based real-time transcription cleanup, autocorrection, and writing enrichment.
- **拉取时间**：2026-07-23 22:57:38

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# LiveKit Local AI Agent

Local-first, tool-augmented LiveKit voice assistant focused on practical daily workflows.

This repository already supports conversational help and personal productivity actions, and it is evolving toward a dedicated dictation mode with LLM-based real-time transcription cleanup, autocorrection, and writing enrichment.

## What It Does Today

- Runs a realtime voice assistant using LiveKit Agents.
- Uses local or self-hosted endpoints for the core speech pipeline:
  - STT: local OpenAI-compatible endpoint (for example a local faster-whisper server)
  - LLM: Ollama OpenAI-compatible endpoint
  - TTS: Kokoro OpenAI-compatible endpoint
- Uses Silero VAD for interruption-friendly voice interactions.
- Ensures required background services are available via the local service daemon.
- Includes practical built-in tools in `agents/livekit_general_agent.py`, including:
  - web search (DuckDuckGo via Docker MCP gateway)
  - clipboard read/write helpers
  - focused Windows app detection
  - Obsidian daily note read/write helpers

## Planned Direction

The main product direction is a focused dictation mode that adds:

- real-time transcript cleanup
- automatic spelling and punctuation correction
- writing enrichment for clearer, more polished output
- smoother capture-to-note workflows for journaling and task management

## Requirements

- Python `>=3.11,<3.14`
- `uv` package manager
- Windows-oriented local setup (current services and tooling are primarily Windows-tested)
- Optional but recommended for search tooling: Docker (for MCP gateway)

## Quick Start

1) Install dependencies

```bash
uv sync
uv sync --extra dev
```

2) Configure environment

```bash
cp .env.example .env
```

If needed, also create `.env.local` for machine-specific overrides. The runtime loading order is:

1. `.env.local`
2. `.env`

3) Start the general assistant in console mode

```bash
uv run python agents/livekit_general_agent.py console
```

You can also run the basic example:

```bash
uv run python agents/livekit_basic_example.py console
```

## Key Environment Variables

Commonly used settings:

- `OLLAMA_BASE_URL` (default: `http://127.0.0.1:11434/v1`)
- `OLLAMA_MODEL` (default: `qwen3:8b`)
- `LOCAL_STT_BASE_URL` (default: `http://127.0.0.1:8001/v1`)
- `LOCAL_STT_HEALTH_URL` (default: `http://127.0.0.1:8001/health`)
- `LOCAL_STT_MODEL` (default: `whisper-1`)
- `KOKORO_BASE_URL` (default: `http://127.0.0.1:8880/v1`)
- `KOKORO_VOICE` (default: `af_heart`)
- `OBSIDIAN_JOURNAL_FOLDER` (optional, daily note path)
- `LIVEKIT_URL`, `LIVEKIT_API_KEY`, `LIVEKIT_API_SECRET` (optional for non-console scenarios)

## Project Layout

- `agents/livekit_general_agent.py` - main local-first assistant entrypoint
- `agents/livekit_basic_example.py` - minimal assistant example
- `services/local_stt_server.py` - local STT service
- `services/service_daemon.py` - daemon that manages local services
- `services/daemon_client.py` - daemon client and lease handling
- `services/docker_mcp_gateway.py` / `services/mcp_gateway.py` - MCP gateway support
- `livekit.toml` - LiveKit deployment/runtime config

## Development Commands

```bash
uv run ruff check .
uv run black .
uv run mypy agents services
uv run pytest
```

Useful smoke tests:

```bash
uv run python agents/livekit_basic_example.py console
uv run python agents/livekit_general_agent.py console
```

## Notes

- This project is under active evolution; the README reflects the current code path in `agents/livekit_general_agent.py` and the operating guidance in `AGENTS.md`.
- Keep secrets out of git. Do not commit `.env` or credentials.
