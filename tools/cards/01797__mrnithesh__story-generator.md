---
id: tool-01797
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: story-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/mrnithesh/story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1797
category: 二、网文 / 长篇 AI 写作系统 库
repo: mrnithesh/story-generator
stars: 3
url: https://github.com/mrnithesh/story-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: d6ab0cfc256db8c6
  - methods/最强写作方法论_全球最强综合版.md
---

# mrnithesh/story-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/mrnithesh/story-generator
- **Stars**：3
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：An interactive web application that generates customized stories using Google's Gemini AI. Create engaging stories tailored to specific age groups, themes, and creative elements.
- **本地描述**：An interactive web application that generates customized stories using Google's Gemini AI. Create engaging stories tailored to specific age groups, themes, and creative elements.
- **拉取时间**：2026-07-23 23:31:26

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 📚 AI Story Generator

An interactive web application that generates customized stories using Google's Gemini AI. Create engaging stories tailored to specific age groups, themes, and creative elements.

![AI Story Generator Screenshot](https://github.com/mrnithesh/story-generator/blob/main/screenshot.png)

## ✨ Features

- Generate stories of varying lengths (100-2000 words)
- Choose from multiple story themes (Adventure, Fantasy, Science Fiction, etc.)
- Target specific age groups (3-6 years, 7-12 years, 13-16 years, 16+ years)
- Add custom creative elements to personalize stories
- Download generated stories as text files

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mrnithesh/story-generator.git
   cd story-generator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables (see Configuration section)

## ⚙️ Configuration

1. Create a `.env` file in the project root directory
2. Add your Google Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

> 🔑 **Get an API Key**: Obtain your Gemini API key from the [Google AI Studio](http://aistudio.google.com/apikey/).

## 🚀 Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL displayed in your terminal (typically http://localhost:8501)

3. Configure your story settings:
   - Select a theme
   - Choose an age group
   - Set the desired word count
   - Add optional custom elements

4. Click "Generate Story" and enjoy your personalized story!

## 📋 Requirements

- Python 3.7+
- Streamlit
- Google Generative AI Python SDK
- python-dotenv

## 📝 License

MIT

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/mrnithesh/story-generator/issues).
