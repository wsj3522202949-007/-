---
id: tool-00295
type: tool
area: 库
status: active
tags: [校对, HTML, 协议未明, 需API密钥, 英文文档, 改稿润色]
title: AI-Assistant
summary: 错别字/语法/风格校对
source: https://github.com/prayingforthelastsunbeam/ai-assistant
created: 2026-07-18
updated: 2026-07-18
no: 295
category: 二、网文 / 长篇 AI 写作系统 库
repo: prayingforthelastsunbeam/AI-Assistant
stars: 1
url: https://github.com/prayingforthelastsunbeam/ai-assistant
tier: "B"
use_case: "错别字/语法/风格校对"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# prayingforthelastsunbeam/AI-Assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/prayingforthelastsunbeam/ai-assistant
- **Stars**：1
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：A Flask-based web application that provides four AI-powered writing tools using Google's Gemini API
- **本地描述**：A Flask-based web application that provides four AI-powered writing tools using Google's Gemini API
- **拉取时间**：2026-07-23 22:47:40

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI Tool Suite

AI Tool Suite is a single Flask app that combines AI writing utilities and video processing tools in one dashboard.

## Tools Included

- Text Summarizer
- Grammar & Style Checker
- Idea Generator
- Smart To-Do List
- Fake Profile Generator
- Premium Video Compressor
- Unique Frame Extractor (SSIM)
- Motion Frame Extractor
- Processing History (time-limited ZIP downloads)

## Quick Start

1. Install dependencies:

```bash
pip install flask requests faker python-dotenv opencv-python scikit-image numpy
```

2. Create your environment file:

```bash
Copy-Item .env.example .env
```

3. Set your keys/config in `.env`:

```env
GEMINI_API_KEY=your-real-gemini-key
GEMINI_MODEL=gemini-flash-latest
FLASK_DEBUG=false
PROCESSING_RETENTION_MINUTES=60
FFMPEG_PATH=
```

4. Run the app:

```bash
python app.py
```

5. Open:

```text
http://localhost:5000
```

## Documentation

This project intentionally keeps only two documentation files:

- `README.md` (overview + quick start)
- `GUIDE.md` (complete setup, operations, troubleshooting, deployment guidance)

For detailed instructions, see `GUIDE.md`.
