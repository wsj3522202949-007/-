---
id: tool-00298
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: PromptEnhancer
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/bhartithakran1/promptenhancer
created: 2026-07-18
updated: 2026-07-18
no: 298
category: 二、网文 / 长篇 AI 写作系统 库
repo: bhartithakran1/PromptEnhancer
stars: 0
url: https://github.com/bhartithakran1/promptenhancer
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# bhartithakran1/PromptEnhancer

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/bhartithakran1/promptenhancer
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Prompt Enhancer is a simple Python tool that uses Bria AI to turn your basic prompts into rich, detailed descriptions. Ideal for image generation or creative writing. Just input your prompt, and get a vivid enhanced version back. Great for learning APIs and building quick AI-based tools.
- **本地描述**：Prompt Enhancer is a simple Python tool that uses Bria AI to turn your basic prompts into rich, detailed descriptions. Ideal for image generation or creative writing. Just input your prompt, and get a vivid enhanced version back. Great for learning APIs and building quick AI-based tools.
- **拉取时间**：2026-07-23 22:47:46

---

# 🪄 Prompt Enhancer using Bria AI

This is a simple Python project that uses the [Bria AI Prompt Enhancer API](https://docs.bria.ai/image-generation/endpoints/prompt-enhancer) to automatically enhance text prompts for better image generation results.

---

## 🚀 Features

- Takes a simple text prompt from the user
- Sends the prompt to Bria AI's `/prompt_enhancer` endpoint
- Returns an enhanced version of the prompt suitable for image generation
- Uses environment variables to keep your API key safe

---

## 🧰 Requirements

- Python 3.7+
- `requests` module
- Bria AI API key

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 🔧 Setup & Usage

1. **Clone this repo** or download the `.py` file.
2. **Install dependencies**:
   ```bash
   pip install requests
