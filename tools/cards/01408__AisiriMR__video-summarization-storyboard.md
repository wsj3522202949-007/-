---
id: tool-01408
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: video-summarization-storyboard
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/aisirimr/video-summarization-storyboard
created: 2026-07-18
updated: 2026-07-18
no: 1408
category: 二、网文 / 长篇 AI 写作系统 库
repo: AisiriMR/video-summarization-storyboard
stars: 1
url: https://github.com/aisirimr/video-summarization-storyboard
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 2a5abe0bd3f2d384
  - methods/最强写作方法论_全球最强综合版.md
---

# AisiriMR/video-summarization-storyboard

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/aisirimr/video-summarization-storyboard
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：gemini-ai, nlp, python, storyboard, streamlit, video-summarization, youtube
- **GitHub 描述**：ai-powered YouTube video summarizer and visual storyboard generator using Google Gemini Pro
- **本地描述**：ai-powered YouTube video summarizer and visual storyboard generator using Google Gemini Pro
- **拉取时间**：2026-07-23 23:20:10

---

# 🎬 Video Summarization — Visual Storyboard using Video Clips

> An AI-powered web application that summarizes YouTube videos, extracts key points, generates an engaging story, and produces a Stable Diffusion-ready storyboard prompt — all in seconds.

**RV College of Engineering, Bengaluru | 2023–24**  
Department of Computer Science and Engineering

---

---

## 📌 Overview

Modern users face information overload when consuming video content. This project tackles that problem by building a system that:

1. Takes a **YouTube video link** as input
2. Extracts the **transcript** automatically
3. Uses **Google Gemini Pro** to summarize and generate an engaging story with key points
4. Produces a **Stable Diffusion prompt** for generating a visual storyboard image

The app is built with **Streamlit** and tested across 4 video categories: Kids Short Stories, Education, Vlogs, and Science Experiments.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend / UI | Streamlit |
| AI / LLM | Google Gemini Pro (`google-generativeai`) |
| Transcript Extraction | `youtube-transcript-api` |
| Environment Management | `python-dotenv` |
| Data & Analysis | Python, CSV |
| Visualization | Custom graphs (`graphs.py`) |

---

## 📁 Project Structure

```
video-summarization/
│
├── app.py                          # Main Streamlit application
├── test.py                         # Performance testing script (avg time measurement)
├── graphs.py                       # Evaluation graph generation
├── table.py                        # Table generation for metrics
├── Prompts.txt                     # All prompts used in experiments
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variable template (safe to share)
├── .gitignore
├── README.md
│
├── data/
│   ├── Videos_-_Kids_short_story.csv
│   ├── Videos_-_Education.csv
│   ├── Videos_-_Vlog.csv
│   ├── Videos_-_Science_Experiments.csv
│   ├── Comprehensive_Evaluation_Metrics.csv
│   ├── User_Satisfaction_Scores.csv
│   ├── storyboard_analysis_scores.csv
│   └── youtube.csv
│
├── assets/
│   ├── screenshots/                # App screenshots and charts
│   └── pictures/                   # Generated storyboard images per category
│
└── docs/
    └── project_report.pdf          # Full project report
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/video-summarization.git
cd video-summarization
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

> 🔑 Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### 5. Run the app

```bash
streamlit run app.py
```

---

## 🚀 How It Works

1. Paste any **YouTube video URL** into the input box
2. The app fetches the video's **auto-generated transcript** via `youtube-transcript-api`
3. The transcript is sent to **Gemini Pro** with a crafted prompt to generate:
   - A summary of key points
   - An engaging story with appropriate tonality
4. The story is then passed back to Gemini Pro to generate a **Stable Diffusion image prompt** for visual storyboard creation

---

## 📊 Evaluation & Results

The system was tested on **4 YouTube video categories** with 2 prompt variations each:

| Category | Avg Processing Time | User Satisfaction |
|----------|-------------------|-------------------|
| Kids Short Story | ~3 sec/min | High |
| Education | ~3 sec/min | High |
| Vlog | ~3 sec/min | High |
| Science Experiments | ~3 sec/min | High |

Key findings:
- Handles videos from **2 minutes to 1 hour** in length
- Supports up to **500 simultaneous users**
- Statistical analysis (t-test, effect size, correlation) confirmed robustness across prompt variations

Full metrics and charts are available in the `/data` and `/assets/screenshots` folders, and detailed analysis is in `docs/project_report.pdf`.

---

## 📸 Screenshots

_(See `/assets/screenshots/` for all charts and app UI screenshots)_

---

## 🔮 Future Enhancements

- Real-time video summarization (live streams)
- Direct integration with Stable Diffusion for in-app image generation
- Multi-language transcript support
- User feedback loop to refine prompts adaptively
- Support for non-YouTube video platforms

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---
