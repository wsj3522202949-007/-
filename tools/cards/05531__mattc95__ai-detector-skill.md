---
id: tool-05531
type: tool
area: 库
status: active
tags: [去AI味, 协议未明, 本地优先, 英文文档, 本地写作]
title: ai-detector-skill
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/mattc95/ai-detector-skill
created: 2026-07-18
updated: 2026-07-18
no: 5531
category: 一、去 AI 味 / Humanizer 库
repo: mattc95/ai-detector-skill
stars: 1
url: https://github.com/mattc95/ai-detector-skill
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 4f362bf347f12714
  - methods/改稿润色指令库.md
---

# mattc95/ai-detector-skill

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/mattc95/ai-detector-skill
- **Stars**：1
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：An OpenClaw skill that classifies text as human, AI, AI-humanized, or light-edited using the GPTHumanizer detection API.
- **本地描述**：An OpenClaw skill that classifies text as human, AI, AI-humanized, or light-edited using the GPTHumanizer detection API.
- **拉取时间**：2026-07-25 18:22:08

---

# GPTHumanizer AI Detector Skill for OpenClaw

🌐 **Official Website:** [GPTHumanizer](https://www.gpthumanizer.ai/)

[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://github.com/openclaw/openclaw)
[![ClawHub](https://img.shields.io/badge/ClawHub-Live-brightgreen)](https://clawhub.ai/mattc95/ai-detector)
[![API](https://img.shields.io/badge/API-GPTHumanizer-orange)](./api.md)
[![License](https://img.shields.io/badge/License-MIT--0-lightgrey)](#license)

A professional OpenClaw skill for detecting whether text is likely **human-written**, **AI-generated**, **AI-humanized**, or **lightly edited** using the **GPTHumanizer Detection API**.

Designed for lightweight deployment, clean skill packaging, and straightforward publishing to ClawHub.

---

## Overview

This repository provides a production-ready OpenClaw skill package for AI text detection.

It is useful for:

- AI text review workflows
- moderation and quality screening
- pre-submission writing checks
- editorial and compliance analysis
- OpenClaw skill pipelines that need fast classification + probability scoring

The skill returns:

- a final classification label
- aggregated AI-likelihood
- per-class probability distribution
- original input text

---

## Why this repository

OpenClaw skills are distributed as simple folders centered around a `SKILL.md` file, optionally with supporting files. This repository follows that model and keeps the package minimal, readable, and easy to publish. It is well suited for users who want a clean, standalone skill instead of a large plugin or monolithic integration.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Repository Structure

```text
.
├── SKILL.md
├── api.md
└── examples.md
