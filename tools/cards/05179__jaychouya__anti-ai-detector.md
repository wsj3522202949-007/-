---
id: tool-05179
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 中文友好, 去AI味, 本地写作]
title: anti-ai-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/jaychouya/anti-ai-detector
created: 2026-07-18
updated: 2026-07-18
no: 5179
category: 一、去 AI 味 / Humanizer 库
repo: jaychouya/anti-ai-detector
stars: 2
url: https://github.com/jaychouya/anti-ai-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# jaychouya/anti-ai-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/jaychouya/anti-ai-detector
- **Stars**：2
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：一款专为降低学术写作 AI 检测率打造的开源 Skill。它通过智能重构文本结构与用词，在保留核心学术观点的同时，赋予文字更自然、地道的人类表达质感。表达，同时不丢失原文含义。An open-source skill engineered to lower AI detection rates in academic writing. It intelligently restructures text to deliver a natural, human-like tone while strictly preserving the original academic integrity and core arguments.
- **本地描述**：一款专为降低学术写作 AI 检测率打造的开源 Skill。它通过智能重构文本结构与用词，在保留核心学术观点的同时，赋予文字更自然、地道的人类表达质感。表达，同时不丢失原文含义。An open-source skill engineered to lower AI detection rates in academic writing. It intelligently restructures text to deliver a natural, human-like tone while strictly preserving the original academic integrity and core arguments.
- **拉取时间**：2026-07-25 18:09:01

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# jaychouya/anti-ai-detector-skill

[English](https://github.com/jaychouya/anti-ai-detector/blob/main/README.en.md) | [ZH](https://github.com/jaychouya/anti-ai-detector/blob/main/README.zh-CN.md)

`anti-ai-detector` is an open-source skill designed specifically to lower AI-detection risk in academic writing.
It rewrites text to sound more like human expert writing while preserving technical meaning.

## Quick Links

- Main skill: `skill/skills/anti-ai-detector/SKILL.md`
- Install guide: `INSTALL.md`
- Roadmap: `ROADMAP.md`
- Contributing: `CONTRIBUTING.md`
- GitHub repo: [github.com/jaychouya/anti-ai-detector](https://github.com/jaychouya/anti-ai-detector)

## Start in 30 Seconds

```bash
python skill/skills/anti-ai-detector/scripts/check_ai_traces.py path/to/paper.txt
python skill/skills/anti-ai-detector/scripts/check_ai_traces.py path/to/chinese_draft.txt --zh
```
