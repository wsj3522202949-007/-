---
id: tool-05016
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 需API密钥, 英文文档, 去AI味]
title: AI-vs-Human-Text-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/akshay5896/ai-vs-human-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5016
category: 一、去 AI 味 / Humanizer 库
repo: AKSHAY5896/AI-vs-Human-Text-Detector
stars: 0
url: https://github.com/akshay5896/ai-vs-human-text-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 9a95cc51b1e25365
  - methods/改稿润色指令库.md
---

# AKSHAY5896/AI-vs-Human-Text-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/akshay5896/ai-vs-human-text-detector
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：Flask web app that detects AI-generated vs human-written text using Groq's Llama 3.1 LLM. Features confidence scoring, forensic indicators, and animated UI.
- **本地描述**：Flask web app that detects AI-generated vs human-written text using Groq's Llama 3.1 LLM. Features confidence scoring, forensic indicators, and animated UI.
- **拉取时间**：2026-07-25 18:03:02

---

# 🔍 TextForensics — AI vs Human Text Detector

A Flask web app that classifies whether a given piece of text was written by an **AI** or a **human**, powered by **Groq's Llama 3.1 LLM** — fast, free, no credit card required.

## 🌐 Live Demo
> Deploy on PythonAnywhere: `https://yourusername.pythonanywhere.com`

---

## ✨ Features

- **Binary classification** — AI-Generated vs Human-Written
- **Confidence score** with animated progress bar
- **AI & Human probability** side-by-side meters
- **Key forensic indicators** — LLM explains its reasoning
- **One-line forensic summary** of the verdict
- Built-in sample texts to test instantly
- `Ctrl+Enter` shortcut to analyze
- Animated scanner effect during analysis

---

## 🛠 Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Backend    | Python 3.10+, Flask 3.x           |
| AI Model   | Llama 3.1 8B (via Groq API)       |
| Frontend   | HTML / CSS / Vanilla JS           |
| Fonts      | Space Grotesk, Inter, JetBrains Mono |

---

## 📁 Project Structure

```
fake-text-detector/
├── app.py              # Flask routes + Groq API logic
├── templates/
│   └── index.html      # Full UI
├── .env                # API key (not committed to GitHub)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Local Setup

### 1. Clone & install

```bash
git clone https://github.com/AKSHAY5896/fake-text-detector.git
cd fake-text-detector
pip install -r requirements.txt
```

### 2. Get free Groq API key

👉 [console.groq.com](https://console.groq.com) → Sign up with Google → API Keys → Create Key

No credit card required.

### 3. Add API key to `.env`

```
GROQ_API_KEY=gsk_...your_key_here...
```

### 4. Run

```bash
python app.py
```

Open `http://localhost:5000` in your browser.

---

## 🌐 Deploy to PythonAnywhere

1. Upload all project files to PythonAnywhere
2. Go to **Web** tab → Add new web app → Manual config → Python 3.10
3. Set WSGI file to point to your `app.py`
4. Open a **Bash console** and install dependencies:
```bash
pip3.10 install flask groq python-dotenv --user
```
5. In WSGI config file, add at the top:
```python
import os
os.environ['GROQ_API_KEY'] = 'gsk_...your_key...'
```
6. Reload the web app

---

## 🧠 How It Works

1. User pastes text (min 20 words, max 6000 characters)
2. Flask sends it to **Groq API** (Llama 3.1 8B model)
3. LLM analyzes writing patterns, tone, and structure
4. Returns structured JSON with:
   - `classification` — AI-Generated or Human-Written
   - `confidence` — how certain the model is (55–98%)
   - `ai_probability` — raw 0–100 score
   - `indicators` — 3–4 specific observations about the text
   - `summary` — one-sentence verdict
5. UI animates the result with color-coded cards

---

## 🔎 What the LLM Looks For

**AI-generated text often has:**
- Formulaic transitions — *"Furthermore"*, *"Moreover"*, *"It is worth noting"*
- Perfectly balanced structure — *"On one hand... on the other hand"*
- Over-hedged language — *"may"*, *"could"*, *"some argue"*
- Uniform formal register with no tonal shifts
- No personal anecdotes or specific real-world details

**Human-written text often has:**
- Personal voice and emotional irregularities
- Specific names, places, and real-world details
- Casual language, contractions, and colloquialisms
- Inconsistent tone — formal and informal mixed
- Natural imperfections and stream-of-consciousness flow

---

## 📦 Requirements

```
flask==3.0.3
groq==0.11.0
python-dotenv==1.0.1
```

---

## ⚠️ .gitignore

Make sure `.env` is never pushed to GitHub:

```
.env
__pycache__/
*.pyc
```

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 📜 License

MIT — free to use and modify.
