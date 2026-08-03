---
id: tool-01594
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: aiStoryGenerator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/dtyutyunik/aistorygenerator
created: 2026-07-18
updated: 2026-07-18
no: 1594
category: 二、网文 / 长篇 AI 写作系统 库
repo: dtyutyunik/aiStoryGenerator
stars: 0
url: https://github.com/dtyutyunik/aistorygenerator
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

# dtyutyunik/aiStoryGenerator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/dtyutyunik/aistorygenerator
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：dtyutyunik/aiStoryGenerator
- **拉取时间**：2026-07-23 23:25:32

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI Story Generator

## Overview

AI Story Generator is a creative tool that leverages OpenAI's GPT-3.5-turbo model to craft captivating stories. Users can define characters, settings, genres, and plot points, and then let the AI bring their vision to life with a story tailored to their preferences.

![Intro Screen](./client/images/IntroScreen.png)

## Features

- **Customizable Story Elements**: Input your desired characters, settings, genres, and plot points to guide the story's direction.
- **Selectable Story Length**: Choose how long you want your story to be, ranging from under 3 paragraphs to 5-8 paragraphs.
- **Live Loading Screen**: As the AI generates your story, watch the progress on a dynamic loading bar.

![Loading Screen](./client/images/SampleLoadingScreen.png)

- **Scrollable Display**: The generated story is presented in a scrollable container, accommodating stories of any length without overwhelming the screen.
- **Responsive Design**: Whether on desktop or mobile, the layout adjusts to provide an optimal viewing experience.

![Generated Story](./client/images/SampleGeneratedImage.png)

## How It Works

1. **Input Story Details**: Fill out the form with the elements of your story.
2. **Choose Length**: Select the desired length for your story.
3. **Generate**: Hit the 'Generate Story' button to send your prompt to the AI.
4. **View**: The generated story will appear on the right, styled appropriately based on the genre and with an indicative title.

## Installation

Before running the project, ensure you have `node` and `npm` installed on your system.

```bash
# Clone the repository
git clone https://github.com/your-username/ai-story-generator.git

# Navigate to the project directory
cd ai-story-generator

# Install dependencies
npm install

# Start the application
npm start
```

## Environment Variables
Make sure to set up your environment variables before starting the app:
REACT_APP_OPENAI=your_openai_api_key


## Usage
After starting the app, the interface will guide you through crafting your story. Once generated, you can interact with the story container:

1. **Scroll Indicator**: A subtle ↓ appears if the story overflows the container, guiding you to scroll for more content.
2. **Scrollable Content**: Use your mouse or touchpad to scroll through the story.
