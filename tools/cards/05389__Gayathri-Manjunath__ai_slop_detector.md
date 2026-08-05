---
id: tool-05389
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 去AI味]
title: ai_slop_detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/gayathri-manjunath/ai_slop_detector
created: 2026-07-18
updated: 2026-07-18
no: 5389
category: 一、去 AI 味 / Humanizer 库
repo: Gayathri-Manjunath/ai_slop_detector
stars: 0
url: https://github.com/gayathri-manjunath/ai_slop_detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Gayathri-Manjunath/ai_slop_detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/gayathri-manjunath/ai_slop_detector
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：Gayathri-Manjunath/ai_slop_detector
- **拉取时间**：2026-07-25 18:16:45

---


# 🧪 AI Slop Detector

A Flask web app that analyzes text — or scrapes it directly from a URL — and predicts whether the content was **AI-generated ("slop")** or **human-written**, using a Hugging Face transformer model combined with a secondary reasoning check from the OpenAI API.

---

## 📌 Overview

With the flood of low-effort AI-generated content online, **AI Slop Detector** gives a quick, explainable verdict on any piece of text:

1. **Web Scraping** — pulls the readable text out of any article URL.
2. **Hugging Face Model** — runs a pretrained RoBERTa classifier to get a statistical AI-probability score.
3. **OpenAI Reasoning Check** — asks an LLM to reason qualitatively about stylistic "AI tells" (genericness, filler phrases, lack of specificity) as a second opinion.
4. **Combined Verdict** — merges both signals into one clear, color-coded result.

---

## ✨ Features

- 🔗 Analyze by pasting raw text **or** submitting a URL to scrape
- 🤖 Transformer-based AI-text classification (Hugging Face)
- 🧠 Secondary reasoning check via OpenAI API with explanation
- 🚦 Clear color-coded verdict: 🟢 Human-written / 🟡 Possibly AI-assisted / 🔴 AI-generated
- 🌐 Clean, responsive dark-mode web UI
- ⚡ Simple REST endpoint (`/analyze`) usable from other apps/scripts

---

## 🛠️ Tech Stack

| Layer          | Technology                                   |
|----------------|-----------------------------------------------|
| Backend        | Python, Flask                                 |
| AI Model       | Hugging Face Transformers (`roberta-base-openai-detector`) |
| LLM Check      | OpenAI API (`gpt-4o-mini`)                    |
| Web Scraping   | Requests, BeautifulSoup4                      |
| Frontend       | HTML, CSS, vanilla JavaScript                 |

---

## 📂 Project Structure

ai_slop_detector/
│
├── app.py                     # Flask app & routes
├── scraper/
│   └── web_scraper.py         # URL scraping logic
├── detector/
│   ├── hf_detector.py         # Hugging Face model inference
│   └── openai_checker.py      # OpenAI API reasoning check
├── templates/
│   └── index.html             # Web UI
├── static/
│   ├── style.css              # Styling
│   └── script.js              # Frontend logic
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/ai_slop_detector.git
   cd ai_slop_detector
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your OpenAI API key**
   ```bash
   cp .env.example .env
   # then edit .env and add your key:
   # OPENAI_API_KEY=sk-...
   ```

5. **Run the app**
   ```bash
   python app.py
   ```

6. Open your browser at:
   ```
   http://127.0.0.1:5000
   ```

> Note: on first run, the Hugging Face model (~500MB) will download automatically and be cached locally.

---

## 🚀 Usage

### Via the Web UI
- Paste any article text, or switch to the **Analyze URL** tab and paste a link.
- Click **Analyze** to get the verdict, confidence score, and reasoning.

### Via the API directly
```bash
curl -X POST http://127.0.0.1:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"type": "text", "content": "Your text here..."}'
```

**Sample response:**
```json
{
  "word_count": 142,
  "huggingface_result": {
    "label": "Fake",
    "confidence": 0.91,
    "ai_probability": 0.91
  },
  "openai_result": {
    "label": "ai-generated",
    "reasoning": "The text uses generic transitions and lacks specific personal detail."
  },
  "final_verdict": {
    "tag": "AI-Generated (Slop)",
    "emoji": "🔴",
    "confidence": 91.0
  }
}
```

---

## 🎯 Use Cases

- Screening blog/article submissions for AI-generated spam
- Research on AI content proliferation
- Browser extensions or CMS plugins for content moderation
- Educational tool for spotting AI writing patterns

---

## 📈 Future Improvements

- Batch analysis for multiple URLs at once
- Browser extension for one-click checking
- Support for additional detector models and ensembling
- Highlight specific AI-sounding sentences within the text

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the `[issues page](../../issues)`.

---

## 📄 License

This project is licensed under the MIT License.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 👤 Author

**Your Name**
GitHub: [@your-username](https://github.com/Gayathri-Manjunath)

