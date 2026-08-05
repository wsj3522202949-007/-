---
id: tool-01551
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: AI_Story_Generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/uzmakhatun/ai_story_generator
created: 2026-07-18
updated: 2026-07-18
no: 1551
category: 二、网文 / 长篇 AI 写作系统 库
repo: UzmaKhatun/AI_Story_Generator
stars: 1
url: https://github.com/uzmakhatun/ai_story_generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# UzmaKhatun/AI_Story_Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/uzmakhatun/ai_story_generator
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Generate creative stories powered by Groq LLM — choose genre, theme, characters, and style.  Download stories as TXT or HTML , "Let AI Weave Your Next Great Story — Powered by Groq LLM"
- **本地描述**：Generate creative stories powered by Groq LLM — choose genre, theme, characters, and style.  Download stories as TXT or HTML , "Let AI Weave Your Next Great Story — Powered by Groq LLM"
- **拉取时间**：2026-07-23 23:24:19

---

# 🧙‍♀️ AI Story Generator – Powered by Groq LLM
A web app that generates imaginative, unique stories based on your selected genre, theme, writing style, and custom characters – all in a few seconds using the Groq LLM API. Built with Streamlit and designed for creators, writers, and AI enthusiasts.

---

## 🚀 Demo
- 🌐 Live App: [Click here to try it out!](https://ai-story-generator-webapp.streamlit.app/)
- 📽️ Video Walkthrough: [LinkedIn Demo]()
  !`[Screenshot](Screenshot.png)`

----

## 🔮 Features
-  Select from various genres: Sci-fi, Fantasy, Mystery, Thriller...
-  Choose a story theme: Good vs Evil, Betrayal, Redemption...
-  Pick your preferred writing style: Light, Neutral, Dark
-  Add your own character names
-  Optional emoji enhancement for fun storytelling
-  Download stories as .txt or .html (PDF coming soon)
-  View and filter past story history

---

## 🛠️ Tech Stack
| Tool           | Purpose                                |
|----------------|----------------------------------------|
| **Python**     | Core scripting and logic               |
| **Streamlit**  | Frontend UI for story customization and output|
| **Groq LLM**   | Fast and intelligent language model    |
| **Dotenv**     |API key protection                      |
| **Tempfile**   | Dynamic file download handling         |

----

## ⚙️ Setup Instructions
1. ***Clone the Repo***
``` bash
    git clone https://github.com/uzma-khatun/ai-story-generator.git
    cd ai-story-generator
```

2. ***Install Dependencies***
``` bash
   pip install -r requirements.txt
```

3. ***Add Your Groq API Key***
- Create a .env file in the root directory and add:
```
GROQ_API_KEY=your_api_key_here
```
4.***Run the App***
```
streamlit run app.py
```
---

## 📦 Upcoming Features
- PDF download support
- Login/Signup for user-based story tracking
- Prompt fine-tuning for more creative control
- Analytics dashboard for user activity

-related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 👩‍💻 Author
Uzma Khatun – [LinkedIn]() | [GitHub]()

## <p align="center">Made with ❤️</p>
