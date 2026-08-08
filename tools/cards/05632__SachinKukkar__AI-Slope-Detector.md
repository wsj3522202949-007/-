---
id: tool-05632
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 去AI味]
title: AI-Slope-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/sachinkukkar/ai-slope-detector
created: 2026-07-18
updated: 2026-07-18
no: 5632
category: 一、去 AI 味 / Humanizer 库
repo: SachinKukkar/AI-Slope-Detector
stars: 0
url: https://github.com/sachinkukkar/ai-slope-detector
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
content_hash: c99366d124c7feec
  - methods/改稿润色指令库.md
---

# SachinKukkar/AI-Slope-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/sachinkukkar/ai-slope-detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：SachinKukkar/AI-Slope-Detector
- **拉取时间**：2026-07-25 18:25:54

---

# 🤖 AI Slop Detector

Detect AI-generated content using a multi-signal pipeline:
**HuggingFace Transformers + OpenAI GPT-4o-mini + Web Scraping + Slop Phrase Analysis**

---

## 🚀 Setup

### 1. Clone & install dependencies
```bash
git clone <your-repo>
cd ai-slop-detector
pip install -r requirements.txt
```

### 2. Set your OpenAI API key (optional but recommended)
```bash
# Linux / Mac
export OPENAI_API_KEY="sk-..."

# Windows
set OPENAI_API_KEY=sk-...
```

### 3. Run the app
```bash
python app.py
```

Open **http://localhost:5000** in your browser.

---

## 🧠 How It Works

### Detection Pipeline

| Signal | Model / Method | Weight |
|---|---|---|
| **HuggingFace RoBERTa** | `Hello-SimpleAI/chatgpt-detector-roberta` | 40% |
| **Sentence Uniformity** | Std deviation of sentence lengths | 25% |
| **Slop Phrase Density** | 50+ known AI clichés matched | 20% |
| **Structural Patterns** | Markdown headers, bullets, numbered lists | 15% |
| **OpenAI GPT-4o-mini** | Prompted expert judge (optional) | Redistributes weights |

### Verdict Thresholds

| Score | Verdict |
|---|---|
| 75–100 | 🤖 Almost Certainly AI |
| 55–74  | ⚠️ Likely AI-Generated |
| 35–54  | 🤔 Mixed / Uncertain |
| 0–34   | ✍️ Likely Human-Written |

---

## 📦 Features

- **URL Mode** — Paste any article URL, scrapes and analyzes the main content
- **Text Mode** — Directly paste text for instant analysis
- **Batch Mode** — Analyze up to 10 URLs at once
- **OpenAI Toggle** — Enable GPT-4o-mini for deeper reasoning
- **Animated score ring** with color-coded verdict
- **Slop phrase highlighting** — See exactly which AI clichés were found

---

## 🗂 Project Structure

```
ai-slop-detector/
├── app.py                    # Flask app & routes
├── requirements.txt
├── README.md
├── models/
│   └── detector.py           # Core detection pipeline
├── scraper/
│   └── web_scraper.py        # BeautifulSoup web scraper
├── static/
│   ├── css/style.css         # Dark theme UI
│   └── js/app.js             # Frontend logic
└── templates/
    └── index.html            # Main template
```

---

## 🔧 Tech Stack

- **Flask** — Backend web framework
- **BeautifulSoup4** — Web scraping & HTML parsing
- **HuggingFace Transformers** — RoBERTa-based AI text classifier
- **PyTorch** — Model inference
- **OpenAI API** — GPT-4o-mini for deep reasoning (optional)

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 📝 Notes

- The HuggingFace model (`chatgpt-detector-roberta`) downloads ~500MB on first run
- For best accuracy enable OpenAI analysis
- Works best on articles 200+ words
- Batch mode processes URLs sequentially to avoid rate limits
