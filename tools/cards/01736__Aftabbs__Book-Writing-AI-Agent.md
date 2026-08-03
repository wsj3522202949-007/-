---
id: tool-01736
type: tool
area: 库
status: active
tags: [多Agent, 校对, Jupyter Notebook, 协议宽松, 本地优先, 英文文档, 改稿润色, 本地写作]
title: Book-Writing-AI-Agent
summary: 多 Agent 协作自动产文
source: https://github.com/aftabbs/book-writing-ai-agent
created: 2026-07-18
updated: 2026-07-18
no: 1736
category: 二、网文 / 长篇 AI 写作系统 库
repo: Aftabbs/Book-Writing-AI-Agent
stars: 12
url: https://github.com/aftabbs/book-writing-ai-agent
tier: "B"
use_case: "多 Agent 协作自动产文"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Aftabbs/Book-Writing-AI-Agent

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/aftabbs/book-writing-ai-agent
- **Stars**：12
- **语言**：Jupyter Notebook
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：An intelligent, multi-agent system to autonomously plan, write, edit, fact-check, and publish a complete book using the CrewAI framework and Groq's LLaMA-3-70B model. This AI pipeline mimics the collaborative process of human authors, editors, and publishers to streamline creative book development.
- **本地描述**：An intelligent, multi-agent system to autonomously plan, write, edit, fact-check, and publish a complete book using the CrewAI framework and Groq's LLaMA-3-70B model. This AI pipeline mimics the collaborative process of human authors, editors, and publishers to streamline creative book development.
- **拉取时间**：2026-07-23 23:29:38

---

# 📚 Book Writing AI Agent

An intelligent, multi-agent system to autonomously **plan, write, edit, fact-check, and publish** a complete book using the **CrewAI framework** and **Groq's LLaMA-3-70B model**. This AI pipeline mimics the collaborative process of human authors, editors, and publishers to streamline creative book development.


---

##  Project Overview

This project leverages multiple specialized AI agents, each assigned a distinct role in the book creation pipeline:

- **Planning Agent**: Outlines the concept, characters, and story world.
- **Writing Agent**: Drafts each chapter based on the structured plan.
- **Editing Agent**: Refines grammar, coherence, and clarity.
- **Fact-Checking Agent**: Ensures all facts and real-world references are accurate.
- **Publishing Agent**: Formats the manuscript and prepares it for final release.

All agents work **sequentially** using the `CrewAI` orchestrator to simulate a real-world publishing team.

---

##  Tech Stack

- **Python**
- **[CrewAI](https://github.com/joaomdmoura/crewAI)** — Multi-agent workflow framework
- **[Langchain-Groq](https://pypi.org/project/langchain-groq/)** — LLaMA 3 integration via Groq API
- **Groq LLaMA-3-70B** — High-performance LLM for creativity and reasoning
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---
##  How It Works

1. **Planning Agent**: Generates a story outline with characters and setting.
2. **Writing Agent**: Writes chapters (1000+ words each).
3. **Editing Agent**: Edits chapters for flow, grammar, and style.
4. **Fact-Checking Agent**: Verifies real-world references.
5. **Publishing Agent**: Produces the final formatted manuscript.

Each task runs in sequence and contributes to a comprehensive output.

##  Requirements

```
crewai
langchain
langchain_groq
numpy
```

