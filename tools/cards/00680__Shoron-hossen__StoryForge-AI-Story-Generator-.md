---
id: tool-00680
type: tool
area: 库
status: active
tags: [Dart, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: StoryForge-AI-Story-Generator-
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/shoron-hossen/storyforge-ai-story-generator-
created: 2026-07-18
updated: 2026-07-18
no: 680
category: 二、网文 / 长篇 AI 写作系统 库
repo: Shoron-hossen/StoryForge-AI-Story-Generator-
stars: 0
url: https://github.com/shoron-hossen/storyforge-ai-story-generator-
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Shoron-hossen/StoryForge-AI-Story-Generator-

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/shoron-hossen/storyforge-ai-story-generator-
- **Stars**：0
- **语言**：Dart
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：Shoron-hossen/StoryForge-AI-Story-Generator-
- **拉取时间**：2026-07-23 22:58:52

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Story Generator
Story Generator is a mobile app that generates random stories based on user input. The app is built using Flutter, a cross-platform mobile development framework by Google.

## Features
- **Animations**: Use of *animated_text_kit* to animate text widget.
- **Responsive Design**: The app is responsive across screen sizes.
- **Generative AI**: The app uses a generative model to generate stories based on user input.

## Mobile App
Story Generator app is built using the following technologies:

- [Flutter](https://flutter.dev/), a cross-platform mobile development framework by Google.
- [Google Generative AI](https://pub.dev/packages/google_generative_ai), a Flutter package that provides access to Google's generative AI models.

**Story Generator can be previewed on iOS and Android.*

## Setting up Project
- Requirements: 
  - [Flutter SDK](https://flutter.dev/)
  - [Gemini API Key](https://aistudio.google.com/app/apikey)
- Setup your env file:
  - Create a .env folder
  - Create an env.json file and add the following content
    ```
    {
      "API_KEY": "<Your API Key>"
    }
    ```

## Video Demo
![story_gen](https://github.com/Lord-Chris/story-generator/assets/58702861/1d59b122-3c45-49c7-a122-4ec0f9c8c4fc)

