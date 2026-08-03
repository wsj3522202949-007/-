---
id: tool-05564
type: tool
area: 库
status: active
tags: [互动叙事, 协议宽松, 本地优先, 英文文档, 本地写作]
title: ai-slop-detector
summary: 互动叙事/聊天写故事
source: https://github.com/siliconsnark/ai-slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5564
category: 一、去 AI 味 / Humanizer 库
repo: siliconsnark/ai-slop-detector
stars: 2
url: https://github.com/siliconsnark/ai-slop-detector
tier: "B"
use_case: "互动叙事/聊天写故事"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# siliconsnark/ai-slop-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/siliconsnark/ai-slop-detector
- **Stars**：2
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A reusable prompt checklist for detecting AI slop in chatbot output, summaries, plans, and drafts.
- **本地描述**：A reusable prompt checklist for detecting AI slop in chatbot output, summaries, plans, and drafts.
- **拉取时间**：2026-07-25 18:23:22

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Slop Detector

AI Slop Detector is a reusable prompt checklist for reviewing AI-generated writing, summaries, plans, code explanations, product copy, and chatbot answers.

It does not try to answer the increasingly boring question, "was this made by AI?" Instead, it asks the useful one: is this output grounded, specific, checkable, and worth trusting?

## What It Checks

AI Slop Detector scores output across 10 factors:

1. Commitment
2. Load-bearing specifics
3. Rhythm
4. Substance over structure
5. Checkable claims
6. The weird part
7. Timeliness and contact with reality
8. Taste and discrimination
9. Job clarity
10. Challenge survival

Each factor is scored from 0 to 2, producing a total score out of 20 and a Low, Medium, or High slop-risk rating.

## Quick Start

Download [`ai-slop-detector.md`](ai-slop-detector.md), paste the file into Claude Cowork, Codex, ChatGPT, or your favorite chatbot, then either a) save it as a skill or b) insert the output you want reviewed under `Text To Review`.

The detector asks the model to return:

- A score out of 20
- A slop-risk rating
- Factor-by-factor scores
- The 3 biggest problems
- The 3 most useful fixes
- A replacement version when rewriting makes sense

## Why This Exists

AI-generated output often looks finished before it is good. It has headings, bullet points, balance, confidence, and the faint scent of a quarterly planning memo. That polish can hide weak claims, generic prose, missing evidence, template thinking, and conclusions that never quite decide anything.

This prompt is a review layer. It is meant to help humans catch blandness, vagueness, false confidence, and content-shaped foam before it ships.

## Example Use Cases

- Reviewing a chatbot answer before publishing it
- Checking AI-written product copy for generic sludge
- Auditing an AI-generated research summary for missing evidence
- Tightening a draft article or blog post
- Reviewing AI-generated meeting summaries
- Testing whether a coding-agent explanation actually understood the code
- Helping a team define what "good AI output" should mean

## Slop Risk Guide

- `Low`: Specific, grounded, useful, and clear about uncertainty
- `Medium`: Some useful work, but generic, under-evidenced, or under-committed in places
- `High`: Smooth, confident, vague, and probably wearing loafers

## Files

- [`ai-slop-detector.md`](ai-slop-detector.md): the reusable prompt
- [`LICENSE`](LICENSE): MIT license

## Attribution

Created by SiliconSnark / CircuitSmith as a practical companion to the SiliconSnark essay on spotting AI slop.

## License

MIT. Use it, fork it, remix it, paste it into your chatbot, and make the beige soup less beige.
