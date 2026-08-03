---
id: tool-00824
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Dialogue-Editor
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/boyquotes/dialogue-editor
created: 2026-07-18
updated: 2026-07-18
no: 824
category: 二、网文 / 长篇 AI 写作系统 库
repo: Boyquotes/Dialogue-Editor
stars: 0
url: https://github.com/boyquotes/dialogue-editor
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Boyquotes/Dialogue-Editor

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/boyquotes/dialogue-editor
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Software for creating storyboards and visual novels
- **本地描述**：Software for creating storyboards and visual novels
- **拉取时间**：2026-07-23 23:03:04

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Dialogue Editor

Software for creating storyboards and visual novels.

I originally made it for the story writers of a murder mystery visual novel. It was meant to make it easier for them to structurise the story, as well as make the data directly transferable to the project, thus making it easier for the programming team to implement.



## To-Do

- Fix the expression that calculates the position of new nodes

  - I found the line with the problem, and I have a general idea of whats wrong, just not exactly sure what to change

  - It's an expression with 4 variables that calculates some position

  - I have to figure out what variables have to be changed to their global equivalent

- Make a version for MacOS

  - Not sure why I haven't done this yet

- Remove every feature related to "clues" as it's not a universally needed feature.

  - The dedicated tab

  - Node that adds clues

  - Node that lets you use clues

