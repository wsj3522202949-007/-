---
id: tool-05522
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 需API密钥, 英文文档, 去AI味]
title: AI_Text_Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/sivabanala/ai_text_detector
created: 2026-07-18
updated: 2026-07-18
no: 5522
category: 一、去 AI 味 / Humanizer 库
repo: SivaBanala/AI_Text_Detector
stars: 0
url: https://github.com/sivabanala/ai_text_detector
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

# SivaBanala/AI_Text_Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/sivabanala/ai_text_detector
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：Flask-based AI Text Detector powered by a fine-tuned DistilBERT model. It classifies text as Human-Written or AI-Generated, returns confidence scores, logs prediction history, displays performance metrics on a dashboard, and offers a secure API with API-key management for easy integration into apps and workflows. Built for fast, practical use-case.
- **本地描述**：Flask-based AI Text Detector powered by a fine-tuned DistilBERT model. It classifies text as Human-Written or AI-Generated, returns confidence scores, logs prediction history, displays performance metrics on a dashboard, and offers a secure API with API-key management for easy integration into apps and workflows. Built for fast, practical use-case.
- **拉取时间**：2026-07-25 18:21:48

---

# AI Text Detector

A Flask-based web application that detects whether text is **Human-Written** or **AI-Generated** using a fine-tuned DistilBERT classifier. The project includes:
- A browser UI for live prediction
- A secured API endpoint for programmatic access
- API key generation and management pages
- Dashboard and history pages for model/performance visibility

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Setup](#setup)
- [Run the App](#run-the-app)
- [API Usage](#api-usage)
- [Training the Model](#training-the-model)
- [Data and Artifacts](#data-and-artifacts)
- [Security Notes](#security-notes)
- [Known Limitations](#known-limitations)
- [Troubleshooting](#troubleshooting)
- [Future Improvements](#future-improvements)

## Overview
This project serves a fine-tuned DistilBERT sequence classification model from local files and predicts whether input text is AI-generated or human-written.

At runtime, the Flask backend:
1. Loads tokenizer + model from a local model folder
2. Accepts text input from UI or API
3. Runs inference with PyTorch
4. Returns class label + confidence
5. Logs prediction activity for admin/history tracking

## Features
- **Text classification**: Predicts `Human-Written` or `AI-Generated`
- **Confidence score**: Returns probability of the predicted class
- **Web UI**: Input box + animated confidence visualization
- **Dashboard**: Displays training metrics (accuracy, precision, recall, F1)
- **History/Admin page**: Tracks totals and recent predictions
- **Protected API**: Key-based auth via `X-API-KEY` or `Authorization: Bearer`
- **API key management UI**: Generate, delete, and download keys

## Tech Stack
- **Backend**: Flask
- **ML/Inference**: PyTorch, Transformers (Hugging Face)
- **Model**: DistilBERT for sequence classification
- **Training utilities**: datasets, scikit-learn, Trainer API
- **Frontend**: HTML, CSS, JavaScript, Chart.js

## Project Structure
```text
IOMP/
+- app.py                        # Flask server + routes + inference
+- train_finetuned_model.py      # DistilBERT training pipeline
+- desklib_predict.py            # Reusable prediction helper
+- requirements.txt              # Python dependencies
+- templates/
├── index.html                 # Main predictor UI
├── dashboard.html             # Training metrics page
├── admin.html                 # Prediction history page
├── about.html                 # Project/model explanation
├── api_keys.html              # API key management UI
└── api_docs.html              # API docs template (not currently routed)
+- static/
├── style.css
├── about.css
└── api.css
+- Human&Ai_model/               # Local fine-tuned model files
+- logs/                         # Training logs
+- results/                      # Checkpoints/results
+- metrics.json                  # Runtime prediction stats
+- training_metrics.json         # Training metric summary for dashboard
+- runtime_metrics.json          # Runtime metric outputs
+- predictions_log.jsonl         # Prediction logs
+- api_keys.json                 # API keys storage (local)
```

## How It Works
### Inference flow
1. User submits text on `/` or via `/api/v1/predict`
2. Text is tokenized with `AutoTokenizer`
3. Model runs forward pass (`AutoModelForSequenceClassification`)
4. Softmax probabilities are computed
5. Predicted class is mapped:
   - `0 -> Human-Written`
   - `1 -> AI-Generated`
6. Response returns predicted label and confidence

### Logging flow
Each `/predict` web request updates `metrics.json`:
- `total_checks`
- `ai_count`
- `human_count`
- `recent` list (time, snippet, label, confidence)

## Setup
### 1. Clone repository
```bash
git clone <your-repo-url>
cd IOMP
```

### 2. Create and activate virtual environment
Windows (PowerShell):
```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Ensure model files exist
`app.py` expects local model files at:
```text
C:\Users\HP\OneDrive\Documents\IOMP\Human&Ai_model
```

If you move the project, update `MODEL_PATH` in `app.py`.

## Run the App
```bash
python app.py
```

Default Flask URL:
```text
http://127.0.0.1:5000
```

Main routes:
- `/` -> Text detector UI
- `/about` -> About page
- `/dashboard` -> Training metrics dashboard
- `/admin` -> Prediction history/summary
- `/api-keys` -> API key manager

## API Usage
### Endpoint
`POST /api/v1/predict`

### Authentication
Send one of:
- `X-API-KEY: <key>`
- `Authorization: Bearer <key>`

### Request body
```json
{
  "text": "Your text to analyze"
}
```

### Response example
```json
{
  "label": "AI-Generated",
  "confidence": 0.8731
}
```

### cURL example
```bash
curl -X POST http://127.0.0.1:5000/api/v1/predict \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: YOUR_KEY" \
  -d "{\"text\":\"This is a sample input\"}"
```

## Training the Model
The training script is `train_finetuned_model.py`.

### Current training pipeline
- Reads CSV dataset (`LLM_1.csv`)
- Maps labels:
  - `student -> 0`
  - `ai -> 1`
- Splits train/test
- Tokenizes with `distilbert-base-uncased`
- Trains with `Trainer`
- Computes accuracy/precision/recall/F1

Run training:
```bash
python train_finetuned_model.py
```

After training, export the model/tokenizer to your chosen output directory and point `MODEL_PATH` to that location.

## Data and Artifacts
- `training_metrics.json` is used by the dashboard page
- `metrics.json` is updated by live predictions
- `predictions_log.jsonl` and `runtime_metrics.json` store runtime-related outputs
- `results/` and `logs/` contain training/checkpoint artifacts

## Security Notes
- `api_keys.json` contains active API keys and should not be committed
- Replace default key generation and storage with a secure secret manager for production
- Disable Flask `debug=True` in production
- Add rate limiting and request validation for public deployment

## Known Limitations
- `MODEL_PATH` is currently absolute and machine-specific
- `/api-docs` template exists but no route is currently defined in `app.py`
- `/templates\frontend` route in `app.py` appears invalid and should be cleaned up
- No database; metrics and keys are file-based
- Limited input validation and no role-based admin auth

## Troubleshooting
### Model loading error
- Verify model files exist in `Human&Ai_model/`
- Ensure tokenizer and model configs are present (`config.json`, tokenizer files)

### Unauthorized API response
- Confirm key exists in `api_keys.json`
- Send header exactly as `X-API-KEY` or `Authorization: Bearer <key>`

### Dashboard values missing
- Ensure `training_metrics.json` exists and has valid JSON fields:
  - `accuracy`, `precision`, `recall`, `f1`
  - `accuracy_curve`, `loss_curve`

## Future Improvements
- Move API keys and metrics to a database
- Add user authentication for admin-only routes
- Add unit/integration tests
- Add model versioning + experiment tracking
- Containerize with Docker and add CI/CD pipeline
- Improve API docs and expose `/api-docs` route

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

If you want, this README can be converted next into a shorter public version and a separate developer-focused `CONTRIBUTING.md`.
