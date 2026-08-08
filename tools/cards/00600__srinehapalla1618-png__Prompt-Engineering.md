---
id: tool-00600
type: tool
area: 库
status: active
tags: [提示词, 协议未明, 本地优先, 英文文档, 多Agent, 本地写作]
title: Prompt-Engineering
summary: 提示词/写作工作流
source: https://github.com/srinehapalla1618-png/prompt-engineering
created: 2026-07-18
updated: 2026-07-18
no: 600
category: 二、网文 / 长篇 AI 写作系统 库
repo: srinehapalla1618-png/Prompt-Engineering
stars: 0
url: https://github.com/srinehapalla1618-png/prompt-engineering
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
content_hash: 9533d9deb610775a
  - methods/最强写作方法论_全球最强综合版.md
---

# srinehapalla1618-png/Prompt-Engineering

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/srinehapalla1618-png/prompt-engineering
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Prompt writing and golden-answer authoring for frontier AI training
- **本地描述**：Prompt writing and golden-answer authoring for frontier AI training
- **拉取时间**：2026-07-23 22:56:33

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Prompt Engineering & Golden-Answer Authoring

Hey, I'm Srineha. This repo covers how I approach writing prompts and golden answers for frontier AI training — mostly frontend engineering tasks, but the same thinking applies across reasoning, business, and multi-domain work.

## What "good prompt writing" actually means here

A prompt for AI training isn't just a question — it's a self-contained task with a clear, verifiable correct answer attached. If the golden answer is ambiguous or the prompt allows multiple valid interpretations, the whole training signal gets noisy. My job is to close those gaps before they ever reach a reviewer.

## What I actually do

- **Write realistic, self-contained prompts** — tasks that read like something a real user would ask, not artificially simplified test cases
- **Author golden answers** — the verified "correct" response a model's output gets compared against
- **Apply different prompting strategies** depending on the task — chain-of-thought for multi-step reasoning, few-shot examples when a model needs pattern grounding, zero-shot when I'm testing raw capability
- **Cover interactive, code-heavy tasks** — web apps, simulations, games, UI-driven tools in JavaScript, TypeScript, React, and Vanilla JS

## How I approach writing a prompt

1. Start with a real-world scenario, not an abstract instruction — realistic prompts surface realistic model failures
2. Make sure there's exactly one defensible "correct" answer, or a clearly bounded set of acceptable ones
3. Write the golden answer *before* finalizing the prompt wording — if I can't cleanly write the correct answer, the prompt needs rework
4. Stress-test the prompt myself: could this be misread in a way I didn't intend? If yes, tighten the wording

## Prompting strategies I use

- **Chain-of-thought** — when the task needs visible step-by-step reasoning to be gradable
- **Few-shot** — when a model needs 2-3 examples to understand the expected format or pattern
- **Zero-shot** — when I want to test whether a model can generalize without hand-holding

## Some numbers

- Authored 150+ frontend prompts and golden-answer pairs for frontier LLM training
- Designed prompts and rubrics evaluating reasoning, instruction adherence, and task completion across 5+ concurrent evaluation workflows
- Maintained consistent quality scores through calibrated, well-evidenced prompt design

## Skills

Prompt Engineering · Golden-Answer Authoring · Chain-of-Thought Prompting · Few-Shot & Zero-Shot Prompting · Frontend Task Design (React, TypeScript, JavaScript)
