---
id: tool-01579
type: tool
area: 库
status: active
tags: [TTS, Python, 协议传染, 本地优先, 英文文档, 人物设定, RAG, 本地写作]
title: blog_post_creator_v1.0
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/jimjamscott22/blog_post_creator_v1.0
created: 2026-07-18
updated: 2026-07-18
no: 1579
category: 二、网文 / 长篇 AI 写作系统 库
repo: jimjamscott22/blog_post_creator_v1.0
stars: 1
url: https://github.com/jimjamscott22/blog_post_creator_v1.0
tier: "B"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# jimjamscott22/blog_post_creator_v1.0

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/jimjamscott22/blog_post_creator_v1.0
- **Stars**：1
- **语言**：Python
- **License**：GPL-3.0
- **Topics**：—
- **GitHub 描述**：A tool that helps content creators generate blog outlines, social media calendars, and creative writing prompts using AI assistance.
- **本地描述**：A tool that helps content creators generate blog outlines, social media calendars, and creative writing prompts using AI assistance.
- **拉取时间**：2026-07-23 23:25:07

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Content Generator - AI-Powered Local LLM Content Creation

## Project Overview
A specialized tool that helps creators generate complete technical blogs, coding practice sets, social calendars, and writing prompts with minimal prompting. Uses local LLMs (Ollama/LM Studio) for privacy-focused, cost-free content generation.

## Core Features

### 1. Tech Blog Generator
**Inputs:**
- Topic/keyword focus (technical subject)
- Target audience (beginners, intermediate, experts)
- Desired length (short, medium, long)
- Content type (tutorial, listicle, how-to, opinion)
- **Custom Knowledge Base** (optional): Add your own documentation, API specs, or technical context

**Outputs:**
- Complete, publish-ready technical blog post
- Markdown-formatted sections with practical guidance
- Optional technical details based on your custom context
- Audience and content-type aware writing style

### 2. Coding Practice Problem Generator
**Inputs:**
- Topic/skill focus
- Difficulty (beginner, intermediate, advanced)
- Programming language
- Number of problems
- Optional focus areas

**Outputs:**
- Structured coding problems with statements and constraints
- Input/output format and examples
- Hints and starter code
- Solution strategy + complexity guidance

### 3. Social Media Calendar Generator
**Inputs:**
- Content themes/categories
- Posting frequency (daily, 3x week, weekly)
- Platform focus (Twitter, LinkedIn, Instagram)
- Time period (week, month, quarter)
- Brand voice/tone preferences

**Outputs:**
- Scheduled content ideas with dates
- Post formats (text, thread, image, video)
- Engagement prompt suggestions
- Hashtag recommendations

### 4. Creative Writing Prompt Generator
**Inputs:**
- Genre preferences (sci-fi, mystery, romance, fantasy)
- Prompt type (character, plot, world-building)
- Complexity level
- Additional constraints (word count, theme)

**Outputs:**
- Original writing prompts
- Character development questions
- Plot twist suggestions
- Setting detail ideas

## Technical Architecture

### Frontend:
- **Streamlit** - Interactive web interface with real-time generation

### Backend Structure:
```
blog_post_creator_v1.0/
├── main.py              # Streamlit application entry point
├── generators/
│   ├── blog_generator.py
│   ├── coding_practice_generator.py
│   ├── social_generator.py
│   └── writing_generator.py
├── utils/
│   ├── llm_interface.py      # LLM provider abstraction
│   ├── prompt_templates.py
│   └── logger.py
└── config/
    └── settings.py           # Environment configuration
```

### LLM Provider Support:
The application supports **two local LLM providers** for privacy-focused, cost-free generation:

1. **Ollama** - Open-source local LLM runner
   - Easy to install and use
   - Supports many models (llama3.2, mistral, codellama, etc.)
   - Default endpoint: `http://localhost:11434`

2. **LM Studio** - User-friendly local LLM server
   - Graphical interface for model management
   - OpenAI-compatible API
   - Default endpoint: `http://localhost:1234/v1`

