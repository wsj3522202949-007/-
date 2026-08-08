---
id: tool-01356
type: tool
area: 库
status: active
tags: [校对, 协议未明, 本地优先, 英文文档, 改稿润色, 本地写作]
title: profile-quality-scorer
summary: 错别字/语法/风格校对
source: https://github.com/objectiveai-claude-code-1/profile-quality-scorer
created: 2026-07-18
updated: 2026-07-18
no: 1356
category: 二、网文 / 长篇 AI 写作系统 库
repo: ObjectiveAI-claude-code-1/profile-quality-scorer
stars: 0
url: https://github.com/objectiveai-claude-code-1/profile-quality-scorer
tier: "C"
use_case: "错别字/语法/风格校对"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 29cc42b3c98b90f3
  - methods/最强写作方法论_全球最强综合版.md
---

# ObjectiveAI-claude-code-1/profile-quality-scorer

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/objectiveai-claude-code-1/profile-quality-scorer
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：ObjectiveAI Function that evaluates dating profile quality. Scores photo technical quality, bio writing quality, profile completeness, and overall effort. Returns a score in [0,1].
- **本地描述**：ObjectiveAI Function that evaluates dating profile quality. Scores photo technical quality, bio writing quality, profile completeness, and overall effort. Returns a score in [0,1].
- **拉取时间**：2026-07-23 23:18:39

---

# profile-quality-scorer

An [ObjectiveAI](https://objectiveai.co) Function that evaluates individual dating profile quality in isolation.

## Overview

This is a **scalar function** that takes a dating profile as input and returns a single quality score in **[0, 1]**, where higher scores indicate better quality profiles.

The function does **not** judge attractiveness — only presentation quality and effort.

## Input

| Field | Type | Required | Description |
|-------|------|----------|----------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| `profile_pictures` | array of images | Yes | Profile photos to evaluate (at least 1) |
| `bio` | string | Yes | The profile bio text |
| `name` | string | No | Display name |
| `age` | integer | No | Age in years |
| `occupation` | string | No | Occupation or job title |
| `interests` | array of strings | No | List of interests or hobbies |

## Evaluation Dimensions

The function uses 4 vector completion tasks to assess profile quality:

1. **Photo Technical Quality** — Clarity, lighting, composition, resolution, and variety of the profile photos.
2. **Bio Writing Quality** — Grammar, spelling, length appropriateness, substance, personality, and tone.
3. **Profile Completeness** — Whether optional fields are filled with substantive content.
4. **Overall Effort & Presentation** — Holistic assessment of photo variety, text-image coherence, and curation quality.

Each task uses a 5-level ordinal scale mapped to scores:
- Excellent/Exceptional: 1.0
- Good/Above Average: 0.75
- Adequate/Average: 0.5
- Poor/Below Average: 0.25
- Very Poor/Minimal: 0.0

## Output

A single floating-point score in [0, 1] representing the weighted average across all 4 evaluation dimensions.

## Usage

```bash
# Build and test
ts-node build.ts

# Commit and push
ts-node commitAndPush.ts "commit message"
```

## License

Proprietary — ObjectiveAI
