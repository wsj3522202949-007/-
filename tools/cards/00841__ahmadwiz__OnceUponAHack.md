---
id: tool-00841
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: OnceUponAHack
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/ahmadwiz/onceuponahack
created: 2026-07-18
updated: 2026-07-18
no: 841
category: 二、网文 / 长篇 AI 写作系统 库
repo: ahmadwiz/OnceUponAHack
stars: 2
url: https://github.com/ahmadwiz/onceuponahack
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 4c322acca379b893
  - methods/最强写作方法论_全球最强综合版.md
---

# ahmadwiz/OnceUponAHack

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ahmadwiz/onceuponahack
- **Stars**：2
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI Story Generator
- **本地描述**：AI Story Generator
- **拉取时间**：2026-07-23 23:03:33

---

## 👥 Team Members (4)
- Ahmad Ibrahim  
- Jonathan Okushi  
- Jonathan Shekoni  
- Uche Onwukeme  

---

## 🎯 Purpose
The purpose of this project was to provide users with a fun, game-like application where they can express their creativity through clever wordplay and compelling storytelling.

---

## 🛠️ Tools Utilized

### Front End
- React  
- Vite  
- Figma  

### Back End
- Python  
- Flask  

### Additional Tools
- AI (support role for both Front & Back End)
- Vercel (Hosting)
- Render (Hosting)

---

## 🔌 APIs Used
- OpenAI  
- Gemini  
- Herokuapp  
- ElevenLabs  

---

## ⚠️ Problems Encountered & Solutions

### 🖼️ Problem 1: Figma Image Resizing Issues  
**Problem:** We experienced difficulties when trying to properly resize images in Figma for our front-end design.  

**Solution:** Instead of relying heavily on Figma for the full front-end layout, we used its stylistic components as a design reference and implemented similar designs directly using HTML and CSS.

---

### ⏳ Problem 2: Image Generation Lag  
**Problem:** Waiting for Gemini to generate images caused the entire application to hang and lag.  

**Solution:** We implemented parallel processing to generate and wait for images independently, allowing the rest of the application’s functionality to continue running smoothly.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

### 🌐 Problem 3: Hosting Under a .tech Domain  
**Problem:** One of our biggest challenges was figuring out how to host our website under a `.tech` domain.  

**Solution:** With guidance from our hackathon organizers, we learned how to properly deploy our application using the Render and Vercel platforms.
