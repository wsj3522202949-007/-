---
id: tool-01029
type: tool
area: 库
status: active
tags: [TTS, TypeScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: essay_helper
summary: 小说转语音/有声书
source: https://github.com/vishal-vunnam/essay_helper
created: 2026-07-18
updated: 2026-07-18
no: 1029
category: 二、网文 / 长篇 AI 写作系统 库
repo: Vishal-Vunnam/essay_helper
stars: 0
url: https://github.com/vishal-vunnam/essay_helper
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: ed3e35703183fb33
  - methods/最强写作方法论_全球最强综合版.md
---

# Vishal-Vunnam/essay_helper

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/vishal-vunnam/essay_helper
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Essay Helper is a writing assistant that aims to enhance creativity without controlling it. This tool focuses on post-creation analysis rather than pre-creation assistance. It allows you to express your thoughts freely and receive constructive feedback afterward.
- **本地描述**：Essay Helper is a writing assistant that aims to enhance creativity without controlling it. This tool focuses on post-creation analysis rather than pre-creation assistance. It allows you to express your thoughts freely and receive constructive feedback afterward.
- **拉取时间**：2026-07-23 23:09:01

---

# Essay Helper

**Essay Helper** is a writing assistant that aims to enhance creativity without controlling it. This tool focuses on **post-creation analysis** rather than pre-creation assistance. It allows you to express your thoughts freely and receive constructive feedback afterward.

The goal is to support **free thought, clarity, and autonomy**, while still offering the benefits of AI, such as logic checking, fallacy detection, and helpful suggestions.

---

![alt text](https://github.com/Vishal-Vunnam/essay_helper/blob/master/src/img/Screenshot%202025-06-18%20at%2011.37.20%E2%80%AFAM.png)

![alt text](https://github.com/Vishal-Vunnam/essay_helper/blob/master/src/img/Screenshot%202025-06-18%20at%2011.47.37%E2%80%AFAM.png)

## Features

- Rich-text editor with intuitive formatting
- AI-powered issue detection (e.g., logical fallacies, vague reasoning)
- Sentence-level highlighting of flagged issues
- Sidebar explanation of detected problems
- Local LLM using [Ollama](https://ollama.com)

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/essay-helper.git
cd essay-helper

#INSTALL DEPENDENCIES 
npm install
# or
yarn
# or
pnpm install

#START DEVELOPMENT SERVER
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev


The app will run at http://localhost:3000.

##Local LLM Setup with Ollama
This project uses Ollama to run a local language model.

##Install and Run Mistral
Install Ollama: https://ollama.com/download

##Run the following command:
ollama run mistral

#FUTURE GOALS
Detect stylistic issues (e.g., passive voice, redundancy)

Add citation and source-checking support

Customize feedback based on writing goals (persuasive, narrative, academic)

Enable export to formats like PDF or Google Docs with margin comments

#Philosophy
This tool is designed to support reflection, not restriction. AI is used here to enhance thought, not replace it. Essay Helper encourages critical thinking and revision without compromising the writer’s voice.

##Contributors
Vishal Vunnam

##License
MIT License — free to use and modify. Contributions are welcome.
Let me know if you want to add a usage GIF, contribution guide, or environment variables section.
