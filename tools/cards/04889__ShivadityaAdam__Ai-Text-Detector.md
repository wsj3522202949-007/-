---
id: tool-04889
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: Ai-Text-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/shivadityaadam/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 4889
category: 一、去 AI 味 / Humanizer 库
repo: ShivadityaAdam/Ai-Text-Detector
stars: 0
url: https://github.com/shivadityaadam/ai-text-detector
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
content_hash: aba1533d4aa1f7ea
  - methods/改稿润色指令库.md
---

# ShivadityaAdam/Ai-Text-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/shivadityaadam/ai-text-detector
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：ShivadityaAdam/Ai-Text-Detector
- **拉取时间**：2026-07-25 17:58:13

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Text Detector

A high-fidelity forensic platform designed to identify machine-generated content in text and images. By analyzing linguistic patterns—specifically **Perplexity** and **Burstiness**—the system provides a mathematical probability of AI involvement.

## 🔬 Scientific Methodology
This project utilizes two primary statistical markers to verify authenticity:
* **Perplexity:** Measures the "randomness" of text. Since LLMs predict the next most likely token, AI text often exhibits lower perplexity (high predictability).
* **Burstiness:** Analyzes the variance in sentence structure. Human writing is naturally "bursty," while AI tends toward a uniform rhythmic flatness.

## 🛠️ Architecture
- **AI Engine (Python):** A FastAPI core utilizing GPT-2 for linguistic scoring and EasyOCR for image text extraction.
- **Audit Service (Go):** A high-performance Fiber service dedicated to generating cryptographically stable PDF reports.
- **Frontend (React):** A modern dashboard built with Vite and Tailwind CSS for real-time forensic visualization.
- **Persistence (Supabase):** Managed PostgreSQL and Auth to ensure data integrity.

🚀 Getting Started
1. Environment Configuration

Create a .env file in the root directory (and a copy in the /reports folder) with the following:
Code snippet

SUPABASE_URL=your_project_url
SUPABASE_KEY=your_anon_key
DATABASE_URL=your_postgresql_connection_string

2. Run AI Engine (Root)
Bash

pip install -r requirements.txt
uvicorn main:app --reload

3. Run Audit Service (Go)
Bash

cd reports
go run main.go

4. Run Frontend (React)
Bash

cd frontend
npm install
npm run dev
## 📂 Project Structure
```text
/                  # Python AI Engine & API Logic
├── frontend/      # React (Vite) User Interface
└── reports/       # Go Reporting & Audit Service
