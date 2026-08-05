---
id: tool-05598
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/faizitguy/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5598
category: 一、去 AI 味 / Humanizer 库
repo: faizitguy/ai-text-detector
stars: 0
url: https://github.com/faizitguy/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# faizitguy/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/faizitguy/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：faizitguy/ai-text-detector
- **拉取时间**：2026-07-25 18:24:38

---

# Verdict — AI Text Detection by Model Consensus

A full-stack app that decides whether a piece of text is **AI-generated**,
**human-written**, or **ambiguous** by asking a panel of frontier LLMs the same
question in parallel and combining their answers under a strict-consensus rule.

This is a monorepo with a cleanly separated backend and frontend:

```
.
├── backend/         FastAPI service — the detection API (Python)
│   ├── app/         application package (main, config, detector, consensus, providers…)
│   ├── tests/       pytest suite (runs fully offline, no API keys needed)
│   ├── examples/    sample request bodies
│   ├── docs/        architecture docs (HLD / LLD) + service overview page
│   ├── pyproject.toml
│   ├── .env.example
│   └── README.md    backend setup, API contract, design rationale
│
├── frontend/        React + TypeScript + Vite single-page app — the UI
│   ├── src/         components, typed API client, design system
│   ├── vite.config.ts
│   ├── vercel.json / netlify.toml
│   └── README.md    frontend setup + deployment options
│
├── CLAUDE.md        project brief / build standards
├── PROMPTS.md       prompt notes
├── .editorconfig    shared editor formatting
└── .gitignore
```

The two halves are independently deployable — the frontend can be hosted on a
static platform (Vercel/Netlify) against the API anywhere, **or** the backend can
serve the built frontend for a single-origin deploy.

---

## Architecture

A security edge (auth → rate limit → validation) feeds an async orchestration
core. The core assembles a prompt with **separated system and user roles**, fans
out in parallel to a key-gated panel of models (OpenAI, Groq, Google today), wraps
every call in a resilience layer (timeout + retry + graceful degradation), then
collapses the replies with a **strict-agreement** consensus rule before building
the response.

!`[High-level design — security edge feeds an async orchestration core that fans out to a parallel model panel and collapses the results under a strict-consensus rule](backend/docs/HLD.svg)`

> Request flow, left to right: **edge** (authentication, rate limiting, ≤5,000-char
> validation) → **orchestration** (prompt assembly, parallel fan-out under a time
> budget) → **model panel** (each provider wrapped by the resilience layer) →
> **consensus** (agree ⇒ that verdict · disagree ⇒ ambiguous · one survivor ⇒
> degraded · all fail ⇒ 503) → **response**. The full write-up lives in
> `[backend/docs/LLD.md](backend/docs/LLD.md)`.

---

## Getting started

**Prerequisites:** Python **3.10+**, Node **18+**, and at least one provider API
key (OpenAI, Groq, or Google Gemini) for live verdicts.

Run the API and the UI in two terminals.

**1 · Backend** — FastAPI on `:8000`

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[test]"
cp .env.example .env          # then open .env and add at least one real API key
uvicorn app.main:app --reload
```

**2 · Frontend** — Vite dev server on `:5173` (proxies the API)

```bash
cd frontend
npm install
npm run dev
```

Open **http://localhost:5173** — the dev server proxies `/detect` and `/health`
to the backend, so there's no CORS and nothing else to configure.

> **No keys yet?** The backend needs at least one real key in `backend/.env` to
> return live verdicts. The test suite still runs entirely offline with mocked
> providers — see "Run the tests" below.

**Run the tests** (offline, no keys required)

```bash
cd backend && source .venv/bin/activate
pytest -q
```

---

## Single-origin production build

Build the frontend; the backend automatically serves it (it looks for
`frontend/dist/`). Now the app and API share one origin — no CORS, no separate
host.

```bash
cd frontend && npm install && npm run build
cd ../backend && source .venv/bin/activate && uvicorn app.main:app
# → UI + API together at http://127.0.0.1:8000
```

For hosting the frontend separately (Vercel/Netlify) against a deployed API, see
`[frontend/README.md](frontend/README.md)`. For the API contract, deployment, and
design rationale, see `[backend/README.md](backend/README.md)`.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## What's under the hood

- **Backend:** FastAPI + async SDK calls fanned out with `asyncio.gather` under a
  shared time budget, a resilience layer (per-call timeouts, retry-on-transient,
  graceful degradation), and a strict-agreement consensus engine. One endpoint:
  `POST /detect`. Interactive docs at `/docs`.
- **Frontend:** React + TypeScript + Vite. A typed API client mirrors the
  backend schema; the UI shows the consensus verdict plus every model's verdict,
  reasoning, confidence, and latency.

Verdict is a heuristic aid — no AI detector is infallible.
