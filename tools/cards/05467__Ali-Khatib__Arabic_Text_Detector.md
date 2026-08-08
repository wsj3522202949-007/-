---
id: tool-05467
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 去AI味]
title: Arabic_Text_Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/ali-khatib/arabic_text_detector
created: 2026-07-18
updated: 2026-07-18
no: 5467
category: 一、去 AI 味 / Humanizer 库
repo: Ali-Khatib/Arabic_Text_Detector
stars: 1
url: https://github.com/ali-khatib/arabic_text_detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: ef63380d1eb8fb67
  - methods/改稿润色指令库.md
---

# Ali-Khatib/Arabic_Text_Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ali-khatib/arabic_text_detector
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Extract Arabic text from images with formatting using Google Gemini Vision AI. Includes config, Python detector, and a Streamlit app for easy use.
- **本地描述**：Extract Arabic text from images with formatting using Google Gemini Vision AI. Includes config, Python detector, and a Streamlit app for easy use.
- **拉取时间**：2026-07-25 18:19:46

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

Arabic Text Extractor using Google Gemini Vision API
This project extracts Arabic text from images while preserving exact formatting and layout. It uses Google’s Gemini Vision AI to perform accurate OCR optimized for Arabic script.

Features
Extracts all Arabic text from images without missing any part

Maintains original formatting, line breaks, and paragraph structure

Properly segments text with line breaks after numbers or dashes

Displays text right-to-left as Arabic is naturally written

Supports multiple image formats (PNG, JPG, JPEG, GIF, BMP)

Includes a simple web app built with Streamlit for easy uploading and text extraction

Setup
Clone this repo

Create a .env file and add your Gemini API key:

ini
Copy
Edit
GEMINI_API_KEY=your_api_key_here
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run streamlit_app.py
Usage
Open the web app in your browser

Enter your Gemini API key in the sidebar

Upload an image containing Arabic text

Click Detect Arabic Text

View and download the extracted text with correct formatting

Requirements
Python 3.8+

google-generativeai

pillow

python-dotenv

streamlit

Notes
This tool leverages Google’s Gemini Vision API, so you need a valid API key from Google AI Studio.

