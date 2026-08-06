---
id: tool-05588
type: tool
area: 库
status: active
tags: [提示词, 协议宽松, 本地优先, 英文文档, 多Agent, 本地写作]
title: ai-slop-detector
summary: 提示词/写作工作流
source: https://github.com/gevayu/ai-slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5588
category: 一、去 AI 味 / Humanizer 库
repo: gevayu/ai-slop-detector
stars: 0
url: https://github.com/gevayu/ai-slop-detector
tier: "C"
use_case: "提示词/写作工作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# gevayu/ai-slop-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/gevayu/ai-slop-detector
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：ai-slope-detecter
- **本地描述**：ai-slope-detecter
- **拉取时间**：2026-07-25 18:24:15

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Slop Detector

A complete guide for producing content, code, and design that doesn't look or read like default AI output.

The slop comes from **mode collapse** and **distributional convergence**: when given a vague prompt, the model samples from the high-probability statistical center of its training data. The fix is always the same shape — inject specificity, constraint, and human context until the model has no choice but to leave the center.

## What's in here

- **[SKILL.md](https://github.com/gevayu/ai-slop-detector/blob/main/SKILL.md)** — the full skill: workflow, domain-specific guides (writing, visual, design, web, social), red-flag vocabulary list, pre-delivery checklist, and reusable prompt templates (English + Hebrew).

## How to use

### As a Claude / ChatGPT skill

Drop the contents of `SKILL.md` into your system prompt, custom instructions, or skill folder. The model will apply anti-slop constraints to anything you generate.

### As a prompt template

Skip to [Reusable Anti-Slop Prompt Template](https://github.com/gevayu/ai-slop-detector/blob/main/SKILL.md#reusable-anti-slop-prompt-template). Paste the compact version before any content request.

### As a checklist

Use [Pre-delivery Checklist](https://github.com/gevayu/ai-slop-detector/blob/main/SKILL.md#pre-delivery-checklist) as a manual review pass on AI-generated content before you publish.

## Coverage

- Writing & copy (blog, marketing, emails, READMEs)
- Visual (image and video generation)
- Design & UI (typography, color, layout, components)
- Web & landing pages (SEO, conversion, trust signals)
- Social (LinkedIn and short-form)
- Both English and Hebrew patterns

## License

MIT.
