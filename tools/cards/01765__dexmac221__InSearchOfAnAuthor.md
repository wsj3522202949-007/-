---
id: tool-01765
type: tool
area: 库
status: active
tags: [多Agent, TTS, Python, 协议宽松, 需API密钥, 英文文档]
title: InSearchOfAnAuthor
summary: 多 Agent 协作自动产文
source: https://github.com/dexmac221/insearchofanauthor
created: 2026-07-18
updated: 2026-07-18
no: 1765
category: 二、网文 / 长篇 AI 写作系统 库
repo: dexmac221/InSearchOfAnAuthor
stars: 0
url: https://github.com/dexmac221/insearchofanauthor
tier: "C"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 仓库疑似停更/归档，bug 不会修、依赖可能过期"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# dexmac221/InSearchOfAnAuthor

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/dexmac221/insearchofanauthor
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：ai-agents, artificial-intelligence, literature, llm, rag, writing-tool
- **GitHub 描述**：Multi-agent LLM system for collaborative book writing inspired by Pirandello. Characters are autonomous AI agents with their own consciousness, memories, and voices.
- **本地描述**：Multi-agent LLM system for collaborative book writing inspired by Pirandello. Characters are autonomous AI agents with their own consciousness, memories, and voices.
- **拉取时间**：2026-07-23 23:30:29

---

# 📖 In Search of an Author

> *"The characters were born alive, so alive that the writer simply gave them the gift of speech"*  
> — Luigi Pirandello

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A **multi-agent LLM system** for collaborative book writing, where characters are autonomous AI agents with their own consciousness, memories, and voices.

---

## 🎭 Philosophy

Inspired by **Pirandello's** *"Six Characters in Search of an Author"* and **Joyce's** stream of consciousness:

- The **orchestrator does NOT write** the story directly
- **Characters ARE separate LLMs** with their own "consciousness"  
- The story **EMERGES from interactions** between characters
- The **world is shared** via RAG, but **perceptions are individual**

## ✨ Features

- 🤖 **Multi-Agent Architecture**: Director, Screenwriter, Characters, Orchestrator, Editor
- 🎭 **Actors-Only Mode**: Pure Pirandellian storytelling—story emerges from characters alone, no director/screenwriter
- 📝 **Git Revision Workflow**: Track book evolution with branches, reviews, and merges per chapter
- 🧠 **Individual Character Memory**: Each character has subjective, distortable memories
- 📚 **Dual Memory Backend**: Choose between RAG (JSON) or PostgreSQL coherent memory
- 🐘 **PostgreSQL Coherent Memory**: Structured relational data for precise context retrieval
- 🎨 **Style Tracking**: Prevents repetitive patterns (body language, atmosphere clichés)
- ✏️ **Automatic Editing**: Show-don't-tell fixes, synonym replacement, voice validation
- 🔧 **YAML Prompt System**: All prompts externalized for easy customization
- 🌍 **Multi-language**: English and Italian support
- 🐳 **Docker Ready**: PostgreSQL and Gitea setup via docker-compose

---

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/in-search-of-an-author.git
cd in-search-of-an-author

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### Configuration

```bash
cp .env.example .env
# Edit .env with your API keys
```

### Usage

```bash
# With OpenAI (RAG backend - default)
python run.py --provider openai --model gpt-5-mini "Your book idea here"

# With PostgreSQL coherent memory
python run.py --provider openai --model gpt-5-mini --memory-backend postgres "Your book idea"

# In English (default is Italian)
python run.py --lang en "A detective discovers their partner is the killer"

# Custom chapters and characters
python run.py --chapters 5 --max-characters 4 "Your epic saga idea"

# 🎭 Actors-Only Mode (Pure Pirandellian)
# Story emerges from character interactions alone—no director, no screenwriter
python run.py --actors-only --provider openai --model gpt-5-mini "A pianist and dancer meet in an abandoned theater"

# With Ollama (local)
python run.py --provider ollama --model llama3.2 "Your idea"
```

### PostgreSQL Setup (Optional)

For structured coherent memory instead of RAG:

```bash
# Start PostgreSQL container
docker-compose up -d

# Verify database is ready
docker exec author_db psql -U author -d narrative_world -c "\\dt"
# Should show 16 tables

# Now run with PostgreSQL backend
python run.py --memory-backend postgres "Your book idea"
```

---

## 🌐 Web Interface

A modern React frontend and REST API for a visual book creation experience.

### Starting the API Server

```bash
# Start API server (port 8000)
python run_api.py

# Or with auto-reload for development
python run_api.py --reload

# API documentation
open http://localhost:8000/docs
```

### Starting the Frontend

