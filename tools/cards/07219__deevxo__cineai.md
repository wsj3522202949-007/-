---
id: tool-07219
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: cineai
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/deevxo/cineai
created: 2026-07-18
updated: 2026-07-18
no: 7219
category: 画龙补充 / 扩容入库 — 补充源
repo: deevxo/cineai
stars: 1
url: https://github.com/deevxo/cineai
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# deevxo/cineai

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/deevxo/cineai
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：cineai
- **拉取时间**：2026-07-25 19:14:31

---

# 🎬 CineAI — AI Movie Production Agent

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=Streamlit\&logoColor=white)](https://streamlit.io/)
[![Gemini AI](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge\&logo=google\&logoColor=white)](https://gemini.google.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

👉 **[Live Demo](https://cine-ai.streamlit.app)**
👉 **[GitHub Repo](https://github.com/deevXO/CineAI)**

CineAI transforms your raw movie idea into a **production-ready concept** with AI-powered script writing, smart casting, production planning, and live industry insights.

---

## ✨ Features

### 🎭 Script Writing

* AI-generated **3-act structure**
* Character bios & backstories
* Plot twists & key scenes
* Genre-specific storytelling

### 🌟 Smart Casting

* AI-suggested **actors for roles**
* Bollywood & Hollywood coverage
* Diversity & chemistry checks

### 🎬 Production Planning

* Budget estimation (with breakdown)
* Location & director suggestions
* AI marketing strategy ideas
* Timeline & milestones

### 📊 Industry Intelligence

* Real-time **box office trend analysis**
* Market insights & audience targeting
* Current Bollywood/Hollywood news

### 🔐 Simple API Config

* Configure **Google Gemini API key** directly in the app’s frontend
* No `.env` or backend setup required

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/deevXO/CineAI.git
cd CineAI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

### 5. Enter your API Key in the frontend

* Launch the app → You’ll see a config panel to enter your **Gemini API key**.
* No manual `.env` editing needed.

---

## 📂 Project Files

```
CineAI/
│── app.py             # Streamlit frontend + API key config
│── movie_agent.db     # SQLite3 database (local storage)
│── requirements.txt   # Dependencies
│── README.md          # Documentation
```

---

## 📸 Demo Screenshots

*(Add screenshots/GIFs here of script generation, casting, and planning outputs — this massively boosts repo appeal.)*

---

## 🛠️ Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch (`git checkout -b feature-idea`)
3. Commit your changes
4. Push and open a PR

---

## 📅 Roadmap

* [ ] Export scripts to **PDF/Final Draft**
* [ ] Add **multi-language support** (Hindi, Spanish, etc.)
* [ ] Integration with **IMDb/TMDB APIs**
* [ ] Team collaboration mode
* [ ] AI-powered storyboard generation (images)

---

## 📜 License

This project is licensed under the **MIT License** — see `[LICENSE](LICENSE)` for details.

related:
  - methods/QUICK_START.md
---
