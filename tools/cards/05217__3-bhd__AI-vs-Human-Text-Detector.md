---
id: tool-05217
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-vs-Human-Text-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/3-bhd/ai-vs-human-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5217
category: 一、去 AI 味 / Humanizer 库
repo: 3-bhd/AI-vs-Human-Text-Detector
stars: 1
url: https://github.com/3-bhd/ai-vs-human-text-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: ceaf3464ee54a833
  - methods/改稿润色指令库.md
---

# 3-bhd/AI-vs-Human-Text-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/3-bhd/ai-vs-human-text-detector
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：ci-cd, flask, machine-learning, nlp, python, svm, text-classification
- **GitHub 描述**：Real-time AI vs Human text classifier — 99.96% accuracy, Flask API, CI/CD auto-retraining
- **本地描述**：Real-time AI vs Human text classifier — 99.96% accuracy, Flask API, CI/CD auto-retraining
- **拉取时间**：2026-07-25 18:10:25

---

# AI vs Human Text Detector

Real-time text origin classifier — 99.96% accuracy · Flask API · CI/CD auto-retraining

---

## Overview

A fully deployed AI vs Human text classification system built around a lightweight Flask backend,
a hybrid TF-IDF and stylistic feature representation, and a high-performance Linear SVM classifier.

The system provides two client interfaces — a command-line tool and a browser-based GUI — that
communicate with the backend through standardized REST endpoints for prediction, feedback
submission, and feedback retrieval. User corrections feed into an automated offline retraining
pipeline that periodically retrains the model and redeploys through GitHub → Railway CI/CD.

> A live demo was previously deployed on Railway. The full system can be run locally using
> the instructions below.

---

## Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 99.96% |
| Macro-Precision | 99.96% |
| Macro-Recall | 99.96% |
| Macro-F1 | 99.96% |
| ROC-AUC | 0.9999 |
| PR-AUC | 0.9999 |

Evaluated on a held-out test set not used during training or feature selection.

---

## Features

- Real-time text classification via a Flask REST API
- Browser-based GUI (HTML/JS) for predictions, confidence scores, and feedback
- Command-line client for local testing and feedback submission
- Automated offline retraining using accumulated user feedback
- CI/CD auto-redeployment through GitHub → Railway
- Modular preprocessing and inference pipeline (deterministic between training and deployment)

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Flask |
| ML Model | Linear SVM (scikit-learn) |
| Features | TF-IDF (20k terms) + 7 stylistic numeric features |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Railway, GitHub CI/CD |

---

## Repository Structure
```
├── api_server.py              # Flask backend (prediction, feedback, admin)
├── cli_client.py              # Command-line client for local testing
├── inference_svm.py           # Vectorization, feature scaling, SVM inference
├── preprocess_utils.py        # Text cleaning + numeric stylistic features
├── train_linear_svm.py        # Final model training script
├── retrain_with_feedback.py   # Automated offline retraining + CI/CD push
├── artifacts/
│   └── models/                # Serialized model, vectorizer, scaler
├── static/
│   └── index.html             # Browser-based GUI
├── requirements.txt
├── Procfile                   # Railway deployment config
└── README.md
```
---

## Installation
```bash
pip install -r requirements.txt
```

Python 3.9+ is required.

---

## Running Locally

### Start the backend
```bash
python api_server.py
```

### Available endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Web interface |
| `/predict` | POST | Run inference on input text |
| `/feedback` | POST | Submit a corrected label |
| `/download-feedback?key=1234` | GET | Export feedback log (admin) |
| `/health` | GET | Service status |

### Command-line client
```bash
python cli_client.py
```

Prompts for input text, displays prediction and confidence score, and optionally submits feedback.

### Web interface

Access locally at: `http://localhost:8000`

---

## How It Works

1. User submits text via GUI or CLI
2. Backend applies preprocessing: lowercasing, URL/HTML removal, whitespace normalization
3. Hybrid feature vector is constructed: TF-IDF (20k χ²-selected terms) + 7 stylistic features
4. Linear SVM produces prediction, decision margin, and confidence score
5. User can optionally submit a corrected label for retraining
6. Retraining script downloads feedback, retrains on combined dataset, and pushes updated model via CI/CD

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Authors

- **Omar Abdelhady** — [@3-bhd](https://github.com/3-bhd)
- **Ahmed Monir** — [@MonirCSauc](https://github.com/MonirCSauc)

The American University in Cairo
