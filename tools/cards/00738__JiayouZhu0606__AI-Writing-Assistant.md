---
id: tool-00738
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: AI-Writing-Assistant
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/jiayouzhu0606/ai-writing-assistant
created: 2026-07-18
updated: 2026-07-18
no: 738
category: 二、网文 / 长篇 AI 写作系统 库
repo: JiayouZhu0606/AI-Writing-Assistant
stars: 0
url: https://github.com/jiayouzhu0606/ai-writing-assistant
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 795dc0274b8bcdad
  - methods/最强写作方法论_全球最强综合版.md
---

# JiayouZhu0606/AI-Writing-Assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/jiayouzhu0606/ai-writing-assistant
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：academic-writing
- **GitHub 描述**：A website tool designed to polish, reduce AI rate and peer-review manuscripts.
- **本地描述**：A website tool designed to polish, reduce AI rate and peer-review manuscripts.
- **拉取时间**：2026-07-23 23:00:33

---

# AI Writing Assistant 1.5.12 🎓

![Version](https://img.shields.io/badge/version-1.5.12-blue) ![Type](https://img.shields.io/badge/Web_App-SPA-green) ![Focus](https://img.shields.io/badge/Focus-SSCI_Academic-orange)

A specialized **Single Page Application (SPA)** designed for researchers, PhD candidates, and academics aiming for top-tier SSCI publications. This tool acts as a personal Chief Editor, providing academic polishing, high-entropy AI text humanization, and simulated peer review—all running locally in your browser for maximum privacy.

---

## ✨ Key Features

The application utilizes deeply engineered system prompts to simulate specific academic roles:

### 1. 🖊️ Academic Polishing (Green Theme)
*   **Role**: Chief Editor of flagship SSCI journals (Applied Linguistics, Psychology, Education).
*   **Function**: Refines grammar, enhances lexical precision, optimizes sentence architecture (periodic/cumulative sentences), and strengthens logical flow.
*   **Output**: Generates a "Revision Analysis Table" and the final polished text with changes highlighted.

### 2. 🌱 AI Humanization / De-similitude (Blue Theme)
*   **Role**: Elite Academic Text Humanization Specialist & Forensic Linguist.
*   **Function**: Increases linguistic entropy and perplexity to eliminate AI watermarks (e.g., overuse of "delve," "crucial," "tapestry") while maintaining a rigorous academic register. 
*   **Technique**: Uses an "Anti-Pattern" protocol to avoid detection without resorting to colloquialisms or slang.

### 3. 🕵️ Peer Review Simulation (Orange Theme)
*   **Role**: The rigorous "Reviewer 2".
*   **Function**: Simulates the SSCI peer review process, critiquing methodology, theoretical frameworks, and argumentation. Automatically generates a **Response Letter** draft and actionable revision strategies.

---

## 🚀 What's New in v1.5.12

*   **🛑 Abort Control**: Added a "Stop Generating" button to immediately halt the AI's processing.
*   **⚛️ Minimalist Research UI**: Replaced game-style animations with a professional "Data Scan / Neural Node" loading visualization.
*   **🔧 Custom Instructions**: Added an "Extra Requirement" input field, allowing users to layer specific constraints (e.g., "Keep passive voice," "Limit to 200 words") on top of the standard modes.
*   **📱 Responsive Layout**: Optimized split-screen design with overflow protection for Markdown tables on smaller screens.

---

## 🛠️ How to Use

1.  **Open the App**: Visit the [GitHub Pages Link](https://jiayouzhu0606.github.io/AI-Writing-Assistant/).
2.  **Configure API**:
    *   Open the settings sidebar (top-left icon).
    *   Select your AI Provider (Supports **Moonshot (Kimi)**, **DeepSeek**, **Zhipu AI**, **Qwen**, etc.).
    *   Enter your API Key (Keys are stored locally in your browser cache and never sent to our server).
3.  **Select Mode**: Choose between Polishing, Humanize AI, or Peer Review from the sidebar.
4.  **Input Text**:
    *   Paste your manuscript text directly.
    *   Or click "Upload" to parse `.docx` / `.txt` files.
    *   *(Optional)* Add extra instructions in the bottom input field.
5.  **Execute**: Click the button and watch the real-time analysis and revision in the right panel.

---

## 🔒 Privacy & Security

*   **Client-Side Architecture**: This is a pure HTML/JS application.
*   **No Backend Storage**: Your API Keys and manuscript content are transmitted **directly from your browser to the AI provider's API**. No data passes through or is stored on the author's servers.
*   **Open Source**: The code is fully transparent. You can audit the `index.html` source code at any time.

---

## 💻 Tech Stack

*   **Vue.js 3**: Reactive UI framework.
*   **Tailwind CSS**: Utility-first CSS framework for styling.
*   **Marked.js**: Markdown rendering.
*   **Mammoth.js**: `.docx` file parsing.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 🤝 Contribution

Issues and Pull Requests are welcome! If you encounter any bugs or have ideas for new features, please feel free to contribute.

Welcome to any suggestions and criticism!

**Author**: Jiayou Zhu
