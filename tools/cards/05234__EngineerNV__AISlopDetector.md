---
id: tool-05234
type: tool
area: 库
status: active
tags: [Claude插件, JavaScript, 协议宽松, 需API密钥, 英文文档]
title: AISlopDetector
summary: Claude Code 插件式写作流
source: https://github.com/engineernv/aislopdetector
created: 2026-07-18
updated: 2026-07-18
no: 5234
category: 一、去 AI 味 / Humanizer 库
repo: EngineerNV/AISlopDetector
stars: 0
url: https://github.com/engineernv/aislopdetector
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# EngineerNV/AISlopDetector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/engineernv/aislopdetector
- **Stars**：0
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：an interface for going through text and detecting AI Slop writing patterns and determining if something was written by AI.  Breaks down key writing styles and verbosity. 
- **本地描述**：an interface for going through text and detecting AI Slop writing patterns and determining if something was written by AI.  Breaks down key writing styles and verbosity.
- **拉取时间**：2026-07-25 18:11:02

---

# AISlopDetector

Detect AI-generated text ("AI slop") via stylometry, an AI-tells lexicon, and
optional transformer / LLM-as-judge backends. Ships as both a **CLI** and an
**MCP server** so it plugs straight into Claude Code, Claude Desktop, and any
other MCP-aware client.

> **What problem this solves.** Bulk LLM-generated posts, comments, and articles
> have a fingerprint: uniform sentence rhythm, a narrow "delve / tapestry /
> multifaceted" register, a fondness for em-dashes and "X, Y, and Z" triads,
> and predictable summary closers. AISlopDetector measures those signals and
> produces a calibrated 0–100 score with a per-signal explanation, so you can
> see *why* the text was flagged.

---

## Screenshots

| Landing | Annotated passage | Score breakdown |
|---------|------------------|-----------------|
| ![Landing page](docs/screenshots/landing.png) | ![Highlighted spans](docs/screenshots/highlights.png) | ![Score panel](docs/screenshots/score_panel.png) |

---

## Quick start

```bash
# Install (zero-dep core).
pip install -e .

# Score a string.
aislop "In today's fast-paced world, it's important to note that AI plays a crucial role…"

# From a file.
aislop -f post.md

# JSON for scripts.
cat post.md | aislop --json

# Just the score (for piping).
aislop -f post.md --score-only
```

Optional backends:

```bash
pip install -e '.[transformer]'     # adds HuggingFace text classifier
pip install -e '.[anthropic]'       # adds Claude as judge
pip install -e '.[openai]'          # adds GPT as judge
pip install -e '.[mcp]'             # adds MCP server entrypoint
pip install -e '.[all]'             # everything

aislop -f post.md --transformer
aislop -f post.md --llm anthropic --llm-model claude-haiku-4-5-20251001
aislop -f post.md --llm openai --llm-model gpt-4o-mini
```

The transformer backend defaults to
[`roberta-base-openai-detector`](https://huggingface.co/openai-community/roberta-base-openai-detector).
Override with `--transformer-model <hf-id>` to swap in a newer detector.

---

## Architecture

Four layers, each producing signals that fuse into a single score.

```
┌─────────────────────────────────────────────────────────────────┐
│                          Input text                             │
└─────────────────────────────────────────────────────────────────┘
        │                  │                │                │
        ▼                  ▼                ▼                ▼
┌─────────────┐    ┌──────────────┐  ┌───────────────┐  ┌─────────────┐
│ Stylometry  │    │ AI-tells     │  │ HF transformer│  │ LLM-as-judge│
│ (features.py)│   │ lexicon      │  │ (optional)    │  │ (optional)  │
│ burstiness, │    │ (heuristics) │  │ roberta-      │  │ Claude /    │
│ TTR, em-    │    │ "delve",     │  │ openai-       │  │ OpenAI →    │
│ dashes, etc.│    │ "tapestry",  │  │ detector etc. │  │ JSON prob.  │
│             │    │ "delve into" │  │               │  │             │
└─────┬───────┘    └──────┬───────┘  └───────┬───────┘  └──────┬──────┘
      │                   │                  │                  │
      └───────────────┬───┴───────┬──────────┴──────────────────┘
                      ▼           ▼
                 ┌───────────────────────┐
                 │ Signal fusion (0–100) │
                 │   scoring.py          │
                 └──────────┬────────────┘
                            ▼
                 ┌───────────────────────┐
                 │  DetectionReport      │
                 │  + verdict / pretty / │
                 │    JSON / MCP tool    │
                 └───────────────────────┘
```

Layers 1 and 2 are **pure Python, zero dependencies, always on**. Layers 3 and
4 are optional and gated behind extras + flags. Every signal exposes its
weight, so the CLI and MCP report can show the user which evidence drove the
verdict.

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) and
[`docs/DETECTION_METHODS.md`](docs/DETECTION_METHODS.md) for design notes.

