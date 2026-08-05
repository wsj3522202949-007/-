---
id: tool-04999
type: tool
area: 库
status: active
tags: [TTS, 协议未明, 本地优先, 英文文档, 本地写作]
title: slop-remover
summary: 小说转语音/有声书
source: https://github.com/write-with-ai/slop-remover
created: 2026-07-18
updated: 2026-07-18
no: 4999
category: 一、去 AI 味 / Humanizer 库
repo: write-with-ai/slop-remover
stars: 0
url: https://github.com/write-with-ai/slop-remover
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# write-with-ai/slop-remover

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/write-with-ai/slop-remover
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Claude skill that audits academic papers line by line for AI slop and fixes it.
- **本地描述**：Claude skill that audits academic papers line by line for AI slop and fixes it.
- **拉取时间**：2026-07-25 18:02:27

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# slop-remover

Claude skill that audits academic papers line by line for AI slop and fixes it. Checks sentence overload, em dashes, passive voice, AI vocabulary, tense consistency, terminology drift, math notation, structural issues, and claims-evidence gaps. Grades innovation on five dimensions and flags papers that shouldn't be submitted.

Developed by analyzing writing patterns in top theoretical CS papers, then generalizing across paper types.

## Installation

Drop `paper-slop-remover/` into your Claude skills directory.

```
paper-slop-remover/
└── SKILL.md
```

## License

[CC BY 4.0](LICENSE) — use it however you want, just credit [Madhava Gaikwad](https://github.com/write-with-ai).
