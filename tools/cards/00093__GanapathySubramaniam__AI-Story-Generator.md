---
id: tool-00093
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: AI-Story-Generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/ganapathysubramaniam/ai-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 93
category: 二、网文 / 长篇 AI 写作系统 库
repo: GanapathySubramaniam/AI-Story-Generator
stars: 1
url: https://github.com/ganapathysubramaniam/ai-story-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# GanapathySubramaniam/AI-Story-Generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ganapathysubramaniam/ai-story-generator
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI powered Storybook (Generates stories with images  as a PDF)
- **本地描述**：AI powered Storybook (Generates stories with images  as a PDF)
- **拉取时间**：2026-07-23 22:41:35

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI Story Generator
```
           _____    _____ _                      _____                           _             
     /\   |_   _|  / ____| |                    / ____|                         | |            
    /  \    | |   | (___ | |_ ___  _ __ _   _  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
   / /\ \   | |    \___ \| __/ _ \| '__| | | | | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
  / ____ \ _| |_   ____) | || (_) | |  | |_| | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 /_/    \_\_____| |_____/ \__\___/|_|   \__, |  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                         __/ |                                                 
                                        |___/                                                  

```

## 📖 Project Overview
The **AI Story Generator** is a powerful tool that leverages OpenAI's GPT-4 and DALL-E 3 to create immersive, illustrated stories. It generates dynamic story chapters with AI-crafted content and images, compiling them into a professional-quality PDF.
## 📚 Checkout the samples it generated
- [Peeking Into Future](https://github.com/GanapathySubramaniam/AI-Story-Generator/blob/main/outputs/peeking_into_future.pdf)
- [Time Travel Adventure](https://github.com/GanapathySubramaniam/AI-Story-Generator/blob/main/outputs/time_travel_adventure.pdf)

## 🚀 Features
- **Story Generation:** Uses GPT-4 to generate engaging story chapters.
- **Image Generation:** Creates detailed illustrations for each chapter using DALL-E 3.
- **PDF Compilation:** Converts stories and images into a beautifully formatted PDF.
- **Custom Chapter Counts:** Generate stories with a flexible number of chapters.

## 🛠️ How It Works
1. **Initialize the Generator:** Provide a story prompt and specify the desired number of chapters.
2. **Generate Story Content:** GPT-4 generates detailed chapters based on the input prompt.
3. **Generate Images:** DALL-E 3 creates chapter-specific illustrations.
4. **Compile PDF:** The PDFBuilder class formats and compiles the story into a final PDF document.

## 🧰 Technologies Used
- **Python**
- **OpenAI GPT-4** for text generation
- **DALL-E 3** for image generation
- **LangChain** for prompt engineering
- **ReportLab** for PDF creation
- **pydantic** for data validation
- **asyncio** for asynchronous operations

## 📂 Project Structure
```
├── main.py                 # Entry point for story generation
├── outputs/                # generated stories pdf
├── scripts/
│   └── story_generator.py  # Core AI story and PDF generation logic
└── requirements.txt        # Project dependencies
```

## 🚦 Usage
```bash
# Install dependencies
pip install -r requirements.txt

# Run the story generator
python main.py
```

## 🧑‍💻 Example
```python
import asyncio
from scripts.story_generator import AIStoryGenerator

async def main() -> None:
    generator = AIStoryGenerator("An epic fantasy adventure", chapter_count=5)
    await generator.generate_pdf("fantasy_story.pdf")

asyncio.run(main())
```

## 📑 Requirements
- Python 3.8+
- OpenAI API key (Set in your .env file)

## ⚠️ Error Handling
The system includes robust error handling for:
- Invalid input data
- Failed API calls
- PDF generation issues



