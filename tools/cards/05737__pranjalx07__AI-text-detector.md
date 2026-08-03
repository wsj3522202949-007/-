---
id: tool-05737
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/pranjalx07/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5737
category: 一、去 AI 味 / Humanizer 库
repo: pranjalx07/AI-text-detector
stars: 0
url: https://github.com/pranjalx07/ai-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# pranjalx07/AI-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/pranjalx07/ai-text-detector
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：pranjalx07/AI-text-detector
- **拉取时间**：2026-07-25 18:29:45

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Text Detector

AI Text Detector is a full-stack application for classifying text as **AI-generated** or **human-written**. It combines a FastAPI backend, a Next.js frontend, and a fine-tuned BERT model stored locally in the repository.

The app supports:

- text classification with confidence scores
- detection history with filtering and search
- user feedback submission on past predictions
- an admin dashboard with usage stats and submission management

## Project Overview

The system is split into two parts:

- `backend/` exposes the prediction API, stores detection history, and loads the local model assets
- `frontend/` provides the web UI for detection, history browsing, about pages, and admin views

The main model checkpoint used by default is:

- `backend/bert-base-uncased_80_20_0.05wd_2lr_3epoch/`

Additional trained checkpoints are also included in the backend folder for experimentation and comparison.

## Features

- Detects whether a text is AI-generated or human-written
- Returns confidence, human probability, AI probability, perplexity, and inference time
- Supports optional preprocessing before inference
- Stores each prediction in a SQLite database
- Lets users submit feedback on a result
- Shows a searchable, filterable history of previous analyses
- Includes an admin dashboard with totals, daily trends, and moderation tools
- Provides LIME-based explanation output for word-level feature inspection

## Tech Stack

- Backend: FastAPI, SQLAlchemy, SQLite, Uvicorn
- ML/NLP: PyTorch, Transformers, Hugging Face pipeline, GPT-2 perplexity, LIME
- Frontend: Next.js 16, React 19, TypeScript, Tailwind CSS v4

## Requirements

- Python 3.10 or newer
- Node.js 20 or newer
- npm

## Setup

### 1. Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The backend creates `detections.db` automatically on first run if you are using the default SQLite database.

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

Open the app at:

```text
http://localhost:3000
```

## Environment Variables

### Backend

- `DATABASE_URL` - database connection string. Default: `sqlite:///./detections.db`
- `MODEL_PATH` - path to the local fine-tuned model. Default: `./bert-base-uncased_80_20_0.05wd_2lr_3epoch`
- `MODEL_MAX_LENGTH` - maximum token length for the classifier. Default: `350`
- `MIN_WORDS` - minimum word count required for detection and explanation. Default: `80`
- `CALIBRATION_TEMPERATURE` - probability calibration temperature. Default: `1.6`
- `CORS_ORIGINS` - comma-separated list of allowed frontend origins
- `CORS_ORIGIN_REGEX` - fallback origin regex for localhost development

### Frontend

- `NEXT_PUBLIC_API_URL` - backend base URL. Default: `http://localhost:8000`

## API Endpoints

### Detection

- `POST /api/detect` - classifies text and stores the result

### History

- `GET /api/history` - paginated detection history with search, label filtering, and sorting
- `GET /api/history/{detection_id}` - fetches a single detection record

### Feedback and Admin

- `POST /api/feedback` - stores feedback for a prediction
- `GET /api/stats` - returns dashboard metrics
- `GET /api/admin/feedback` - returns submitted feedback records
- `DELETE /api/admin/submissions/{detection_id}` - removes a submission

## Data Flow

1. The user enters text in the frontend.
2. The frontend sends the text to the FastAPI backend.
3. The backend optionally preprocesses the text, runs the BERT classifier, computes perplexity, and saves the result.
4. The response is shown in the UI, and the record is stored in the history table.
5. Feedback from the UI can later be reviewed in the admin dashboard.

## Model Notes

- The default classifier is a fine-tuned BERT-base-uncased model.
- The project ships with local model artifacts so it can run without retraining.
- Perplexity is computed with GPT-2 and is used as an additional signal in the result payload.
- LIME explanations are available for feature-level inspection of the prediction.

## Repository Layout

```text
AI-detection-system/
  backend/
    main.py
    database.py
    model.py
    models.py
    preprocessing.py
    requirements.txt
    bert-base-uncased_80_20_0.05wd_2lr_3epoch/
    albert-base-v2_70_30_0.05wd_2lr_4epoch/
    distilbert-base-uncased_length_set_balanced/
  frontend/
    src/
      app/
      components/
      lib/
```

## Troubleshooting

- If the backend cannot find the model, confirm `MODEL_PATH` points to one of the bundled checkpoint folders.
- If the frontend cannot reach the API, verify `NEXT_PUBLIC_API_URL` matches the running backend URL.
- The backend requires a text input of at least 80 words by default. Shorter inputs will be rejected with a validation error.
- The first run may take longer while Transformer and GPT-2 assets are loaded.

## Notes

- The UI includes pages for Home, History and About
- The project is built as a group semester project and includes project background content in the About page.
## BCT minor project
- The repository currently uses SQLite for persistence, so no external database server is required for local development.
## DEMO
https://github.com/user-attachments/assets/0e6eb148-6c51-4997-b0f5-6a7749791360
