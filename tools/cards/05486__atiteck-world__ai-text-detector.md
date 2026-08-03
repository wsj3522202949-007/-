---
id: tool-05486
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/atiteck-world/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5486
category: 一、去 AI 味 / Humanizer 库
repo: atiteck-world/ai-text-detector
stars: 0
url: https://github.com/atiteck-world/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# atiteck-world/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/atiteck-world/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Project Course
- **本地描述**：Project Course
- **拉取时间**：2026-07-25 18:20:29

---

# German AI Text Detector — Politics & History Domain

M.Sc. project (Prof. Ralf C. Staudemeyer). Detects AI-generated German text in the political and historical domains using stylometric and character n-gram features, with both supervised (binary) and one-class (OC-SVM) approaches.

---

## Results

| Model | AUC-ROC | FPR (human) | TPR (AI) | Threshold criterion |
|---|---|---|---|---|
| Binary — Logistic Regression | **0.9655** | 2.83% | 79.79% | val-tuned, TPR ≥ 80% |
| Char n-gram OC-SVM | see `models/chargram/eval_results.json` | — | — | val-tuned |
| Stylometric OC-SVM | see `models/stylometric/eval_results.json` | — | — | val-tuned |
| Embedding OC-SVM (gbert) | see `models/ocsvm_results.json` | — | — | val-tuned |

Threshold selection criterion for all models: **minimise FPR subject to val TPR ≥ 80%**, applied to the validation set only. Test set evaluated once after thresholds are fixed.

---

## Data

| Source | Domain | Sentences |
|---|---|---|
| Bundestag plenary protocols (pp14–pp20, excl. pp20) | Politics | ~3.1 M |
| German Wikipedia — history categories | History | ~1.0 M |
| AI-generated (gemma3:4b via eTeach Thuringia) | Both | ~400 K |

Training uses a balanced 400 K subset (200 K human, 200 K AI not applicable for OC-SVM) with an 80/10/10 train/val/test split (seed 42, SHA-256 deduplication).

Data files are not tracked in git (4.7 GB total). The scraping and generation scripts reproduce them.

---

## Project structure

```
scripts/
  data_sourcing/
    bundestag_scraper.py          # canonical Bundestag XML scraper
    scrape_wikipedia_history.py   # BFS Wikipedia history scraper
    generate_ai_text_final.py     # AI text generation (eTeach / Ollama)
  preprocessing/
    assign_splits_combined.py     # 80/10/10 split assignment for human data
    assign_splits_wikipedia.py    # split assignment for Wikipedia data
    extract_embeddings.py         # gbert-base mean-pool embeddings
    reduce_dimensions.py          # PCA on embeddings
  modeling/
    train_binary.py               # stylometric + char n-gram → LR/SVC/RF
    train_chargram_ocsvm.py       # char n-gram TF-IDF + SVD → OC-SVM
    train_stylometric_ocsvm.py    # 22 stylometric features → OC-SVM
    train_ocsvm.py                # gbert + PCA embeddings → OC-SVM
    error_analysis.py             # binary vs OC-SVM disagreement examples
    evaluate.py                   # general evaluation utilities
    evaluate_disaggregated.py     # per-source and per-domain breakdown

models/
  binary/         # best_model.joblib, tfidf.joblib, svd.joblib, scaler.joblib,
                  # threshold.json, eval_results.json, eval_scores.png
  chargram/       # tfidf_vectorizer.joblib, svd_transformer.joblib, scaler.joblib,
                  # ocsvm_model.joblib, threshold.json, eval_results.json
  stylometric/    # scaler.joblib, ocsvm_model.joblib, threshold.json, eval_results.json
  ocsvm_model.joblib / scaler.joblib   # gbert embedding OC-SVM (models/ root)

data/             # not tracked — see scripts/data_sourcing/ to reproduce
config/
  config.yaml
requirements.txt
```

---

## Run sequence

### 1 — Scrape human text

```bash
# Bundestag (requires downloaded XML files in data/raw/bundestag/)
python scripts/data_sourcing/bundestag_scraper.py --periods 14 15 16 17 18 19

# German Wikipedia — history categories
python scripts/data_sourcing/scrape_wikipedia_history.py --target 1000000
```

### 2 — Generate AI text

```bash
# Political domain
python scripts/data_sourcing/generate_ai_text_final.py \
    --backend eteach --model gemma3:4b --domain political --target 200000

# Historical domain
python scripts/data_sourcing/generate_ai_text_final.py \
    --backend eteach --model gemma3:4b --domain historical --target 200000
```

### 3 — Preprocessing

```bash
python scripts/preprocessing/assign_splits_combined.py
python scripts/preprocessing/extract_embeddings.py      # requires GPU for speed
python scripts/preprocessing/reduce_dimensions.py
```

### 4 — Train models

```bash
python scripts/modeling/train_binary.py               # ~5 min
python scripts/modeling/train_chargram_ocsvm.py       # ~15 min
python scripts/modeling/train_stylometric_ocsvm.py    # ~10 min
python scripts/modeling/train_ocsvm.py                # ~60 min (CPU) / ~10 min (GPU)
```

### 5 — Error analysis

```bash
python scripts/modeling/error_analysis.py --n_examples 3
```

---

## Features

**Stylometric (22 features):** word count, avg word length, long-word ratio, type-token ratio, umlaut ratio, compound ratio, uppercase-mid ratio, punctuation rates (comma, semicolon, colon, dash), digit ratio, question/exclamation endings, function-word ratio, subjunctive ratio, passive ratio, negation ratio, discourse-marker ratio, hedging ratio, avg syllables per word, clause density.

**Char n-gram:** character-level TF-IDF (2–5 grams, 50 K features) + TruncatedSVD (300 dims).

**Embeddings:** deepset/gbert-base mean-pool (768 dim) → PCA (100 dim).

Binary classifier combines stylometric + char n-gram (30 K features, 100 SVD dims) → 122-dim feature vector → Logistic Regression.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Installation

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

Requires Python 3.10+. GPU optional but strongly recommended for `extract_embeddings.py` and `train_ocsvm.py`.
