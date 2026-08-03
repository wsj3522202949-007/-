---
id: tool-05120
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai_text_detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/ravi341712349/ai_text_detector
created: 2026-07-18
updated: 2026-07-18
no: 5120
category: 一、去 AI 味 / Humanizer 库
repo: ravi341712349/ai_text_detector
stars: 0
url: https://github.com/ravi341712349/ai_text_detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# ravi341712349/ai_text_detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ravi341712349/ai_text_detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：ravi341712349/ai_text_detector
- **拉取时间**：2026-07-25 18:06:52

---

# AI Generated Text Detection with Linguistic Explainability

A production-grade system to detect AI-generated vs human-written text using fine-tuned
RoBERTa combined with 20+ linguistic features and full explainability via SHAP, LIME,
and gradient-based token attribution.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│  React Frontend  (Vite + TypeScript)                            │
│  ├── TextInput          ← paste / type text                     │
│  ├── ResultDashboard    ← verdict card + tabs                   │
│  ├── SentenceHighlighter← colour-coded heatmap                  │
│  ├── LinguisticFeatures ← grouped bar charts                    │
│  └── ExplainabilityPanel← attention / LIME / SHAP views         │
└──────────────────┬──────────────────────────────────────────────┘
                   │ REST (JSON)
┌──────────────────▼──────────────────────────────────────────────┐
│  FastAPI  (Python 3.11)                                         │
│  POST /api/v1/analyse      ← main endpoint                      │
│  POST /api/v1/analyse/batch← bulk analysis                      │
│  GET  /health                                                   │
└──────────────────┬──────────────────────────────────────────────┘
          ┌────────┴────────┐
┌─────────▼──────┐  ┌───────▼────────────────────────────────────┐
│  ML Services   │  │  Explainability Services                    │
│  ─────────     │  │  ─────────────────────                      │
│  RoBERTa       │  │  SHAPExplainer   (token attributions)       │
│  (fine-tuned)  │  │  LIMEExplainer   (word-level weights)       │
│  + sliding     │  │  AttentionHighlighter (fast, inline)        │
│    window      │  │  GradientSaliency (input × gradient)        │
└───────┬────────┘  └───────┬────────────────────────────────────┘
        │                   │
┌───────▼───────────────────▼────────────────────────────────────┐
│  Linguistic Feature Extractor (spaCy + NLTK)                    │
│  Perplexity │ Burstiness │ TTR │ Repetition │ Discourse markers │
└─────────────────────────────────────────────────────────────────┘
```

---

## Quick Start

### 1. Clone and install

```bash
git clone <repo>
cd ai_text_detector

# Python environment
python -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# Copy environment config
cp .env.example .env
# Edit .env — at minimum set SECRET_KEY
```

### 2. Train (or skip and use base model)

```bash
# Full training (downloads datasets automatically)
python training/train.py --epochs 5 --max-samples 50000

# Fast dev run (fewer samples for testing)
python training/train.py --epochs 2 --max-samples 5000
```

The trained model is saved to `./models/ai_detector_roberta/`.
If you skip training, the system falls back to the base `roberta-base` checkpoint
(works but with lower accuracy — ~65% vs ~93% fine-tuned).

### 3. Run backend

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
# Docs available at: http://localhost:8000/docs
```

### 4. Run frontend

```bash
cd frontend
npm install
npm run dev
# UI available at: http://localhost:3000
```

### 5. Docker (full stack)

```bash
cd docker
docker compose up --build
# API: http://localhost:8000
# UI:  http://localhost:3000
# Celery monitor: http://localhost:5555
```

---

## Datasets

| Dataset | Source | Size | Description |
|---------|--------|------|-------------|
| HC3 | `Hello-SimpleAI/HC3` | 58k pairs | Human vs ChatGPT answers |
| GPT-wiki-intro | `aadityaubhat/GPT-wiki-intro` | 150k | Wikipedia intros vs GPT-3 |
| TuringBench | `turingbench/TuringBench` | 168k | 19 different AI generators |
| MixSet | `IVUL-KAUST/MixSet` | varies | Mixed AI/human sentences |

All are available on HuggingFace Hub and downloaded automatically during training.

### Preprocessing steps

1. **Length filter**: drop texts under 50 chars (too short for reliable features)
2. **Deduplication**: MD5 hash on first 200 chars, drop duplicates
3. **Encoding fix**: `ftfy.fix_text()` for garbled Unicode
4. **Balance**: downsample majority class to 1:1 ratio per source
5. **Split**: 80/10/10 train/val/test — stratified by source domain

---

## Evaluation

After training, check `models/ai_detector_roberta/classification_report.txt`.

Expected performance on balanced test set:

| Metric | Fine-tuned RoBERTa | + Linguistic features |
|--------|-------------------|----------------------|
| Accuracy | 93–95% | 94–96% |
| F1 (AI) | 0.93–0.95 | 0.94–0.96 |
| ROC-AUC | 0.97–0.99 | 0.97–0.99 |

