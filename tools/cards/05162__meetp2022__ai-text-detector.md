---
id: tool-05162
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/meetp2022/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5162
category: 一、去 AI 味 / Humanizer 库
repo: meetp2022/ai-text-detector
stars: 0
url: https://github.com/meetp2022/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# meetp2022/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/meetp2022/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：meetp2022/ai-text-detector
- **拉取时间**：2026-07-25 18:08:24

---

# AI Text Detector

> Multi-signal detection engine that classifies text as AI-generated or human-written using a scientifically aggregated scoring pipeline.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-aichecking.me-blue?style=for-the-badge)](https://aichecking.me)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

---

## Live Demo

**[https://aichecking.me](https://aichecking.me)**

---

## Tech Stack

| Layer | Technology |
|---|---|
| Core Engine | Python 3.9+, PyTorch (CPU-optimised inference) |
| Classifier | `fakespot-ai/roberta-base-ai-text-detection-v1` via HuggingFace Transformers |
| NLP | NLTK (sentence tokenisation, n-gram analysis) |
| Backend | FastAPI (async, high-concurrency) |
| Frontend | Vanilla JS / CSS (zero-dependency) |
| Containerisation | Docker + Docker Compose |
| Deployment | Fly.io |

---

## Scoring Pipeline

The engine rejects single-metric heuristics in favour of a **four-dimensional statistical consensus**:

### 1. Perplexity (Predictability)
The text is evaluated against a language model to measure how "surprised" the model is at each token choice.
- **Low perplexity** — text follows exact statistical patterns of LLM training distributions — likely AI
- **High perplexity** — creative or non-linear word choices a model would not predict — likely human

### 2. Burstiness (Structural Variation)
Coefficient of variation across sentence lengths measures rhythmic uniformity.
- **Uniform lengths** — AI tends to produce even, well-structured sentences
- **High variance** — humans naturally mix short punchy sentences with long descriptive ones

### 3. N-gram Repetition
Bigram and trigram frequency analysis surfaces repeating phrase structures.
- AI outputs frequently loop back to similar patterns and transitional phrasing

### 4. Stylometric Variance
Perplexity is measured *within* the document in segments, not just globally.
- **Monotone predictability** — consistent AI signal throughout
- **Fluctuating predictability** — human writers shift registers, ramp complexity, digress

### Score Aggregation (Consensus Model)
The global 0-100 score is derived mathematically from three sentence-level signals:

| Signal | Description |
|---|---|
| **AI Sentence Ratio** | Percentage of sentences flagged as highly predictable |
| **Mean Probability** | Average AI risk across every sentence, smoothing outliers |
| **AI Streak Detection** | Sustained sequences of AI-like writing (rare in human prose) |

**Score thresholds:**
- `0-30` — Likely human-written
- `30-70` — Uncertain / mixed
- `70-100` — Likely AI-generated

---

## Architecture

```
ai-text-detector/
├── app/
│   ├── main.py              # FastAPI entry point, CORS config, static file serving
│   ├── api/
│   │   └── analyze.py       # POST /api/analyze endpoint
│   ├── core/
│   │   ├── config.py        # Environment-based settings (Pydantic)
│   │   └── logging.py       # Structured logging setup
│   ├── services/
│   │   ├── perplexity.py    # Token-level perplexity via RoBERTa
│   │   ├── burstiness.py    # Sentence-length coefficient of variation
│   │   ├── repetition.py    # N-gram repetition scoring
│   │   ├── scoring.py       # Consensus aggregation model
│   │   ├── modality.py      # Code / technical text detection
│   │   └── preprocessing.py # Text cleaning and sentence splitting
│   ├── models/              # HuggingFace model loader (lazy-loaded on first request)
│   └── schemas/             # Pydantic request/response models
├── frontend/
│   ├── index.html           # Main UI
│   ├── script.js            # API calls, sentence highlighting
│   └── styles.css
├── tests/                   # Unit tests (pytest)
├── scripts/                 # Benchmarking and fine-tuning utilities
├── Dockerfile
├── docker-compose.yml
├── fly.toml                 # Fly.io deployment config
└── requirements.txt
```

**Key design decisions:**
- The RoBERTa classifier is **lazy-loaded** on the first request to avoid blocking server startup
- A **Modality Detection Service** identifies code and technical text, which are naturally low-perplexity, and warns the user that results may be unreliable — preventing false positives on human-written code
- All four scoring signals are computed at the **sentence level** before being aggregated globally, enabling per-sentence highlighting in the UI

---

## Run Locally

### Prerequisites
- Python 3.9+
- ~1 GB disk space for model weights (downloaded automatically on first run)

### Setup

```bash
# Clone the repo
git clone https://github.com/<your-username>/ai-text-detector.git
cd ai-text-detector

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download NLTK tokeniser data
python -c "import nltk; nltk.download('punkt')"

# Start the server
uvicorn app.main:app --reload --port 8000
```

Open [http://localhost:8000](http://localhost:8000) — the frontend is served directly by FastAPI.

### Docker

```bash
docker-compose up --build
```

---

## API Reference

### `POST /api/analyze`

```bash
curl -X POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "Your text to analyse here..."}'
```

**Response:**
```json
{
  "score": 82.1,
  "label": "AI-generated",
  "confidence": "high",
  "metrics": {
    "perplexity": 9.4,
    "burstiness": 0.31,
    "repetition": 0.74
  },
  "sentence_scores": [
    { "text": "First sentence.", "score": 88.0 },
    { "text": "Second sentence.", "score": 76.5 }
  ]
}
```

### `GET /health`

```bash
curl http://localhost:8000/health
# {"status": "ok", "app": "AI Text Detector"}
```

Swagger UI is available at `http://localhost:8000/docs`.

---

## Testing

```bash
# Unit tests
pytest tests/ -v

# Sanity check (smoke test with known samples)
python scripts/sanity_check.py

# Benchmark on labelled examples
python scripts/benchmark_examples.py
```

---

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `ENVIRONMENT` | `development` | `development` or `production` |
| `MODEL_NAME` | `fakespot-ai/roberta-base-ai-text-detection-v1` | HuggingFace model ID |
| `MAX_LENGTH` | `5000` | Max input character length |

---

## Deployment

The app is deployed on **Fly.io** (see `[`fly.toml`](fly.toml)`). Any ASGI host works:

```bash
# Render / Railway — connect GitHub repo and set start command:
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

---

## Roadmap

- [ ] Source attribution (multi-class: GPT-4 vs Claude vs Llama fingerprinting)
- [ ] Ensemble scoring across multiple classifiers (RoBERTa + BERT + DistilGPT-2)
- [ ] Fine-tuning pipeline for new LLMs as they release
- [ ] INT8/FP16 quantisation for lower memory footprint
- [ ] Semantic consistency graph for long-document analysis

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## License

MIT — see `[LICENSE](LICENSE)` for details.
