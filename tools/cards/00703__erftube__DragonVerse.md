---
id: tool-00703
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: DragonVerse
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/erftube/dragonverse
created: 2026-07-18
updated: 2026-07-18
no: 703
category: 二、网文 / 长篇 AI 写作系统 库
repo: erftube/DragonVerse
stars: 1
url: https://github.com/erftube/dragonverse
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# erftube/DragonVerse

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/erftube/dragonverse
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：DragonVerse Ai Sci-Fi Horror story generator
- **本地描述**：DragonVerse Ai Sci-Fi Horror story generator
- **拉取时间**：2026-07-23 22:59:31

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# DragonVerse

DragonVerse is an AI-powered story generation tool that creates sci-fi horror stories, generates images, and compiles them into videos. It integrates various AI models to generate ideas, write stories, create images, and handle media processing.

This is the tool I use on my YouTube channel: [DragonVerseAI](https://www.youtube.com/@DragonVerseAI).

## Features
- **Story Generation**: AI-generated story ideas and detailed scripts.
- **AI Image Generation**: Creates visuals for scenes using AI.
- **Media Processing**: Converts images and audio into video clips.
- **Automated Video Creation**: Compiles all media into a final video.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/dragonverse.git
   cd dragonverse
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Add API keys to `api.json`:
   ```json
   {
       "REPLICATE_API_TOKEN": "your_replicate_api_key",
       "ELEVENLABS_API_TOKEN": "your_elevenlabs_api_key",
       "ANTHROPIC_API_TOKEN": "your_anthropic_api_key"
   }
   ```
4. create and put your ffmpeg binary files under ffmpeg/bin 

## Usage

Run the program:
```sh
python dragonVerse.py
```

### Menu Options
1. **Generate Ideas** - Creates new story ideas.
2. **Show Ideas** - Displays available story ideas.
3. **Generate Story** - Expands a selected idea into a full story.
4. **Generate Video** - Creates a video from the generated story.

## File Structure
```
├── dragonVerse.py        # Main application file
├── storyGen.py           # Handles AI-based story generation
├── mediaHandler.py       # Manages media processing and file handling
├── mediaGenerator.py     # Generates images using AI
├── parse.py              # Parses AI-generated JSON outputs
├── prompt.json           # Contains prompts for AI models
├── api.json              # API key configuration (DO NOT SHARE)
└── requirements.txt      # Python dependencies
```

## Dependencies
- Python 3.8+
- MoviePy
- FFmpeg
- Requests
- JSON

Ensure `ffmpeg` is installed and accessible via the system path.

## License
This project is licensed under the MIT License.

## Author
[erftube](https://github.com/erftube)
