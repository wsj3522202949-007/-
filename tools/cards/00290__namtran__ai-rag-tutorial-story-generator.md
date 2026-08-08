---
id: tool-00290
type: tool
area: 库
status: active
tags: [RAG, Python, 协议未明, 需API密钥, 英文文档, 人物设定]
title: ai-rag-tutorial-story-generator
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/namtran/ai-rag-tutorial-story-generator
created: 2026-07-18
updated: 2026-07-18
no: 290
category: 二、网文 / 长篇 AI 写作系统 库
repo: namtran/ai-rag-tutorial-story-generator
stars: 3
url: https://github.com/namtran/ai-rag-tutorial-story-generator
tier: "B"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 465a70d56a2a9b13
  - methods/最强写作方法论_全球最强综合版.md
---

# namtran/ai-rag-tutorial-story-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/namtran/ai-rag-tutorial-story-generator
- **Stars**：3
- **语言**：Python
- **License**：None
- **Topics**：ai, chromadb, ollama, openai, rag, story-generator
- **GitHub 描述**：Learn RAG (Retrieval-Augmented Generation) by building a story generator that learns writing styles from your ebook collection
- **本地描述**：Learn RAG (Retrieval-Augmented Generation) by building a story generator that learns writing styles from your ebook collection
- **拉取时间**：2026-07-23 22:47:31

---

