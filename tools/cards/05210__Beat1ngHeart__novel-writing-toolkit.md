---
id: tool-05210
type: tool
area: 库
status: active
tags: [Claude插件, 协议未明, 本地优先, 英文文档, 本地写作]
title: novel-writing-toolkit
summary: Claude Code 插件式写作流
source: https://github.com/beat1ngheart/novel-writing-toolkit
created: 2026-07-18
updated: 2026-07-18
no: 5210
category: 一、去 AI 味 / Humanizer 库
repo: Beat1ngHeart/novel-writing-toolkit
stars: 0
url: https://github.com/beat1ngheart/novel-writing-toolkit
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Beat1ngHeart/novel-writing-toolkit

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/beat1ngheart/novel-writing-toolkit
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Claude Code Custom Skills: AI-Assisted Web Novel Writing (7 Golden Rules + Anti-AI Detection + Platform Adaptation + Data Feedback Loop)
- **本地描述**：Claude Code Custom Skills: AI-Assisted Web Novel Writing (7 Golden Rules + Anti-AI Detection + Platform Adaptation + Data Feedback Loop)
- **拉取时间**：2026-07-25 18:10:10

---

<div align="center">

# Novel Writing Toolkit

**AI-Powered Commercial Web Novel Writing System for Claude Code**

一套基于 Claude Code 的商业网文写作系统 — 从选题到投稿的完整 AI 辅助工序

[![Platform](https://img.shields.io/badge/platform-Claude%20Code-blue?style=flat-square)](https://claude.ai/code)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Language](https://img.shields.io/badge/language-中文%20|%20English-orange?style=flat-square)](#-quick-start)

**English** | **[中文](#-简介)**

</div>

---

## Quick Start

Three custom slash commands for Claude Code — covering the entire novel production pipeline from concept to submission.

| Command | Purpose |
|---------|---------|
| `/novel` | **Main Hub** — Draft generation, revision/de-AI-ification, quality self-check, submission packaging, data analysis |
| `/novel-plan` | **Writer's Workshop** — Full pre-production: concept, outline, character design, worldbuilding |
| `/novel-topic` | **Topic Analysis** — Genre evaluation, platform matching, chart data analysis |

### Installation

Copy the files from `.claude/commands/` into your project's `.claude/commands/` directory. The slash commands will be available immediately in Claude Code.

### Core Features

**7 Iron Rules of Writing** — Sentence rhythm, zero emotion labeling, dialogue purity, personalized metaphor, unpredictable paragraphing, imperfect protagonists, anti-AI detection

**Anti-AI Detection System** — Systematic correction across regression-to-mean, parallel structure, hollow sentences, high-frequency word patterns, and 7 additional dimensions

**Platform Adaptation** — Differentiated rules for Qimao (Male/Female), Tomato (Short Story/Serialization), and Qidian (Male Frequency)

**Real Author Workflow** — 11-step production pipeline: topic selection → concept → outline → characters → sample chapters → revision → submission

**Data Feedback Loop** — Submission data collection → attribution analysis → parameter adjustment → next generation cycle

### Architecture

```
Novel Writing Toolkit/
├── .claude/commands/
│   ├── novel.md          # Main skill: all iron rules + writing rules integrated
│   ├── novel-plan.md     # Concept skill: author-style pre-production
│   └── novel-topic.md    # Topic skill: genre evaluation + platform matching
└── README.md
```

---

## 简介

三支 Claude Code 自定义斜杠命令，覆盖从选题构思到投稿发布的完整商业网文生产链路。

| 命令 | 功能 |
|------|------|
| `/novel` | **主入口** — 正文生成、改稿/去 AI 化、质量自检、投稿包装、数据分析 |
| `/novel-plan` | **作家式构思** — 长篇/短篇完整前置构思流程：创意、大纲、人设、世界观 |
| `/novel-topic` | **选题分析** — 题材评估、平台匹配、榜单数据参考 |

### 安装

将 `.claude/commands/` 目录下的文件复制到你项目的 `.claude/commands/` 中，即可在 Claude Code 中通过 `/novel` 等斜杠命令直接调用。

### 核心特性

**7 条写作铁律** — 句长参差、禁止情绪标注、对白不承载设定、比喻个性化、段落不可预测、主角不完美、反 AI 痕迹

**反 AI 痕迹体系** — 基于均值回归、排比结构、空心句、高频词等 11 个维度的系统性检测与修正，附带 38 条高频禁用词速查表

**平台适配** — 七猫女频/男频、番茄短故事/连载、起点男频的差异化写作规则

**作家式流程** — 11 步完整工序：选题 → 构思 → 大纲 → 人物 → 样章 → 改稿 → 投稿

**数据闭环** — 投稿数据回收 → 归因分析 → 模型调参 → 下一轮生成

### 目录结构

```
Novel Writing Toolkit/
├── .claude/commands/
│   ├── novel.md          # 主技能：集成全部铁律和写作规则
│   ├── novel-plan.md     # 构思技能：作家式新书前置流程
│   └── novel-topic.md    # 选题技能：题材评估和平台匹配
└── README.md
```

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

<div align="center">

**Built for writers who ship.**

</div>
