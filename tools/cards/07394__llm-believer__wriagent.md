---
id: tool-07394
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 需API密钥, 英文文档]
title: wriagent
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/llm-believer/wriagent
created: 2026-07-18
updated: 2026-07-18
no: 7394
category: 画龙补充 / 扩容入库 — 补充源
repo: llm-believer/wriagent
stars: 0
url: https://github.com/llm-believer/wriagent
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 875ba338228780ca
  - methods/QUICK_START.md
---

# llm-believer/wriagent

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/llm-believer/wriagent
- **Stars**：0
- **语言**：Python
- **License**：Apache-2.0
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：wriagent
- **拉取时间**：2026-07-25 19:20:35

---

# Novel Writing Agent / 小说写作助手

An AI-powered agent for collaborative novel writing with long-term memory, built using LangChain. Supports multiple AI providers including OpenAI GPT and Google Gemini. **Full Chinese language support included** for Chinese users. The agent guides you through the entire novel writing process from initial concept to completed chapters.

一个基于LangChain构建的智能小说写作助手，具有长期记忆功能。支持OpenAI GPT和Google Gemini等多个AI提供商。**完全支持中文**，专为中文用户优化。助手将指导您完成从初始概念到完整章节的整个小说写作过程。

## Features / 功能特性

### 📖 **Complete Novel Writing Workflow / 完整的小说写作流程**
- **Planning Phase / 规划阶段**: Interactive discussion to develop story concept, characters, and plot / 交互式讨论，发展故事概念、角色和情节
- **Guideline Generation / 指导原则生成**: Automatic creation of writing guidelines based on your preferences / 根据您的偏好自动创建写作指导原则
- **Chapter Writing / 章节写作**: AI-assisted chapter-by-chapter writing with context awareness / AI辅助的逐章写作，具有上下文感知能力
- **Chapter Revision / 章节修订**: Ability to rewrite chapters based on feedback / 根据反馈重写章节的能力
- **Long-term Memory / 长期记忆**: Persistent storage of all story elements, characters, and written content / 持久存储所有故事元素、角色和已写内容

### 🌏 **Chinese Language Support / 中文语言支持**
- **Auto Language Detection / 自动语言检测**: Automatically detects Chinese or English input / 自动检测中文或英文输入
- **Chinese Character Counting / 中文字符计数**: Proper character-based counting for Chinese text / 中文文本的正确字符计数
- **Bilingual Interface / 双语界面**: Complete Chinese UI and prompts / 完整的中文用户界面和提示
- **Cultural Context / 文化语境**: Chinese-optimized writing suggestions and guidelines / 针对中文优化的写作建议和指导原则

### 🧠 **Intelligent Memory System**
- **Character Profiles**: Detailed character information with personality, backstory, and role
- **Plot Tracking**: Organized plot points with importance levels and chapter assignments
- **Writing Guidelines**: Consistent tone, style, and thematic direction
- **Chapter History**: Complete revision history and word count tracking

### 🤖 **AI-Powered Features**
- **Multiple AI Providers**: OpenAI GPT, Google Gemini, or Local LLMs (HuggingFace models)
- **Context-Aware Writing**: Each chapter considers previous content and character development
- **Smart Suggestions**: Get AI suggestions for what should happen in upcoming chapters
- **Style Consistency**: Maintains your chosen writing style throughout the novel
- **Feedback Integration**: Rewrites incorporate specific user feedback and requests
- **Local LLM Support**: Run models locally without API costs or internet dependency

## Installation

