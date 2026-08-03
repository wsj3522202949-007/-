---
id: tool-01803
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: ai_story_generator1
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/rosh-1349/ai_story_generator1
created: 2026-07-18
updated: 2026-07-18
no: 1803
category: 二、网文 / 长篇 AI 写作系统 库
repo: Rosh-1349/ai_story_generator1
stars: 0
url: https://github.com/rosh-1349/ai_story_generator1
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Rosh-1349/ai_story_generator1

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/rosh-1349/ai_story_generator1
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：using this app one will be able to generate story of any length whether a short story of 100 words or an essay length story,it is a flexible story generator for users.
- **本地描述**：using this app one will be able to generate story of any length whether a short story of 100 words or an essay length story,it is a flexible story generator for users.
- **拉取时间**：2026-07-23 23:31:37

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI Story Generator using Hugging Face & Streamlit

This project is a simple AI-powered story generator. Users can enter a prompt like “A time traveler visits ancient Egypt,” and the system generates a short creative story using a GPT-2 model.

## 🔧 Tools Used
- Python
- Hugging Face Transformers (`gpt2`)
- Streamlit (for UI)
- Google Colab
- pyngrok (to host Streamlit from Colab)

## 🚀 How to Run (in Google Colab)
1. Install dependencies:
   ```bash
   !pip install streamlit transformers torch pyngrok
