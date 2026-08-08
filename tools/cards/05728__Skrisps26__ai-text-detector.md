---
id: tool-05728
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/skrisps26/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5728
category: 一、去 AI 味 / Humanizer 库
repo: Skrisps26/ai-text-detector
stars: 0
url: https://github.com/skrisps26/ai-text-detector
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
content_hash: 840bd9f968058b7c
  - methods/改稿润色指令库.md
---

# Skrisps26/ai-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/skrisps26/ai-text-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-Generated Text Detector with Document Upload (PDF/PPTX) - VRAM-Constrained Local Training Pipeline
- **本地描述**：AI-Generated Text Detector with Document Upload (PDF/PPTX) - VRAM-Constrained Local Training Pipeline
- **拉取时间**：2026-07-25 18:29:26

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Text Detector

🔍 Detect AI-generated text from pasted content or uploaded documents (PDF, PPTX, DOCX, TXT).

## Quick Setup

### Prerequisites
- Python 3.10+
- Node.js 18+
- GPU recommended (CUDA), but works on CPU too

### Backend

```bash
cd backend
pip install -r requirements.txt

# Run the server
python -m backend.main
# or
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Training the Model

```bash
# Train with synthetic data (GPU, VRAM-constrained)
python backend/scripts/train.py

# Custom settings
python backend/scripts/train.py --samples 1000 --epochs 4 --vram-mb 1200
```

The model uses **DistilBERT** (268M params) with VRAM constrained to ~1.2GB maximum, leaving room for other GPU processes.

## API

- `GET /health` - Health check
- `POST /api/analyze` - Analyze text or uploaded file
- `POST /api/analyze/batch` - Batch analysis (up to 20 texts)
- `GET /api/train` - Trigger model training

## Architecture

```
┌─────────────┐     POST /api/analyze     ┌──────────────┐
│  Frontend   │ ─────────────────────► │   FastAPI     │
│  Next.js    │                          │   Backend     │
│  (3000)     │ ◄───────────────────── │   (8000)      │
│             │    JSON Result           │              │
└─────────────┘                          │ ┌──────────┐ │
                                         │ │DistilBERT│ │  VRAM ≤ 1.2GB
                                         │ └──────────┘ │
                                         │ ┌──────────┐ │
                                         │ │DocParser │ │  PDF/PPTX/DOCX
                                         │ └──────────┘ │
                                         └──────────────┘
```

## Features

- 🔍 AI vs Human text classification
- 📄 Document upload (PDF, PPTX, DOCX, TXT)
- 📊 Perplexity, burstiness, vocabulary analysis
- 🔋 VRAM-constrained (works alongside other GPU workloads)
- 🤖 Heuristic fallback when no model is loaded