1. **Clone or download this repository**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up AI Provider** (choose one):

   **Option A: Cloud APIs** (Recommended for beginners)
   - Copy `.env.example` to `.env`
   - Add your API key(s). You need at least one:
     ```bash
     # For OpenAI GPT models
     OPENAI_API_KEY=your_openai_api_key_here
     
     # For Google Gemini models  
     GOOGLE_API_KEY=your_google_api_key_here
     
     # Optional: Set default provider
     DEFAULT_LLM_PROVIDER=openai  # or gemini
     ```

   **Option B: Local LLMs** (No API costs, runs offline)
   - Install additional dependencies:
     ```bash
     pip install transformers torch accelerate bitsandbytes
     ```
   - Copy `.env.example` to `.env` and configure local LLM settings:
     ```bash
     # Set local as default provider
     DEFAULT_LLM_PROVIDER=local
     
     # Choose your local model (shorthand or full HuggingFace name)
     LOCAL_LLM_MODEL=phi-2  # Options: phi-2, mistral-7b, llama2-7b, etc.
     
     # Optional: Optimize for your hardware
     LOCAL_LLM_DEVICE=auto     # auto, cpu, cuda, mps
     LOCAL_LLM_4BIT=true       # Enable 4-bit quantization (saves ~75% memory)
     LOCAL_LLM_MAX_TOKENS=2000
     LOCAL_LLM_TEMPERATURE=0.7
     ```
   - No API keys needed! See [Local LLM Guide](https://github.com/llm-believer/wriagent/blob/main/docs/LOCAL_LLM_GUIDE.md) for details

## Quick Start / 快速开始

### Using the CLI Demo / 使用命令行演示

Run the interactive demo:
```bash
python novel_writer.py
```

The CLI will guide you through:
1. **Project Creation**: Name your novel project
2. **Language Selection**: Choose Chinese (zh) or English (en), or let it auto-detect
3. **Planning Phase**: Discuss your story concept with the AI
4. **Character & Plot Development**: Add characters and plot points
5. **Writing Phase**: Write chapters one by one
6. **Revision**: Rewrite chapters based on feedback

运行交互式演示:
```bash
python novel_writer.py
```

命令行界面将指导您完成:
1. **项目创建**: 为您的小说项目命名
2. **语言选择**: 选择中文(zh)或英文(en)，或让它自动检测
3. **规划阶段**: 与AI讨论您的故事概念
4. **角色和情节发展**: 添加角色和情节点
5. **写作阶段**: 逐一写作章节
6. **修订**: 根据反馈重写章节

### Using the Agent Programmatically / 编程使用

```python
from novel_agent import NovelWritingAgent

# Initialize agent with default provider
agent = NovelWritingAgent("my_novel")

# Or specify provider and language explicitly
agent = NovelWritingAgent("my_novel", llm_provider="gemini", language="zh")

# Or with custom parameters
agent = NovelWritingAgent("my_novel", llm_provider="openai", language="en", temperature=0.8)

# Chinese example / 中文示例
agent = NovelWritingAgent("我的小说", language="zh")

# Start planning discussion / 开始规划讨论
response = agent.start_novel_planning()
print(response)  # Will be in Chinese if language="zh"

# Add Chinese character / 添加中文角色
character = agent.add_character(
    name="李小明",
    description="年轻的工程师",
    personality="聪明、勇敢",
    backstory="来自农村的天才少年",
    role="主角"
)

# Start planning discussion
response = agent.start_novel_planning()
print(response)

# Continue discussion
response = agent.continue_discussion("I want to write a sci-fi thriller about AI")
print(response)

# Finalize planning
result = agent.finalize_planning("yes")

# Add a character
character = agent.add_character(
    name="Alex Chen",
    description="A brilliant AI researcher",
    personality="Curious but cautious",
    backstory="Lost parents in tech accident",
    role="Protagonist"
)

# Write first chapter
result = agent.write_next_chapter(
    chapter_title="The Discovery",
    specific_instructions="Focus on introducing Alex and the mysterious AI signal"
)

# Get the chapter
chapter = result['chapter']
print(f"Chapter: {chapter.title}")
print(f"Content: {chapter.content}")
```

## Architecture

### Core Components

1. **LLMFactory** (`llm_factory.py`)
   - Multi-provider LLM support (OpenAI GPT, Google Gemini)
   - Automatic provider selection and fallback
   - Configurable LLM parameters

2. **NovelMemory** (`memory_system.py`)
   - Persistent storage for all novel elements
   - JSON-based file system for reliability
   - Structured data models for characters, plot, chapters, and guidelines

3. **NovelDiscussionAgent** (`discussion_module.py`)
   - Interactive planning and concept development
   - Character and plot suggestion generation
   - Writing guideline creation

4. **ChapterWriter** (`chapter_writer.py`)
   - Context-aware chapter generation
   - Chapter revision capabilities
   - Next chapter suggestions

5. **NovelWritingAgent** (`novel_agent.py`)
   - Main orchestrator that integrates all components
   - High-level API for novel writing workflow
   - Phase management (planning → writing → revision)

### Memory Structure

Projects are stored in the `projects/` directory:
```
projects/
└── your_novel_name/
    ├── characters.json     # Character profiles
    ├── plot.json          # Plot points and story structure
    ├── chapters.json      # Written chapters with metadata
    └── guidelines.json    # Writing style and guidelines
```

## Multi-LLM Support

The agent supports multiple AI providers, allowing you to choose between different models based on your preferences, availability, and cost considerations.

### Supported Providers

1. **OpenAI** (provider: `"openai"`)
   - Models: GPT-3.5, GPT-4
   - Requires: `OPENAI_API_KEY`
   - Known for: High quality, consistent output

2. **Google Gemini** (provider: `"gemini"`)
   - Models: Gemini Pro
   - Requires: `GOOGLE_API_KEY`
   - Known for: Fast response, good reasoning

### Provider Selection

```python
from novel_agent import NovelWritingAgent
from llm_factory import LLMFactory

# Check available providers
available = LLMFactory.get_available_providers()
print(f"Available: {available}")

# Auto-select (uses first available)
agent = NovelWritingAgent("my_novel")

# Specify provider
agent = NovelWritingAgent("my_novel", llm_provider="gemini")

# Custom parameters
agent = NovelWritingAgent("my_novel", 
                         llm_provider="openai",
                         temperature=0.9,
                         max_tokens=1500)
```

### Fallback Behavior

The agent automatically falls back to available providers:
1. If specified provider fails, tries auto-selection
2. If no providers available, raises informative error
3. Provider preferences are preserved in error messages

## API Reference

### NovelWritingAgent Methods

#### Planning Phase
- `start_novel_planning()` - Begin interactive planning
- `continue_discussion(user_input)` - Continue planning conversation
- `finalize_planning()` - Complete planning and generate guidelines

#### Content Management
- `add_character(name, description, personality, backstory, role)` - Add character
- `add_plot_point(title, description, chapter_number, importance)` - Add plot point

#### Writing Phase
- `write_next_chapter(title, instructions)` - Write next chapter in sequence
- `rewrite_chapter(chapter_number, feedback, changes)` - Revise existing chapter
- `get_next_chapter_suggestions()` - Get AI suggestions for next chapter

#### Information Retrieval
- `get_chapter(chapter_number)` - Retrieve specific chapter
- `get_all_chapters()` - Get all chapters with statistics
- `get_novel_status()` - Comprehensive project status
- `export_novel(format)` - Export complete novel

## Examples

### Planning a Mystery Novel

```python
agent = NovelWritingAgent("mystery_novel")

# Start planning
agent.start_novel_planning()
agent.continue_discussion("I want to write a cozy mystery set in a small bookstore")
agent.continue_discussion("The main character should be the bookstore owner who solves crimes")
agent.continue_discussion("The tone should be light and humorous, not dark")

# Finalize planning
agent.finalize_planning("yes")

# Add characters
agent.add_character(
    name="Emma Hartwell",
    description="Bookstore owner and amateur detective",
    personality="Witty, observant, loves puzzles",
    backstory="Former librarian who inherited the bookstore",
    role="Protagonist"
)

agent.add_character(
    name="Detective Mike Torres",
    description="Local police detective",
    personality="By-the-book but appreciates Emma's insights",
    backstory="Recently transferred from the city",
    role="Supporting character"
)

# Add plot points
agent.add_plot_point(
    title="Murder at the Book Club",
    description="A member of the weekly book club is found dead in the store",
    importance="major"
)

agent.add_plot_point(
    title="Discovery of the Hidden Room",
    description="Emma finds a secret room behind the bookshelf with clues",
    chapter_number=3,
    importance="major"
)
```

### Writing and Revising Chapters

```python
# Write first chapter
result = agent.write_next_chapter(
    chapter_title="A Deadly Discussion",
    specific_instructions="Introduce Emma and the book club, end with the discovery of the body"
)

chapter = result['chapter']
print(f"Written: {chapter.title} ({chapter.word_count} words)")

# Get suggestions for next chapter
suggestions = agent.get_next_chapter_suggestions()
print("Suggestions:", suggestions)

# Write second chapter
agent.write_next_chapter(
    chapter_title="Enter Detective Torres",
    specific_instructions="Focus on the police investigation and Emma's first meeting with Torres"
)

# Rewrite first chapter based on feedback
agent.rewrite_chapter(
    chapter_number=1,
    feedback="The pacing is too slow. Add more tension and move the discovery earlier.",
    specific_changes="Have the body discovered within the first 500 words"
)
```

## Customization

### Adjusting AI Behavior

You can customize the AI's behavior by modifying the prompts in the respective modules:

- **Chapter Writing Style**: Edit `_create_writing_prompt()` in `chapter_writer.py`
- **Discussion Flow**: Modify prompts in `discussion_module.py`
- **Memory Context**: Adjust `_build_chapter_context()` for different context priorities

### Adding Export Formats

Extend the `export_novel()` method in `novel_agent.py` to support additional formats:

```python
def export_novel(self, format_type: str = "text") -> str:
    if format_type.lower() == "markdown":
        # Add markdown export logic
    elif format_type.lower() == "epub":
        # Add EPUB export logic
    # ... existing text format logic
```

## Troubleshooting

### Common Issues

1. **API Key Errors**
   - Ensure your OpenAI API key is correctly set in the `.env` file
   - Verify you have sufficient API credits

2. **Memory Not Persisting**
   - Check that the `projects/` directory has write permissions
   - Ensure the project name doesn't contain invalid file system characters

3. **Chapter Context Issues**
   - The agent automatically manages context, but very long novels may hit token limits
   - Consider summarizing early chapters if the context becomes too large

### Performance Tips

- **Faster Response**: Reduce `max_tokens` in the LLM initialization
- **Better Quality**: Increase `temperature` for more creative writing
- **Consistency**: Lower `temperature` for more predictable output

## Testing

The project includes comprehensive unit tests to ensure reliability:

```bash
# Install test dependencies (included in requirements.txt)
pip install -r requirements.txt

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_memory_system.py

# Run with coverage
pytest --cov=. --cov-report=html
```

### Test Coverage

- **Memory System**: Data persistence, character/plot management, guidelines
- **LLM Factory**: Multi-provider support, fallback behavior, configuration
- **Discussion Module**: Planning conversations, character suggestions, guidelines
- **Chapter Writer**: Content generation, rewriting, context building
- **Novel Agent**: Integration tests, complete workflow validation

### Running Tests

All tests use mocking for LLM calls, so no API keys are required for testing. The tests verify:

- Component initialization and configuration
- Data flow between components
- Error handling and edge cases
- Complete workflow integration
- Multi-provider LLM support

## Contributing

This is a foundational implementation. Areas for enhancement:

- **Advanced Memory**: Vector databases for semantic search
- **Additional LLM Providers**: Claude, Llama, local models
- **Rich Exports**: PDF, EPUB, and formatted document generation
- **Collaboration**: Multi-user support and version control
- **Analytics**: Writing statistics and progress tracking
- **UI Interface**: Web-based or desktop GUI

### Development Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `pytest`
4. Set up API keys in `.env`
5. Run demo: `python novel_writer.py`

related:
  - methods/QUICK_START.md
---

**Happy Writing! 📚✨**
