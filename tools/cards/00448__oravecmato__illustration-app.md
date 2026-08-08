---
id: tool-00448
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: illustration-app
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/oravecmato/illustration-app
created: 2026-07-18
updated: 2026-07-18
no: 448
category: 二、网文 / 长篇 AI 写作系统 库
repo: oravecmato/illustration-app
stars: 0
url: https://github.com/oravecmato/illustration-app
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
content_hash: 900b945b5f1d2ed1
  - methods/最强写作方法论_全球最强综合版.md
---

# oravecmato/illustration-app

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/oravecmato/illustration-app
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI story & illustrations generator
- **本地描述**：AI story & illustrations generator
- **拉取时间**：2026-07-23 22:52:10

---

# Anime Illustrator

A locally-hosted web application that creates short illustrated anime stories through
an interactive chat. Uses Claude (Anthropic API) for story development and character
planning, and a RunPod Serverless ComfyUI endpoint with Illustrious XL + My Hero
Academia character LoRAs for anime-style illustration generation.

---

## Requirements

- **Python 3.11+** (installed via `brew install python@3.11`)
- **Node.js 18+** and **npm**

---

## Installation

### Backend

```bash
cd backend
python3.11 -m venv .venv
# Activate venv for installation:
source .venv/bin/activate
pip install -e ".[dev]"
pip install ruff
```

Copy the env example and fill in your API keys:

```bash
cp .env.example .env
# Edit .env with your ANTHROPIC_API_KEY, RUNPOD_API_KEY, RUNPOD_ENDPOINT_ID
```

### Frontend

```bash
cd frontend
npm install
cp .env.example .env  # already filled with http://localhost:8000
```

---

## Configuration

### Backend (`backend/.env`)

| Variable | Description |
|----------|-------------|
| `ANTHROPIC_API_KEY` | Your Anthropic API key |
| `RUNPOD_API_KEY` | Your RunPod API key |
| `RUNPOD_ENDPOINT_ID` | Your RunPod Serverless endpoint ID |
| `DATABASE_URL` | SQLite URL (default: `sqlite+aiosqlite:///./data/app.db`) |
| `OUTPUT_DIR` | Directory for generated images (default: `./output`) |
| `WORKFLOW_PATH` | Path to ComfyUI workflow JSON (default: `./app/workflows/default.json`) |
| `ALLOWED_ORIGIN` | Frontend origin for CORS (default: `http://localhost:5173`) |

### Frontend (`frontend/.env`)

| Variable | Description |
|----------|-------------|
| `VITE_API_BASE` | Backend base URL (default: `http://localhost:8000`) |

---

## Running

### Backend

```bash
cd backend
./start.sh
```

The `start.sh` script automatically runs database migrations and starts uvicorn with auto-reload enabled. It doesn't require activating the virtual environment first.

### Frontend

```bash
cd frontend
npm run dev
```

Then open [http://localhost:5173](http://localhost:5173) in your browser.

---

## Running Tests

### Backend (requires venv activation)

```bash
cd backend
source .venv/bin/activate
pytest
ruff check .
ruff format --check .
```

### Frontend

```bash
cd frontend
vitest run
npm run lint
npm run type-check
```

---

## Architecture

### Backend (`backend/app/`)

- **`main.py`** — FastAPI app, CORS, lifespan startup
- **`config.py`** — Settings via pydantic-settings (reads `.env`)
- **`constants.py`** — Numeric limits and model name
- **`db/`** — SQLAlchemy ORM models, async session factory, repository CRUD
- **`schemas/`** — Pydantic models for API and Claude I/O
- **`services/`** — Claude client (5 distinct calls), RunPod client, workflow placeholder replacement, image file I/O
- **`orchestrator/`** — Pipeline (top-level), Branch (per-illustration state machine), EventBus (SSE pub/sub)
- **`api/`** — FastAPI router: `POST /api/runs`, `GET /api/runs/{id}`, `GET /api/runs/{id}/events` (SSE), `POST /api/runs/{id}/cancel`

### Frontend (`frontend/src/`)

- **`types/`** — Shared TypeScript types mirroring backend schemas
- **`services/api.ts`** — fetch wrappers and SSE EventSource
- **`stores/run.ts`** — Pinia store: run state, illustrations, SSE event handling
- **`views/HomeView.vue`** — Story input form
- **`views/RunView.vue`** — Live progress with illustration grid
- **`components/`** — `IllustrationCard`, `ProgressCounter`, `CancelButton`

### State machine (per illustration)

```
PENDING → GENERATING_PROMPTS → RENDERING → EVALUATING
  ↓ (verdict=concept)           ↓ (verdict=prompt)
RETHINKING_CONCEPT       REVISING_PROMPTS → RENDERING ...
  ↓
GENERATING_PROMPTS
  ↓ (max 3 concepts × 3 prompts = 9 jobs max)
COMPLETED | FAILED | CANCELLED
```

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## What is tested

- **Unit tests (backend):** Workflow placeholder replacement, all 5 Claude response schemas (valid + invalid), branch state machine (happy path, prompt revision, concept restart, concept rejection, exhaustion, cancellation), pipeline orchestration (3/5/8 illustrations, mixed outcomes, step 0 failure), SSE event bus, RunPod client (success, polling, timeout, failure statuses)
- **Integration tests (backend):** End-to-end happy path with HTTP-mocked Anthropic and RunPod; input validation (empty/too-long story); 404 for unknown runs; 409 cancel of non-running run
- **Unit tests (frontend):** `IllustrationCard` — all 9 state Slovak labels, spinner visibility, attempt counters, image rendering, error display; `ProgressCounter` — count display, unknown count; `CancelButton` — visibility by status, inline confirmation flow; `runStore` — snapshot, state update, completion, cancellation, error tolerance

## Deviations from spec

- The spec says `POST /api/runs/{run_id}/cancel` may return 409 if the run is already in a terminal state. In MVP, RunPod jobs already dispatched are allowed to finish (not cancelled mid-flight); subsequent branches check the cancel flag cooperatively.
- The `_update_snapshot` helper in `pipeline.py` calls `event_bus.set_snapshot()` which is synchronous (no await needed); in unit tests using `AsyncMock` for event_bus this generates a harmless `RuntimeWarning` about an un-awaited coroutine.