**Provider Selection:**
- Choose your preferred provider in the sidebar UI
- Switch between providers without restarting the app
- Select from available models for each provider
- Real-time connection status and model availability

## Implementation Roadmap

### Phase 1: MVP (Week 1-2)
- Basic tech blog generator with hardcoded prompts
- Simple UI with text input and output display
- Single LLM integration (OpenAI API)

### Phase 2: Feature Expansion (Week 3-4)
- Add social media calendar feature
- Implement creative writing prompts
- Save/export functionality (PDF, copy to clipboard)

### Phase 3: Enhancement (Week 5-6)
- User customization options
- Template library
- History/previous generations
- Multiple output formats

## Sample Prompts to Get Started

### Blog Generator Prompt Template:
```
Write a complete technical blog post about "{topic}" for {audience} readers.
Target length: {length}
Content type: {format}
Include:
- Intro with clear reader promise
- Fully developed sections with practical examples
- Conclusion with call-to-action
- FAQ section
```

### Coding Practice Prompt Template:
```
Create {problem_count} coding practice problems on "{topic}".
Difficulty: {difficulty}
Language: {language}
Focus areas: {focus_areas}

For each problem include:
- Problem statement
- Constraints
- Input/output format and examples
- Hints
- Starter code
- Complexity expectations
```

### Social Media Prompt Template:
```
Create {frequency} social media post ideas about "{theme}" 
for {platform} over a {timeframe} period.
Target audience: {audience}
Brand voice: {tone}

Format each post as:
[Date]: [Post type] - [Content idea]
Engagement prompt: [Question or call-to-action]
```

### Writing Prompt Template:
```
Generate a {genre} {prompt_type} writing prompt.
Include:
- Main scenario/conflict
- Character elements (if character-focused)
- Setting details
- Potential plot directions

Keep complexity level: {complexity}
```

## Installation & Setup

### Prerequisites
1. **Python 3.8+** installed on your system
2. **One of the following LLM providers:**
   - **Ollama:** Download from [ollama.ai](https://ollama.ai)
   - **LM Studio:** Download from [lmstudio.ai](https://lmstudio.ai)

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd blog_post_creator_v1.0
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your LLM provider:**
   Create a `.env` file (or copy from `.env.example`):
   ```bash
   # Choose provider: "ollama" or "lm_studio"
   LLM_PROVIDER=ollama
   
   # Ollama settings
   OLLAMA_BASE_URL=http://localhost:11434
   OLLAMA_MODEL=llama3.2
   
   # LM Studio settings
   LM_STUDIO_BASE_URL=http://localhost:1234/v1
   LM_STUDIO_MODEL=local-model
   
   # Generation parameters
   MAX_TOKENS=2000
   TEMPERATURE=0.7
   ```

4. **Start your LLM service:**
   
   **For Ollama:**
   ```bash
   ollama serve
   # Or start the Ollama desktop app
   # Pull a model if you haven't already:
   ollama pull llama3.2
   ```
   
   **For LM Studio:**
   - Open LM Studio application
   - Load a model
   - Start the local server (usually on port 1234)

5. **Run the application:**
   ```bash
   streamlit run main.py
   ```

6. **Access the web interface:**
   - Open your browser to `http://localhost:8501`
   - Select your provider in the sidebar
   - Choose a model and start generating content!

### Required Python Packages
- `streamlit` - Web interface framework
- `requests` - HTTP client for LLM APIs
- `python-dotenv` - Environment variable management
- `pydantic` - Data validation

**No API keys required!** All processing happens locally on your machine.

## Success Metrics
- Generate coherent, actionable content ideas
- Provide variety in outputs
- Reasonable generation speed (<10 seconds)
- User can easily copy/use generated content

## Next Steps
1. Set up development environment
2. Create basic LLM connection test
3. Build simple tech blog generator first
4. Test with sample topics
5. Iterate based on output quality

