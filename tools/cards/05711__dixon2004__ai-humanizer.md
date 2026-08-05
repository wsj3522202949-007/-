---
id: tool-05711
type: tool
area: 库
status: active
tags: [去AI味, Python, 协议宽松, 需API密钥, 英文文档]
title: ai-humanizer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/dixon2004/ai-humanizer
created: 2026-07-18
updated: 2026-07-18
no: 5711
category: 一、去 AI 味 / Humanizer 库
repo: dixon2004/ai-humanizer
stars: 6
url: https://github.com/dixon2004/ai-humanizer
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# dixon2004/ai-humanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/dixon2004/ai-humanizer
- **Stars**：6
- **语言**：Python
- **License**：MIT
- **Topics**：ai-humanizer, google-gemini-ai, large-language-model, natural-language-processing, prompt-engineering
- **GitHub 描述**：AI Humanizer is a free, open-source tool that rewrites AI-generated text to sound more natural, fluent, and human.
- **本地描述**：AI Humanizer is a free, open-source tool that rewrites AI-generated text to sound more natural, fluent, and human.
- **拉取时间**：2026-07-25 18:28:47

---

# AI Humanizer

## Overview

AI Humanizer is a free, open-source tool that transforms AI-generated text into language that reads naturally and authentically. Powered by Google Gemini 2.5 and guided by custom prompt engineering, it refines robotic or overly structured outputs into text with improved tone, rhythm, and clarity.

Ideal for writers, developers, researchers, and content creators, AI Humanizer is accessible through a public web app or can be deployed locally using Python or Docker depending on your preferred workflow.

Access the web version here:
https://ai-humanizer.streamlit.app

---

## Key Features

- **Powered by Google Gemini 2.5**

    Utilizes the capabilities of Google’s Gemini 2.5 API to generate context-aware, fluent, and human-like text.

- **Natural Language Enhancement**

    Rewrites AI-generated content by improving sentence structure, tone, and variety while preserving original intent.

- **Custom Prompt Engineering**

    Employs carefully crafted prompts that guide the model to produce more expressive and natural-sounding results.

- **Locally Deployable**

    Can be installed and run on your own system using either a Python script or Docker container for greater control.

- **Free and Open Source**

    Licensed under the MIT License and available for anyone to use, modify, or contribute to.
    
---

## Table of Contents

- [How It Works](#how-it-works)
- [Showcase](#showcase)
- [Local Installation](#local-installation)
  - [Prerequisites](#prerequisites)
  - [Deployment Options](#deployment-options)
    - [Option 1: Docker Deployment](#option-1-docker-deployment)
    - [Option 2: Local Python Script](#option-2-local-python-script)
- [License](#license)

---

## Showcase

Here’s a quick demo of AI Humanizer in action.

https://github.com/user-attachments/assets/0a661f7a-4238-4941-9f9a-fe879544b468

Try it live: https://ai-humanizer.streamlit.app

---

## How It Works

AI Humanizer sends input text to the Google Gemini 2.5 API using a specialized prompt that enhances sentence flow and tone. The result is text that feels more natural and engaging while maintaining the original meaning.

Enhancements include:
- Varying sentence structure and length to reduce repetition
- Removing robotic phrasing and unnatural transitions
- Improving tone and making the content more readable
- Preserving the original message, context, and logic

This makes the tool suitable for professional, creative, academic, and general writing purposes.

---

## Local Installation

The following instructions are for users who wish to install and run AI Humanizer locally using either Python or Docker. An internet connection is required to access the Gemini API.

**Prerequisites**

Before installing AI Humanizer locally, ensure that you have the following:
- A valid Google Gemini 2.5 API key, available from [Google AI Studio](https://aistudio.google.com/apikey)
- Python version 3.12 or later (for the Python script setup)
- Docker installed (for the Docker-based setup)

### Deployment Options

#### Option 1: Docker Deployment

This option runs AI Humanizer inside a Docker container.

1. **Clone the Repository**

    ```bash
    git clone https://github.com/dixon2004/ai-humanizer.git
    cd ai-humanizer
    ```

2. **Configure Environment Variables**

    - Rename `template.env` to `.env` in the root directory.
    - Open `.env` and update the following:
        ```ini
        GEMINI_API_KEY = "your_gemini_api_key_here"
        ```
        **GEMINI_API_KEY**: Insert your Gemini API key, available from [Google AI Studio](https://aistudio.google.com/apikey).

3. **Build and Start the Application**

    ```bash
    docker-compose up --build -d
    ```
    Visit http://localhost:8501 in your browser to access the interface.

4. **Stop the Application**

    ```bash
    docker-compose down
    ```

5. **Restart After Changes**

    ```bash
    docker-compose down && docker-compose up --build -d
    ```

6. **View Logs**

    ```bash
    docker-compose logs -f
    ```

#### Option 2: Local Python Script

This option runs AI Humanizer using Python and Streamlit on your local machine.

1. **Clone the Repository**

    ```bash
    git clone https://github.com/dixon2004/ai-humanizer.git
    cd ai-humanizer
    ```

2. **Create and Activate a Virtual Environment**

    - On Linux or macOS:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

    - On Windows:
        ```bash
        python3 -m venv venv
        venv\Scripts\activate
        ```

3. **Install Required Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**

    - Rename `template.env` to `.env` in the root directory.
    - Open `.env` and update the following:
        ```ini 
        GEMINI_API_KEY = "your_gemini_api_key_here"
        ```
        **GEMINI_API_KEY**: Insert your Gemini API key, available from [Google AI Studio](https://aistudio.google.com/apikey).

5. **Run the Application**

    ```bash 
    streamlit run src/main.py
    ```
    After launching, open http://localhost:8501 in your browser to begin using the tool.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## License

This project is licensed under the MIT License. See the `[LICENSE](LICENSE)` file for details.
