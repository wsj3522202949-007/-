---
id: tool-01342
type: tool
area: 库
status: active
tags: [RAG, Python, 协议未明, 需API密钥, 英文文档, 人物设定]
title: BookCreator
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/cjwpenner/bookcreator
created: 2026-07-18
updated: 2026-07-18
no: 1342
category: 二、网文 / 长篇 AI 写作系统 库
repo: cjwpenner/BookCreator
stars: 0
url: https://github.com/cjwpenner/bookcreator
tier: "C"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# cjwpenner/BookCreator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/cjwpenner/bookcreator
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered mystery novel writing tool with Agatha Christie-style structure
- **本地描述**：AI-powered mystery novel writing tool with Agatha Christie-style structure
- **拉取时间**：2026-07-23 23:18:15

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Mystery Novel AI Co-Writer

An AI-powered tool for co-writing Agatha Christie-style mystery novels, featuring context-aware chapter generation, character management, and manuscript export.

## Features

- **AI Co-Writing**: Generate chapters using Claude or ChatGPT with customizable temperature
- **Story Consistency**: Maintains character profiles and plot points across chapters
- **Context Management**: Graph-based story tracking to handle 50K word novels
- **Chapter-by-Chapter Writing**: Split-pane interface for AI generation and human editing
- **Export Options**: Download complete manuscript as DOCX or TXT
- **Fair-Play Mystery**: Built-in clue tracking and red herring management

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Keys
Edit `.streamlit/secrets.toml` and add your API keys:

```toml
ANTHROPIC_API_KEY = "your_anthropic_key_here"
OPENAI_API_KEY = "your_openai_key_here"
```

### 3. Run the Application
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Usage

### Writing Workflow

1. **Load Story Context**: Click "Load Story Bible Context" to load the complete story bible
2. **Select Chapter**: Choose chapter number (1-15) and enter a title
3. **Generate Content**: Click "Generate Chapter" to create AI content
4. **Edit & Refine**: Use the right pane to edit the AI-generated content
5. **Save Chapter**: Click "Save Chapter" to commit your edits

### Story Management

- **Characters Tab**: Manage character profiles, secrets, and status
- **Story Graph Tab**: Add plot points, clues, and track story elements
- **Statistics Tab**: Monitor word count and chapter completion
- **Export Tab**: Download your completed manuscript

### Context Window Management

The tool automatically manages context by:
- Loading the story bible for consistency
- Summarizing recent chapters for continuity
- Tracking character arcs and plot points
- Maintaining clue placement and red herrings

## Story Structure

The tool is configured for a 15-chapter Agatha Christie-style mystery:

- **Target Length**: ~50,000 words (3,000-3,500 words per chapter)
- **Setting**: 1930s English countryside house party
- **Detective**: Arina Kravchenko (housekeeper with police background)
- **Style**: Golden Age detective fiction with fair-play clues

## Database Schema

The app uses SQLite to store:
- **Chapters**: Content, AI generations, word counts, status
- **Characters**: Profiles, secrets, motivations, current status
- **Plot Points**: Clues, red herrings, importance ratings
- **Story Graph**: Relationship tracking and context summaries

## Architecture

```
Frontend (Streamlit)
├── Chapter Writing Interface
├── Character Management
├── Plot Tracking
└── Export Tools

Backend (Python)
├── LLM Integration (Claude/ChatGPT)
├── Database Management (SQLite)
├── Story Graph (NetworkX)
└── Export Engine (python-docx)
```

## File Structure

```
BookCreator/
├── app.py                 # Main Streamlit application
├── STORY_BIBLE.md         # Complete story reference
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .streamlit/
│   └── secrets.toml       # API keys (not committed)
└── novel.db              # SQLite database (auto-created)
```

## Customization

### Adding New LLM Providers
Extend the `LLMManager` class in `app.py` to support additional providers.

### Modifying Story Structure
Edit `STORY_BIBLE.md` to change characters, plot, or chapter structure.

### Custom Export Formats
Extend the `export_manuscript()` function to support additional formats.

## Tips for Best Results

1. **Temperature Settings**:
   - Use 0.3-0.5 for dialogue and plot consistency
   - Use 0.7-0.9 for creative descriptions and atmosphere

2. **Chapter Generation**:
   - Always load story context before generating
   - Review and edit AI content for consistency
   - Save chapters regularly to maintain progress

3. **Character Management**:
   - Update character status after major plot events
   - Track secrets and motivations for red herrings
   - Use character arcs to drive plot development

4. **Plot Tracking**:
   - Mark clues as "real" or "red herring"
   - Rate importance 1-5 for context prioritization
   - Add plot points immediately after writing scenes

## Troubleshooting

### API Issues
- Check that your API keys are correctly formatted in `secrets.toml`
- Verify you have sufficient API credits
- Try reducing max_tokens if hitting rate limits

### Performance
- The app uses caching to improve performance
- Large chapters (>4000 words) may be slow to process
- Consider breaking very long chapters into scenes

### Database Issues
- Delete `novel.db` to reset all data
- Export your work regularly as backup
- Use the Statistics tab to monitor data integrity

## Contributing

This tool is designed for your specific mystery novel project. Feel free to modify the code to suit your writing needs.

## License

This project is for personal use in writing your mystery novel.
