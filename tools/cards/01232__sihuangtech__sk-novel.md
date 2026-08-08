---
id: tool-01232
type: tool
area: 库
status: active
tags: [TypeScript, 协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: sk-novel
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/sihuangtech/sk-novel
created: 2026-07-18
updated: 2026-07-18
no: 1232
category: 二、网文 / 长篇 AI 写作系统 库
repo: sihuangtech/sk-novel
stars: 0
url: https://github.com/sihuangtech/sk-novel
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: de2c2dff50839866
  - methods/最强写作方法论_全球最强综合版.md
---

# sihuangtech/sk-novel

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/sihuangtech/sk-novel
- **Stars**：0
- **语言**：TypeScript
- **License**：MIT
- **Topics**：creative-writing, novel-platform, novel-writing, reading-platform, webnovel
- **GitHub 描述**：SK Novel is a modern, premium platform designed for both reading and writing novels, offering an immersive experience for readers and AI-powered tools to assist authors in their creative process.
- **本地描述**：SK Novel is a modern, premium platform designed for both reading and writing novels, offering an immersive experience for readers and AI-powered tools to assist authors in their creative process.
- **拉取时间**：2026-07-23 23:15:01

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# SK Novel

SK Novel is a modern, premium platform for reading and writing novels, designed with a focus on aesthetics and user experience. It seamlessly bridges the gap between authors and readers, offering AI-powered tools to assist writers and a clean, immersive interface for readers.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![React](https://img.shields.io/badge/React-19.0-61dafb.svg?style=flat&logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178c6.svg?style=flat&logo=typescript)
![Vite](https://img.shields.io/badge/Vite-7.0-646cff.svg?style=flat&logo=vite)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-3.4-38b2ac.svg?style=flat&logo=tailwind-css)

## ✨ Features

### For Readers

* **Immersive Reading Experience**: A clean, distraction-free reader interface optimized for novel consumption.
* **Library Management**: Track your reading progress, manage your bookshelf, and bookmark your favorite stories.
* **Discovery**: Browse rankings, explore new genres, and find hidden gems.
* **Membership Tiers**: Access exclusive content through membership tiers (Free, Member, Supporter).

### For Authors

* **Author Studio**: A powerful dashboard to manage manuscripts, meaningful stats, and membership data.
* **Chapter Editor**: A dedicated editor for writing and refining chapters.
* **Analytics**: Track newsletter performance, open rates, and reader engagement.

### 🤖 AI-Powered Assistants

SK Novel integrates Google's Gemini AI (`gemini-3-flash-preview`) to supercharge the writing process:

* **Story Continuation**: Stuck on a scene? Let AI suggest the next few paragraphs based on your current context.
* **Chapter Summarization**: Automatically generate engaging summaries for your chapters to tease readers.

### 🛠️ Technical Highlights

* **Modern Stack**: Built with React 19, TypeScript, and Vite for blazing fast performance.
* **Styling**: Beautiful, responsive UI crafted with Tailwind CSS and Lucide icons.
* **Data Visualization**: Integrated Recharts for visualizing author statistics.
* **Export**: Built-in tools to export novels and chapters to TXT format.

## 🚀 Getting Started

Follow these steps to get a local copy up and running.

### Prerequisites

* Node.js (v18 or higher recommended)
* npm or yarn

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/sihuangtech/sk-novel.git
    cd sk-novel
    ```

2. **Install dependencies**

    ```bash
    npm install
    ```

3. **Environment Setup**
    Create a `.env.local` file in the root directory and add your Google Gemini API Key. This is required for AI features to work.

    ```properties
    GEMINI_API_KEY=your_api_key_here
    ```

4. **Run the application**

    ```bash
    npm run dev
    ```

    Open <http://localhost:3000> to view it in the browser.

## 📁 Project Structure

```text
sk-novels/
├── src/
│   ├── components/     # Reusable UI components (Layouts, etc.)
│   ├── pages/          # Application pages (Public & Admin)
│   ├── services/       # API and logic services (Gemini AI, Export)
│   ├── types.ts        # TypeScript definitions
│   ├── store.tsx       # State management (Context)
│   ├── App.tsx         # Main router and app entry
│   └── main.tsx        # Entry point
├── .env.local          # Environment variables (API Keys)
├── package.json        # Project dependencies and scripts
└── vite.config.ts      # Vite configuration
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.
