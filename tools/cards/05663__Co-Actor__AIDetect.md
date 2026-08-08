---
id: tool-05663
type: tool
area: 库
status: active
tags: [去AI味, Python, 协议未明, 需API密钥, 英文文档]
title: AIDetect
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/co-actor/aidetect
created: 2026-07-18
updated: 2026-07-18
no: 5663
category: 一、去 AI 味 / Humanizer 库
repo: Co-Actor/AIDetect
stars: 0
url: https://github.com/co-actor/aidetect
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 18cea274ff7f8b8c
  - methods/改稿润色指令库.md
---

# Co-Actor/AIDetect

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/co-actor/aidetect
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Multi-signal AI text detector (statistical + patterns + LLM-judge) with humanizer rewriter
- **本地描述**：Multi-signal AI text detector (statistical + patterns + LLM-judge) with humanizer rewriter
- **拉取时间**：2026-07-25 18:27:03

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AIDetect

Multi-signal AI text detector. Hybrid scoring: statistical signals + pattern matching + LLM-as-judge with calibrated rubric.

> Working title. Public/commercial name TBD.

## Layout

```
AIDetect/
├── backend/          # FastAPI service: detection API, scoring engine, rubric
├── frontend/         # Quasar 2 SPA: web UI for the detector
├── docker-compose.yml
└── Makefile          # convenience commands
```

Each subproject has its own README with setup instructions.

## Quick start (local dev)

```bash
# backend (terminal 1) — serves on http://localhost:8010
cd backend
cp .env.example .env        # set AIDETECT_INTERNAL_TOKEN and OPENROUTER_API_KEY
uv sync                     # or: pip install -e ".[dev]"
uv run uvicorn aidetect.main:app --reload --port 8010

# frontend (terminal 2) — serves on http://localhost:9000
cd frontend
cp .env.example .env
pnpm install                # or: npm install
pnpm dev
```

Default ports: backend `8010`, frontend `9000`, redis `6380` (Redis is optional —
the cache falls back to in-memory if unreachable).

Or use Docker Compose:

```bash
docker compose up --build
```

## Architecture

Three independent signal layers feed a calibrated aggregator:

- **Layer A — Statistical** (sync, ~5ms): burstiness, TTR, sentence-CV, formatting density.
- **Layer B — Pattern matching** (sync, ~10ms): banned phrases, structural patterns, formatting habits. Driven by `backend/src/aidetect/rubric/v1/`.
- **Layer C — LLM-as-judge** (async, 1-3s): rubric-based scoring via OpenRouter (default `claude-haiku-4-5`).

Aggregator weights are calibrated on a ground-truth dataset (Co.Actor live posts + synthetic AI + public benchmarks).

## Status

Phase 0: skeleton. Phase 1 (MVP): in progress.