# AI RAG Story Generator

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Ollama](https://img.shields.io/badge/Ollama-Supported-purple.svg)](https://ollama.ai)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange.svg)](https://openai.com)

> **A hands-on tutorial for learning RAG (Retrieval-Augmented Generation)** through building a story generator that learns writing styles from your ebook collection.

<p align="center">
  <img src="https://img.shields.io/badge/Tutorial-RAG-red?style=for-the-badge" alt="RAG Tutorial"/>
  <img src="https://img.shields.io/badge/ChromaDB-Vector_DB-blue?style=for-the-badge" alt="ChromaDB"/>
  <img src="https://img.shields.io/badge/LLM-Multi_Backend-green?style=for-the-badge" alt="Multi LLM"/>
</p>

<p align="center">
  <img src="ai-story-generator.jpg" alt="AI Story Generator Screenshot" width="800"/>
</p>

## About This Project

**This repository is primarily a tutorial/learning resource for understanding RAG (Retrieval-Augmented Generation).** It demonstrates how to build a complete RAG pipeline from scratch, using story generation as a practical example.

### What You'll Learn

- How RAG works end-to-end (from data ingestion to generation)
- Building a vector database with ChromaDB
- Text chunking and embedding strategies
- Similarity search and retrieval
- Prompt engineering with retrieved context
- Integrating multiple LLM backends

### Tutorial Focus

This project prioritizes **educational clarity** over production optimization. The code is designed to be readable and well-documented, making it ideal for learning RAG concepts.

## Overview

This project uses AI to learn writing styles from your ebook collection and generate new stories in similar styles. **The system can learn ANY writing style** - simply add your favorite books to the `data/raw/` folder and the AI will learn to write in that style!

### Built-in Genre Presets

The web interface includes presets for popular genres:

- **Xianxia/Cultivation** - Chinese fantasy with immortal cultivation
- **Western Fantasy** - Magic schools, wizards, and hidden magical worlds
- **Dark Fantasy** - Political intrigue and morally complex characters
- **Epic Fantasy** - Ancient prophecies, different races, and epic quests
- **Urban Fantasy** - Modern world with hidden supernatural elements
- **Sci-Fi Fantasy** - Futuristic worlds with magical elements

### Custom Styles

Want to generate romance novels? Science fiction? Mystery thrillers? Historical fiction? **Just add books of that genre to your collection!** The RAG system will learn the writing patterns, vocabulary, and narrative style from whatever books you provide.

## What is RAG?

**RAG (Retrieval-Augmented Generation)** is an AI technique that enhances language models by giving them access to external knowledge. Instead of relying solely on what the model learned during training, RAG retrieves relevant information from a custom knowledge base and uses it to generate more accurate, contextual responses.

### How RAG Works in This Project

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Your Ebooks   │────▶│  Text Chunks    │────▶│ Vector Database │
│  (.epub, .pdf)  │     │  (Paragraphs)   │     │   (ChromaDB)    │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
                                                        ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Generated      │◀────│    LLM Model    │◀────│ Similar Style   │
│    Story        │     │ (Ollama/OpenAI) │     │    Samples      │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

**Key Components:**

1. **Knowledge Base**: Your ebook collection serves as the writing style reference
2. **Vector Embeddings**: Text is converted to numerical vectors that capture semantic meaning
3. **Similarity Search**: When generating, the system finds text passages with similar style/context
4. **Augmented Generation**: The LLM uses retrieved passages as style examples to generate new content

### Why RAG for Story Generation?

| Traditional LLM | RAG-Enhanced LLM |
|-----------------|------------------|
| Generic writing style | Learns from YOUR book collection |
| Limited to training data | Access to unlimited custom knowledge |
| Same output for everyone | Personalized to your preferred style |
| Cannot update knowledge | Easy to add new books anytime |

## Process Flow: How Stories Are Generated

Here's the complete end-to-end process from ebooks to generated stories:

### Phase 1: Data Preparation

```
┌──────────────────────────────────────────────────────────────────┐
│                    EBOOK PARSING PIPELINE                        │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  data/raw/                    parse_ebooks.py                    │
│  ┌─────────┐                  ┌─────────────┐      data/txt/     │
│  │ book1.  │                  │             │     ┌─────────┐    │
│  │  epub   │──┐               │  Extracts   │     │ book1.  │    │
│  ├─────────┤  │               │    text     │  ┌──│  txt    │    │
│  │ book2.  │──┼──────────────▶│   from all  │──┤  ├─────────┤    │
│  │  pdf    │  │               │   formats   │  │  │ book2.  │    │
│  ├─────────┤  │               │             │  └──│  txt    │    │
│  │ book3.  │──┘               └─────────────┘     └─────────┘    │
│  │  mobi   │                                                     │
│  └─────────┘                                                     │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

**What happens:**
- `parse_ebooks.py` reads all ebooks from `data/raw/`
- Supports: `.epub`, `.pdf`, `.mobi`, `.prc`, `.txt`
- Extracts clean text content from each book
- Saves as `.txt` files in `data/txt/`

### Phase 2: Building the Vector Database

```
┌──────────────────────────────────────────────────────────────────┐
│                  VECTOR DATABASE PIPELINE                        │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  data/txt/          build_style_db.py            chroma_db/     │
│  ┌─────────┐       ┌───────────────────┐       ┌─────────────┐  │
│  │ book1.  │       │                   │       │             │  │
│  │  txt    │──┐    │ 1. Split into     │       │   Vector    │  │
│  ├─────────┤  │    │    chunks         │       │   Database  │  │
│  │ book2.  │──┼───▶│                   │──────▶│  (ChromaDB) │  │
│  │  txt    │  │    │ 2. Generate       │       │             │  │
│  ├─────────┤  │    │    embeddings     │       │  Stores:    │  │
│  │ book3.  │──┘    │                   │       │  - Vectors  │  │
│  │  txt    │       │ 3. Store in DB    │       │  - Metadata │  │
│  └─────────┘       └───────────────────┘       │  - Text     │  │
│                                                 └─────────────┘  │
│                                                                  │
│  Embedding Model: sentence-transformers/paraphrase-multilingual  │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

**What happens:**
1. **Text Chunking**: Each book is split into smaller passages (chunks)
   - Chunk size: ~500-1000 characters
   - Overlap between chunks to maintain context

2. **Embedding Generation**: Each chunk is converted to a vector
   - Uses SentenceTransformer model
   - Captures semantic meaning of text
   - 384-768 dimensional vectors

3. **Database Storage**: Vectors stored in ChromaDB
   - Enables fast similarity search
   - Stores original text alongside vectors
   - Metadata includes source book info

### Phase 3: Story Generation (Runtime)

```
┌──────────────────────────────────────────────────────────────────┐
│                   STORY GENERATION PIPELINE                      │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  User Input                                                      │
│  ┌─────────────────────────────────────────┐                     │
│  │ Prompt: "A young warrior discovers..."  │                     │
│  │ Genre:  Xianxia                         │                     │
│  │ Length: 1000 tokens                     │                     │
│  └─────────────────────────────────────────┘                     │
│                          │                                       │
│                          ▼                                       │
│  ┌─────────────────────────────────────────┐                     │
│  │         1. QUERY EMBEDDING              │                     │
│  │    Convert prompt to vector             │                     │
│  └─────────────────────────────────────────┘                     │
│                          │                                       │
│                          ▼                                       │
│  ┌─────────────────────────────────────────┐                     │
│  │         2. SIMILARITY SEARCH            │                     │
│  │    Find similar passages in ChromaDB    │                     │
│  │    Returns: Top 5-10 matching chunks    │                     │
│  └─────────────────────────────────────────┘                     │
│                          │                                       │
│                          ▼                                       │
│  ┌─────────────────────────────────────────┐                     │
│  │         3. PROMPT CONSTRUCTION          │                     │
│  │                                         │                     │
│  │    System: "You are a story writer..."  │                     │
│  │    Context: [Retrieved style samples]   │                     │
│  │    User: "Write a story about..."       │                     │
│  └─────────────────────────────────────────┘                     │
│                          │                                       │
│                          ▼                                       │
│  ┌─────────────────────────────────────────┐                     │
│  │         4. LLM GENERATION               │                     │
│  │                                         │                     │
│  │    ┌─────────┐  ┌─────────┐  ┌───────┐  │                     │
│  │    │ Ollama  │  │ OpenAI  │  │ Claude│  │                     │
│  │    │ (Local) │  │  (API)  │  │ (API) │  │                     │
│  │    └─────────┘  └─────────┘  └───────┘  │                     │
│  └─────────────────────────────────────────┘                     │
│                          │                                       │
│                          ▼                                       │
│  ┌─────────────────────────────────────────┐                     │
│  │         5. OUTPUT STORY                 │                     │
│  │    Generated story with learned style   │                     │
│  └─────────────────────────────────────────┘                     │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

**Detailed Steps:**

1. **Query Embedding**
   - User's prompt is converted to a vector using the same embedding model
   - This vector represents the semantic meaning of the request

2. **Similarity Search**
   - ChromaDB finds chunks most similar to the query
   - Uses cosine similarity to rank results
   - Returns passages that match the theme/style

3. **Prompt Construction**
   - System prompt defines the AI's role as a story writer
   - Retrieved passages are injected as "style examples"
   - User's prompt specifies what to write

4. **LLM Generation**
   - The augmented prompt is sent to the LLM
   - Model generates text following the retrieved style
   - Streaming output for real-time display

5. **Output**
   - Complete story in the learned writing style
   - Maintains consistency with source material's tone

### Complete System Architecture

```
┌────────────────────────────────────────────────────────────────────────┐
│                         AI RAG STORY GENERATOR                         │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────────────┐    │
│   │    Ebooks    │───▶│    Parser    │───▶│    Text Files        │    │
│   │  (data/raw)  │    │              │    │    (data/txt)        │    │
│   └──────────────┘    └──────────────┘    └──────────┬───────────┘    │
│                                                      │                 │
│                                                      ▼                 │
│                                           ┌──────────────────────┐    │
│                                           │   Text Chunking      │    │
│                                           │   & Embedding        │    │
│                                           └──────────┬───────────┘    │
│                                                      │                 │
│                                                      ▼                 │
│   ┌──────────────┐                        ┌──────────────────────┐    │
│   │  Web UI      │                        │   ChromaDB           │    │
│   │  (Gradio)    │◀──────────┐            │   Vector Database    │    │
│   └──────┬───────┘           │            └──────────┬───────────┘    │
│          │                   │                       │                 │
│          ▼                   │                       │                 │
│   ┌──────────────┐           │            ┌──────────▼───────────┐    │
│   │  User Input  │───────────┼───────────▶│  Similarity Search   │    │
│   │  - Prompt    │           │            │  (Find style samples)│    │
│   │  - Genre     │           │            └──────────┬───────────┘    │
│   │  - Settings  │           │                       │                 │
│   └──────────────┘           │                       ▼                 │
│                              │            ┌──────────────────────┐    │
│                              │            │  Augmented Prompt    │    │
│                              │            │  + Style Context     │    │
│                              │            └──────────┬───────────┘    │
│                              │                       │                 │
│                              │                       ▼                 │
│                              │            ┌──────────────────────┐    │
│                              │            │      LLM Backend     │    │
│                              │            │  ┌────┐ ┌────┐ ┌───┐ │    │
│                              └────────────│  │Olla│ │Open│ │Cla│ │    │
│                               Generated   │  │ma  │ │AI  │ │ude│ │    │
│                                 Story     │  └────┘ └────┘ └───┘ │    │
│                                           └──────────────────────┘    │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

## Features

- 📚 Parse multiple ebook formats: `.pdf`, `.epub`, `.prc`, `.mobi`, `.txt`
- 🧠 Build vector database for style learning (ChromaDB)
- ✨ Generate stories with learned styles
- 🤖 Support multiple LLM backends:
  - **Ollama** (Local) - Qwen, Gemma, Llama, Mistral
  - **OpenAI API** - GPT-4, GPT-3.5
  - **Google API** - Gemini Pro
  - **Anthropic API** - Claude 3
- 🌐 Web interface (Gradio)
- 💾 All data stored on external drive

## Project Structure

```
ai-rag-story-generator/
├── data/
│   ├── raw/               # Source ebooks (.pdf, .epub, .prc, .mobi, .txt)
│   └── txt/               # Parsed text files
├── generated_stories/     # Output directory for multi-chapter stories
├── models/                # HuggingFace model cache
├── ollama_models/         # Ollama model cache
├── chroma_db/             # Vector database
├── .venv/                 # Python virtual environment
│
├── config.py              # Configuration & prompt templates
├── parse_ebooks.py        # Ebook parser
├── build_style_db.py      # Build vector database
├── generate_with_style.py # Story generator (CLI) + chapter generation
├── generate_long_story.py # Multi-chapter story generator
├── app.py                 # Web interface
│
├── setup.sh               # Setup script
├── run.sh                 # Quick run script
└── requirements.txt       # Python dependencies
```

## Installation

### Prerequisites

- Python 3.10+
- 8GB+ RAM (16GB recommended for larger models)
- macOS, Linux, or Windows

### Quick Setup

```bash
git clone https://github.com/namtran/ai-rag-story-generator.git
cd ai-rag-story-generator
chmod +x setup.sh
./setup.sh
```

### Optional: Install Ollama (for local models)

```bash
# macOS
brew install ollama

# Then pull a model
ollama pull qwen2.5:7b    # Best for multilingual
ollama pull gemma2:9b     # Good balance
ollama pull llama3.1:8b   # Fast, English-focused
```

## Usage

### 1. Activate Environment

```bash
source activate.sh
```

### 2. Add Your Ebooks

Copy ebooks to `data/raw/` directory:

```bash
cp ~/Books/*.epub data/raw/
cp ~/Books/*.pdf data/raw/
```

**Supported formats:** `.pdf`, `.epub`, `.prc`, `.mobi`, `.txt`

> **Tip:** The AI learns from whatever books you provide. Add romance novels for romance style, mystery books for detective fiction, sci-fi for science fiction, etc. The more books of a particular style, the better the AI learns that style!

### 3. Parse Ebooks

```bash
python parse_ebooks.py
```

### 4. Build Style Database

```bash
python build_style_db.py
```

### 5. Generate Stories

**Command Line:**
```bash
python generate_with_style.py
```

**Web Interface:**
```bash
python app.py
# Open http://localhost:7860
```

## Quick Commands

```bash
# Data Pipeline
./run.sh parse       # Parse ebooks from data/raw/
./run.sh build       # Build vector database
./run.sh status      # Check project status

# Story Generation
./run.sh generate    # Generate short story (CLI)
./run.sh chapter     # Generate a full chapter (~3000 words)
./run.sh story       # Generate multi-chapter story (interactive)
./run.sh stories     # List all generated stories
./run.sh resume <id> # Resume an interrupted story

# Web Interface
./run.sh web         # Run web app (Ollama backend)
./run.sh web-api     # Run web app (Cloud API backend)
```

### Generate Multi-Chapter Stories

```bash
# Interactive mode - prompts for all options
python generate_long_story.py --interactive

# Direct generation with parameters
python generate_long_story.py \
  --premise "A young cultivator discovers an ancient artifact" \
  --genre "Xianxia" \
  --chapters 10

# Resume an interrupted story
python generate_long_story.py --resume story_20240101_120000

# List all saved stories
python generate_long_story.py --list
```

**Output:** Stories are saved to `generated_stories/story_YYYYMMDD_HHMMSS/`
- `chapter_01.txt`, `chapter_02.txt`, ... - Individual chapters
- `full_story.txt` - Complete story in one file
- `state.json` - Progress state (for resume capability)

## Story Genres & Examples

### Xianxia / Cultivation (Chinese Fantasy)

Settings: Ancient China-inspired world, cultivation sects, immortal realms

Example prompts:
- "A young orphan discovers an ancient jade pendant that contains the soul of a supreme cultivator"
- "The weakest disciple of a prestigious sect accidentally absorbs forbidden energy"
- "A mortal physician saves a dying immortal and receives a heavenly inheritance"

### Western Fantasy (Magic School)

Settings: Magic schools, wizarding world, hidden magical society

Example prompts:
- "An ordinary teenager discovers a letter inviting them to an academy of magic"
- "A young mage at an ancient academy accidentally unleashes a curse from a forbidden book"
- "Students at a magical school uncover a dark secret in the forbidden library"

### Epic Fantasy (High Fantasy)

Settings: Medieval world, different races, epic quests, ancient evil

Example prompts:
- "A humble blacksmith finds an ancient artifact that kings and dark lords seek"
- "The last elven princess must unite fractured kingdoms against an awakening darkness"
- "A fellowship of unlikely heroes journeys to destroy a cursed artifact"

### Dark Fantasy (Grimdark)

Settings: Political intrigue, morally gray characters, brutal medieval world

Example prompts:
- "The illegitimate child of a murdered lord infiltrates the court of their enemies"
- "A mercenary company discovers their employer plans to unleash an ancient plague"
- "Three kingdoms wage war while an ancient evil stirs in the frozen wastelands"

### Urban Fantasy (Modern Magic)

Settings: Modern world with hidden magic, supernatural creatures

Example prompts:
- "A detective discovers the city's elite are actually immortal supernatural beings"
- "A barista accidentally serves coffee to a deity, who becomes a regular customer"
- "Underground magic duels threaten to expose the hidden magical world"

## Configuration

### Using Cloud APIs (Better Quality)

Set environment variables or edit `config.py`:

```bash
# OpenAI
export OPENAI_API_KEY="sk-..."

# Google Gemini
export GOOGLE_API_KEY="..."

# Anthropic Claude
export ANTHROPIC_API_KEY="sk-ant-..."
```

```python
# config.py
LLM_BACKEND = "openai"  # or "google", "anthropic"
LLM_MODEL = "gpt-4"
```

### Using Local Models (Ollama)

```python
LLM_BACKEND = "ollama"
LLM_MODEL = "qwen2.5:7b"  # or gemma2:9b, llama3.1:8b
```

### Generation Settings

```python
GENERATION_CONFIG = {
    "max_new_tokens": 1000,    # Story length
    "temperature": 0.85,        # Creativity (0.7-1.0)
    "top_p": 0.92,             # Sampling diversity
    "repetition_penalty": 1.15, # Reduce repetition
}
```

## Model Recommendations

| Model | Size | Quality | Speed | Best For |
|-------|------|---------|-------|----------|
| gemma:2b | 1.7GB | ⭐⭐ | Fast | Testing |
| qwen2.5:7b | 4.5GB | ⭐⭐⭐⭐ | Medium | Multilingual |
| llama3.1:8b | 4.7GB | ⭐⭐⭐⭐ | Medium | English |
| gemma2:9b | 5.5GB | ⭐⭐⭐⭐ | Medium | Balanced |
| qwen2.5:14b | 9GB | ⭐⭐⭐⭐⭐ | Slow | Best local |
| GPT-4 | Cloud | ⭐⭐⭐⭐⭐ | Fast | Best overall |
| Claude 3 | Cloud | ⭐⭐⭐⭐⭐ | Fast | Creative writing |

## Current Limitations

> **Note:** This is a tutorial project focused on teaching RAG concepts. It has several limitations compared to production systems:

### RAG Limitations

| Limitation | Description | Potential Improvement |
|------------|-------------|----------------------|
| **Simple chunking** | Fixed-size character chunks | Use semantic chunking or sentence-based splitting |
| **Basic retrieval** | Single-query similarity search | Implement hybrid search (semantic + keyword) |
| **No re-ranking** | Uses raw similarity scores | Add cross-encoder re-ranking for better relevance |
| **Static embeddings** | Pre-computed embeddings only | Fine-tune embeddings on your specific domain |
| **No metadata filtering** | Retrieves from entire database | Add filters by book, genre, author, etc. |

### Story Generation Limitations

| Limitation | Description | Potential Improvement |
|------------|-------------|----------------------|
| **Context window** | Limited by LLM context size | Implement hierarchical summarization |
| **Consistency** | May lose character/plot details over long stories | Add explicit state tracking (character DB, plot graph) |
| **Style drift** | Writing style may vary between chapters | Re-inject style samples more frequently |
| **No editing** | One-shot generation, no revision | Add self-critique and revision loops |
| **Token limits** | Output limited by model's max tokens | Implement scene-by-scene generation for longer chapters |

### Technical Limitations

- **No GPU optimization** - Runs on CPU/MPS, may be slow for large models
- **Single-threaded** - No parallel chunk processing during indexing
- **No caching** - Embeddings regenerated on each build
- **Basic error handling** - Minimal retry logic for API failures

### What This Tutorial Covers vs. Production Needs

```
┌─────────────────────────────────────────────────────────────────┐
│                    THIS TUTORIAL COVERS                         │
├─────────────────────────────────────────────────────────────────┤
│  ✓ Basic RAG pipeline (ingest → embed → store → retrieve)      │
│  ✓ Vector database setup (ChromaDB)                            │
│  ✓ Embedding generation (Sentence Transformers)                │
│  ✓ Prompt engineering with context injection                   │
│  ✓ Multiple LLM backend integration                            │
│  ✓ Simple multi-chapter generation with summaries              │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                 PRODUCTION SYSTEMS WOULD ADD                    │
├─────────────────────────────────────────────────────────────────┤
│  ○ Hybrid search (BM25 + semantic)                             │
│  ○ Query expansion and rewriting                               │
│  ○ Re-ranking with cross-encoders                              │
│  ○ Streaming with chunked responses                            │
│  ○ Evaluation metrics (retrieval quality, generation quality)  │
│  ○ A/B testing for prompt variations                           │
│  ○ Caching layer for embeddings and responses                  │
│  ○ Rate limiting and cost management                           │
│  ○ Observability (logging, tracing, metrics)                   │
└─────────────────────────────────────────────────────────────────┘
```

## Troubleshooting

**"Collection not found" error:**
```bash
python build_style_db.py --reset
```

**"Ollama connection failed":**
```bash
ollama serve  # Start Ollama server
```

**Out of memory:**
- Use smaller model (gemma:2b)
- Reduce max_tokens
- Use cloud API instead

**Slow generation:**
- Use cloud API (faster)
- Use quantized models (e.g., qwen2.5:7b-q4)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - Feel free to use and modify.

## Author

**Nam Tran** - Software Developer

- GitHub: [@namtran](https://github.com/namtran)
- Other Projects:
  - [DiskCleanKit](https://diskcleankit.com) - Disk cleaning utility for macOS
  - [DiskCleanKit MCP](https://github.com/namtran/diskcleankit-mcp) - MCP server for DiskCleanKit
  - [PhoneCleanKit](https://phonecleankit.com) - Phone storage optimization tool

## Acknowledgments

- Built with [Gradio](https://gradio.app), [ChromaDB](https://www.trychroma.com), [Sentence Transformers](https://www.sbert.net)
- Powered by [Ollama](https://ollama.ai), [OpenAI](https://openai.com), [Google AI](https://ai.google), [Anthropic](https://anthropic.com)

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<p align="center">
  <sub>If you find this project useful, please consider giving it a ⭐</sub>
</p>
