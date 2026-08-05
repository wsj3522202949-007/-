---
id: tool-01084
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: efootball-stats-automation
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/ann-dobr/efootball-stats-automation
created: 2026-07-18
updated: 2026-07-18
no: 1084
category: 二、网文 / 长篇 AI 写作系统 库
repo: Ann-Dobr/efootball-stats-automation
stars: 0
url: https://github.com/ann-dobr/efootball-stats-automation
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Ann-Dobr/efootball-stats-automation

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ann-dobr/efootball-stats-automation
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：automation, google-sheets, gpt-4o, javascript, n8n, ocr, telegrambot
- **GitHub 描述**：AI-powered workflow for extracting match statistics from screenshots and writing to Google Sheets via n8n
- **本地描述**：AI-powered workflow for extracting match statistics from screenshots and writing to Google Sheets via n8n
- **拉取时间**：2026-07-23 23:10:35

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 🏆 eFootball Match Statistics Automation

Automated workflow for extracting match data from screenshots and writing to Google Sheets.

## 📋 What it does

User sends a series of match screenshots to a Telegram bot (3–8 images).  
The system automatically:
- Recognizes team names, player ratings, goals and match statistics via GPT-4o Vision
- Structures extracted data into JSON
- Maps players and stats to the correct cells in Google Sheets
- Confirms successful upload via Telegram message

## 🛠 Tech Stack

- **n8n** — workflow automation
- **GPT-4o Vision** — OCR and data extraction from images
- **Google Sheets API** — data storage
- **Telegram Bot API** — user interface
- **JavaScript** — data processing and mapping logic

## 📊 Architecture

<img width="1706" height="388" alt="image" src="https://github.com/user-attachments/assets/2f0bcbff-5445-4c66-8353-0e94e52ad5a0" />

## ⚙️ Key Features

- Handles variable number of screenshots per match (3–8 images)
- Aggregates all images before sending to AI (solves Telegram multi-upload issue)
- Smart player name normalization (handles special characters: ä, ö, ü, ñ, ø, č etc.)
- Tour number extraction from free-form text ("Тур 23", "тур-25", "26 тур")
- Safety guard: stops execution if tour number cannot be determined (prevents data corruption)

## 📁 Files
- [`workflow.json`](workflow.json) — n8n workflow export (import directly into your n8n instance)
