---
id: tool-04840
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI--Powered-Fake-News-Detection-Using-Text-Classification
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/mahithavarshininagisetty-cmyk/ai--powered-fake-news-detection-using-text-classification
created: 2026-07-18
updated: 2026-07-18
no: 4840
category: 一、去 AI 味 / Humanizer 库
repo: mahithavarshininagisetty-cmyk/AI--Powered-Fake-News-Detection-Using-Text-Classification
stars: 0
url: https://github.com/mahithavarshininagisetty-cmyk/ai--powered-fake-news-detection-using-text-classification
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
content_hash: c8fa347c3add941d
  - methods/改稿润色指令库.md
---

# mahithavarshininagisetty-cmyk/AI--Powered-Fake-News-Detection-Using-Text-Classification

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/mahithavarshininagisetty-cmyk/ai--powered-fake-news-detection-using-text-classification
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered fake news detector built from scratch — manual TF-IDF vectorization plus KNN, Logistic Regression, Random Forest, and Neural Network classifiers, served via a Flask API with a real-time web UI ("Veritas Desk") for classifying news articles as real or fake.
- **本地描述**：AI-powered fake news detector built from scratch — manual TF-IDF vectorization plus KNN, Logistic Regression, Random Forest, and Neural Network classifiers, served via a Flask API with a real-time web UI ("Veritas Desk") for classifying news articles as real or fake.
- **拉取时间**：2026-07-25 17:56:22

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Fake News Detection — Frontend ("Veritas Desk")

Plain HTML/CSS/JS single-page app — no build step, no framework required.
Talks to the Flask backend over REST.

## Run

1. Start the backend first (see `backend/README.md`):
   ```bash
   cd backend
   python3 app.py
   ```
   It should be listening on `http://127.0.0.1:5000`.

2. Serve this folder with any static file server, e.g.:
   ```bash
   cd frontend
   python3 -m http.server 8080
   ```
   Then open `http://127.0.0.1:8080` in your browser.

   (Opening `index.html` directly by double-clicking usually also works,
   since the app only makes `fetch()` calls to the backend's own origin.)

3. Paste an article/headline into the textarea and click **Analyze Article**.
   The right-hand panel stamps a **LIKELY REAL** / **LIKELY FAKE** verdict and
   shows each of the four models' individual predictions. The bottom panel
   shows the saved training-time accuracy/precision/recall/F1 for all models.

## Pointing at a different backend URL

If the backend isn't on `http://127.0.0.1:5000`, set it before `app.js` loads,
e.g. add this line in `index.html` right before `<script src="app.js">`:

```html
<script>window.API_BASE = "http://your-backend-host:5000";</script>
```

## Files

```
frontend/
  index.html   page structure
  style.css    "newsroom forensics" visual theme
  app.js       fetch() calls to the backend + rendering logic
```
