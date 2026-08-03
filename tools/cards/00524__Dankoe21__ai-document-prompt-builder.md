---
id: tool-00524
type: tool
area: 库
status: active
tags: [提示词, HTML, 协议未明, 本地优先, 英文文档, 多Agent, 本地写作]
title: ai-document-prompt-builder
summary: 提示词/写作工作流
source: https://github.com/dankoe21/ai-document-prompt-builder
created: 2026-07-18
updated: 2026-07-18
no: 524
category: 二、网文 / 长篇 AI 写作系统 库
repo: Dankoe21/ai-document-prompt-builder
stars: 0
url: https://github.com/dankoe21/ai-document-prompt-builder
tier: "C"
use_case: "提示词/写作工作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Dankoe21/ai-document-prompt-builder

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/dankoe21/ai-document-prompt-builder
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：A comprehensive HTML-based prompt builder for AI document generation featuring modular controls for document type, analysis, writing style, citations, formatting, typography, colors, tables, charts, and companion outputs. Generate optimized prompts for ChatGPT, Claude, Gemini, and other LLMs.
- **本地描述**：A comprehensive HTML-based prompt builder for AI document generation featuring modular controls for document type, analysis, writing style, citations, formatting, typography, colors, tables, charts, and companion outputs. Generate optimized prompts for ChatGPT, Claude, Gemini, and other LLMs.
- **拉取时间**：2026-07-23 22:54:19

---

# AI Document Prompt Builder

A browser-based HTML application for building detailed, professional
prompts for AI document generation. Instead of writing long prompts from
scratch, you configure your document through a series of organized
options. The builder combines those selections into a structured prompt
that works with ChatGPT, Claude, Gemini, and other instruction-following
language models.

The goal is simple: spend less time figuring out how to ask the AI for
what you want and more time creating high-quality documents.

------------------------------------------------------------------------

# Demo

https://github.com/user-attachments/assets/7c859eb8-7395-4bee-8561-b7dd35a3572d

------------------------------------------------------------------------

# Why This Project Exists

Writing a good prompt is often harder than writing the document itself.
Small changes in wording, structure, or missing instructions can produce
very different results.

This project turns prompt engineering into a guided process. Rather than
expecting users to remember dozens of best practices, the interface
walks them through the decisions that influence the final output. Each
section controls a specific aspect of the prompt, making it easy to
build detailed instructions without becoming overwhelming.

Whether you're creating a business report, research paper, whitepaper,
proposal, user manual, study guide, or technical documentation, the
builder helps generate prompts that are organized, consistent, and easy
to customize.

------------------------------------------------------------------------

# Features

The builder is organized into modular sections that each control a
different part of the generated prompt. Users can choose the document
type, define its purpose, specify the desired length and level of
detail, select an analytical approach, choose a writing style, identify
the target audience, configure citation and reference formats, and
customize the document's visual presentation.

Visual formatting goes beyond basic styling. The builder supports
typography hierarchies, font selection, strategic color palettes,
tables, charts, diagrams, accessibility options, and other formatting
choices that influence both readability and presentation.

Many document types can also generate companion outputs such as
executive summaries, presentation outlines, study guides, discussion
questions, action plans, FAQs, and other supporting material.

------------------------------------------------------------------------

# Compatibility

Generated prompts are designed for modern AI language models that follow
detailed instructions. While the prompts are optimized for ChatGPT, they
also work well with Claude, Gemini, Microsoft Copilot, Grok, DeepSeek,
and most other current large language models.

Because the builder generates plain text prompts rather than
model-specific code, it remains portable across AI platforms.

------------------------------------------------------------------------

# Technology

The project is written entirely in HTML, CSS, and JavaScript. It runs
locally in any modern web browser and does not require installation,
build tools, external frameworks, or server-side components. Download
the repository, open the HTML file, and start building prompts.

---------------------------------------------------------------------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Design Philosophy

The builder is designed around three ideas.

First, every option should represent a meaningful decision that affects
the quality of the generated document.

Second, beginners should be able to produce strong prompts without
understanding prompt engineering, while experienced users should have
enough control to fine-tune nearly every aspect of the output.

Finally, the generated prompts should remain readable. A prompt isn't
just something sent to an AI model; it's also documentation that
explains exactly what the model has been asked to produce.