---

## What gets scored

| Signal family            | Examples                                                  | Why it matters                                              |
|--------------------------|-----------------------------------------------------------|-------------------------------------------------------------|
| Stylometry               | burstiness, avg sentence length, em-dash density, triadic-list density, sentence-starter repetition, type-token ratio | LLMs decode toward a comfortable mean and over-pattern      |
| Lexicon (AI tells)       | "delve", "tapestry", "rich tapestry of", "it's important to note", "in conclusion" | Token preferences differ between LLM register and human web writing |
| HF transformer (opt)     | `roberta-base-openai-detector` or any drop-in classifier  | Model-based opinion; strong on in-distribution text, weaker on modern LLMs |
| LLM-as-judge (opt)       | Claude / OpenAI returning `{probability_ai, rationale}`   | A second opinion from a frontier model, with an explanation |

The verdict bands are:

| Score   | Verdict                     |
|---------|-----------------------------|
| 0–19    | likely_human                |
| 20–39   | uncertain_lean_human        |
| 40–59   | uncertain                   |
| 60–79   | uncertain_lean_ai           |
| 80–100  | likely_ai                   |

Confidence (`low`/`medium`/`high`) gates on text length and how many signals
fired — short snippets cap at low confidence even with extreme scores.

---

## Use it from Python

```python
from aislopdetector import detect

rep = detect("Some text…", enable_transformer=False, llm_judge=None)
print(rep.score, rep.verdict, rep.confidence)
print(rep.pretty())          # human-readable
print(rep.to_json())         # JSON
```

For programmatic use:

```python
from aislopdetector import Detector
from aislopdetector.detector import DetectorConfig

det = Detector(DetectorConfig(
    enable_transformer=True,
    transformer_model="roberta-base-openai-detector",
    llm_judge="anthropic",
    llm_model="claude-haiku-4-5-20251001",
))
rep = det.analyze(text)
```

---

## CLI

```text
aislop [TEXT] [-f FILE] [--json] [--score-only]
       [--transformer] [--transformer-model HF_ID]
       [--llm {anthropic,openai}] [--llm-model MODEL]
       [--max-chars N] [--quiet]
```

See [`docs/USAGE.md`](docs/USAGE.md) for full CLI examples.

---

## MCP server

Install the `[mcp]` extra and add this to your MCP config (Claude Desktop,
Claude Code, etc.):

```json
{
  "mcpServers": {
    "aislopdetector": {
      "command": "aislop-mcp",
      "env": {
        "AISLOP_ENABLE_TRANSFORMER": "0",
        "AISLOP_LLM_JUDGE": "",
        "ANTHROPIC_API_KEY": "sk-..."
      }
    }
  }
}
```

Tools exposed:

- `detect_ai_content(text, format="json"|"pretty")` — full report.
- `score_ai_content(text)` — `{score, verdict, confidence}`.

Configurable via env vars: `AISLOP_ENABLE_TRANSFORMER`, `AISLOP_TRANSFORMER_MODEL`,
`AISLOP_LLM_JUDGE` (`anthropic` / `openai`), `AISLOP_LLM_MODEL`,
`AISLOP_MAX_CHARS`.

---

## Limitations

