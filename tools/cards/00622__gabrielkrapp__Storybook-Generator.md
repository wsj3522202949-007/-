---
id: tool-00622
type: tool
area: 库
status: active
tags: [TTS, TypeScript, 协议未明, 需API密钥, 英文文档]
title: Storybook-Generator
summary: 小说转语音/有声书
source: https://github.com/gabrielkrapp/storybook-generator
created: 2026-07-18
updated: 2026-07-18
no: 622
category: 二、网文 / 长篇 AI 写作系统 库
repo: gabrielkrapp/Storybook-Generator
stars: 1
url: https://github.com/gabrielkrapp/storybook-generator
tier: "B"
use_case: "小说转语音/有声书"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: edf3e55d6d0b50e4
  - methods/最强写作方法论_全球最强综合版.md
---

# gabrielkrapp/Storybook-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/gabrielkrapp/storybook-generator
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A web application designed to spark the imagination of children by generating unique, engaging stories using the power of AI
- **本地描述**：A web application designed to spark the imagination of children by generating unique, engaging stories using the power of AI
- **拉取时间**：2026-07-23 22:57:13

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

![Logo](https://github.com/gabrielkrapp/AI-Historys/assets/109620152/0b380094-6c62-46a5-9412-65942e345b61)

# Storybook Generator

Welcome to the Storybook Generator! This innovative application integrates with OpenAI's powerful language model to create enchanting and personalized stories for children.

## Live Demo

https://storybook-generator.vercel.app/

## Application Prints

![Home](https://github.com/gabrielkrapp/AI-Historys/assets/109620152/6b84aca8-e800-4fb4-b6d4-623b94de8c7a)

![Loading](https://github.com/gabrielkrapp/AI-Historys/assets/109620152/288c4e64-7495-4aa8-bc18-92ec1fabf428)

![Story](https://github.com/gabrielkrapp/Storybook-Generator/assets/109620152/4a504e75-8e42-48b8-9c9a-efb572eb1cac)


## New Feature: Text-to-Speech

Enhancing the storytelling experience, we've now integrated a Text-to-Speech (TTS) feature! With just a click, stories are narrated aloud, bringing them to life and offering a more immersive experience for children. This feature utilizes the latest TTS technologies to deliver clear and engaging story narration.

## Technologies Used

- React.js
- Tailwind CSS
- Axios for HTTP requests
- ViteJS as the build tool
- OpenAI's GPT-3 for generating stories
- Web Speech API for Text-to-Speech functionality

## Integration with OpenAI

This project leverages OpenAI's GPT-3 to dynamically generate stories based on user inputs. By providing a theme, the app communicates with the OpenAI API to retrieve a unique story each time.

## Configuration

To run this project locally, you'll need to set up your environment variables. Create a `.env` file in the root of the project and define the following variables:

### In the frontend

```plaintext
VITE_BACKEND_URL=your-backend-url
```

### In the backend

```plaintext
OPENAI_API_URL=your-openai-api-url
OPENAI_API_KEY=your-openai-api-key
FRONT_END_URL=your-frontend-url
```

Replace your-backend-url with the URL of your backend and your-openai-api-key with your OpenAI API key.

## Known Bug

There's a known issue where occasionally the OpenAI API may return incomplete stories. This is being investigated, and a fix will be implemented as soon as possible.

## Mobile Application

The mobile version of this application is currently under development using React Native. It will be available on both iOS and Android platforms. Stay tuned for the release and the addition of download links.

## Contributing

We welcome contributions to this project. If you have suggestions or encounter any bugs, please open an issue in the repository.

Thank you for visiting the Storybook Generator project!
