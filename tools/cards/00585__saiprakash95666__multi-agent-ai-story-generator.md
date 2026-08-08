---
id: tool-00585
type: tool
area: 库
status: active
tags: [多Agent, Python, 协议未明, 需API密钥, 英文文档]
title: multi-agent-ai-story-generator
summary: 多 Agent 协作自动产文
source: https://github.com/saiprakash95666/multi-agent-ai-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 585
category: 二、网文 / 长篇 AI 写作系统 库
repo: saiprakash95666/multi-agent-ai-story-generator
stars: 1
url: https://github.com/saiprakash95666/multi-agent-ai-story-generator
tier: "B"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: cdd5ef4bcfadb3b8
  - methods/最强写作方法论_全球最强综合版.md
---

# saiprakash95666/multi-agent-ai-story-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/saiprakash95666/multi-agent-ai-story-generator
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：This is a repository for multi-agent story generator AI agents project.
- **本地描述**：This is a repository for multi-agent story generator AI agents project.
- **拉取时间**：2026-07-23 22:56:07

---

# 🧠 Multi-Agent AI Bedtime Story Generator

An AI-powered bedtime story generator for children aged **5–10**, built using a **multi-agent architecture** powered by **GPT-3.5-turbo**.  
The system coordinates multiple autonomous agents to create, evaluate, and refine engaging, age-appropriate stories.

This project demonstrates applied **LLM system design**, **prompt engineering**, and **agent orchestration**.

It features a three-step agent pipeline:
1. **Storyteller Agent** – generates an initial bedtime story
2. **Judge Agent** – evaluates story quality, safety, and age suitability
3. **Refiner Agent** – improves coherence, tone, and engagement

---

## 🏗️ Architecture Overview

```text
User Prompt
   ↓
Storyteller Agent
   ↓
Judge Agent (feedback & scoring)
   ↓
Refiner Agent
   ↓
Final Polished Story

1. User Prompt: The user provides a short story idea or theme.

2. Storyteller Agent: Generates an initial story draft using the user’s idea.

3. Judge Agent: Evaluates the story’s quality, creativity, moral value, and suitability for children aged 5–10, then provides feedback.

4. Refiner Agent: Improves the story based on the Judge’s feedback to produce the final version of the story.

5. Output: The final refined story is displayed to the user.
```
---

## 🚀 How To Run
1. Create a `.env` file in the project root with your API key.
    ```
    OPENAI_API_KEY=sk-your-api-key-here
    ```
2. Create and activate a virtual environment.
    ```python
    python -m venv venv
    venv\Scripts\activate   # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```
3. Install Dependencies
    ```
    pip install -r requirements.txt
    ```
4. Run the program
    ```
    python main.py
    ```
After this you will be prompted to enter a story idea, and the AI will generate, evaluate, and give you the refined story.

---

## 🔮 Future Enhancements

1. Add a simple web interface to input prompts and view stories using **Streamlit**.

2. Integrate **Text-to-Speech (TTS)** so children can listen to stories.

3. Implement a **Save as PDF** option so users can easily download and preserve their favorite stories, or **replay** them anytime.

4. Introduce **themes** like animals, friendship, adventure, space, etc.

5. Story illustrations using image generation models.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 👨‍💻 Author

Kurmathi Sai Prakash Reddy

🔗 [Github](https://github.com/saiprakash95666)
🔗 [LinkedIn](https://www.linkedin.com/in/kurmathi-sai-prakash-reddy-944a43169/)
🔗 [Portfolio](https://kurmathisaiprakashportfolio.netlify.app/)