```bash
# Install dependencies
cd frontend
npm install

# Start development server (port 3000)
npm run dev

# Open browser
open http://localhost:3000
```

### Features

- 📚 **Dashboard**: View all generated books with status
- ✨ **Create Books**: Form with idea input, language, mode selection
- 📖 **Read Books**: Beautiful markdown rendering of completed books
- 🔄 **Real-time Progress**: Live updates during generation
- 🌍 **Bilingual**: Italian and English interface (toggle in sidebar)
- 🎭 **Actors-Only Mode**: Enable Pirandellian emergent storytelling

### API Endpoints

```bash
# Create a new book
curl -X POST http://localhost:8000/books \
  -H "Content-Type: application/json" \
  -d '{"idea": "A detective discovers their partner is the killer", "language": "en"}'

# List all books
curl http://localhost:8000/books

# Get book status
curl http://localhost:8000/books/{book_id}

# Get book content (completed books only)
curl http://localhost:8000/books/{book_id}/content
```

---

## 🏗️ Architecture

```
                         INPUT: Book Idea
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      DIRECTOR LLM                           │
│  • Defines narrative structure (acts, chapters)             │
│  • Sets rhythm and tone                                     │
│  • Does NOT write content, only structure                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    SCREENWRITER LLM                         │
│  • Creates characters with psychology and voice             │
│  • Builds the world (settings, rules)                       │
│  • Defines conflicts and themes                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                 MEMORY BACKEND (choose one)                 │
├─────────────────────────────────────────────────────────────┤
│  📚 RAG (--memory-backend rag)                              │
│  • JSON-based keyword matching                              │
│  • Locations, Events, Objects, Rules                        │
│  • Frequency control (avoids overusing elements)            │
│  • All LLMs can READ, only Orchestrator can WRITE           │
├─────────────────────────────────────────────────────────────┤
│  🐘 PostgreSQL (--memory-backend postgres)                  │
│  • Relational structured data (16 tables)                   │
│  • Coherent context: only relevant data per scene           │
│  • Character knowledge tracking (who knows what)            │
│  • Event timeline with participants                         │
│  • Relationship mapping between characters                  │
└─────────────────────────────────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│  CHARACTER 1    │  │  CHARACTER 2    │  │  CHARACTER N    │
│  (Separate LLM) │  │  (Separate LLM) │  │  (Separate LLM) │
│                 │  │                 │  │                 │
│  • Identity     │  │  • Identity     │  │  • Identity     │
│  • Memory       │  │  • Memory       │  │  • Memory       │
│  • Voice/Style  │  │  • Voice/Style  │  │  • Voice/Style  │
│  • Cognitive    │  │  • Cognitive    │  │  • Cognitive    │
│    Pattern      │  │    Pattern      │  │    Pattern      │
└─────────────────┘  └─────────────────┘  └─────────────────┘
          │                   │                   │
          └───────────────────┼───────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    ORCHESTRATOR LLM                         │
│  • INTERVIEWS characters ("what do you think? what do you   │
│    do?")                                                    │
│  • Synthesizes into narrative prose                         │
│  • Updates RAG after events                                 │
│  • Does NOT decide what characters think                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                       EDITOR LLM                            │
│  • Fixes show-don't-tell violations                         │
│  • Replaces repetitive words with synonyms                  │
│  • Validates character voice consistency                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                         OUTPUT: book.md
```

### Memory Backend Comparison

| Feature | 📚 RAG (JSON) | 🐘 PostgreSQL |
|---------|--------------|---------------|
| **Data Model** | Flat JSON documents | 16 relational tables |
| **Retrieval** | Keyword matching | SQL queries + joins |
| **Context** | All matching elements | Only scene-relevant data |
| **Knowledge Tracking** | Manual in prompt | Automatic per character |
| **Relationships** | Described in text | Explicit relationship table |
| **Usage Frequency** | Counter per element | DB triggers + views |
| **Setup** | None (built-in) | Docker + PostgreSQL |
| **Best For** | Quick experiments | Complex narratives |

### 🎭 Actors-Only Mode

The most Pirandellian feature: **story emerges from characters alone**, without director or screenwriter.

```bash
# Standard mode
python run.py "Your idea"
#  Director → Screenwriter → Characters → Orchestrator → Editor

# 🎭 Actors-only mode  
python run.py --actors-only "Your idea"
#  Idea → Characters (emergent) → Orchestrator (discovery) → Editor
```

| Aspect | Standard | Actors-Only |
|--------|----------|-------------|
| Structure | Pre-planned chapters | Discovered organically |
| Characters | Full profiles from Screenwriter | Minimal traits from idea |
| World | Detailed upfront | Emerges scene by scene |
| Output | `book_TIMESTAMP/` | `book_emergent_TIMESTAMP/` |

