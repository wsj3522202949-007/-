---
id: tool-05256
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai_text_detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/mpcodx/ai_text_detector
created: 2026-07-18
updated: 2026-07-18
no: 5256
category: 一、去 AI 味 / Humanizer 库
repo: mpcodx/ai_text_detector
stars: 0
url: https://github.com/mpcodx/ai_text_detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# mpcodx/ai_text_detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/mpcodx/ai_text_detector
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：mpcodx/ai_text_detector
- **拉取时间**：2026-07-25 18:11:50

---

# Hybrid AI Text/Code Detector (Offline)

A lightweight **offline AI detector** that analyzes text and code files to determine if they are **AI-generated** or **human-written**. Works without internet or API keys and supports multiple file formats including `.txt`, `.pdf`, `.docx`, `.py`, `.js`, `.html`, `.json`, `.md`, and `.csv`.

---

## Features

- ✅ Fully **offline** and **free** to use  
- ✅ Detects **AI-generated text and code**  
- ✅ **Hybrid detection** using heuristics + lightweight ML model  
- ✅ **Supports multiple file formats**: `.txt`, `.pdf`, `.docx`, `.py`, `.js`, `.html`, `.json`, `.md`, `.csv`  
- ✅ **GUI interface** with file/folder selection, progress bar, and detailed results  
- ✅ Lightweight: uses **scikit-learn** and **pickle**, no heavy transformer models required  

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MPByte/ai_text_detector
cd ai_text_detector
