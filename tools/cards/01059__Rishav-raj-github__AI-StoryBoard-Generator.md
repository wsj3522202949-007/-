---
id: tool-01059
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: AI-StoryBoard-Generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/rishav-raj-github/ai-storyboard-generator
created: 2026-07-18
updated: 2026-07-18
no: 1059
category: 二、网文 / 长篇 AI 写作系统 库
repo: Rishav-raj-github/AI-StoryBoard-Generator
stars: 0
url: https://github.com/rishav-raj-github/ai-storyboard-generator
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
content_hash: d18535b8a3413f30
  - methods/最强写作方法论_全球最强综合版.md
---

# Rishav-raj-github/AI-StoryBoard-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/rishav-raj-github/ai-storyboard-generator
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：Rishav-raj-github/AI-StoryBoard-Generator
- **拉取时间**：2026-07-23 23:09:52

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI StoryBoard Generator 🎬

A creative tool designed for filmmakers, animators, and writers. You provide a single sentence prompt, and this tool uses an LLM to generate a full 3-act narrative, extracts key scenes, and writes highly-optimized image generation prompts for Midjourney/Stable Diffusion.

## Overview
Writing good prompts for image generators is hard. This project chains two LLM calls:
1. **The Writer**: Expands the seed idea into a structured short story.
2. **The Director**: Parses the story and extracts 4 visual "shots", formatting them perfectly as Stable Diffusion/Midjourney prompts (e.g., specifying lighting, camera angle, and lens type).

## Tech
- Python, LangChain, Pydantic for structured outputs.
- Gradio for the UI.

## Usage
Run `python src/gradio_app.py` and open your browser!
