---
id: tool-01359
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: OwnStory--AI-Story-Generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/shivsspace/ownstory--ai-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1359
category: 二、网文 / 长篇 AI 写作系统 库
repo: shivsspace/OwnStory--AI-Story-Generator
stars: 3
url: https://github.com/shivsspace/ownstory--ai-story-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# shivsspace/OwnStory--AI-Story-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/shivsspace/ownstory--ai-story-generator
- **Stars**：3
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：shivsspace/OwnStory--AI-Story-Generator
- **拉取时间**：2026-07-23 23:18:45

---

# OwnStory - AI Story Generator ✨

## Overview
OwnStory is a Streamlit-based web application that creates imaginative and engaging stories using modern Large Language Models (LLMs). Users can customize their stories by selecting inputs such as genre, tone, characters, and narrative style, allowing for a personalized storytelling experience.

The project focuses on combining creative flexibility with high-performance AI to deliver rich stories in real time.


## Live Preview 🚀
You can try the application live here:

🔗 **Live App:** [https://ownstory-ai-story-generator.streamlit.app](https://ownstory--ai-story-generator-shivsspace.streamlit.app/)  

---

## AI Inference Engine: Groq
This application uses **Groq** as the inference provider for running Large Language Models.

**Why Groq?**  
Groq’s custom **Language Processing Unit (LPU)** architecture enables extremely low-latency inference, resulting in:
- Lightning-fast response times  
- Smooth, real-time story generation  
- An improved and seamless user experience  

---

## Language Models & Narrative Styles
Different storytelling styles require different model strengths. The application supports multiple narrative styles, each powered by a carefully selected model.

| Narrative Style | Model Used | Why This Model |
|-----------------|-----------|----------------|
| **Cinematic** | `llama-3.3-70b-versatile` | High-fidelity storytelling with rich descriptions, emotional depth, and complex narrative structures—ideal for cinematic experiences. |
| **Classic** | `llama-3.1-70b-versatile` | A reliable and balanced model that follows instructions well while maintaining clear, coherent, and elegant prose. |
| **Fast** | `mixtral-8x7b-32768` | A highly efficient Mixture-of-Experts model optimized for speed, making it perfect for rapid ideation and quick story generation. |

---

## Tech Stack
- **Frontend & UI:** Streamlit  
- **AI Models:** LLaMA & Mixtral (via Groq)  
- **Inference Provider:** Groq LPU  

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Purpose
This project demonstrates how high-speed inference and carefully chosen LLMs can be combined to create a responsive, creative, and user-friendly AI storytelling application.
