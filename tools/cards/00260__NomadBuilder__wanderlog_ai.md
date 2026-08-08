---
id: tool-00260
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: wanderlog_ai
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/nomadbuilder/wanderlog_ai
created: 2026-07-18
updated: 2026-07-18
no: 260
category: 二、网文 / 长篇 AI 写作系统 库
repo: NomadBuilder/wanderlog_ai
stars: 1
url: https://github.com/nomadbuilder/wanderlog_ai
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: dd5c17233405ec38
  - methods/最强写作方法论_全球最强综合版.md
---

# NomadBuilder/wanderlog_ai

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/nomadbuilder/wanderlog_ai
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered travel story generator with interactive world map
- **本地描述**：AI-powered travel story generator with interactive world map
- **拉取时间**：2026-07-23 22:46:40

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# WanderLog AI

A beautiful travel journal app that lets you create stories about your adventures and visualize them on an interactive world map.

## 🏗️ Project Structure

```
wanderlog_ai/
├── backend/                    # Backend Python code
│   ├── main.py                # Main Flask/Cloud Functions app
│   ├── requirements.txt       # Python dependencies
│   ├── config/               # Configuration files
│   ├── utils/                # Utility modules
│   ├── data/                 # Data storage
│   └── scripts/              # Utility scripts
├── frontend/                  # Frontend web assets
│   ├── index.html            # Main HTML file
│   └── assets/               # Static assets (CSS, JS, images, maps)
├── docs/                     # Documentation
├── scripts/                  # Build/deployment scripts
└── backups/                  # Backup files
```

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Start the servers:**
   ```bash
   ./scripts/start_servers.sh
   ```

3. **Open your browser:**
   - Frontend: http://localhost:8000
   - Backend API: http://localhost:8080

## 🛠️ Development

- **Frontend**: HTML, CSS, JavaScript (vanilla)
- **Backend**: Python Flask with Google Cloud Functions Framework
- **Storage**: Local JSON files (can be configured for Google Cloud Storage)

## 📁 Key Files

- `frontend/index.html` - Main application interface
- `frontend/assets/js/` - JavaScript modules (app, map, ui, api)
- `frontend/assets/css/styles.css` - Main stylesheet
- `backend/main.py` - Backend API server
- `scripts/start_servers.sh` - Development server startup script

## 🗺️ Features

- **Interactive World Map**: Click countries to see your stories
- **Story Creation**: Write and save travel memories
- **Country Tracking**: Visualize visited countries on the map
- **Responsive Design**: Works on desktop and mobile
- **Local Storage**: No external dependencies required

## 📚 Documentation

See the `docs/` folder for detailed documentation:
- `QUICKSTART.md` - Getting started guide
- `DEPLOYMENT_GUIDE.md` - Deployment instructions
- `TESTING.md` - Testing procedures 
