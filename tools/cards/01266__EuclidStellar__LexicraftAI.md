---
id: tool-01266
type: tool
area: 库
status: active
tags: [TTS, 校对, JavaScript, 协议未明, 需API密钥, 英文文档, 改稿润色]
title: LexicraftAI
summary: 小说转语音/有声书
source: https://github.com/euclidstellar/lexicraftai
created: 2026-07-18
updated: 2026-07-18
no: 1266
category: 二、网文 / 长篇 AI 写作系统 库
repo: EuclidStellar/LexicraftAI
stars: 12
url: https://github.com/euclidstellar/lexicraftai
tier: "B"
use_case: "小说转语音/有声书"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# EuclidStellar/LexicraftAI

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/euclidstellar/lexicraftai
- **Stars**：12
- **语言**：JavaScript
- **License**：None
- **Topics**：ai, ai-agents, novel, novel-view-synthesis, writing, writing-tool
- **GitHub 描述**：We build what writer's love :) An Open Source magical tool for writing books and novels built by : @euclidstellar https://deepwiki.com/EuclidStellar/LexicraftAI
- **本地描述**：We build what writer's love :) An Open Source magical tool for writing books and novels built by : @euclidstellar https://deepwiki.com/EuclidStellar/LexicraftAI
- **拉取时间**：2026-07-23 23:16:00

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI Writing Assistant: Your All-in-One Creative Writing Partner

An open-source, AI-powered writing suite designed for authors, screenwriters, and creators. This tool goes beyond simple grammar checks, offering a comprehensive toolkit for every stage of the writing process—from initial brainstorming to final manuscript analysis. Built as a free, powerful alternative to paid platforms like QuillBot, it leverages the Google Gemini API to provide nuanced and context-aware assistance.

## ✨ Key Features

This application is structured as a suite of specialized tools, each targeting a specific aspect of the writing craft.

### Core Writing Suite

-   **✍️ Enhanced Paraphraser** ([`EnhancedParaphraser.js`](https://github.com/EuclidStellar/LexicraftAI/blob/main/src/components/EnhancedParaphraser.js)): Transform your text with various literary modes and styles. Whether you need a formal tone, a creative flourish, or a specific author's voice, this tool provides sophisticated rewriting capabilities.
-   **🔍 Advanced Grammar & Style Checker** ([`GrammarChecker.js`](https://github.com/EuclidStellar/LexicraftAI/blob/main/src/components/GrammarChecker.js)): Get in-depth analysis of your text, identifying issues from critical grammar errors to subtle style inconsistencies. It provides an overall score, detailed issue breakdowns, and actionable suggestions.
-   **📊 Readability Optimizer** ([`ReadabilityOptimizer.js`](https://github.com/EuclidStellar/LexicraftAI/blob/main/src/components/ReadabilityOptimizer.js)): Tailor your writing to your intended audience. This tool analyzes readability scores, sentence complexity, and vocabulary, providing an optimized version of your text to ensure it resonates perfectly with readers.
-   **🎭 Tone Analyzer** ([`ToneAnalyzer.js`](https://github.com/EuclidStellar/LexicraftAI/blob/main/src/components/ToneAnalyzer.js)): Understand the emotional undercurrent of your writing. It detects the primary tone, sentiment, and confidence level, offering suggestions to align the tone with your creative vision.
-   **📄 Smart Summarizer** ([`Summarizer.js`](https://github.com/EuclidStellar/LexicraftAI/blob/main/src/components/Summarizer.js)): Quickly condense long passages of text into short, medium, or detailed summaries, complete with compression statistics.

### Creative Writing Toolkit for Novelists & Screenwriters

-   **📖 Manuscript Manager** ([`ManuscriptManager.js`](https://github.com/EuclidStellar/LexicraftAI/blob/main/src/components/ManuscriptManager.js)): Organize your novel or screenplay chapter by chapter. This feature allows you to write, edit, and reorder chapters while providing high-level analytics on your entire manuscript, including word counts, pacing analysis, and consistency checks.
-   **🎪 Interactive Scene Builder** ([`SceneBuilder.js`](https://github.com/EuclidStellar/LexicraftAI/blob/main/src/components/SceneBuilder.js)): Craft and analyze individual scenes with precision. Write your scene and get instant feedback on conflict levels, tension, pacing, and dialogue quality. It provides actionable suggestions to make every scene impactful.
-   **📊 Plot Structure Analyzer** ([`PlotAnalyzer.js`](https://github.com/EuclidStellar/LexicraftAI/blob/main/src/components/PlotAnalyzer.js)): Deconstruct your narrative against proven storytelling frameworks like the **Three-Act Structure**, **Hero's Journey**, and **Seven-Point Story Structure**. It visualizes your plot's progression and provides insights to strengthen its foundation.
-   **👥 Character Development Assistant** ([`CharacterAssistant.js`](https://github.com/EuclidStellar/LexicraftAI/blob/main/src/components/CharacterAssistant.js)): Breathe life into your characters. Analyze their voice, traits, and emotional range. The assistant checks for consistency across your manuscript and generates creative suggestions for dialogue, backstory, and development.

## 🛠️ Technology Stack

-   **Frontend**: React, React Router
-   **AI Integration**: Google Gemini API via [`geminiAPI.js`](https://github.com/EuclidStellar/LexicraftAI/blob/main/src/services/geminiAPI.js)
-   **Styling**: Plain CSS with a responsive, modern design in [`main.css`](https://github.com/EuclidStellar/LexicraftAI/blob/main/src/styles/main.css)

## 🚀 Getting Started

### Prerequisites

-   Node.js and npm installed on your machine.
-   A Google Gemini API Key.

### Installation & Setup

1.  **Clone the repository:**
    ````sh
    git clone https://github.com/euclidstellar/elstefano.git
    cd elstefano
    ````

2.  **Install dependencies:**
    ````sh
    npm install
    ````

3.  **Set up your API Key:**
    The application requires a Google Gemini API key to function. You can set it in one of two ways:
    -   **Recommended**: Run the application and use the "API Key" button in the UI. The key is stored securely in your browser's local storage and is never exposed.
    -   **Alternative**: Create a `.env` file in the root directory and add `REACT_APP_GEMINI_API_KEY=YOUR_API_KEY_HERE`.

### Running the Application

1.  **Start the development server:**
    ````sh
    npm start
    ````

2.  Open your browser and navigate to `http://localhost:3000` to begin writing.

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Please feel free to submit a pull request or open an issue for any enhancements, bug fixes, or feature suggestions.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