- **No detector is reliable on short or heavily edited text.** Treat scores
  on <80 words as suggestive at best.
- The lexicon is biased toward English and toward post-2022 LLM register.
  Languages, domains, and styles drift; extend the lexicon with
  `heuristics.add_phrases([...])` or via `DetectorConfig(extra_phrases=...)`.
- `roberta-base-openai-detector` was trained on GPT-2 outputs and
  underperforms on current frontier models. The HF backend is most useful as
  a third opinion, not as ground truth.
- LLM-as-judge calls cost money and add latency. Use them when you want an
  explainable second opinion, not as a hot-path classifier.
- This tool reports likelihood, not proof. **Never use it as the sole basis
  for a high-stakes decision** (academic discipline, hiring, etc.).

---

## Repo layout

```
src/aislopdetector/
  __init__.py          public API
  features.py          stylometric feature extraction
  heuristics.py        AI-tells lexicon + density scoring
  scoring.py           signal fusion → 0–100 score
  llm_judge.py         optional Anthropic / OpenAI judge
  transformer_detect.py optional HF text classifier
  report.py            DetectionReport + pretty renderer
  detector.py          orchestrator (Detector class)
  cli.py               `aislop` CLI entrypoint
  mcp_server.py        `aislop-mcp` MCP server
tests/                 pytest suite (fixtures in tests/samples.py)
docs/                  ARCHITECTURE, DETECTION_METHODS, USAGE
```

---

## License

MIT. See `LICENSE`.

## HTTP server

For when you want the frontend (or any other client) to talk to the real
detector instead of the in-browser fallback.

```bash
pip install -e '.[server]'
uvicorn aislopdetector.server:app --reload
# POST http://127.0.0.1:8000/analyze {"text": "..."}
# GET  http://127.0.0.1:8000/healthz
# GET  http://127.0.0.1:8000/metrics    # Prometheus text format
```

Or run the whole stack (API + nginx-served frontend) with Docker Compose:

```bash
docker compose up --build
# Frontend: http://localhost:8080      (nginx proxies /api -> api:8000)
# API:      http://localhost:8080/api  (or via the api service inside the network)
```

The server emits the "internal" UI shape directly (numeric `confidence`,
typed `category`, stable `id`, `start`/`end` offsets), so the frontend's
normalizer is a no-op when pointed at it. The same normalizer still
accepts the compact `{label, score, reason}` shape if you write a
different backend.

### Hardening knobs

| Env var | Default | Effect |
|---|---|---|
| `AISLOP_CORS_ORIGINS` | `http://localhost:5173,…` | Comma-separated allowlist (or `*`). |
| `AISLOP_RATE_LIMIT` | `60/60` | Token bucket per IP, written as `requests/seconds`. `off` disables. |
| `AISLOP_TRUST_PROXY_HEADERS` | unset/false | Trust `X-Forwarded-For` for client IP extraction (enable only behind trusted proxy). |
| `WORKERS` (Docker) | `2` | Gunicorn worker count. The image launches gunicorn + uvicorn workers. |
| `PORT` (Docker) | `8000` | Listen port. |

Each request gets a JSON access-log line on stdout (with `request_id`,
`ip`, `ms`, `status`) and is mirrored back to the caller in the
`X-Request-ID` response header. `/healthz` and `/metrics` are exempt from
both the access log noise and the rate limit.

## Frontend (React + Vite)

A fully-featured web interface with a gritty back-alley graffiti aesthetic,
featuring an animated cartoon rat that scurries across detected AI text,
highlighted evidence spans, and an interactive slop meter. The UI includes
sound effects, animated flies, and a modern dark theme with neon accents.

**Features:**
- **Real-time analysis** with instant scoring and highlighting
- **Animated rat detector** that runs across suspicious text spans
- **Interactive slop meter** with trash can visualization and burst effects
- **Evidence highlighting** with hover tooltips and category legends
- **List view toggle** for evidence-based browsing
- **Sound controls** for ambient audio and detection effects
- **PNG export** with shareable card generation
- **Responsive design** with graffiti-themed styling

