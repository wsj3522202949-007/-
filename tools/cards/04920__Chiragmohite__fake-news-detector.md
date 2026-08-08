---
id: tool-04920
type: tool
area: 库
status: active
tags: [互动叙事, JavaScript, 协议未明, 需API密钥, 英文文档]
title: fake-news-detector
summary: 互动叙事/聊天写故事
source: https://github.com/chiragmohite/fake-news-detector
created: 2026-07-18
updated: 2026-07-18
no: 4920
category: 一、去 AI 味 / Humanizer 库
repo: Chiragmohite/fake-news-detector
stars: 0
url: https://github.com/chiragmohite/fake-news-detector
tier: "C"
use_case: "互动叙事/聊天写故事"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: e4a1e6489a08da30
  - methods/改稿润色指令库.md
---

# Chiragmohite/fake-news-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/chiragmohite/fake-news-detector
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered fact-checking platform that verifies claims using Google Search + Groq AI. Analyzes text, URLs, images & PDFs with credibility scoring, evidence links, and an AI chatbot.
- **本地描述**：AI-powered fact-checking platform that verifies claims using Google Search + Groq AI. Analyzes text, URLs, images & PDFs with credibility scoring, evidence links, and an AI chatbot.
- **拉取时间**：2026-07-25 17:59:25

---

# TruthScan — AI-Powered Fact Verification Platform

![TruthScan](https://img.shields.io/badge/TruthScan-v4.5-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-Python-green) ![React](https://img.shields.io/badge/React-18-blue) ![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green) ![Deployed](https://img.shields.io/badge/Deployed-Render-purple)

> **Live Demo:** https://truthscan-frontend.onrender.com

---

## What is TruthScan?

TruthScan is a full-stack AI-powered fact-checking web application that analyzes text, URLs, images, and PDFs to determine how credible a claim is. It searches the live internet, reasons about the evidence using Groq's AI, and returns a credibility score from 0 to 100 with detailed reasoning.

Built to fight misinformation — TruthScan gives users the tools to verify news before sharing it.

---

## Live Demo

| Feature | Link |
|--------|------|
| 🌐 Frontend | https://truthscan-frontend.onrender.com |
| ⚙️ Backend API | https://truthscan-backend.onrender.com |

> **Note:** Free tier — backend may take ~30 seconds to wake up on first visit.

---

## Key Features

- **Multi-modal input** — analyze text, URLs, images (OCR), and PDF documents
- **Real-time internet search** — uses Google Custom Search API to find live evidence
- **AI reasoning** — Groq AI reads the evidence and decides if the claim is true or false
- **Smart death claim detection** — automatically detects and correctly scores false death claims about living people
- **Credibility score** — 0-100 score with label (Likely True / Likely False / Needs Verification etc.)
- **Evidence links** — shows supporting and debunking sources with direct links
- **AI chatbot** — ask follow-up questions about any fact-check result
- **User accounts** — register, login, view history and analytics dashboard
- **Consistent scoring** — results are cached so the same claim always gets the same score

---

## Tech Stacks

### Frontend
- **React 18** — component-based UI
- **Tailwind CSS** — modern responsive styling
- **Recharts** — analytics dashboard charts
- **Axios** — API communication

### Backend
- **FastAPI** (Python) — high-performance REST API
- **Google Custom Search API** — real-time web search
- **Groq AI** — LLM reasoning engine (LLaMA 3.3 70B)
- **MongoDB Atlas** — cloud database for users, analyses, and cache
- **Motor** — async MongoDB driver
- **Trafilatura** — web article extraction
- **OCR.Space API** — cloud OCR for image text extraction
- **PDFMiner** — PDF text extraction
- **spaCy** — Named Entity Recognition
- **JWT** — secure authentication with access/refresh tokens

### Deployment
- **Render** — backend (Web Service) + frontend (Static Site)
- **MongoDB Atlas** — M0 free tier cloud database
- **GitHub** — CI/CD via auto-deploy on push

---

## How It Works

```
User inputs claim
       ↓
NLP analysis (suspicious language, clickbait detection)
       ↓
Named Entity Recognition (extract people, places, dates)
       ↓
Google Search (3 queries → real-time results)
       ↓
Evidence scoring (credible domains, fact-checkers, denial/confirm signals)
       ↓
Groq AI reasons about the evidence
       ↓
Python hardcap layer (death claims, negation claims, temporal claims)
       ↓
Credibility score + label + reasoning + evidence links
       ↓
Cached in MongoDB (consistent scores on repeat queries)
```

---

## Scoring System

| Score | Label |
|-------|-------|
| 80–100 | ✅ Likely True |
| 65–79 | 🟡 Partially True |
| 45–64 | ⚠️ Needs Verification |
| 25–44 | 🟠 Misleading / Missing Context |
| 0–24 | ❌ Likely False |

---

## Running Locally

### Prerequisites
- Python 3.11+
- Node.js 18+
- MongoDB (local or Atlas)

### Backend Setup
```bash
cd backend
pip install -r requirements.txt

# Create .env file with these values:
MONGO_URL=mongodb://localhost:27017
DB_NAME=truthscan_db
JWT_SECRET=your_secret_key
GROQ_API_KEY=your_groq_key
GOOGLE_SEARCH_API_KEY=your_google_key
GOOGLE_SEARCH_CX=your_search_engine_id
OCR_SPACE_API_KEY=your_ocr_space_key
FRONTEND_URL=http://localhost:3000

# Start server
uvicorn server:app --reload --port 8001
```

### Frontend Setup
```bash
cd frontend
npm install --legacy-peer-deps

# Create .env file with:
REACT_APP_BACKEND_URL=http://localhost:8001

# Start app
npm start
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/analyze` | Analyze text claim |
| POST | `/api/analyze/url` | Analyze article from URL |
| POST | `/api/analyze/image` | Analyze image via OCR |
| POST | `/api/analyze/pdf` | Analyze PDF document |
| POST | `/api/chat` | AI chatbot for follow-up questions |
| GET | `/api/history` | User's analysis history |
| GET | `/api/stats` | User analytics |
| POST | `/api/auth/register` | Register new user |
| POST | `/api/auth/login` | Login |
| GET | `/api/cache/clear` | Clear result cache |

---

## Project Structure

```
fake-news-detector/
├── backend/
│   ├── server.py          # Main FastAPI application (1700+ lines)
│   ├── requirements.txt   # Python dependencies
│   └── runtime.txt        # Python version for Render
├── frontend/
│   ├── src/
│   │   ├── pages/         # LandingPage, AnalyzerPage, DashboardPage, etc.
│   │   ├── components/    # Navbar, ResultCard, ChatBot, GaugeMeter
│   │   ├── contexts/      # AuthContext (JWT auth)
│   │   └── lib/           # Utilities
│   └── public/
│       └── index.html
└── README.md
```

---

## Author

**Chirag Mohite**
- GitHub: [@Chiragmohite](https://github.com/Chiragmohite)

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## License

MIT License — free to use and modify.