### 📝 Git Revision Workflow

Track book evolution with a Git-based revision system. Each chapter goes through a branch-based review cycle:

```bash
# Enable Git revision tracking
python run.py --with-revisions "Your book idea"

# View book evolution
cd output/book_TIMESTAMP
git log --oneline --graph

# See diff between revisions
git diff HEAD~5 HEAD -- book.md
```

#### Workflow Diagram

```
main ────●────●────●────●────●────●────●────●────●───▶ v1.0
         │    │    │         │    │    │    │
         │    │    │         │    │    │    └── Chapter 3 approved
         │    │    │         │    │    └── Review feedback
         │    │    │         │    └── Draft scenes
         │    │    │         │
         │    │    │         └── draft/chapter-3
         │    │    │
         │    │    └── Chapter 2 approved
         │    └── World/Characters
         └── Structure

```

#### Git Branches Per Chapter

| Branch | Purpose |
|--------|---------|
| `main` | Final approved content |
| `draft/chapter-N` | Working draft with scene commits |
| `review/chapter-N` | Editor feedback and revisions |

#### Generated Commits

```
* (tag: v1.0) Finalize book: "Your Book Title"
* Approve Chapter 3
* Chapter 3 revision: apply editor fixes
* Chapter 3 review: 3 comments
* Scene 3.2: [scene description]
* Scene 3.1: [scene description]
* Start draft for Chapter 3
* Approve Chapter 2
...
* Character: John Smith
* Character: Jane Doe  
* World: setting and rules
* Book structure: 5 chapters
* Initialize book: "Your Book Title"
```

#### Gitea Local GitHub (Optional)

For a web UI to monitor book evolution:

```bash
# Start all services including Gitea
docker-compose up -d

# Access Gitea web UI
open http://localhost:3001

# First time: register admin user
# Then create repository and push your book
cd output/book_TIMESTAMP
git remote add origin http://localhost:3001/your-user/book.git
git push -u origin main
```

---

## 🧠 Key Concepts

### Character Cognitive Patterns

Each character has a unique cognitive style that influences their thoughts, speech, and actions:

| Pattern | Thinking Style | Speech Style | Example |
|---------|---------------|--------------|---------|
| `artist` | Visual metaphors, sensory | Poetic, elliptical | "The light bleeds through..." |
| `philosopher` | Logical chains, abstractions | Precise, structured | "Therefore, we must consider..." |
| `survivor` | Threat assessment, pragmatic | Direct, essential | "We need to move. Now." |
| `dreamer` | Associations, tangents | Fluid, imaginative | "It reminds me of when..." |
| `analytical` | Data-driven, systematic | Technical, detailed | "The probability suggests..." |
| `impulsive` | Gut reactions, emotions | Exclamatory, raw | "I can't stand this anymore!" |
| `cynic` | Skeptical, deconstructive | Ironic, cutting | "Oh sure, that'll work..." |
| `mystic` | Intuitive, symbolic | Enigmatic, layered | "The signs are clear..." |

### Style Usage Tracker

Prevents repetitive patterns like:
- "shoulders slumped" (appears max 2x per chapter)
- "ran a hand through hair"
- "the air crackled with tension"
- "heart raced"

The tracker injects avoidance prompts after patterns are overused.

### Forbidden Words

Each cognitive style has words they would **never** use:

```yaml
artist:
  forbidden_words: ["therefore", "consequently", "thus", "basically"]

philosopher:
  forbidden_words: ["wow", "amazing", "cool", "like", "whatever"]
```

---

## 📁 Project Structure

```
libro_generator/
├── llm/
│   ├── base.py           # Base LLM class (Ollama + OpenAI support)
│   ├── director.py       # Narrative structure
│   ├── screenwriter.py   # World and character creation
│   ├── character.py      # Character agents with validation
│   ├── orchestrator.py   # Scene synthesis
│   └── editor.py         # Post-processing fixes
├── memory/
│   ├── shared_rag.py     # RAG world truth with frequency control
│   ├── coherent_memory.py # PostgreSQL structured memory
│   ├── character_memory.py   # Subjective, distortable memory
│   └── style_tracker.py  # Pattern repetition prevention
├── models/
│   ├── book_structure.py # Chapters, scenes, arcs
│   ├── character_sheet.py # Character definition
│   ├── world.py          # Locations, objects, rules
│   └── mystery_tracker.py # Unresolved narrative threads
├── prompts/              # YAML prompt files
│   ├── director.yaml
│   ├── screenwriter.yaml
│   ├── character.yaml
│   ├── orchestrator.yaml
│   └── editor.yaml
├── db/
│   └── init.sql          # PostgreSQL schema (16 tables)
├── docker-compose.yml    # PostgreSQL container setup
└── output/
    └── [book_timestamp]/
        ├── structure.json
        ├── world.json
        ├── characters/
        └── book.md
```

