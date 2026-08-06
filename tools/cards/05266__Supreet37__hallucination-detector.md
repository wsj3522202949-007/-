---
id: tool-05266
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: hallucination-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/supreet37/hallucination-detector
created: 2026-07-18
updated: 2026-07-18
no: 5266
category: 一、去 AI 味 / Humanizer 库
repo: Supreet37/hallucination-detector
stars: 1
url: https://github.com/supreet37/hallucination-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Supreet37/hallucination-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/supreet37/hallucination-detector
- **Stars**：1
- **语言**：HTML
- **License**：None
- **Topics**：chatgpt, css, developer-tools, gemini, google-extension, hallucination-detection, html, javascript, nli, unicorn, vectara
- **GitHub 描述**：The Hallucination Detector is a Chrome extension + FastAPI backend that evaluates AI‑generated text (from ChatGPT, Gemini, Claude, etc.) for hallucinations using a Natural Language Inference (NLI) model. It provides real‑time classification of text into categories like Safe, Suspicious, or Highly Hallucinated, helping users quickly judge the reliab
- **本地描述**：The Hallucination Detector is a Chrome extension + FastAPI backend that evaluates AI‑generated text (from ChatGPT, Gemini, Claude, etc.) for hallucinations using a Natural Language Inference (NLI) model. It provides real‑time classification of text into categories like Safe, Suspicious, or Highly Hallucinated, helping users quickly judge the reliab
- **拉取时间**：2026-07-25 18:12:12

---

# AI Hallucination Detector — Chrome Extension
Detects hallucinations in AI-generated text from ChatGPT, Gemini, and Claude.

---

## Project Structure
```
hallucination-extension/
├── backend/
│   ├── main.py            # FastAPI backend
│   └── requirements.txt
└── extension/
    └── public/
        ├── manifest.json  # Chrome extension config
        ├── content.js     # Extracts AI text from page
        ├── popup.html     # Extension popup UI
        ├── popup.js       # Popup logic + API call
        └── icon.png
```

---

## Step 1 — Run the Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
First run downloads the model (~500MB). Wait for:
```
Model loaded!
INFO: Uvicorn running on http://127.0.0.1:8000
```
Test it works:
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Einstein invented the telephone in 1875."}'
```
Expected response:
```json
{"score": 0.87, "label": "Highly Hallucinated"}
```

---

## Step 2 — Load the Chrome Extension
1. Open Chrome → go to `chrome://extensions`
2. Enable **Developer Mode** (top right toggle)
3. Click **Load unpacked**
4. Select the `extension/public/` folder
5. Extension appears in your toolbar

---

## Step 3 — Use It
1. Open ChatGPT, Gemini, or Claude
2. Get any AI response on screen
3. Click the extension icon
4. Click **Analyze**
5. See: ✅ Safe / ⚠️ Suspicious / 🚨 Highly Hallucinated

---

## How It Works
```
User clicks Analyze
    → popup.js asks content.js for AI text
    → content.js extracts text from the page DOM
    → popup.js sends text to FastAPI backend
    → backend runs NLI classification model
    → returns { score, label }
    → popup.js displays result with color + confidence bar
```

---

## Model
Uses `cross-encoder/nli-MiniLM2-L6-H768` from HuggingFace — a Natural Language Inference (NLI) model that detects contradiction between a claim and factual context as a hallucination signal. No training required — pre-trained and production-ready.

## Demo

| Safe Response | Suspicious Response |
|---|related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| ![Safe](https://github.com/Supreet37/hallucination-detector/blob/main/demo1) | ![Suspicious](https://github.com/Supreet37/hallucination-detector/blob/main/demo2) |
