---
id: tool-01509
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 需API密钥, 英文文档, 大纲规划]
title: Storyboard-Builder
summary: 搭大纲/分卷/节拍
source: https://github.com/nidhiu-24/storyboard-builder
created: 2026-07-18
updated: 2026-07-18
no: 1509
category: 二、网文 / 长篇 AI 写作系统 库
repo: NidhiU-24/Storyboard-Builder
stars: 1
url: https://github.com/nidhiu-24/storyboard-builder
tier: "B"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# NidhiU-24/Storyboard-Builder

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/nidhiu-24/storyboard-builder
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：An AI-powered storyboard generator that creates consistent, styled images for each panel of your story and exports them as a downloadable PDF.
- **本地描述**：An AI-powered storyboard generator that creates consistent, styled images for each panel of your story and exports them as a downloadable PDF.
- **拉取时间**：2026-07-23 23:23:06

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 🎬  Storyboard Builder
An AI-powered storyboard generator that creates consistent, styled images for each panel of your story — and exports them as a downloadable PDF.
Built with Streamlit, Hugging Face Inference API, and Ollama (Llama 3).

## Features

🖼️ Generate AI images for each storyboard panel
🎨 Choose from 5 consistent visual styles across all panels
✍️ Write your own panel descriptions or auto-generate them from a story idea
🤖 Uses local Ollama (Llama 3) to turn story ideas into detailed image prompts
📥 Export your complete storyboard as a PDF
💸 Runs on Hugging Face's free API — no GPU required on your machine


## 🎨 Available Styles

### StyleDescription
 - 🎨 Anime / Studio GhibliSoft watercolor, hand-drawn, warm lighting
 - 🖼️ Cinematic / Realistic35mm film look, dramatic lighting, sharp focus
 - ✏️ Comic BookBold outlines, flat colors, graphic novel feel
 - 🖌️ Oil PaintingClassical brushstrokes, rich colors, chiaroscuro
 - 🌑 Dark FantasyMoody atmosphere, dramatic shadows, dark palette

## 🛠️ Tech Stack

 - Streamlit — Web UI
 - Hugging Face Router API — Image generation (Stable Diffusion XL)
 - Ollama + Llama 3 — Local LLM for auto-generating panel descriptions
 - ReportLab — PDF export
 - Pillow — Image handling


## 📋 Prerequisites

 - Python 3.12+
 - Ollama installed and running
 - A free Hugging Face account and API token

