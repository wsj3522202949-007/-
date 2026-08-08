---
id: tool-00105
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: Shayari-Generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/rodeo12/shayari-generator
created: 2026-07-18
updated: 2026-07-18
no: 105
category: 二、网文 / 长篇 AI 写作系统 库
repo: rodeo12/Shayari-Generator
stars: 1
url: https://github.com/rodeo12/shayari-generator
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
content_hash: b727c09e1fcf48ba
  - methods/最强写作方法论_全球最强综合版.md
---

# rodeo12/Shayari-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/rodeo12/shayari-generator
- **Stars**：1
- **语言**：JavaScript
- **License**：None
- **Topics**：css, express, gemini-api, html, javascript, nodejs
- **GitHub 描述**：This Content Generator App allows users to enter a keyword and receive a creatively AI generated Shayari poem,joke,quote, story based on the selection. It utilizes Gemini API (from Google AI) model for creative text generation.
- **本地描述**：This Content Generator App allows users to enter a keyword and receive a creatively AI generated Shayari poem,joke,quote, story based on the selection. It utilizes Gemini API (from Google AI) model for creative text generation.
- **拉取时间**：2026-07-23 22:42:02

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Content-Generator App
![content](https://github.com/rodeo12/Shayari-Generator/assets/112781993/a7c4f372-c3a2-4306-bf07-12ef3799b798)

# Introduction
    This Content Generator App allows users to enter a keyword and receive a creatively generated Shayari poem,joke,quote, story based on that keyword. It utilizes Gemini API (from Google AI) model for creative text generation.

# Project Type

    Fullstack (Frontend & Backend)

# Deployed App

    * Frontend:  https://contentgenerator12.netlify.app/
    * Backend:   https://shayarigeminibackend.onrender.com
    

# Directory Structure

shayari-generator/
    ├── backend/  (Node.js server code)
    │   ├── package-lock.json
    │   ├── package.json
    │   └── server.js
    │
    ├── frontend/  (HTML, CSS, and JavaScript code)
    │   ├── index.html
    │   ├── style.css
    │   └── script.js
    └── README.md  (This file)

# Features

    Generates a Shayari poem based on the entered keyword by the user, using OpenAI's API.
    Generates a Joke based on the entered keyword by the user, using OpenAI's API.
    Generates a Quote based on the entered keyword by the user, using OpenAI's API.
    Generates a Story based on the entered keyword by the user, using OpenAI's API.
    
    
# Design Decisions & Assumptions

    Used Gemini Api for creative text generation due to its ability to generate different creative text formats.
    Assumed users have a basic understanding of what content generation is.
    Installation & Getting Started

# Clone this repository:

    Git Bash
    Use code with caution & do not copy the code.
    git clone https://github.com/rodeo12/Shayari-Generator
    
    cd shayari-generator
    cd backend
    Install dependencies: npm install express dotenv @google/generative-ai cors
    
    Create a .env file in the project root directory and add your OpenAI API key:
    API_KEY=your_openai_api_key
    Run the server: npm start

This will start the server on port 3000 by default.

Usage

Open http://localhost:3000 (or your server's URL) in a web browser.
Enter a keyword in the input field.
Click the "Generate Shayari" button.
The generated Shayari will be displayed below the button.

# Source for Reference
    https://ai.google.dev/gemini-api/docs

# Technology Stack

    Frontend: HTML, CSS, JavaScript
    Backend: Node.js, Express.js
    External API: OpenAI API
