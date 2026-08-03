---
id: tool-00266
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: novel-writing-toolkit
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/qwerty5826/novel-writing-toolkit
created: 2026-07-18
updated: 2026-07-18
no: 266
category: 二、网文 / 长篇 AI 写作系统 库
repo: QWERTY5826/novel-writing-toolkit
stars: 1
url: https://github.com/qwerty5826/novel-writing-toolkit
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# QWERTY5826/novel-writing-toolkit

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/qwerty5826/novel-writing-toolkit
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：网文写作工具包 - 写作流程指南 + 反AI检测脚本
- **本地描述**：网文写作工具包 - 写作流程指南 + 反AI检测脚本
- **拉取时间**：2026-07-23 22:46:49

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 网文写作工具包

一个面向网络小说作者的写作辅助工具包，包含格式规则、写后检查清单和反AI检测脚本。

## 文件说明

- `写作流程.md` — 完整的写作流程指南，包含格式规则、每章检查清单、避坑指南
- `反AI检测脚本.py` — 基于 AI-Novel-Writing-Assistant 规则的反AI特征检测脚本

## 使用方式

1. 看完 `写作流程.md`，按步骤走
2. 写完章节后运行检测：
   ```bash
   python 反AI检测脚本.py 你的章节.md
   ```
3. 根据检测报告修A类违规，B/C类建议修正

## 反AI检测报告分级

- **A类（禁止型）** — 必须修正（如"他感到""他意识到"等解释型心理描写、段尾升华、总结主题等）
- **B类（风险型）** — 建议修正（段落整齐度、连续纯叙述段等）
- **C类（鼓励型）** — 缺失提示，建议补充（无意义小动作、现实落差、嘴硬台词等）

## 规则来源

反AI检测脚本的12条检测规则来源于 [AI-Novel-Writing-Assistant](https://github.com/) 的反AI特征库，规则冻结，一字不改。

## License

MIT
