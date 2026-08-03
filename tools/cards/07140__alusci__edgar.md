---
id: tool-07140
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 需API密钥, 英文文档]
title: edgar
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/alusci/edgar
created: 2026-07-18
updated: 2026-07-18
no: 7140
category: 画龙补充 / 扩容入库 — 补充源
repo: alusci/edgar
stars: 3
url: https://github.com/alusci/edgar
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/QUICK_START.md
---

# alusci/edgar

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/alusci/edgar
- **Stars**：3
- **语言**：Python
- **License**：Apache-2.0
- **Topics**：—
- **GitHub 描述**：A story teller bot application developed in honor of the famous Edgar Allan Poe
- **本地描述**：edgar
- **拉取时间**：2026-07-25 19:12:03

related:
  - methods/QUICK_START.md
---

# Edgar: Story Generator

A Python application that generates story scenes using OpenAI's GPT-4 model and LangChain. The application takes story elements (characters, background, etc.) as input and generates the next scene while maintaining consistency with the established narrative.

## Prerequisites

- Python 3.11 or higher
- Conda package manager
- OpenAI API key

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a conda environment:
```bash
conda create -n story-gen python=3.11
conda activate story-gen
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```bash
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

## Usage

1. Make sure your conda environment is activated:
```bash
conda activate story-gen
```

2. Prepare your story data:
   - Use the provided example in `data/inputs/stone_giant_heroons.json` as a template
   - Create your own JSON file following the same structure
   - Required fields: title, genre, main_characters, introduction (facts, outcome), story_beginning

3. Run the application in one of two ways:

### Command Line Interface
```bash
# Use default story data
python main.py --cli

# Specify custom story data
python main.py --cli --input path/to/your/story.json
```
This will launch the interactive command-line interface where you can:
- Generate chapters one by one
- Provide feedback to refine chapters
- Save the completed story

### Graphical User Interface
```bash
python main.py
```
This will launch a web-based Gradio interface where you can:
- Upload JSON story data
- Enter story elements through forms
- Generate and regenerate chapters with feedback
- Save the completed story to a file

## Input Data Structure

The input JSON should follow this structure:
```json
{
    "title": "Your Story Title",
    "genre": "Genre / Sub-genre",
    "main_characters": [
        {
            "name": "Character Name",
            "description": "Character description"
        }
    ],
    "introduction": {
        "facts": "Background information",
        "outcome": "Known outcome or future events"
    },
    "story_beginning": "The current scene or starting point"
}
```

## Features

### Command Line Interface
- Interactive story generation loop
- Chapter-by-chapter generation
- Feedback-based regeneration
- Automatic story saving

### Gradio UI
- Web-based interface accessible from any browser
- Form-based story data creation
- Simplified chapter generation workflow
- Feedback integration for story refinement
- Reset functionality to start over with the same story data

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)

## Note

Make sure to keep your `.env` file secure and never commit it to version control. The `.gitignore` file is configured to exclude it automatically.
