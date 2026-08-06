---
id: tool-04969
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: smart-job-scam-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/karangobade/smart-job-scam-detector
created: 2026-07-18
updated: 2026-07-18
no: 4969
category: 一、去 AI 味 / Humanizer 库
repo: karangobade/smart-job-scam-detector
stars: 0
url: https://github.com/karangobade/smart-job-scam-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# karangobade/smart-job-scam-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/karangobade/smart-job-scam-detector
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered web app that detects fake/scam job postings using NLP (ML classifier) — supports text input and image (OCR) uploads.
- **本地描述**：AI-powered web app that detects fake/scam job postings using NLP (ML classifier) — supports text input and image (OCR) uploads.
- **拉取时间**：2026-07-25 18:01:20

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Job Scam Detection System

An AI-powered web application that detects fraudulent job postings from **text input** or **uploaded images (OCR)**. Built to help job seekers quickly verify whether a job listing is likely genuine or a scam.

## Features

- 🔍 **Text Analysis** — Paste a job description and get an instant scam probability score
- 🖼️ **Image/OCR Support** — Upload a screenshot of a job post (e.g. WhatsApp, LinkedIn, email) and the system extracts text via OCR before analysis
- 🤖 **ML-Based Classification** — Uses a trained scikit-learn model to flag common scam indicators (vague roles, generic email IDs, urgency language, upfront fee requests, etc.)
- ⚡ **Flask Backend** — Lightweight and easy to deploy

## Tech Stack

- **Backend:** Flask (Python)
- **ML/NLP:** scikit-learn
- **OCR:** Tesseract / pytesseract (for image-based job post detection)
- **Frontend:** HTML, CSS, JS (Jinja templates)

## Screenshot
1.simple user interface
![App Screenshot](https://github.com/karangobade/smart-job-scam-detector/blob/main/img/base.png)

2.enter job description(text or img )
![App Screenshot](https://github.com/karangobade/smart-job-scam-detector/blob/main/img/des.png)

3.predict the result
![App Screenshot](https://github.com/karangobade/smart-job-scam-detector/blob/main/img/det.png)

## How It Works

1. User submits a job description as text, or uploads a screenshot of a job post
2. If an image is uploaded, OCR extracts the raw text
3. The text is preprocessed and passed to the trained classification model
4. The model returns a prediction — **Genuine** or **Scam** — along with a confidence score
5. Result is displayed to the user with key red flags highlighted (if any)

## Installation

```bash
git clone https://github.com/karangobade/smart-job-scam-detector.git
cd smart-job-scam-detector
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.



## Future Improvements

- Deep learning-based text classification for higher accuracy
- Browser extension for real-time scam detection on job portals
- Support for multilingual job postings

## Author

**Karan Gobade**
- Portfolio: [karangobade.github.io/portfolio](https://karangobade.github.io/portfolio)
- GitHub: [github.com/karangobade](https://github.com/karangobade)
