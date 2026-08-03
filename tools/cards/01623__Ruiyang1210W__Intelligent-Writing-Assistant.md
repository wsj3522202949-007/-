---
id: tool-01623
type: tool
area: 库
status: active
tags: [TTS, Java, 协议宽松, 需API密钥, 英文文档]
title: Intelligent-Writing-Assistant
summary: 小说转语音/有声书
source: https://github.com/ruiyang1210w/intelligent-writing-assistant
created: 2026-07-18
updated: 2026-07-18
no: 1623
category: 二、网文 / 长篇 AI 写作系统 库
repo: Ruiyang1210W/Intelligent-Writing-Assistant
stars: 0
url: https://github.com/ruiyang1210w/intelligent-writing-assistant
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Ruiyang1210W/Intelligent-Writing-Assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ruiyang1210w/intelligent-writing-assistant
- **Stars**：0
- **语言**：Java
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A writing tool integrates the OpenAI that focusing on areas like Job Cover letter, Statements of Purposes, essays with more human-sounding.
- **本地描述**：A writing tool integrates the OpenAI that focusing on areas like Job Cover letter, Statements of Purposes, essays with more human-sounding.
- **拉取时间**：2026-07-23 23:26:22

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Intelligent Writing Assistant

## Team Members
- Ruiyang Wang (016087383)
- Colin Shiung (017426461)

## Project Description
A writing tool integrates the OpenAI API, focusing on areas like Job Cover letters, Statements of Purposes, and essays, making them more Profession, Academic, or Creative.

## Features Implemented
- [x] Creative mode, Professional mode, Academic mode
- [x] MVC Architecture
- [x] API integration
- [x] Junit Tests 28 passed
- [x] Swing GUI

## Design Patterns Used
1. **Strategy Pattern** - Different writing modes
2. **Factory Pattern** - Request creation
3. **Observer Pattern** - UI 

## Setup Instructions
1. Get API key from https://platform.openai.com/
2. `export API_KEY=your_key`
3. Go to https://cloud.google.com/text-to-speech and click "Try Text to Speech"
4. Enable TTS for your project
5. Install Google Cloud from CLI https://docs.cloud.google.com/sdk/docs/install
6. run `gcloud auth application-default login` in Command Prompt and log into Google
7. Select the Google Cloud project that enabled Text-To-Speech API
8. Run Main.java

### Prerequisites
- Java 11 or higher
- OpenAI API key
- Google Account & Google Cloud API Access

### Installation
1. Clone repository
2. `export API_KEY="your-key"`
3. Run `Main.java`

### Dependencies
- org.json (version)
- JUnit 5.10.1


## API Usage & Costs
- Model used: gpt-3.5-turbo
- Estimated cost per request: $0.002
- Cost management strategies

**Cloud Text-to-Speech API**
- Estimated cost per request: $0 for the first 10 million words
- Very cost-effective

## Demo & Code Explanation Video: 
https://youtu.be/jPxafg36wL4

## Future Enhancements
- Multi-language translation
