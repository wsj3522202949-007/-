---
id: tool-05456
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-mood-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/harshitclub/ai-mood-detector
created: 2026-07-18
updated: 2026-07-18
no: 5456
category: 一、去 AI 味 / Humanizer 库
repo: harshitclub/ai-mood-detector
stars: 1
url: https://github.com/harshitclub/ai-mood-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: c6a733da37d9301a
  - methods/改稿润色指令库.md
---

# harshitclub/ai-mood-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/harshitclub/ai-mood-detector
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：ai, ai-chat, artificial-intelligence, emotion-detection, expressjs, fastapi, fullstack, machine-learning, nextjs, nlp, nodejs, python, sentiment-analysis, tailwindcss, text-analysis, typescript
- **GitHub 描述**：AI-powered mood and emotion detection web application using Next.js, Node.js, FastAPI, and NLP for sentiment analysis and emotional insights from text.
- **本地描述**：AI-powered mood and emotion detection web application using Next.js, Node.js, FastAPI, and NLP for sentiment analysis and emotional insights from text.
- **拉取时间**：2026-07-25 18:19:22

---

# AI Mood Detector

AI Mood Detector is a full-stack AI-powered web application that detects mood, emotions, sentiment, and emotional tone from user text using Natural Language Processing (NLP).

---

## Features

- Mood Detection
- Emotion Classification
- Sentiment Analysis
- Emoji Prediction
- Motivational Responses
- Chat-style Interface
- Real-time API Communication

---

## Tech Stack

### Frontend
- Next.js
- TypeScript
- Tailwind CSS

### Backend
- Node.js
- Express.js
- TypeScript

### AI Service
- FastAPI
- Python
- TextBlob
- NLTK

---

## Project Architecture

```txt
Frontend (Next.js)
        ↓
Node.js Backend API
        ↓
Python AI Service
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/harshitclub/ai-mood-detector.git
```

---

# Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

# Backend Setup

```bash
cd backend
npm install
npm run dev
```

---

# AI Service Setup

```bash
cd ai-service

python -m venv venv

# Activate virtual environment

# Windows
venv\\Scripts\\activate

# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## Environment Variables

### Frontend

`.env.local`

```env
NEXT_PUBLIC_API_URL=http://localhost:5000
```

---

### Backend

`.env`

```env
PORT=5000
FRONTEND_URL=http://localhost:3000
AI_SERVICE_URL=http://127.0.0.1:8000
```

---

### AI Service

`.env`

```env
APP_NAME=AI Mood Detector API
APP_VERSION=1.0.0
FRONTEND_URL=http://localhost:3000
```

---

## API Endpoint

```txt
POST /api/v1/analyze
```

### Request

```json
{
  "text": "I am feeling stressed today"
}
```

### Response

```json
{
  "success": true,
  "message": "Text analyzed successfully",
  "data": {
    "mood": "Negative",
    "emotion": "Stress",
    "emoji": "😩",
    "sentiment_score": -0.39,
    "response": "Take a small break and breathe 🌼"
  }
}
```

---

## Future Improvements

- Hugging Face Transformers
- Real ML Models
- Chat History
- Authentication
- Redis Caching
- Docker Deployment
- Analytics Dashboard

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## License

MIT
