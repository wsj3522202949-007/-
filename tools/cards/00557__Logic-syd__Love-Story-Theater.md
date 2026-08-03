---
id: tool-00557
type: tool
area: 库
status: active
tags: [提示词, TypeScript, 协议未明, 需API密钥, 英文文档, 多Agent]
title: Love-Story-Theater
summary: 提示词/写作工作流
source: https://github.com/logic-syd/love-story-theater
created: 2026-07-18
updated: 2026-07-18
no: 557
category: 二、网文 / 长篇 AI 写作系统 库
repo: Logic-syd/Love-Story-Theater
stars: 1
url: https://github.com/logic-syd/love-story-theater
tier: "B"
use_case: "提示词/写作工作流"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Logic-syd/Love-Story-Theater

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/logic-syd/love-story-theater
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI story generator creating personal stories from prompts. Tech: Next.js (React/TS), Kotlin (Ktor), DeepSeek LLM API. A full-stack project showcasing a modern frontend, secure backend proxy, and AI integration.
- **本地描述**：AI story generator creating personal stories from prompts. Tech: Next.js (React/TS), Kotlin (Ktor), DeepSeek LLM API. A full-stack project showcasing a modern frontend, secure backend proxy, and AI integration.
- **拉取时间**：2026-07-23 22:55:17

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Emotional Comfort Cabin

## About This Project

https://github.com/Logic-syd/Love-Story-Theater 

This is a full-stack, AI-powered web application I built to explore the intersection of technology and emotional support. It’s a safe space for users who are feeling down about their relationship. Through a carefully guided, empathetic conversation, the app gathers details about their situation and their partner, then uses an AI to generate a unique, hopeful story that reframes their current problem as a temporary trial on the path to a happy future.

My goal was to create an experience that feels less like a tool and more like a warm, understanding friend.
 
You can try the live version here: https://love-story-theater.vercel.app/

## Key Features

  * **Dynamic & Empathetic Dialogue**: The heart of the app is a non-linear, multi-stage conversational flow. To keep the experience fresh, the app randomizes questions from different pools and uses an AI-driven interaction to generate contextual, follow-up questions. This makes every conversation feel natural and unique.

  * **Advanced Prompt Engineering**: I authored and refined a series of complex prompts to precisely control the AI's "best friend" persona. The prompts guide the AI’s narrative style, content structure, and emotional tone, transforming the user's raw input into a coherent and uplifting story.

  * **Mobile-First & Internationalized**: The chat interface was built with a mobile-first approach using Material-UI for a clean, responsive experience on any device. The entire application is architected for internationalization, with all text content managed in a separate configuration file (currently supporting Chinese, English, and German).

  * **Secure Full-Stack Architecture**: I implemented a decoupled, stateless architecture with a Next.js frontend and a Kotlin/Ktor backend. The backend acts as a secure proxy to the LLM API, ensuring all user data is isolated and API keys are protected.

## Tech Stack

  * **Frontend**: React, Next.js, TypeScript, Material-UI (MUI), Axios
  * **Backend**: Kotlin, Ktor
  * **AI Service**: DeepSeek API
  * **Deployment**: Vercel (Frontend), Render (Backend), Docker

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

  * Node.js (v18+)
  * JDK (11+)
  * Git

### Installation

1.  **Clone the repository:**

    ```sh
    git clone https://github.com/Logic-syd/Love-Story-Theater.git
    cd Love-Story-Theater
    ```

2.  **Set up the Backend:**

    ```sh
    cd love-story-backend

    # Create a .env file and add your API key
    echo "DEEPSEEK_API_KEY=sk-xxxxxxxx" > .env

    # Run the server
    ./gradlew run
    ```

    Your backend will be running at `http://localhost:8080`.

3.  **Set up the Frontend (in a new terminal):**

    ```sh
    cd love-story-frontend
    npm install
    npm run dev
    ```

    Open `http://localhost:3000` in your browser to see the app.
