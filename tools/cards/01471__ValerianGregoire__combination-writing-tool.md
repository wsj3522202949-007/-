---
id: tool-01471
type: tool
area: 库
status: active
tags: [Python, 协议传染, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: combination-writing-tool
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/valeriangregoire/combination-writing-tool
created: 2026-07-18
updated: 2026-07-18
no: 1471
category: 二、网文 / 长篇 AI 写作系统 库
repo: ValerianGregoire/combination-writing-tool
stars: 0
url: https://github.com/valeriangregoire/combination-writing-tool
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# ValerianGregoire/combination-writing-tool

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/valeriangregoire/combination-writing-tool
- **Stars**：0
- **语言**：Python
- **License**：GPL-3.0
- **Topics**：—
- **GitHub 描述**：A combination writing assistant for the game Tekken 7.
- **本地描述**：A combination writing assistant for the game Tekken 7.
- **拉取时间**：2026-07-23 23:21:59

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Tekken_combo_writer
## Quick program to write and save combos for Tekken 7

### How I got the Idea
Learning combos in arcade fighting games may be tough, especially when they are kept in a dark .txt file that no one can decode.
I've been looking for a way to write my combos quickly while I trained, but couldn't find any website that allowed me to do it the way I would have liked to do it, which was a good reason for me to code an app that does the job.

### What's the point of this app ?
It's an efficient way to type custom combos and to save them on your computer.
Also, I used PIL (from pillow library), which was a first for me. Projects like those are a good way to discover new libraries.

### How do I type my combos ?
The rules are simple:
> Each sequence is separated from the others by a space

> The directions are: f (forward), b (backward), u (up), d(down). You can combine them by first inputing up or down then forward or backward (e.g., uf or db)

> Hold directions are written with capital letters

> Attack buttons are 1,2,3,4 and the combinations are expressed with a "+" (e.g., 1+3).

An input like this:
![image](https://user-images.githubusercontent.com/96045631/235797848-2591b8a8-0b2a-4eaf-82ba-fe01dcc3d69a.png)

Outputs this:
![image](https://user-images.githubusercontent.com/96045631/235797909-fedd7083-18ca-4876-bcdd-86584b208cc6.png)

#### The Display Text option is to display which input led to which icon if you'd rather use this notation

Also, you can save your combos in the combos folder of the project to have a quick access to the combos you want to train on. 
