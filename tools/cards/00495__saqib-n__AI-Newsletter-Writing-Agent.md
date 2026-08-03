---
id: tool-00495
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: AI-Newsletter-Writing-Agent
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/saqib-n/ai-newsletter-writing-agent
created: 2026-07-18
updated: 2026-07-18
no: 495
category: 二、网文 / 长篇 AI 写作系统 库
repo: saqib-n/AI-Newsletter-Writing-Agent
stars: 0
url: https://github.com/saqib-n/ai-newsletter-writing-agent
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# saqib-n/AI-Newsletter-Writing-Agent

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/saqib-n/ai-newsletter-writing-agent
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：    An Autonomous Newsletter Generator built in n8n. It uses Perplexity AI for deep research, Google Gemini for content creation, and automatically formats and emails an HTML newsletter based on a simple chat prompt.
- **本地描述**：An Autonomous Newsletter Generator built in n8n. It uses Perplexity AI for deep research, Google Gemini for content creation, and automatically formats and emails an HTML newsletter based on a simple chat prompt.
- **拉取时间**：2026-07-23 22:53:30

---

# AI-Newsletter-Writing-Agent
    An Autonomous Newsletter Generator built in n8n. It uses Perplexity AI for deep research, Google Gemini for content creation, and automatically formats and emails an HTML newsletter based on a simple chat prompt.
    
![n8n](https://img.shields.io/badge/Workflow-n8n-FF6584?style=for-the-badge&logo=n8n&logoColor=white)
![Gemini](https://img.shields.io/badge/AI_Model-Google_Gemini-8E75B2?style=for-the-badge&logo=google-gemini&logoColor=white)
![Perplexity](https://img.shields.io/badge/Research-Perplexity_AI-222222?style=for-the-badge&logo=perplexity&logoColor=white)
![Gmail](https://img.shields.io/badge/Delivery-Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white)

### 🚀 Overview
This repository contains an **Autonomous Content Pipeline** built in **n8n**. 

It solves the biggest problem in content creation: **Research.** Instead of just hallucinating text, this workflow uses a specialized "Research Agent" connected to **Perplexity AI** to gather real-time, factual data before writing. It then formats the content into a beautiful HTML email and sends it out—all from a single prompt.

---

### 🧠 System Architecture

The workflow operates as a linear chain of specialized AI Agents:

#### 🟩 1. The Research Agent (Green Zone)
*   **Role:** Deep Dive & Fact Gathering.
*   **Logic:** Triggered by a simple chat message (e.g., "Write a newsletter about the latest AI trends").
*   **Integration:** It utilizes the **Perplexity API** to browse the live internet and gather up-to-date sources, statistics, and news. It passes this raw "Truth" to the next agent.

#### ⬛ 2. The Newsletter Agent (Middle Zone)
*   **Role:** Content Writer & Designer.
*   **Logic:** Using `Google Gemini`, this agent takes the raw research and transforms it into an engaging newsletter format.
*   **HTML Generation:** It connects to an HTML Template node to ensure the email looks professional (headers, bullet points, footer) rather than a wall of text.

#### 🟦 3. The Publisher Agent (Blue Zone)
*   **Role:** Copywriter & Delivery.
*   **Logic:**
    *   **Title Writer:** It reads the final newsletter and generates a high-converting, catchy Subject Line.
    *   **Delivery:** It packages the HTML content and the Subject Line and sends it via **Gmail** to your subscriber list or yourself.

---

### 🛠️ Prerequisites

1.  **n8n Instance:** Self-hosted or Cloud version.
2.  **Perplexity API Key:** For the online research capability.
3.  **Google Cloud Console:** Enable Gemini API.
4.  **Gmail API:** Credentials for sending the final email.

---

### 📥 Installation

1.  Clone this repository.
2.  Open your **n8n** dashboard.
3.  Click **"Import Workflow"** and select the `.json` file.
4.  Configure your credentials (Perplexity, Google Gemini, Gmail).
5.  **Run:** Open the chat window in n8n, type a topic, and watch the agents work.

---

### 🔮 Use Cases

*   **Industry Updates:** "Give me a weekly summary of Crypto prices and news."
*   **Competitor Analysis:** "Research the latest features launched by [Competitor] and write a brief."
*   **Content Marketing:** Automate the draft creation for your Substack or LinkedIn newsletter.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<div align="center">
  <p>Built with ❤️ by <a href="https://www.wolfxense.agency/">WolfXense AI</a></p>
  <p><i>Your AI Transformation Partner</i></p>
</div>