```bash
cd frontend
npm install
npm run dev          # dev server (default http://127.0.0.1:5173)
npm test             # vitest (analyzer / normalize / segmentation / a11y)
npm run lint         # eslint flat config
npm run format       # prettier --check
npm run build        # production bundle
```

By default the frontend runs entirely in the browser, using a JS lexicon
auto-generated from `src/aislopdetector/heuristics.py`. To call the
HTTP server instead, set `VITE_API_BASE_URL` (e.g.
`VITE_API_BASE_URL=http://localhost:8000`) before `npm run dev` /
`npm run build`. There is no implicit default — when the variable is unset
*or* the configured backend is unreachable, the UI silently falls back to
the in-browser analyzer and a "Source" pill / warning notice tells you
which one actually ran.

The JS lexicon (`frontend/src/lib/lexicon.generated.js`) is committed but
generated. Regenerate after editing the Python heuristics:

```bash
python scripts/export_lexicon.py
```

CI runs the same script and fails the build if the committed copy drifts.

The UI expects a `POST /analyze` response, but tolerates several shapes —
they're normalized at the fetch boundary in `frontend/src/lib/normalize.js`.
Either of the following works:

```jsonc
// Compact wire shape (per-hit `label` + `score` + `reason`):
{
  "overallScore": 0.74,                        // or "score": 0..100
  "verdict": "likely_ai",
  "confidence": 0.65,                          // or "low" | "medium" | "high"
  "explanation": "Uniform sentence rhythm and repetitive framing.",
  "reasons": ["High cliché density", "Low burstiness"],
  "highlights": [
    {"start": 3, "end": 42, "label": "buzzphrase", "score": 0.81, "reason": "Frequent AI-tells"}
  ]
}
```

```jsonc
// Internal/UI shape (matches what the in-browser analyzer emits):
{
  "overallScore": 0.74,
  "verdict": "likely_ai",
  "confidence": 0.65,
  "componentScores": {"buzzphrase": 0.62, "register": 0.41},
  "highlights": [
    {
      "id": "h-3-42-0",       // optional — synthesized from start/end/index if omitted
      "start": 3, "end": 42,
      "category": "buzzphrase",
      "weight": 0.81,
      "label": "Buzzphrase",
      "reason": "Frequent AI-tells"
    }
  ]
}
```

`category` (or `label` if it matches a known category key) drives the
highlight color and tooltip; `weight` (or `score`) drives the per-hit
audio pitch and tooltip detail. Missing fields fall back to safe defaults.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Future Features & Roadmap

### Backend Enhancements
- **Additional LLM judges**: Google Gemini, local Ollama models, Grok
- **Batch processing**: Analyze multiple texts in parallel for bulk workflows
- **Custom model training**: Fine-tune detection models on domain-specific data
- **Multi-language support**: Extend lexicon and features beyond English
- **Advanced export formats**: PDF reports, CSV data dumps, integration APIs
- **Real-time streaming**: WebSocket support for live analysis as text is typed

### Frontend Improvements
- **File upload**: Drag & drop support for analyzing documents and PDFs
- **History & bookmarks**: Save and compare previous analyses
- **Comparison mode**: Side-by-side analysis of multiple texts
- **Keyboard shortcuts**: Full keyboard navigation and hotkeys
- **Settings panel**: Configurable detection thresholds and display options
- **Accessibility**: Screen reader support, high contrast modes, focus management
- **Progressive Web App**: Offline capability and installable interface

### Detection & Analysis
- **Model versioning**: Track and compare different detection model performance
- **Confidence calibration**: Better uncertainty quantification and error bars
- **Cross-validation**: Built-in testing against known AI/human corpora
- **Explainability**: More detailed signal breakdowns and visualization
- **Performance optimization**: Faster analysis for large documents

### Integrations
- **Browser extensions**: Chrome/Firefox plugins for web content analysis
- **API integrations**: Zapier, Make.com, and automation platform support
- **Content management**: WordPress plugins, CMS integrations
- **Social media tools**: Twitter bots, Discord bots for community moderation
