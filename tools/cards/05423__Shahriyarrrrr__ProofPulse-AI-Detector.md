---
id: tool-05423
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: ProofPulse-AI-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/shahriyarrrrr/proofpulse-ai-detector
created: 2026-07-18
updated: 2026-07-18
no: 5423
category: 一、去 AI 味 / Humanizer 库
repo: Shahriyarrrrr/ProofPulse-AI-Detector
stars: 2
url: https://github.com/shahriyarrrrr/proofpulse-ai-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 165bbc9ffcf5a27c
  - methods/改稿润色指令库.md
---

# Shahriyarrrrr/ProofPulse-AI-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/shahriyarrrrr/proofpulse-ai-detector
- **Stars**：2
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Detect AI-generated text & plagiarism with React desktop UI and FastAPI backend.
- **本地描述**：Detect AI-generated text & plagiarism with React desktop UI and FastAPI backend.
- **拉取时间**：2026-07-25 18:18:05

---

# 🚀 ProofPulse — AI Text & Plagiarism Detector (React + FastAPI)

**ProofPulse** scores how likely text is AI-generated and surfaces plagiarism-style matches (“hits”). It’s fast, local-first, and built for demos and coursework: sleek desktop-style UI, **overall score**, **paragraph bands** (`low | moderate | high`), and **paste / upload** workflows.

![Node](https://img.shields.io/badge/node-%3E%3D18-green)
![Python](https://img.shields.io/badge/python-%3E%3D3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-rocket-teal)
![React](https://img.shields.io/badge/React-18-61dafb)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#-license)

> Monorepo: **desktop-ui** (React + TS) • **backend** (FastAPI).  
> Repo: `https://github.com/Shahriyarrrrr/ProofPulse-AI-Detector`

---

## ✨ Highlights

- **Two flows:** Paste text or upload a file (extract → analyze)
- **Signals that matter:** Overall AI score + per-paragraph bands
- **Plagiarism hints:** Top hits (doc id, paragraph, score, optional snippet)
- **Zero cloud dependency:** Run everything locally
- **Configurable & extensible:** ENV-driven; swap models/heuristics/indexes

---
## 👤 Author

Built by [**Shahriyarrrrr**](https://github.com/Shahriyarrrrr).
## 🗺️ Folder Map

---

ProofPulse-AI-Detector/
├─ backend/
│ ├─ app/
│ │ ├─ main.py # FastAPI app (/analyze, /health)
│ │ ├─ models/ # Pydantic schemas
│ │ ├─ services/ # scoring + plagiarism lookups
│ │ └─ core/ # settings, CORS, logging
│ ├─ data/ # local indexes/models (gitignored)
│ ├─ requirements.txt
│ └─ .env # local only
└─ desktop-ui/
├─ src/
│ ├─ App.tsx # main UI
│ ├─ components/ # BandBadge, Results, Upload/Paste
│ └─ lib/api.ts # API client
├─ package.json
└─ .env # local only

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## ⚡ Quick Start (Windows)

> Local folder example: `D:\ai-detector`

### 1) Backend (FastAPI)

```cmd
cd /d D:\ai-detector\backend
py -3.10 -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
notepad .env

backend/.env (example):
HOST=0.0.0.0
PORT=8000
CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
MODEL_PATH=./models/local
PLAGIARISM_INDEX_PATH=./data/index
MAX_TEXT_LENGTH=20000

🧪 How to Use

Choose Paste Text or Upload File

Click Analyze

Review:

Overall score + band

Per-paragraph scores/bands

Plagiarism hits (doc id, paragraph, score, optional snippet)

🔌 API Snapshot

Align these with your actual routes if you’ve customized them.

POST /analyze

Request (JSON):

{ "text": "Your paragraph(s) go here..." }


Response (example):

{
  "overall": { "ai_score": 0.27, "ai_band": "low" },
  "paragraphs": [
    {
      "paragraph": 1,
      "ai_score": 0.18,
      "ai_band": "low",
      "plagiarism_hits": [
        { "score": 0.92, "doc_id": "abc123", "paragraph": 5, "text": "matched snippet..." }
      ]
    }
  ]
}

GET /health
{ "status": "ok", "version": "x.y.z" }

🧩 Config Cheat Sheet

Frontend → Backend URL: desktop-ui/.env

VITE_API_BASE_URL=http://127.0.0.1:8000


CORS origins: backend/.env → CORS_ORIGINS=http://localhost:5173,...

Input limits: MAX_TEXT_LENGTH in backend .env

Local resources: put models/indexes under backend/data / backend/models

🛠 Troubleshooting

UI “Network Error”

Backend running? http://127.0.0.1:8000/docs

VITE_API_BASE_URL correct?

CORS_ORIGINS includes http://localhost:5173

/analyze 404

Confirm route in backend/app/main.py

Confirm client path in desktop-ui/src/lib/api.ts

Import errors

Start with module path:

python -m uvicorn backend.app.main:app --reload --port 8000


PowerShell activation policy

Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

📦 .gitignore (drop-in)

Create at repo root:

# Node / React
node_modules/
dist/
build/
.cache/
coverage/
*.log
.eslintcache
.stylelintcache

# Python / FastAPI
__pycache__/
*.py[cod]
*.egg-info/
.venv/
env/
venv/
.pytest_cache/
.mypy_cache/
.coverage
coverage.xml
htmlcov/

# Env / Secrets
*.env
*.env.*
.env.local
.env.development.local
.env.test.local
.env.production.local

# OS / Editors
.DS_Store
Thumbs.db
.idea/
.vscode/

# Data / Models (optional)
backend/data/
backend/models/
*.db
*.sqlite*
*.pkl
*.h5

🧭 Roadmap

⏳ Export report (PDF/CSV)

⏳ Click-through plagiarism sources

⏳ Model profiles & tuning from UI

⏳ Batch/CLI mode

⏳ API key / basic auth

🤝 Contributing
git checkout -b feat/your-idea
git commit -m "feat: add your-idea"
git push origin feat/your-idea
# open a PR with screenshots + test notes


