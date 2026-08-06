---
id: tool-01723
type: tool
area: 库
status: active
tags: [Svelte, 协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: hypeWriter
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/hype-writer/hypewriter
created: 2026-07-18
updated: 2026-07-18
no: 1723
category: 二、网文 / 长篇 AI 写作系统 库
repo: hype-Writer/hypeWriter
stars: 0
url: https://github.com/hype-writer/hypewriter
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# hype-Writer/hypeWriter

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/hype-writer/hypewriter
- **Stars**：0
- **语言**：Svelte
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：hypeWriter is an AI-assisted writing tool for developing full-length novels.
- **本地描述**：hypeWriter is an AI-assisted writing tool for developing full-length novels.
- **拉取时间**：2026-07-23 23:29:16

---

# hypeWriter

An AI-assisted novel writing application with a modern Svelte 5 frontend and Google Gemini AI integration. Features multiple project support, conversational AI interactions, and high-quality text-to-speech audiobook generation.

## ✨ Features

### 🎨 Modern UI
- **Severance-inspired dark theme** with cyan accents
- **Svelte 5 SPA** with modern runes architecture (`$state`, `$derived`)
- **Multi-project dashboard** for managing multiple novels
- **Responsive design** optimized for desktop and mobile

### 🤖 AI-Powered Writing
- **Google Gemini integration** for intelligent content generation
- **Streaming responses** with real-time AI content generation
- **Specialized agents** for world building, character creation, and storytelling
- **Conversational interface** throughout the application

### 📚 Project Management
- **Multiple project support** with JSON-structured data
- **Import system** for existing manuscripts (.txt, .docx, .epub)
- **Project analytics** and insights from structured metadata
- **Local file persistence** for easy backup and access

### 🎧 Text-to-Speech Integration
- **Kokoro-FastAPI integration** for high-quality audiobook generation
- **60+ voices available** (defaults to Emma - British Female)
- **Full chapter conversion** to MP3/WAV/FLAC formats
- **No length limits** - can process entire chapters
- **Built-in audio player** with voice selection controls

## 🏗️ Architecture

**hypeWriter** uses a hybrid architecture combining modern frontend with FastAPI backend:

### Backend (FastAPI/Python)
- **Main server**: `hypewriter.py` - FastAPI app with Jinja2 templating
- **Core modules**: `core/` directory contains agents, config, prompts, and data models
- **AI Integration**: Google Gemini via `google-generativeai`
- **Storage**: File-based JSON structure in `library/` directory
- **Sessions**: Server-side session management with starlette-session
- **MCP Integration**: FastAPI MCP server for Claude Code interaction

### Frontend (Svelte 5/TypeScript)
- **Framework**: Modern Svelte 5 using Runes API (`$state`, `$effect`, `$derived`)
- **Build**: Vite bundler with TypeScript, assets served by FastAPI
- **Architecture**: SPA embedded in FastAPI template structure
- **Components**: Reusable chat interface and modern UI components

### External Services
- **Google Gemini**: AI content generation and conversation
- **Kokoro-FastAPI**: High-quality text-to-speech conversion (optional)

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 18+ (for frontend development)
- Google API key for Gemini
- (Optional) Kokoro-FastAPI for TTS features


### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/hypeWriter.git
   cd hypeWriter
   ```

2. **Set up Python environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key_here
   GEMINI_MODEL_NAME=gemini-1.5-flash
   APP_SECRET_KEY=your_secret_key_here
   ```

4. **Run the application:**
   ```bash
   uvicorn hypewriter:app --reload
   ```

5. **Open your browser:**
   Navigate to `http://localhost:8000`

### Frontend Development (Optional)

Only needed if you want to modify the Svelte frontend:

```bash
cd frontend
npm install
npm run dev  # Development server on http://localhost:5173
npm run build  # Build for production (copies to backend)
```

### TTS Setup (Optional)

For audiobook features, set up Kokoro-FastAPI:
1. Clone and start Kokoro-FastAPI server
2. Ensure it's running on `localhost:8880`
3. TTS controls will appear automatically in chapter views




## 📖 Writing Workflow

### Project Dashboard
- **Create new projects** or import existing manuscripts
- **View all projects** with metadata and progress tracking
- **Quick project switching** with context preservation

### Novel Development Process
1. **📍 World Building**: Create immersive settings, cultures, and lore
2. **👥 Character Development**: Design compelling characters with depth
3. **📋 Outline Creation**: Structure your story with detailed chapter plans
4. **✍️ Chapter Writing**: Generate and refine individual chapters
5. **🎧 Audio Generation**: Convert chapters to high-quality audiobooks

### Import & Export
- **Import existing work** from .txt, .docx, or .epub files
- **AI analysis** automatically extracts world, characters, and themes
- **Export projects** in multiple formats for sharing or backup

## 💻 Usage

1. **Start the application**: `uvicorn hypewriter:app --reload`
2. **Open browser**: Navigate to `http://localhost:8000`
3. **Create or import** a project from the dashboard
4. **Follow the guided workflow** using conversational AI interactions
5. **Generate audiobooks** with the built-in TTS system

## 📁 Project Structure

Projects are stored in JSON format in the `library/` directory:

```
library/
├── projects.json                    # Project metadata and index
├── Project-Name-abc123def/         # Individual project directories
│   ├── metadata.json              # Project metadata and settings
│   ├── world.json                 # World building data
│   ├── characters.json            # Character profiles and relationships
│   ├── outline.json               # Story structure and chapter outlines
│   ├── chapters.json              # Chapter metadata
│   └── chapters/                  # Generated content
│       ├── chapter_1.txt          # Chapter text content
│       ├── chapter_1.mp3          # Generated audiobook files
│       └── ...
```

## 🛠️ Development Commands

### Backend
- **Start server**: `uvicorn hypewriter:app --reload`
- **Code quality**: `black .`, `flake8 .`, `mypy .`
- **Tests**: `pytest`

### Frontend
- **Development**: `cd frontend && npm run dev`
- **Build**: `cd frontend && npm run build`
- **Lint**: `cd frontend && npm run lint`
- **Type check**: `cd frontend && npm run check`

## ⚙️ Configuration

Configure via `.env` file:
- **GOOGLE_API_KEY**: Your Google Gemini API key
- **GEMINI_MODEL_NAME**: Model to use (default: gemini-1.5-flash)
- **APP_SECRET_KEY**: Secret key for session management

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/hype-Writer/hypeWriter/blob/main/LICENSE) file for details.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

Built with ❤️ using Svelte 5, FastAPI, and Google Gemini AI
