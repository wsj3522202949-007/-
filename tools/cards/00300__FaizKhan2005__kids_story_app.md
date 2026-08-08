---
id: tool-00300
type: tool
area: 库
status: active
tags: [TTS, Python, 协议未明, 需API密钥, 英文文档]
title: kids_story_app
summary: 小说转语音/有声书
source: https://github.com/faizkhan2005/kids_story_app
created: 2026-07-18
updated: 2026-07-18
no: 300
category: 二、网文 / 长篇 AI 写作系统 库
repo: FaizKhan2005/kids_story_app
stars: 1
url: https://github.com/faizkhan2005/kids_story_app
tier: "B"
use_case: "小说转语音/有声书"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 08609662731c01a9
  - methods/最强写作方法论_全球最强综合版.md
---

# FaizKhan2005/kids_story_app

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/faizkhan2005/kids_story_app
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI Kids Story Generator creates custom children’s stories and poems for ages 3-12. Choose theme, characters, and length, then get engaging stories with colorful illustrations and audio narration. Download PDFs and audio files. Simple, fun, and perfect for sparking kids’ imagination anytime.
- **本地描述**：AI Kids Story Generator creates custom children’s stories and poems for ages 3-12. Choose theme, characters, and length, then get engaging stories with colorful illustrations and audio narration. Download PDFs and audio files. Simple, fun, and perfect for sparking kids’ imagination anytime.
- **拉取时间**：2026-07-23 22:47:49

---

# AI Story Generator

An interactive Streamlit web app that generates custom children’s stories and poems with AI, complete with colorful illustrations and audio narration.

---

## Features

- Generate unique stories or poems tailored for children aged 3-12  
- Customize theme, key elements, length, and language (English/Hindi)  
- AI-generated storybook-style illustrations  
- Text-to-speech audio narration with download option  
- Download stories as PDF files  
- Simple and clean user interface  

---

## How It Works

1. Choose whether to create a story or poem  
2. Enter a main theme and optional key element  
3. Select the age range, length, and language  
4. Add any special instructions or notes  
5. Click “Generate” and wait for AI to create the content  
6. View, listen, and download your story with illustration and audio  

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Installation

```bash
git clone https://github.com/yourusername/ai-story-generator.git
cd ai-story-generator
pip install streamlit google-generativeai gtts reportlab requests pillow
streamlit run app.py
Requirements
Python 3.8 or higher

Google Gemini API key (set in the script or via environment variable)

Internet connection

Notes
Replace "YOUR_GOOGLE_GEMINI_API_KEY" in the script with your actual API key before running.

The app uses Pollinations.ai to generate images with retry and fallback handling.

Audio narration is generated with Google Text-to-Speech (gTTS).

Tech Stack
Streamlit

Google Gemini (Generative AI)

Pollinations.ai (Image generation)

gTTS (Text-to-Speech)

ReportLab (PDF generation)
