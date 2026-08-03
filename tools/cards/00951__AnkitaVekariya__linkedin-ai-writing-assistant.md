---
id: tool-00951
type: tool
area: 库
status: active
tags: [RAG, Python, 协议未明, 需API密钥, 英文文档, 人物设定]
title: linkedin-ai-writing-assistant
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/ankitavekariya/linkedin-ai-writing-assistant
created: 2026-07-18
updated: 2026-07-18
no: 951
category: 二、网文 / 长篇 AI 写作系统 库
repo: AnkitaVekariya/linkedin-ai-writing-assistant
stars: 0
url: https://github.com/ankitavekariya/linkedin-ai-writing-assistant
tier: "C"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AnkitaVekariya/linkedin-ai-writing-assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ankitavekariya/linkedin-ai-writing-assistant
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：ai, genai, langchain, llm, machine-learning, prompt-engineering, python, sqlite, streamlit
- **GitHub 描述**：AI-powered LinkedIn post generation using LLMs, few-shot prompting, and Streamlit.
- **本地描述**：AI-powered LinkedIn post generation using LLMs, few-shot prompting, and Streamlit.
- **拉取时间**：2026-07-23 23:06:48

---

# LinkedIn AI Writing Assistant

An AI-powered LinkedIn content generation system built using LLMs, few-shot prompting, and retrieval-based generation.

The application generates context-aware LinkedIn posts by dynamically selecting relevant examples based on:

* topic
* tone
* language
* post length

instead of relying only on static prompting.

---

## Screenshots

### Home Interface

<img width="100%" alt="Home Interface" src="screenshots\img1.png">

---

### Generated LinkedIn Post

<img width="100%" alt="Generated Post" src="screenshots\img2.png">
<img width="100%" alt="Generated Post" src="screenshots\img3.png">

---

## Features

* AI-powered LinkedIn post generation
* Few-shot prompting using real LinkedIn posts
* Tone-based content generation
* Dynamic retrieval using SQLite
* Metadata extraction and filtering
* Interactive Streamlit UI
* Conversational post refinement
* Additional context-based generation
* Emoji style control
---

## Tech Stack

* Python
* Streamlit
* LangChain
* SQLite
* Pandas
* Groq API

---

## Core Concepts Used

* Prompt Engineering
* Few-Shot Learning
* Retrieval-Augmented Generation (RAG)
* LLM Application Development
* Metadata-Based Retrieval
* AI-Assisted Content Generation

---

## System Flow

User Input
→ Example Retrieval
→ Prompt Construction
→ LLM Generation
→ LinkedIn Post Output

---

## Run Locally

Clone the repository:

```bash
git clone https://github.com/your-username/linkedin-ai-writing-assistant.git
cd linkedin-ai-writing-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
GROQ_API_KEY=your_api_key
```

Run the application:

```bash
streamlit run main.py
```

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Future Improvements

* Semantic search using embeddings
* Multi-creator writing styles
* Engagement prediction
* AI hook optimization
* Vector database integration


