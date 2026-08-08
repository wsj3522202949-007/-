---
id: tool-00863
type: tool
area: 库
status: active
tags: [提示词, Python, 协议未明, 本地优先, 英文文档, 多Agent, 本地写作]
title: StoryIdeaGenerator.AI
summary: 提示词/写作工作流
source: https://github.com/dibyosree/storyideagenerator.ai
created: 2026-07-18
updated: 2026-07-18
no: 863
category: 二、网文 / 长篇 AI 写作系统 库
repo: Dibyosree/StoryIdeaGenerator.AI
stars: 0
url: https://github.com/dibyosree/storyideagenerator.ai
tier: "C"
use_case: "提示词/写作工作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 1ab82732fdf2e73c
  - methods/最强写作方法论_全球最强综合版.md
---

# Dibyosree/StoryIdeaGenerator.AI

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/dibyosree/storyideagenerator.ai
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A CLI tool powered by Google’s Gemini API that crafts unique story prompts from user-supplied genre, theme, and character inputs—demonstrating prompt engineering for creative writing.
- **本地描述**：A CLI tool powered by Google’s Gemini API that crafts unique story prompts from user-supplied genre, theme, and character inputs—demonstrating prompt engineering for creative writing.
- **拉取时间**：2026-07-23 23:04:10

---

# 📝 Story Idea Generator (CLI using Gemini API)

The **Story Idea Generator** is a command-line Python application powered by **Google's Gemini API**. It helps users generate original, creative story ideas based on genre, theme, and character inputs. This project showcases prompt engineering techniques and the creative capabilities of large language models.

---

## 🎯 Project Objective

This tool is built as part of a **Prompt Engineering project** to explore how prompt structure, tone, and constraints can influence the quality and style of AI-generated outputs. It allows users to interactively generate creative story prompts using:

- 🎭 Genre (e.g., Fantasy, Sci-Fi)
- 🎨 Theme (e.g., Betrayal, Redemption)
- 👤 Character Description (e.g., a cursed prince)

---

## 🌟 Features

- 🧠 **3 Prompt Styles**:
  - **Basic**: Direct and simple story generation
  - **Elaborate**: Detailed setup including twist and conflict
  - **Constraint**: Creative story beginnings with random opening lines

- ✅ Gemini API integration using `google-generativeai`
- ✅ Interactive user input and feedback
- ✅ Demonstrates core concepts of prompt engineering
- ✅ Lightweight CLI app for creative inspiration

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 🧠 Example Interaction

```bash
📖 Welcome to the Story Idea Generator (Powered by Gemini AI)

Enter a genre: Sci-Fi
Enter a theme: Identity
Describe a main character: A robot who wants to be human

Choose a prompt style:
1. Basic
2. Elaborate
3. Constraint

✨ Here's your story idea:
In a futuristic society, an android named Xyra discovers fragments of human memories embedded in its core. Driven by the desire to become more than its programming, Xyra embarks on a journey of self-discovery, only to uncover it was once a human consciousness transferred during a failed experiment...
