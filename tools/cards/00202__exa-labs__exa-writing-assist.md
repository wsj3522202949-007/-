---
id: tool-00202
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: exa-writing-assist
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/exa-labs/exa-writing-assist
created: 2026-07-18
updated: 2026-07-18
no: 202
category: 二、网文 / 长篇 AI 写作系统 库
repo: exa-labs/exa-writing-assist
stars: 39
url: https://github.com/exa-labs/exa-writing-assist
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# exa-labs/exa-writing-assist

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/exa-labs/exa-writing-assist
- **Stars**：39
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Writing and Citation Assistant Tool
- **本地描述**：Writing and Citation Assistant Tool
- **拉取时间**：2026-07-23 22:44:56

---

# Exa-powered Writing and Citation Assistant

This project demonstrates an advanced writing and citation assistant powered by Exa's prompt-engineered queries and Claude 3.5 Sonnet's generative capabilities. The assistant is designed to help users continue and expand their writing based on initial input.

![Conceptual block diagram of how the writing assistant works](https://files.readme.io/77dd3c1-image.png)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)

## Overview

The Exa-powered Writing and Citation Assistant combines the power of Exa's sophisticated query capabilities with Claude 3.5 Sonnet's advanced language model to create a tool that assists writers in generating content and managing citations seamlessly.

## Features

- Continuation of user-initiated writing
- Context-aware content generation
- Input debouncing to stop generating when a user pauses typing and kick off generation
- Automatic citation suggestions and management
- Integration of Exa's search capabilities for accurate and up-to-date information
- Powered by Claude 3.5 Sonnet for high-quality text generation

## How It Works

1. The user begins writing a piece of text.
2. The assistant analyzes the input using Exa's prompt-engineered queries to understand the context and gather relevant information.
3. Claude 3.5 Sonnet uses this context to generate continuation suggestions for the writing.
4. Exa's search capabilities are utilized to find and suggest relevant citations.
5. The generated content and citations are presented to the user for review and incorporation.

## Getting Started

To set up the project, follow these steps:

1. Clone the repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run the command `npm install` to install the project dependencies.
4. Configure any necessary API keys for Exa and Claude.
5. Run the command `npm run dev` to start the project locally.

Now you're ready to use the writing and citation assistant!

If deploying to vercel or similar, ensure to remove our bespoke domain setup in next.config.mjs

---

For more information about Exa and Claude, please visit their respective websites:
- [Exa](https://exa.ai)
- [Anthropic (creators of Claude)](https://www.anthropic.com)


related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

For more information about Exa and Claude, please visit their respective websites:
- [Exa](https://exa.ai)
- [Anthropic (creators of Claude)](https://www.anthropic.com)
