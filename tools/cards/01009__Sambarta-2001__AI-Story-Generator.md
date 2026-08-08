---
id: tool-01009
type: tool
area: 库
status: active
tags: [HTML, 协议传染, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: AI-Story-Generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/sambarta-2001/ai-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1009
category: 二、网文 / 长篇 AI 写作系统 库
repo: Sambarta-2001/AI-Story-Generator
stars: 1
url: https://github.com/sambarta-2001/ai-story-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: c8311f0f5a13887e
  - methods/最强写作方法论_全球最强综合版.md
---

# Sambarta-2001/AI-Story-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/sambarta-2001/ai-story-generator
- **Stars**：1
- **语言**：HTML
- **License**：GPL-3.0
- **Topics**：—
- **GitHub 描述**：AI Story Generator is a Flask app that creates stories based on your genre and prompt. Simply choose your preferences and get a unique story.
- **本地描述**：AI Story Generator is a Flask app that creates stories based on your genre and prompt. Simply choose your preferences and get a unique story.
- **拉取时间**：2026-07-23 23:08:27

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---


# AI Story Generator

Welcome to the AI Story Generator! This project leverages Google GenAI to create compelling and unique stories based on user inputs. The application is built using Flask, providing a simple and intuitive web interface for users to interact with the AI.


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
## Introduction

The AI Story Generator is a web application that allows users to generate stories in various genres, including horror, detective, thrill, and romcom. By leveraging Google GenAI, the application can produce high-quality, coherent narratives based on user-provided prompts and parameters.
## Features

- Multi-genre Support: Generate stories in multiple genres such as horror, detective, thrill, and romcom.
- User Inputs: Customize story generation with specific prompts and parameters.
- Responsive Design: A user-friendly web interface built with Flask and Bootstrap.
- Scalable: Easily deployable on various platforms, including local servers and cloud environments.

## Installation

### Prerequisites

- Python 3.8+
- Virtual env

### Clone the Repository

```bash
git clone https://github.com/yourusername/ai-story-generator.git
cd ai-story-generator 
```

### Clone the Repository
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a `.env` file in the root directory and add your Google GenAI API key:

```env
GOOGLE_API_KEY=your_google_genai_api_key
FLASK_ENV=development
```
### Running the Application

```bash
flask run
```
Open your web browser and navigate to http://127.0.0.1:5000 to access the AI Story Generator.

## Generating a Story
- Choose a genre (Horror, Detective, Romcom).
- Enter a prompt or a few keywords.
- Click "Generate Story."
- Enjoy your AI-generated story!
    ## API Endpoints

### `POST /generate`

Generate a story based on user inputs.

- **URL:** `/generate`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "genre": "horror",
    "prompt": "A dark and stormy night"
  }

### `GET /`

The main web interface for the AI Story Generator.
## Contributing

Contributions are always welcome!

We welcome contributions to enhance the AI Story Generator. To contribute:

- Fork the repository.
- Create a new branch (git checkout -b feature/your-feature).
- Make your changes.
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature/your-feature).
- Create a new Pull Request.


## License

[GPL-3.0](https://choosealicense.com/licenses/GPL-3.0/)

