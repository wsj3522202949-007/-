---
id: tool-01762
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: ai-story-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/singhrahul2511/ai-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1762
category: 二、网文 / 长篇 AI 写作系统 库
repo: Singhrahul2511/ai-story-generator
stars: 1
url: https://github.com/singhrahul2511/ai-story-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 56d096ec11c29a91
  - methods/最强写作方法论_全球最强综合版.md
---

# Singhrahul2511/ai-story-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/singhrahul2511/ai-story-generator
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：Singhrahul2511/ai-story-generator
- **拉取时间**：2026-07-23 23:30:24

---

# 📖 AI Story Generator

---
[cite_start]This is a Python application built with Streamlit that generates a story based on a series of uploaded images[cite: 1]. It uses the Google Gemini model to create the narrative and Google Text-to-Speech (gTTS) for audio narration.

---
## Features

-   [cite_start]Upload 1 to 10 images to inspire the story[cite: 1].
-   [cite_start]Choose a story style, including Comedy, Thriller, Fairy Tale, and more[cite: 1].
-   Generates a written story connecting all images in sequence.
-   [cite_start]Provides an audio narration of the generated story[cite: 1].
-   Uses Indian names, characters, and places in the narrative.
---

## Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
    cd YOUR_REPOSITORY_NAME
    ```

---

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

---

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
---

4.  **Set up your API Key:**
    Create a file named `.env` in the root of the project and add your Google API key:
    ```
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```
---

## How to Run

[cite_start]Launch the Streamlit application with the following command[cite: 1]:

```bash
streamlit run app.py

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---