Run evaluation manually:
```bash
python training/evaluate.py --model ./models/ai_detector_roberta
```

---

## Explainability methods

### Attention / Gradient saliency (always on, ~50ms)
Computes input × gradient for each token. Highlights which tokens the model
most "looked at" when making its prediction. Fast and good for quick
visual verification.

### LIME (opt-in, ~2–5s)
Locally perturbs the input text (drops words) and fits a linear surrogate.
Best for understanding which *words* are driving the prediction in plain terms.
Enable with `include_lime: true`.

### SHAP (opt-in, ~5–15s)
Uses Shapley values to attribute the prediction to each token.
More theoretically grounded than LIME. Slower but produces signed values
showing direction (toward AI vs toward human).
Enable with `include_shap: true`.

---

## Linguistic features explained

| Feature | AI tendency | Intuition |
|---------|-------------|-----------|
| Unigram perplexity | lower | LLMs pick high-probability tokens |
| Burstiness | lower | LLMs write uniform sentence lengths |
| Type-token ratio | lower | LLMs reuse vocabulary more |
| Bigram repetition | higher | Formulaic phrase reuse |
| Sentence similarity | higher | Parallel structure across sentences |
| Discourse marker density | higher | "Furthermore", "Moreover" overuse |
| Named entity ratio | lower | LLMs avoid concrete specifics |
| Passive voice ratio | higher | LLMs default to passive constructions |

---

## Optimization tips

### Speed
- Use `include_attention=True` only (fastest, sufficient for most use cases)
- Deploy with `--workers 4` for multi-core utilisation
- Cache tokeniser outputs in Redis for repeated texts
- Use `torch.compile()` on PyTorch 2.0+ for 15–30% speedup

### Accuracy
- Fine-tune on domain-specific data (academic, news, social media) separately
- Add calibration with `sklearn.calibration.CalibratedClassifierCV`
- Ensemble RoBERTa + DeBERTa for +1–2% F1
- Use `roberta-large` instead of `roberta-base` for +1–3% accuracy

### Memory
- Use `torch.float16` (half precision) — halves GPU memory with minimal accuracy loss
- `gradient_checkpointing=True` (already enabled) reduces training memory by ~40%
- For CPU deployment, quantise with `optimum` library:
  ```python
  from optimum.intel import INCQuantizer
  ```

---

## Real-world limitations

1. **Paraphrased AI text** — AI text run through a paraphrasing tool scores lower.
   Mitigation: include perplexity as a separate signal.

2. **Domain shift** — Model trained on news/Wikipedia may underperform on code,
   poetry, or domain-specific text. Retrain on in-domain data.

3. **Short texts** — Texts under 100 words are unreliable (confidence is lower).
   The API warns when text is short.

4. **Adversarial prompting** — Users who explicitly prompt for "human-sounding" text
   can reduce detectability. No detector is 100% robust.

5. **False positives on non-native speakers** — Some non-native writing patterns
   overlap with AI features (uniform sentence length, limited vocabulary).
   Always display confidence — do not make binary decisions on confidence < 80%.

---

## Ethical considerations

- **Do not use as sole evidence** in academic integrity cases. It is a signal,
  not proof.
- **Communicate uncertainty**: always show the confidence score alongside the verdict.
- **Bias awareness**: the model may perform differently across languages, dialects,
  and writing styles. Document known limitations to users.
- **Privacy**: do not log submitted texts in production without user consent.
  The default config does NOT log text content, only metadata.
- **Consent**: inform users their text is being processed by an ML model.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Project structure

```
ai_text_detector/
├── backend/
│   ├── main.py                  ← FastAPI app factory
│   ├── core/
│   │   ├── config.py            ← Pydantic settings
│   │   └── feature_engineering.py ← 20+ linguistic features
│   ├── api/
│   │   ├── routes.py            ← /analyse endpoints
│   │   └── schemas.py           ← Request/response models
│   └── services/
│       ├── detector.py          ← RoBERTa inference
│       └── explainability.py    ← SHAP + LIME + attention
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Header.jsx
│   │   │   ├── TextInput.jsx
│   │   │   ├── ResultDashboard.jsx
│   │   │   ├── ConfidenceMeter.jsx
│   │   │   ├── SentenceHighlighter.jsx
│   │   │   ├── LinguisticFeatures.jsx
│   │   │   └── ExplainabilityPanel.jsx
│   │   ├── utils/api.js
│   │   ├── App.jsx
│   │   └── index.css
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── training/
│   ├── train.py                 ← Fine-tuning pipeline
│   └── config.json
├── tests/
│   └── test_all.py              ← pytest test suite
├── docker/
│   ├── docker-compose.yml
│   ├── Dockerfile.api
│   └── Dockerfile.frontend
├── requirements.txt
└── .env.example
```
