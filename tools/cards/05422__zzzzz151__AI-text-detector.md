---
id: tool-05422
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-text-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/zzzzz151/ai-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5422
category: 一、去 AI 味 / Humanizer 库
repo: zzzzz151/AI-text-detector
stars: 4
url: https://github.com/zzzzz151/ai-text-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# zzzzz151/AI-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/zzzzz151/ai-text-detector
- **Stars**：4
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：zzzzz151/AI-text-detector
- **拉取时间**：2026-07-25 18:18:02

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Text Detector - Project for Projeto em Informática 2023

# Team

Alexandre Gazur (102751)

Daniel Ferreira (102885)

Ricardo Pinto (103078)

# Project website

https://zzzzz151.github.io/AI-text-detector/

# Abstract

Our project is an AI Text Detector as a Chrome browser extension.

Whenever you open a web page or PDF in your browser, it will evaluate for AI generated text in it.

It will display an overall evaluation, highlight parts of the text that it considers is probably AI generated, and you can also select any text and evaluate it.

With Mozilla's PDF viewer, it even works on PDFs!

The extension has a thorough and intuitive UI that lets you select the model, highlighting colors, and other settings. It also has buttons that redirect the user to our Model Hub and to Mozilla's PDF Viewer, for easy navigation. Finally, the extension UI also has a text area for the user to write any text and analyse it.

Users can also add their own AI text detector model to our system through our Model Hub, be it as a python script or as an API, making the model available to all users.

# [Video](https://www.youtube.com/watch?v=QulxLQb4c70)

# How to run

To load the extension, in ai4-td-extension folder, run

`npm install`

`npm run dev`

The browser extension is compiled into ai4-td-extension/build/chrome-mv3-dev, load it as unpacked extension in the browser (with npm terminal running)

To launch the backend, have Docker Desktop running and run run.bat in CMD with

`run`

You can add models in our Model Hub at localhost:8000/model-hub


