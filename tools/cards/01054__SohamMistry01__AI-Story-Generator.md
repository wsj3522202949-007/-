---
id: tool-01054
type: tool
area: 库
status: active
tags: [文风迁移, Python, 协议未明, 需API密钥, 英文文档, 改稿润色]
title: AI-Story-Generator
summary: 风格微调/文风迁移
source: https://github.com/sohammistry01/ai-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 1054
category: 二、网文 / 长篇 AI 写作系统 库
repo: SohamMistry01/AI-Story-Generator
stars: 1
url: https://github.com/sohammistry01/ai-story-generator
tier: "B"
use_case: "风格微调/文风迁移"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# SohamMistry01/AI-Story-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/sohammistry01/ai-story-generator
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：SohamMistry01/AI-Story-Generator
- **拉取时间**：2026-07-23 23:09:44

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI Story Generator - Streamlit App

A Streamlit application that uses LangGraph to generate compelling stories through a multi-step prompt chaining workflow.

## Features

- **Multi-step Story Generation**: Uses LangGraph to orchestrate a 3-step story creation process
- **Interactive UI**: Clean, modern Streamlit interface with progress tracking
- **Markdown Output**: All story content is formatted in markdown
- **Download Functionality**: Export generated stories as markdown files
- **Error Handling**: Robust error handling with user-friendly messages

## Story Generation Process

1. **Generate**: Creates an initial story premise based on the user's topic
2. **Improve**: Enhances the story with vivid details and descriptions
3. **Polish**: Adds an unexpected twist to make the story more engaging

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements_streamlit.txt
```

### 2. Set up Environment Variables

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

You can get a free Groq API key by signing up at [https://console.groq.com/](https://console.groq.com/)

### 3. Run the Application

```bash
streamlit run story_generator_app.py
```

The app will open in your default web browser at `http://localhost:8501`

## Usage

1. **Enter a Topic**: Type any topic you'd like to generate a story about (e.g., "Space Exploration", "Time Travel", "Underwater Cities")

2. **Generate Story**: Click the "🚀 Generate Story" button to start the generation process

3. **View Results**: The app will display:
   - Original story premise
   - Enhanced story with vivid details
   - Final story with an unexpected twist

4. **Download**: Use the download button to save your story as a markdown file

## Technical Details

### Architecture

The app uses LangGraph to create a state machine that orchestrates the story generation:

```
START → Generate Story → Check Quality → Improve Story → Polish Story → END
```

### Key Components

- **State Management**: Uses TypedDict for type-safe state handling
- **Conditional Logic**: Automatically retries story generation if quality checks fail
- **Caching**: LLM initialization and graph compilation are cached for performance
- **Error Handling**: Comprehensive error handling with user-friendly messages

### Dependencies

- `streamlit`: Web application framework
- `langchain-groq`: Groq LLM integration
- `langgraph`: Workflow orchestration
- `python-dotenv`: Environment variable management
- `typing-extensions`: Type hints support

## Example Output

When you enter "Space Exploration" as a topic, the app generates:

1. **Original Premise**: A concise story premise about space exploration
2. **Enhanced Story**: A detailed narrative with vivid descriptions and character development
3. **Final Story**: The enhanced story with an unexpected twist that changes the narrative direction

## Customization

You can modify the story generation prompts by editing the functions in `story_generator_app.py`:

- `generate_story()`: Modify the initial story generation prompt
- `improved_story()`: Change how the story is enhanced
- `polish_story()`: Adjust the twist generation logic

## Troubleshooting

### Common Issues

1. **GROQ_API_KEY not set**: Make sure your `.env` file contains the correct API key
2. **Import errors**: Ensure all dependencies are installed correctly
3. **Slow generation**: The app uses the Groq API, so generation speed depends on your internet connection

### Getting Help

If you encounter any issues:
1. Check that all dependencies are installed
2. Verify your GROQ_API_KEY is correct
3. Ensure you have an active internet connection

## License

This project is open source and available under the MIT License. 
