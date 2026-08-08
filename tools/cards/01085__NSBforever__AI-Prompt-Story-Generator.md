---
id: tool-01085
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: AI-Prompt-Story-Generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/nsbforever/ai-prompt-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1085
category: 二、网文 / 长篇 AI 写作系统 库
repo: NSBforever/AI-Prompt-Story-Generator
stars: 0
url: https://github.com/nsbforever/ai-prompt-story-generator
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 3d6210eb7cc6f5c7
  - methods/最强写作方法论_全球最强综合版.md
---

# NSBforever/AI-Prompt-Story-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/nsbforever/ai-prompt-story-generator
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A simple Streamlit-based AI app that generates creative short stories from user prompts using OpenAI's GPT-3.5. Perfect for exploring creative writing with the help of generative AI.
- **本地描述**：A simple Streamlit-based AI app that generates creative short stories from user prompts using OpenAI's GPT-3.5. Perfect for exploring creative writing with the help of generative AI.
- **拉取时间**：2026-07-23 23:10:37

---


# 🧠 AI-Prompt-Story-Generator (Gemini + Gradio)

A simple web app that generates short, creative stories from user prompts using **Google's Gemini model** (via `google-generativeai`) and **Gradio**. Perfect for exploring creative writing with the help of Generative AI.

---

## 📖 AI Story Generator

An interactive app where you input a story prompt (like *“A robot who dreams of being human”*) and Gemini generates a unique, imaginative story in response.

---

## 🧰 Tools Used
- Python
- [Gradio](https://gradio.app/) (UI)
- [Google Generative AI SDK](https://pypi.org/project/google-generativeai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (for API key management)

---

## 🚀 How to Run the App

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/AI-Prompt-Story-Generator.git
   cd AI-Prompt-Story-Generator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Gemini API Key:**
   - Create a `.env` file in the project root:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

4. **Run the app:**
   ```bash
   python app.py
   ```

5. The app will launch at [http://localhost:7860](http://localhost:7860)

---

## 🖼️ Example Prompts
- "A lonely robot explores Mars"
- "A tiger who writes poetry"
- "A girl discovers a magical clock tower"

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## ✅ Features
- Custom story generation from any prompt
- Simple, clean UI via Gradio
- Automatically handles API errors
- Gemini-powered for fast and creative results
