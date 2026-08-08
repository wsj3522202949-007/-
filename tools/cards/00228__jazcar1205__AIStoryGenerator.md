---
id: tool-00228
type: tool
area: 库
status: active
tags: [Java, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: AIStoryGenerator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/jazcar1205/aistorygenerator
created: 2026-07-18
updated: 2026-07-18
no: 228
category: 二、网文 / 长篇 AI 写作系统 库
repo: jazcar1205/AIStoryGenerator
stars: 1
url: https://github.com/jazcar1205/aistorygenerator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 186ccf8243794442
  - methods/最强写作方法论_全球最强综合版.md
---

# jazcar1205/AIStoryGenerator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/jazcar1205/aistorygenerator
- **Stars**：1
- **语言**：Java
- **License**：None
- **Topics**：—
- **GitHub 描述**：The Interactive Storytelling Application is an AI-powered platform that creates unique stories based on user input. Users can choose genres, design characters and worlds, and customize writing style or length.
- **本地描述**：The Interactive Storytelling Application is an AI-powered platform that creates unique stories based on user input. Users can choose genres, design characters and worlds, and customize writing style or length.
- **拉取时间**：2026-07-23 22:45:43

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI Story Generator

## Team Members
- Jazmin Carlos 
- Cedar Hudgens 

## Demo Link
- Check in Demo: https://www.youtube.com/watch?v=kytr02STaDs
- Final Demo: https://www.youtube.com/watch?v=EDmgZXrFrrE

## Project Description
The Interactive Storytelling Application uses AI to create stories based on what the user writes or chooses. Users can pick a genre, make characters, and shape the world of their story. The app can build different types of stories and let users save or export them.

## Features Implemented
- [x] Genre selection (Horror, Romance, Fantasy, SciFi)
- [x] Save / export stories
- [x] Length Selection (Short, Medium, Long)
- [x] Complexity selection (Child friendly, Average, Difficult)
- [x] Pace selection (Slow, Normal, Fast)
- [x] Perspective selection (1st or 3rd)
- [x] Added Prompts for Setting, Tone, Time Period
- [x] Ability to ask for specific characters
- [x] Fully functional GUI

## Design Patterns Used
1. **Strategy Pattern** - Multiple story generation strategies. 
   - Horror, Romance, Fantasy, SciFi
2. **Factory Pattern** - Centralizes the creation of StoryStrategy objects based on the user's selected genre (e.g., automatically creates a FantasyStrategy instance when 'Fantasy' is chosen).
3. **Observer Pattern** - Ui updates when story and/ or model changes
3. **Singleton Pattern** - Configuration manager or API rate limiter

## Setup Instructions
1. Get API key from Open API
2. Update "sample.config.properties" with the API key and API URL. 
3. Change name to "config.properties"

### Prerequisites
- Java 11 or higher
- Dependencies:
  - org.json (20231013)
  - okhttp 4.12.0
  - JUnit 4.13 (unit tests)
  - Mockito 5.21.0 (unit tests)
- OpenAI API key

### Installation (Intellij - Terminal)
1. Clone repository
2. Edit sample.config.properties as described above.
2. Go To main.java.TerminalTest
3. Run  the current file

### Installation (Intellij - GUI) 
1. Clone repository
2. Edit sample.config.properties as described above.
2. Go To main.java.Main
3. Run  the current file

