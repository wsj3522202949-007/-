---
id: tool-01207
type: tool
area: 库
status: active
tags: [Claude插件, 协议未明, 需API密钥, 中文友好]
title: genstory-agent
summary: Claude Code 插件式写作流
source: https://github.com/muryanice/genstory-agent
created: 2026-07-18
updated: 2026-07-18
no: 1207
category: 二、网文 / 长篇 AI 写作系统 库
repo: MuRyanice/genstory-agent
stars: 0
url: https://github.com/muryanice/genstory-agent
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# MuRyanice/genstory-agent

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/muryanice/genstory-agent
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：ai story generator skills
- **本地描述**：ai story generator skills
- **拉取时间**：2026-07-23 23:14:16

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# genstory-agent

English | [中文](https://github.com/MuRyanice/genstory-agent/blob/main/README.zh.md)

Genstory public skill repository.

This repository currently publishes the `genstory-story-generator` skill for connecting external workflows to Genstory story generation.

## Install

### Standard install via skills.sh

```bash
npx skills add MuRyanice/genstory-agent
```

### Register marketplace

```bash
/plugin marketplace add MuRyanice/genstory-agent
```

### Install from marketplace

```bash
/plugin install genstory-agent@genstory-agent
```

### Or copy the skill directly

```bash
curl -fsSL https://www.genstory.app/api/skills/genstory-story-generator/skill-md
```

Once installed, read the `SKILL.md` file in the installed directory and follow its instructions to complete the task.

## Included skill

- `skills/genstory-story-generator`
  - Submit story tasks to Genstory with `GENSTORY_API_KEY`
  - Poll task status from Genstory
  - Return the hosted story URL and cover image

## API key

Users should create their API key in Genstory user center:

- `https://www.genstory.app/my-api-keys`
