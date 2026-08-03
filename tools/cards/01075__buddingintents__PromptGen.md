---
id: tool-01075
type: tool
area: 库
status: active
tags: [Kotlin, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: PromptGen
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/buddingintents/promptgen
created: 2026-07-18
updated: 2026-07-18
no: 1075
category: 二、网文 / 长篇 AI 写作系统 库
repo: buddingintents/PromptGen
stars: 0
url: https://github.com/buddingintents/promptgen
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# buddingintents/PromptGen

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/buddingintents/promptgen
- **Stars**：0
- **语言**：Kotlin
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered prompt generator for writing, blogging, and creative tasks.
- **本地描述**：AI-powered prompt generator for writing, blogging, and creative tasks.
- **拉取时间**：2026-07-23 23:10:20

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# PromptGen — Android (Kotlin) Prompt-Generation App

This project is a minimal, complete Android Studio project that implements a native Android app to:
- Take a user's rough idea
- Detect a theme (on-device heuristic)
- Call a configurable LLM endpoint (OpenAI/HuggingFace/Cohere or custom)
- Return a *refined prompt* (the app enforces the output to be a prompt)

## What's included
- Full Android Studio project under `/app`
- Simple UI: input, generate button, output, copy, settings
- Network code using OkHttp (no external LLM SDKs included)
- Settings to store API key and custom endpoint (SharedPreferences)

## How to open in Android Studio
1. Download the ZIP: `prompt-gen-app.zip`
2. Open Android Studio -> File -> Open... and select the extracted folder `PromptGenApp` (the folder that contains `settings.gradle`).
3. Let Gradle sync/download dependencies.
4. Connect an Android device or run an emulator and press Run.

## Setting up an LLM provider
- Open `Settings` in the app.
- Choose a preset (OpenAI / HuggingFace / Cohere) or Custom.
- Paste your API key (Bearer token) and optional custom endpoint.
- For OpenAI, use endpoint: `https://api.openai.com/v1/chat/completions`
- For Cohere: `https://api.cohere.ai/generate`
- For HuggingFace inference, set endpoint to a model-specific inference URL, e.g. `https://api-inference.huggingface.co/models/<model>`

## Notes & next steps
- This is intentionally simple to be a clear starting point.
- You can replace the lightweight theme classifier with an on-device TFLite model.
- Consider switching to DataStore for robust settings and encrypting stored API keys for production (e.g., EncryptedSharedPreferences).
- Add proper error handling, retries, and UI polish.
