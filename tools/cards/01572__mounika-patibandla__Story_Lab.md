---
id: tool-01572
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Story_Lab
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/mounika-patibandla/story_lab
created: 2026-07-18
updated: 2026-07-18
no: 1572
category: 二、网文 / 长篇 AI 写作系统 库
repo: mounika-patibandla/Story_Lab
stars: 0
url: https://github.com/mounika-patibandla/story_lab
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# mounika-patibandla/Story_Lab

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/mounika-patibandla/story_lab
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A CPU-based AI story generator that uses a single Identity Prompt and multiple Frame Prompts to create structured multi-scene narratives with LLM assistance.
- **本地描述**：A CPU-based AI story generator that uses a single Identity Prompt and multiple Frame Prompts to create structured multi-scene narratives with LLM assistance.
- **拉取时间**：2026-07-23 23:24:55

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Story_Lab
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Gradio](https://img.shields.io/badge/Framework-Gradio-orange)
![LLM](https://img.shields.io/badge/LLM-Ollama-green)
![Model](https://img.shields.io/badge/Model-DreamShaper--7-purple)
![CPU Only](https://img.shields.io/badge/Execution-CPU--Only-red)

Story_Lab is a CPU-based AI story generation system that transforms structured prompts into multi-scene narrative outputs.

##  Features

- Single Identity Prompt for character definition
- Multiple Frame Prompts for scene generation
- Configurable frame count
- LLM-powered Story Assistant (via Ollama)
- CPU-only execution (No GPU required)
- Structured multi-scene output

##  How It Works

1. User provides a character Identity Prompt.
2. User provides multiple Frame Prompts.
3. LLM assistant generates structured story prompts.
4. Diffusion pipeline generates visual story frames.
5. Final story grid is produced.

##  Tech Stack

- Python
- Gradio
- Ollama (Mistral LLM)
- Diffusion Model (DreamShaper-7)
- CPU-based inference

##  Run Locally

```bash
pip install -r requirements.txt
python app.py
