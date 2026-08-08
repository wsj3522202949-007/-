---
id: tool-05395
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai_text_detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/hashemwa/ai_text_detector
created: 2026-07-18
updated: 2026-07-18
no: 5395
category: 一、去 AI 味 / Humanizer 库
repo: hashemwa/ai_text_detector
stars: 0
url: https://github.com/hashemwa/ai_text_detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 0c644a8622881908
  - methods/改稿润色指令库.md
---

# hashemwa/ai_text_detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/hashemwa/ai_text_detector
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：hashemwa/ai_text_detector
- **拉取时间**：2026-07-25 18:16:59

---

# AI Text Detector

A classifier that distinguishes human-written from AI-generated text across three domains: job postings, agricultural listings, and social media. Six trained models are served through an interactive Streamlit app.

**Live demo:** https://cse881-aidetector.streamlit.app

CSE 881 — Spring 2025, Michigan State University.

## Overview

- **4,996** labeled samples across **3** distinct domains
- **9** AI text sources: Claude, ChatGPT, Gemini, Copilot, Perplexity, and 4 NVIDIA NIM models
- **6** trained models: CatBoost, Logistic Regression, Random Forest, SVM, XGBoost, and TinyBERT
- Best model: **TinyBERT at 96.1%** accuracy

## Datasets

| Domain | Samples | Human Source | AI Sources |
|---|---|---|---|
| Job Postings | 3,000 | Indeed (scraped via Octoparse) | Claude, ChatGPT, Copilot, Gemini, Perplexity |
| Agricultural Listings | 790 | Care Farming Network (scraped via Playwright) | 4 NVIDIA NIM models (gpt-oss-120b, qwen2.5-7b, mixtral-8x22b, llama-3.1-70b) |
| Social Media Posts | 1,206 | Reddit | ChatGPT, Claude, Gemini |

## Setup

### Requirements
- **Python 3.12** (TensorFlow 2.20 has no wheels for 3.13+)
- ~2 GB free disk space for model files

### Install

```bash
git clone https://github.com/hashemwa/cse_881_project.git
cd cse_881_project

python3.12 -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

The pinned versions in `requirements.txt` are required — the saved sklearn pickles and the TinyBERT `.keras` file are only guaranteed to load with the exact library versions they were trained on.

### Run the app

```bash
streamlit run app.py
```

The app opens at http://localhost:8501.

### (Optional) Retrain the models

Open `classification_models.ipynb` in Jupyter and run all cells. This regenerates every file in `models/`.

## Project Structure

```
cse_881_project/
├── app.py                      # Streamlit app (entry point)
├── classification_models.ipynb # Training notebook (baselines + TinyBERT)
├── Reddit_Analysis.ipynb       # Social media dataset analysis
├── requirements.txt            # Pinned dependencies
├── models/                     # Trained model artifacts
│   ├── catboost_jobs.cbm
│   ├── lr_jobs.pkl
│   ├── rf_jobs.pkl
│   ├── svm_jobs.pkl
│   ├── xgboost_jobs.json
│   ├── tinybert_jobs.keras
│   └── tfidf_jobs.pkl
└── scraping/
    ├── jobs/                   # Indeed + 5 LLM-generated job postings
    ├── agricultural/           # Care Farming Network + NVIDIA NIM listings
    └── social_media/           # Reddit + 3 LLM-generated posts
```

## App Features

- **Detector** — Paste any text, pick a model, get a prediction with confidence.
- **Performance** — Compare accuracy, precision, recall, and F1 across all 6 models; view confusion matrices.
- **Data** — Browse each dataset with source breakdowns, class balance, and length distributions.

## Team

| Member | Contribution |
|---|related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| Hussain Aljafer | Job posting collection, AI generation, preprocessing (salary/location extraction), baseline models, detection algorithm design |
| Wahid Hashem | Dataset collection, baseline models, Streamlit app (UI/UX), report/presentation |
| Aryan Sharma | AI job postings (ChatGPT Deep Research, Gemini Flash Thinking), social media dataset, baseline research |
| Ricky Li | Agricultural listings scraping, NVIDIA NIM generation pipeline, neural network / LLM detection methods |