---

## ⚙️ Configuration

### Environment Variables

```bash
# LLM Provider
LLM_PROVIDER=openai          # or "ollama"
LLM_MODEL=gpt-5-mini        # or "llama3.2"

# API Keys
OPENAI_API_KEY=sk-...

# Ollama (for local use)
OLLAMA_BASE_URL=http://localhost:11434

# Generation settings
DEFAULT_TEMPERATURE=0.7
MAX_TOKENS=2000

# PostgreSQL (for coherent memory backend)
DATABASE_URL=postgresql://author:author_secret@localhost:5432/narrative_world
```

### Prompt Customization

All prompts are in `prompts/*.yaml` and can be customized:

```yaml
# prompts/editor.yaml
synonyms:
  "heart raced":
    - "pulse quickened"
    - "chest tightened"
    - "breath caught"
  
thresholds:
  min_repetitions_to_fix: 2
  max_same_word_per_scene: 2
```

---

## 📊 Quality Controls

| Issue | Solution | Location |
|-------|----------|----------|
| Word repetition | Synonym auto-replacement | `editor.py` |
| Pattern repetition | StyleUsageTracker with avoidance prompts | `style_tracker.py` |
| Unbalanced rhythm | Max 2 lines description, then action/dialogue | `orchestrator.yaml` |
| Voice blending | Forbidden words + validation with retry | `character.py` |
| Overused RAG elements | Frequency limits per element type | `shared_rag.py` |
| Coherent context | PostgreSQL scene-aware queries | `coherent_memory.py` |

---

## 🛠️ Development

### Prerequisites

- Python 3.9+
- OpenAI API key (or Ollama for local use)

### Running Tests

```bash
pytest tests/
```

### Adding a New Cognitive Pattern

1. Edit `prompts/character.yaml`:

```yaml
cognitive_styles:
  your_new_style:
    triggers: ["keyword1", "keyword2"]
    forbidden_words: ["word1", "word2"]
    thinking: "Description of how they think"
    speaking: "Description of how they speak"
    never_do: "What they never do"
    example: "Example thought or speech"
```

---

## 📝 Example Output

```markdown
# The Last Cipher

## Chapter 1: Shadows in the Archive

The dust motes danced in the narrow beam of Sarah's flashlight, 
suspended like frozen stars in the archive's thick air. Her 
fingers traced the spine of a leather-bound ledger, its surface 
cracked like parched earth.

"This is it," she breathed, more to herself than to Marcus 
lurking behind the shelves. "The Thornwood accounts from 1892."

Marcus emerged from the shadows, his jaw tight. "We have maybe 
ten minutes before security sweeps this floor." He checked his 
watch—a nervous tic she'd noticed in their three weeks of 
partnership. "Whatever you're looking for, find it fast."
```

---

## What's Next

- ~~**PostgreSQL Coherent Memory**: Structured relational data~~ ✅
- ~~**Actors-Only Mode**: Pure Pirandellian emergent storytelling~~ ✅
- ~~**REST API**: FastAPI backend for web integration~~ ✅
- ~~**React Frontend**: Modern UI for book generation~~ ✅
- **Export formats**: EPUB, PDF, DOCX generation
- **Embedding-based voice validation**: Detect character voice drift

---

## 🤝 Contributing

Contributions welcome! Please read [CONTRIBUTING.md](https://github.com/dexmac221/InSearchOfAnAuthor/blob/main/CONTRIBUTING.md) first.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📜 License

MIT License - see [LICENSE](https://github.com/dexmac221/InSearchOfAnAuthor/blob/main/LICENSE) for details.

---

## ⚠️ Disclaimer

This software is provided "as is" without warranty of any kind, express or implied. The authors and contributors are **not responsible** for any use, misuse, or consequences arising from the use of this software.

**Important Notes:**
- Content generated by AI may contain inaccuracies, biases, or inappropriate material
- Users are solely responsible for reviewing, editing, and validating generated content before any publication or distribution
- This tool is intended for creative experimentation and educational purposes
- Commercial use of generated content should comply with applicable AI content disclosure regulations
- The authors assume no liability for any damages, legal issues, or ethical concerns arising from content generated using this software

By using this software, you agree to take full responsibility for its use and any content produced with it.

---

## 🙏 Acknowledgments

- **Luigi Pirandello** - For the philosophical foundation
- **James Joyce** - For stream of consciousness techniques
- The open-source LLM community

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

*"The story writes itself through its characters. We merely provide the stage."*
