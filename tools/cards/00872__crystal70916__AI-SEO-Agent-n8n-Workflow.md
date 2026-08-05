---
id: tool-00872
type: tool
area: 库
status: active
tags: [协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: AI-SEO-Agent-n8n-Workflow
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/crystal70916/ai-seo-agent-n8n-workflow
created: 2026-07-18
updated: 2026-07-18
no: 872
category: 二、网文 / 长篇 AI 写作系统 库
repo: crystal70916/AI-SEO-Agent-n8n-Workflow
stars: 3
url: https://github.com/crystal70916/ai-seo-agent-n8n-workflow
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# crystal70916/AI-SEO-Agent-n8n-Workflow

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/crystal70916/ai-seo-agent-n8n-workflow
- **Stars**：3
- **语言**：None
- **License**：MIT
- **Topics**：ai, automation, marketing-automation, n8n, open-source, workflows
- **GitHub 描述**：This workflow uses n8n, Gemini, and DataForSEO to create an AI agent that spies on your competitors, finds keyword gaps, and automates blog writing.
- **本地描述**：This workflow uses n8n, Gemini, and DataForSEO to create an AI agent that spies on your competitors, finds keyword gaps, and automates blog writing.
- **拉取时间**：2026-07-23 23:04:25

---

### 📺 Full Video Walkthrough & Setup Guide

This repository contains the complete workflow for **Keywordo-kun**, an AI agent specialized in competitor analysis, keyword research, and automated SEO content creation.

It's built for marketers, agencies, and SEO professionals who want to automate their research and writing process. The agent uses a powerful stack to analyze competitors, identify keyword opportunities, and generate high-quality, long-form blog posts.

## 🤖 How It Works: The Tool Stack

This project is built on **n8n** and **v0.dev**, connecting several key AI and data services:

* **n8n:** The central automation platform that runs the entire backend logic and agent "brain."
* **v0.dev:** Provides the sleek, conversational chat interface for the frontend.
* **Google Gemini (2.5 Pro & Flash):** Powers the agent's core reasoning, analysis, and content generation.
* **DataForSEO:** Provides the critical, real-time SERP data, keyword ideas, and competitor metrics.
* **Firecrawl:** Used to scrape and crawl websites for content analysis.

## 📂 What's Included in This Repository

This repository gives you all the components you need to deploy Keywordo-kun:

1.  **`Keywordo-kun (Articollo Agent).json`**: The main n8n workflow. This is the "brain" of the agent that handles the user chat, processes requests, and calls the necessary tools.
2.  **`Keywordo-kun (Tools).json`**: The secondary n8n workflow. This file contains all the individual tools (e.g., "Get Keyword Ideas," "Analyze SERP") that the main agent calls upon.
3.  **`Keywordo-kun Chat Interface (v0.dev).zip`**: The complete frontend UI. You can import this zip file directly into v0.dev to deploy the chat interface.
4.  **`Keywordo-kun image.png`**: The project's hero image.

## 🚀 How to Set Up (Prerequisites)

To get this workflow running, you will need accounts and API keys for the following services:

* An **n8n** account (Cloud or self-hosted).
* A **v0.dev** account to host the chat interface.
* A **Google AI Studio** API key for **Gemini**.
* A **DataForSEO** account and API credentials.
* A **Firecrawl** API key.

### 🏁 Quick Setup Guide

1.  **Deploy n8n Workflows:**
    * Create a new, empty workflow in n8n and import the `Keywordo-kun (Tools).json` file.
    * Create a second workflow and import the `Keywordo-kun (Articollo Agent).json` file.
2.  **Configure Tools Workflow:**
    * Open the "Tools" workflow and configure each HTTP Request node with your **DataForSEO** API credentials, as shown in the `[video guide]([https://www.youtube.com/watch?v=r9WMbzfY-mg&t])`.
    * Configure the Firecrawl node with your **Firecrawl** API key.
    * Save and activate this workflow.
3.  **Configure Agent Workflow:**
    * Open the "Agent" workflow.
    * Connect the **Gemini** nodes with your Google AI Studio API key.
    * In the "Agent" node, connect the tools to the "Tools" workflow you just deployed (by copying its production URL).
4.  **Deploy Frontend:**
    * Go to v0.dev and import the `Keywordo-kun Chat Interface (v0.dev).zip` file.
    * Get the **production webhook URL** from your "Agent" n8n workflow.
    * In the v0.dev chat prompt, ask it to replace the old webhook URL with your new one, as shown in the `[video guide]([https://www.youtube.com/watch?v=r9WMbzfY-mg&t])`.
5.  **Activate & Test:**
    * Activate your "Agent" n8n workflow.
    * Start chatting with your agent in the v0.dev interface!

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---


> For a full content publishing workflow powered by keyword research, see [Rankenstein](https://rankenstein.pro).

## Author

Built by [Agrici Daniel](https://agricidaniel.com/about) - AI Workflow Architect.

- [Blog](https://agricidaniel.com/blog) - Deep dives on AI marketing automation
- [AI Marketing Hub](https://www.skool.com/ai-marketing-hub) - Free community, 2,800+ members
- [YouTube](https://www.youtube.com/@AgriciDaniel) - Tutorials and demos
- [All open-source tools](https://github.com/AgriciDaniel)
