---
id: tool-05107
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-text-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/abhadre66/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5107
category: 一、去 AI 味 / Humanizer 库
repo: abhadre66/AI-text-Detector
stars: 0
url: https://github.com/abhadre66/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: b9fc7e28e6c15eed
  - methods/改稿润色指令库.md
---

# abhadre66/AI-text-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/abhadre66/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：abhadre66/AI-text-Detector
- **拉取时间**：2026-07-25 18:06:23

---

---
title: AI Text Detector
emoji: 🧠
colorFrom: blue
colorTo: red
sdk: gradio
sdk_version: 6.14.0
python_version: '3.13'
app_file: app.py
pinned: false
---

# AI Text Detector

A machine learning system that classifies text as **human-written** or **AI-generated** using an ensemble approach combining statistical feature analysis (XGBoost) with a fine-tuned transformer model (DistilBERT).

## Model Performance

| Metric    | Score   |
|-----------|------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| Accuracy  | 99.18%  |
| F1 Score  | 99.17%  |
| Precision | 99.26%  |
| Recall    | 99.07%  |
| AUROC     | 99.96%  |

## Key Features

- **Ensemble Architecture** — Combines XGBoost (statistical features) and DistilBERT (transformer) with weighted scoring for robust predictions
- **21 Engineered Features** — Includes vocabulary richness, punctuation patterns, sentence structure, GPT-2 perplexity, and burstiness
- **Explainability** — SHAP-based feature importance analysis and Captum token-level attribution for interpretable results
- **Robustness Tested** — Evaluated against adversarial attacks including synonym substitution, character perturbations, and mixed-origin text
- **Web Interface** — Gradio UI with confidence visualization and token heatmap analysis

## Data Sources

The model is trained on a diverse, multi-source dataset:

- **HC3 Dataset** — Human and ChatGPT answers across Wikipedia, Reddit ELI5, medicine, and finance domains
- **data2.csv** — Essay-based human vs AI text samples
- **AI_Human.csv** — Mixed-domain human vs AI text samples

All datasets are merged, deduplicated, class-balanced, and split into 80/10/10 train/val/test sets.

## Setup

```bash
git clone https://github.com/yourusername/AI-text-Detector.git
cd AI-text-Detector
pip install -r requirements.txt
```

## Usage

### Train the Models

```bash
python src/data_collection.py        # Collect and merge datasets
python src/feature_engineering.py    # Extract 21 statistical + LM features
python src/train_statistical.py      # Train XGBoost, Random Forest, Logistic Regression
python src/train_transformer.py      # Fine-tune DistilBERT
python src/explainability.py         # Generate SHAP + Captum analysis (optional)
python src/robustness.py             # Run adversarial robustness tests (optional)
```

> Training auto-detects Apple Silicon (MPS) / CUDA / CPU.

### Run the App

```bash
python app.py
```

## Tech Stack

- **ML/DL:** PyTorch, HuggingFace Transformers, scikit-learn, XGBoost
- **Explainability:** SHAP, Captum
- **Data:** pandas, NumPy, HuggingFace Datasets
- **Visualization:** matplotlib, seaborn
- **Web App:** Gradio

## License

MIT License — see [LICENSE](https://github.com/abhadre66/AI-text-Detector/blob/main/LICENSE) for details.
