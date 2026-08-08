---
id: tool-01632
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: GOKU-AI-CHATBOT
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/gkthirumaran/goku-ai-chatbot
created: 2026-07-18
updated: 2026-07-18
no: 1632
category: 二、网文 / 长篇 AI 写作系统 库
repo: GKTHIRUMARAN/GOKU-AI-CHATBOT
stars: 1
url: https://github.com/gkthirumaran/goku-ai-chatbot
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 7c7a8487f070ca82
  - methods/最强写作方法论_全球最强综合版.md
---

# GKTHIRUMARAN/GOKU-AI-CHATBOT

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/gkthirumaran/goku-ai-chatbot
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：GOKU AI is a full-stack intelligent character chat system that brings fictional personas to life through FastAPI, React, and LM Studio (LLaMA-3 8B). It merges local LLM inference, persistent memory, and modular persona design to simulate dynamic, personality-driven conversations.
- **本地描述**：GOKU AI is a full-stack intelligent character chat system that brings fictional personas to life through FastAPI, React, and LM Studio (LLaMA-3 8B). It merges local LLM inference, persistent memory, and modular persona design to simulate dynamic, personality-driven conversations.
- **拉取时间**：2026-07-23 23:26:37

---

# ⚡ GOKU-AI-CHATBOT

> **Project Z — Intelligent Character Chat System powered by FastAPI, React & LM Studio**  

![Repo Size](https://img.shields.io/github/repo-size/GKTHIRUMARAN/GOKU-AI-CHATBOT?color=brightgreen&style=for-the-badge)
![License](https://img.shields.io/github/license/GKTHIRUMARAN/GOKU-AI-CHATBOT?color=blue&style=for-the-badge)
![Stars](https://img.shields.io/github/stars/GKTHIRUMARAN/GOKU-AI-CHATBOT?color=yellow&style=for-the-badge)

---

## 🧠 Overview

**GOKU AI** is a modular, locally hosted **intelligent character chat system** that brings fictional personalities to life using **FastAPI**, **React**, and **LLaMA-3 (8B)** through **LM Studio**.

It demonstrates complete **end-to-end AI integration** — combining backend logic, frontend design, and local model inference — to emulate personality-driven, memory-based conversations.  
The first character implemented is **Son Goku** from *Dragon Ball*.

Built as part of **Project Z**, this system lays the groundwork for a **multi-character conversational universe**, where each AI has its own memory, knowledge, and tone.

---

## 🎯 Project Summary

| Version | Description | Key Tech |
| :------ | :----------- | :-------- |
| [V.0 — Prototype](https://github.com/GKTHIRUMARAN/GOKU-AI-CHATBOT/tree/main/V.0) | Gradio-based proof of concept using LM Studio and text memory. | Python, Gradio, LLaMA-3 |
| [V.1 — Full Build](https://github.com/GKTHIRUMARAN/GOKU-AI-CHATBOT/tree/main/V.1) | FastAPI + React full implementation with persistent memory and persona system. | FastAPI, React, Tailwind, Zustand, LLaMA-3 |

---

## 🧩 Core Features

- ⚙️ **Full-Stack Pipeline:** React → FastAPI → LM Studio → Memory → UI Response  
- 🧠 **Personality Engine:** Emulates Goku’s tone, humor, and confidence  
- 💾 **Persistent Memory:** Remembers past conversations for context  
- 📚 **Knowledge Integration:** Uses curated lore from the Dragon Ball universe  
- 🧰 **Modular Architecture:** Swap or expand characters easily  
- 🚀 **Local or Cloud Ready:** Runs locally or via containerized deployment  

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    A[User] -->|Message| B[React Frontend]
    B -->|POST /api/chat| C[FastAPI Backend]
    C -->|Send Reply| B
    C -->|Req| D[LM Studio - LLaMA 3 8B]
    D -->|Response| C
    C -->|Update| E[memory.txt]
    E -->|Recall| C
````

---

## 🔍 Technical Stack

| Layer                | Technology                  | Purpose                                       |
| :------------------- | :-------------------------- | :-------------------------------------------- |
| **Frontend**         | React + Vite + Tailwind CSS | Modern, responsive chat interface             |
| **Backend**          | FastAPI                     | Manages API routes, memory, and persona logic |
| **Model Interface**  | LM Studio (LLaMA-3 8B)      | Local model inference engine                  |
| **State Management** | Zustand                     | Frontend global chat state                    |
| **API Client**       | Axios                       | Handles data flow between UI & backend        |
| **Styling & UX**     | Tailwind + Framer Motion    | Interactive and smooth animations             |

---

## 📁 Repository Modules

| Folder                                                                  | Purpose                                                                        |
| :---------------------------------------------------------------------- | :----------------------------------------------------------------------------- |
| [`/V.0`](https://github.com/GKTHIRUMARAN/GOKU-AI-CHATBOT/tree/main/V.0) | Prototype Gradio chatbot using text-based persona, memory, and knowledge files |
| [`/V.1`](https://github.com/GKTHIRUMARAN/GOKU-AI-CHATBOT/tree/main/V.1) | Full-scale build with FastAPI backend and React frontend                       |

---

## 💬 Example Interaction

> **User:** Hey Goku, how’s your training today?
> **Goku:** Haha! Training never stops! I just did 10,000 push-ups — gotta keep my power level high even in this AI realm!

<p align="center">
  <img src="V.1/demo.png" alt="Goku AI Chat Demo" width="800">
</p>

---

## 🧠 Evolution Path

| Stage | Goal                                 | Status         |
| :---- | :----------------------------------- | :------------- |
| V.0   | Gradio prototype with memory         | ✅ Complete     |
| V.1   | Full FastAPI + React build           | ✅ Complete     |
| V.2   | Multi-Character RAG System (Planned) | 🔜 In progress |

---

## 🧩 Future Roadmap

* 🔹 Multi-character expansion (Vegeta, Piccolo, etc.)
* 🔹 Vector memory with **FAISS / ChromaDB**
* 🔹 Rich UI with persona selector & memory viewer
* 🔹 Dockerized full-stack deployment
* 🔹 Integration with external APIs for dynamic data responses

---

## 📘 Architecture Philosophy

GOKU-AI is built around **persona-centric intelligence** — every character is self-contained with:

1. **Prompt personality** (`prompt.txt`)
2. **Knowledge base** (`knowledge.txt`)
3. **Memory persistence** (`memory.txt`)

This modular design ensures each AI maintains its own story, growth, and emotional context within conversations.

---

## 📜 License

Licensed under the [MIT License](https://github.com/GKTHIRUMARAN/GOKU-AI-CHATBOT/blob/main/LICENSE).

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 👤 Author

**GK Thirumaran**  
🎓 *B.Tech — Artificial Intelligence and Data Science*  
🌍 *Coimbatore, Tamil Nadu, India*  
💼 *Aspiring Data Scientist & Analyst | AIML Developer*  
🔗 [LinkedIn](https://www.linkedin.com/in/thirumarangk-ai) | [Portfolio](https://maranthiru180.wixsite.com/my-site)
