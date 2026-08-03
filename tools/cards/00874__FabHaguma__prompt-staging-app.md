---
id: tool-00874
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: prompt-staging-app
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/fabhaguma/prompt-staging-app
created: 2026-07-18
updated: 2026-07-18
no: 874
category: 二、网文 / 长篇 AI 写作系统 库
repo: FabHaguma/prompt-staging-app
stars: 0
url: https://github.com/fabhaguma/prompt-staging-app
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# FabHaguma/prompt-staging-app

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/fabhaguma/prompt-staging-app
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Prompt Staging App provides a structured environment for writing and organizing prompts before sending them to an AI.
- **本地描述**：Prompt Staging App provides a structured environment for writing and organizing prompts before sending them to an AI.
- **拉取时间**：2026-07-23 23:04:29

---

# 🛠️ Prompt Staging App

The **Prompt Staging App** is a companion tool for developers and prompt engineers who interact with AI models. It provides a structured environment for writing and organizing prompts before sending them to an AI.

This tool is especially useful when working on complex tasks involving multiple languages or evolving instructions, where giving the AI clear and contextual input matters most.

---

## ✨ Features

### ✅ Core Functionality (MVP)

- **Markdown Editor**
  - Write and edit prompt bodies in Markdown.
- **Header/Footer Prompt Zones**

  - Drag-and-drop reusable prompt blocks into header and footer sections.
  - Blocks include:
    - Title
    - Toggle to include/exclude from final prompt
    - Remove button

- **Prompt Gallery Panel**

  - Connects to Supabase and pulls prompts filtered by category `prompt-stage`.
  - Prompts are organized by type: `header` or `footer`.
  - Prompts can be dragged into header/footer zones.

- **Action Panel**

  - Copy Final Prompt
  - Clean Staging Area
  - Save Project
  - Load Project

- **Project Saving**
  - Projects are saved locally with:
    - Markdown body
    - Prompt IDs for header and footer
    - Timestamp and project name

---

## 🧱 Tech Stack

| Concern               | Tech                      |
| --------------------- | ------------------------- |
| Frontend Framework    | React                     |
| Styling               | Tailwind CSS + ShadCN UI  |
| Markdown Editor       | CodeMirror                |
| Drag and Drop         | dnd-kit                   |
| Prompt Storage        | Supabase (Prompt Gallery) |
| Project Storage (MVP) | localStorage              |
| State Management      | Zustand                   |

---

## 🗃️ Data Structure

### Prompt (from Supabase)

### Prompt (from Supabase)

| Field      | Type        | Description                                 |
| ---------- | ----------- | ----------------------------------------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
--- |
| id         | int8        | Primary key                                 |
| created_at | timestamptz | Timestamp when the prompt was created       |
| prompt     | text        | The main prompt body                        |
| category   | text        | Category of the prompt (e.g., prompt-stage) |
| tags       | text[]      | Array of tags for organization              |
| rating     | float4      | User-assigned rating                        |
| notes      | text        | Additional notes                            |
| nsfw_score | float4      | NSFW score for content moderation           |

**Example:**

```json
{
  "id": 123,
  "created_at": "2024-06-01T12:34:56.789Z",
  "prompt": "Refactor this code to improve readability and performance.",
  "category": "prompt-stage",
  "tags": ["refactor", "code", "performance"],
  "rating": 4.5,
  "notes": "Useful for code review sessions.",
  "nsfw_score": 0.01
}
```

