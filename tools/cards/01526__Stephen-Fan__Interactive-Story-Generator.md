---
id: tool-01526
type: tool
area: 库
status: active
tags: [大纲规划, Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: Interactive-Story-Generator
summary: 搭大纲/分卷/节拍
source: https://github.com/stephen-fan/interactive-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1526
category: 二、网文 / 长篇 AI 写作系统 库
repo: Stephen-Fan/Interactive-Story-Generator
stars: 1
url: https://github.com/stephen-fan/interactive-story-generator
tier: "B"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: a84ed4071c099b2c
  - methods/最强写作方法论_全球最强综合版.md
---

# Stephen-Fan/Interactive-Story-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/stephen-fan/interactive-story-generator
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：ai, choreo, fastapi, openai-api, python, react
- **GitHub 描述**：A webite to generate your own story and get ready to start your adventure!
- **本地描述**：A webite to generate your own story and get ready to start your adventure!
- **拉取时间**：2026-07-23 23:23:35

---

# Interactive Story Generator

An interactive story generator built with **React** and **FastAPI**, deployed on **Choreo**. Data is managed in SQLite databases.  
It integrates the **OpenAI API** to generate complete, branching storylines at once, allowing users to explore different paths and endings based on their choices.

---

## Features

- **AI-Generated Stories:** The ChatGPT API creates a full story tree with multiple branches and endings based on a selected theme.  
- **Interactive Exploration:** Users navigate through pre-generated story branches by making choices at key decision points.  
- **Responsive Frontend:** Built with React for a seamless, real-time storytelling experience.  
- **Cloud Deployment:** Backend hosted and managed on Choreo for scalability and stability.

---

## Tech Stack

- **Frontend:** React (Vite)  
- **Backend:** FastAPI (Python)  
- **AI Integration:** OpenAI ChatGPT API  
- **Deployment:** Choreo  
- **Version Control:** Git + GitHub

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## How It Works

1. The user selects a story theme (e.g., fantasy, mystery, sci-fi).  
2. The backend requests the ChatGPT API to generate the **entire branching storyline**, including all possible choices and endings.  
3. The full story structure is returned to the frontend.  
4. As users make choices, the UI reveals the corresponding branches from the pre-generated story tree. No further API calls are needed.  
5. Users can replay the story and explore alternate paths instantly.

