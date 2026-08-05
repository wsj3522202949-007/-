---
id: tool-05123
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 去AI味]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/kpedrok/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5123
category: 一、去 AI 味 / Humanizer 库
repo: kpedrok/ai-text-detector
stars: 0
url: https://github.com/kpedrok/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# kpedrok/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/kpedrok/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：kpedrok/ai-text-detector
- **拉取时间**：2026-07-25 18:06:59

---

# AI Text Detector API

Self-hosted REST API that estimates the probability that a text (e.g. a student
essay) was AI-generated. Built as a calibrated ensemble — no per-call vendor fees.

**The honest contract:** no detector is reliable enough to prove AI use. This API
returns a calibrated probability, a confidence interval, and a band
(`likely_human` / `uncertain` / `likely_ai`) — never a verdict — and every
response carries non-removable caveats (false positives, bias against non-native
English writers, unreliability on short texts). The `likely_ai` threshold is
tuned so the false-positive rate on the human dev split stays ≤ 5%, because a
false accusation is the costly error.

## How it works

Three signals feed one calibrated combiner:

1. **Binoculars-style paired perplexity** ([Hans et al., 2024](https://arxiv.org/abs/2401.12070)) —
   an observer/performer LM pair (`BINOCULARS_PROFILE`):
   | profile | models | footprint | notes |
   |---|---|---|---|
   | `small` (default) | SmolLM2-360M + Instruct | ~3 GB, CPU-OK | weakest signal, fastest |
   | `medium` | Qwen2.5-1.5B + Instruct | ~12 GB | better separation |
   | `large` | falcon-7b + instruct | ~28 GB fp16, GPU-only | paper-grade accuracy |
2. **Supervised classifier** — `desklib/ai-text-detector-v1.01` (DeBERTa-v3-large,
   pinned revision), strong on the RAID robustness benchmark.
3. **Stylometry** — burstiness, lexical diversity (MTLD), stopword ratio, etc.

A logistic regression (multi-feature Platt scaling) fit on **HC3** + a **RAID**
sample (incl. GPT-4-class generators and paraphrase/homoglyph attacks) turns the
feature vector into a calibrated probability. The artifact is versioned JSON
(`app/artifacts/calibration_v1.json`) — auditable, no pickle. Calibration is
profile-specific: switching `BINOCULARS_PROFILE` requires re-running
`fit_calibration`.

Inputs are NFKC-normalized and stripped of zero-width characters before scoring,
which neutralizes the cheapest adversarial attacks. Cyrillic/Greek homoglyph
substitution is only partially neutralized (documented limitation).

## Quickstart

Prereqs: [uv](https://docs.astral.sh/uv/) (installs Python for you), ~8 GB free
disk, ~6 GB RAM. macOS/Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh   # skip if you have uv
```

```bash
uv sync                                  # installs Python 3.12 + all deps
cp .env.example .env                     # API key defaults to "dev-key"
uv run python scripts/download_models.py # one-time, ~3.4 GB of model weights
uv run uvicorn app.main:app              # then ~10-30 s to load models
```

Check it's up — `models_loaded` must be `true`:

```bash
curl -s localhost:8000/healthz
```

**Easiest way to play:** open <http://localhost:8000/docs> in a browser —
interactive API docs where you can paste an essay and hit Execute, no curl
needed.

Or from the terminal — both examples below are copy-paste ready (texts need
50+ words).

**Example 1 — AI-written text** (ChatGPT-style essay; expect
`band: "likely_ai"`, probability ≈ 0.99 — plus `confidence: "low"` because
it's only 65 words, demonstrating the short-text guard):

```bash
curl -s localhost:8000/v1/detect \
  -H "X-API-Key: dev-key" -H "Content-Type: application/json" \
  -d '{"text": "The role of technology in modern education represents one of the most significant transformations in the history of learning. It is important to note that digital tools have fundamentally reshaped how students engage with educational content. Furthermore, the integration of online platforms has enabled unprecedented access to information. In conclusion, while technology offers remarkable opportunities, its implementation must be thoughtful and equitable for all students."}' \
  | python3 -m json.tool
```

**Example 2 — human-written text** (personal narrative; expect
`band: "likely_human"`, probability ≈ 0.02):

```bash
curl -s localhost:8000/v1/detect \
  -H "X-API-Key: dev-key" -H "Content-Type: application/json" \
  -d '{"text": "I did not want to take chemistry. My counselor put me in it because band conflicted with art history, and by the time the schedule shook out it was either chemistry or weight training with the football coaches. So chemistry. Mr. Delgado had this habit of starting class with a question nobody could answer. Why does ice float? Everybody knows it does. Nobody in that room could say why, not really. I got a B minus that semester, and honestly I worked harder for that B minus than for any A I got in high school. The thing about chemistry was that you could not fake it. Either the math came out or it did not. Either your titration turned pink at the right moment or you overshot and had to start over while everyone else was packing up. I overshot a lot. I am not a scientist now. I do payroll for a landscaping company, which is about as far from titration as you can get. But sometimes when I cannot sleep I think about ice floating, and how water is the weird one, and how nobody ever told me that before a tired man in a stained tie made it seem like the strangest fact in the world."}' \
  | python3 -m json.tool
```

**What to look for:** the `document.band` flips between the two, and
`sentences[]` shows which parts drove the score. Now paste your own text —
something you wrote yourself vs. something ChatGPT wrote. Heads-up: *formal,
polished essay prose scores AI-ish even when humans write it* — that's the
documented false-positive risk the caveats warn about, and a good thing to see
firsthand before trusting any detector.

Response shape (see `/docs` for full OpenAPI):

```json
{
  "schema_version": "1.0",
  "document": {
    "ai_probability": 0.83,
    "confidence_interval": [0.71, 0.91],
    "band": "likely_ai",
    "confidence": "normal",
    "word_count": 412
  },
  "sentences": [
    {
      "text": "...",
      "start": 0,
      "end": 88,
      "ai_probability": 0.91,
      "band": "likely_ai"
    }
  ],
  "model_versions": {
    "ensemble": "v1",
    "calibration": "calibration_v1",
    "...": "..."
  },
  "caveats": ["AI detectors are probabilistic and produce false positives; ..."]
}
```

Guards: `<50` words → `band: insufficient_text` (no score); `50–150` words →
`confidence: "low"` + widened interval; non-English → 422; >50k chars → 413.
Sentence offsets refer to the normalized text. Auth via `X-API-Key`
(comma-separated `API_KEYS` env); rate limit defaults to 30 req/min per key.

### Docker

```bash
docker compose up --build    # api + redis (shared response cache)
```

First build takes ~10-15 min and the image is ~15 GB (model weights are baked
in). Subsequent starts are ready in ~10 s.

Weights are baked into the image (`scripts/download_models.py`), so cold start
is a disk load, not a download. The service is stateless — scale horizontally
behind any load balancer; set `REDIS_URL` to share the response cache.

## Evaluation ("does it actually work")

```bash
uv run python -m scripts.fit_calibration --dataset both --limit 600   # refit
uv run python -m scripts.evaluate --dataset both --limit 600          # held-out report
```

`evaluate.py` reports AUROC (overall, per-generator, per-length-bucket), FPR at
the `likely_ai` threshold, TPR at fixed 1%/5% FPR, Brier score, and a 10-bin
reliability table; results land in `eval_report.json`. Current numbers for the
committed `calibration_v1.json` (small profile) are recorded below.

Held-out results for `calibration_v1.json` — fit on 1,200 docs (HC3 human/ChatGPT

- RAID sample spanning 11 generators incl. GPT-4-class and paraphrase/homoglyph
  attacks), 941 train / 259 test, `small` profile, Apple-silicon MPS:

| metric                              | value     |
| ----------------------------------- | ------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
--- |
| AUROC                               | **0.990** |
| FPR at `likely_ai` threshold (0.80) | **3.4%**  |
| TPR at `likely_ai` threshold        | 95%       |
| TPR @ 1% FPR                        | 86%       |
| Brier score                         | 0.028     |

Reliability is honest at the extremes (predicted 1.00 → actual 0.99; predicted
0.03 → actual 0.04). Weakest generator in the sample: `cohere-chat`
(AUROC 0.92, TPR 0.69) — adversarial and unfamiliar generators land in the
`uncertain` band more often, by design. For production, re-fit with larger
`--limit` on a GPU box; features are cached so refits are incremental.

## Performance

Expected p95 latency for a 500-word essay: ~2–5 s on an 8-core CPU (small
profile), ~150–500 ms on a T4/A10 GPU. `INFERENCE_CONCURRENCY` gates concurrent
forwards (default 2 — more just thrash on CPU). Identical texts are served from
cache (LRU; Redis if configured).

**v2 scaling path (not built):** split API pods from inference workers behind a
queue. The `Detector` protocol (`app/detectors/__init__.py`) is the seam — swap
the in-process implementations for RPC clients without touching `ensemble.py`.

## Development

```bash
uv run pytest                # unit + integration + golden (no model weights needed)
uv run pytest -m slow        # smoke tests with real weights
uv run ruff check app scripts tests
uv run mypy app
```

The response schema is locked by a golden test
(`tests/golden/fixtures/detect_response_v1.json`); breaking changes require
bumping `SCHEMA_VERSION` and regenerating with `--regen-golden`.

## Known limitations

- Calibration data is ChatGPT-era HC3 plus a RAID sample; brand-new model
  families will be harder, which is what the wide `uncertain` band is for.
- English-only (v1).
- Homoglyph-substituted text is only partially normalized.
- Heavily edited / human-AI hybrid text is fundamentally ambiguous — expect
  `uncertain`.
- **Never use a score alone to accuse a student.** The caveats in the response
  are part of the API contract.

## Roadmap

See [ROADMAP.md](ROADMAP.md) for planned hardening, deployment, and product work.

## Learning

New to ML? Two resources, both written for a TypeScript developer:

- **🕹️ Interactive course** — [`learn-site/index.html`](learn-site/index.html):
  a retro-80s arcade that teaches the concepts behind this project (tokens,
  perplexity, Binoculars, classifiers, calibration, evaluation) with hands-on
  demos, quizzes, XP/levels, and a final exam. Just open the file in a browser
  — no build step. (Or `python3 -m http.server --directory learn-site`.)
- **📖 Deep dive** — [LEARN.md](LEARN.md): the same concepts in prose, from
  "what is a token" to a stage-by-stage track for rebuilding the detector
  yourself.
