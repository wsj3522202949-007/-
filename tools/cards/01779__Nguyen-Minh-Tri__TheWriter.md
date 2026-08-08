---
id: tool-01779
type: tool
area: 库
status: active
tags: [Python, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: TheWriter
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/nguyen-minh-tri/thewriter
created: 2026-07-18
updated: 2026-07-18
no: 1779
category: 二、网文 / 长篇 AI 写作系统 库
repo: Nguyen-Minh-Tri/TheWriter
stars: 0
url: https://github.com/nguyen-minh-tri/thewriter
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 8ff3b00595d72939
  - methods/最强写作方法论_全球最强综合版.md
---

# Nguyen-Minh-Tri/TheWriter

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/nguyen-minh-tri/thewriter
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：CLI-first AI novel-writing tool with graph memory
- **本地描述**：CLI-first AI novel-writing tool with graph memory
- **拉取时间**：2026-07-23 23:30:54

---

# TheWriter

A CLI-first AI novel-writing tool with graph memory.

## Features

- **Interactive Shell**: Beautiful animated shell for continuous writing sessions
- **CLI-first design**: All interactions via commands
- **Plain text storage**: All data in human-editable YAML/JSON files
- **Character memory**: Track events, relationships, and development
- **Chapter management**: Organize chapters and scenes with word counts
- **Plot tracking**: Manage plot threads, beats, and conflicts
- **Worldbuilding**: Create locations, lore, items, and rules
- **Graph memory**: Semantic search and cross-references
- **Consistency checking**: Find contradictions and missing references
- **AI assistance**: Optional integration with local or cloud LLMs

## Installation

```bash
pip install thewriter
```

## Quick Start

### Interactive Shell Mode (Recommended)

```bash
# Start the interactive shell
novel shell

# Or from within a project directory
cd my-novel
novel shell
```

The interactive shell provides:
- 🎨 Beautiful animated interface
- 📚 Auto-detection of your project
- 💾 Continuous session with all commands
- ✨ Context-aware prompts showing your novel name

```
                   ╔═══════════════════════════════════════╗
                   ║          T H E W R I T E R            ║
                   ║        ~ CLI Novel Writing ~          ║
                   ╚═══════════════════════════════════════╝

My Novel ❯ character create --name "Elena"
My Novel ❯ chapter new --title "The Beginning"
My Novel ❯ write                    # Opens latest chapter in editor
My Novel ❯ status
My Novel ❯ help
My Novel ❯ quit
```

### Single Commands (Alternative)

```bash
# Create a new project
novel init --name "My Novel"

# Add a character
novel character create --name "Alice"

# Create a chapter
novel chapter new --number 1

# Start writing
novel chapter open 1

# Check consistency
novel lint
```

## Interactive Shell Commands

| Command | Description |
|---------|----------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| `character create/show/list/edit/log/connect` | Manage characters |
| `chapter new/open/list/scene/status` | Manage chapters |
| `plot add/list/beat/update` | Track plot threads |
| `world location/lore/item/rule` | Worldbuilding |
| `memory query/hint/graph` | Search and hints |
| `ai suggest/ask/character` | AI assistance |
| `export compile/stats/backup` | Export options |
| `status` | Show project status |
| `lint` | Check consistency |
| `write` | Open latest chapter for writing |
| `switch` | Switch to another project |
| `clear` | Clear screen |
| `help` | Show all commands |
| `quit` | Exit shell |

## CLI Commands

### Project Management
- `novel init` - Initialize a new project
- `novel status` - Show project status
- `novel config` - View/edit configuration
- `novel backup` - Create a backup

### Characters
- `novel character create` - Create a character
- `novel character list` - List all characters
- `novel character show <id>` - Show character details
- `novel character log-event <id>` - Log an event
- `novel character connect <id1> <id2>` - Create relationship

### Chapters
- `novel chapter new` - Create a chapter
- `novel chapter list` - List chapters
- `novel chapter open <id>` - Edit a chapter
- `novel chapter add-scene <id>` - Add a scene
- `novel chapter stats` - Word count statistics

### Plot
- `novel plot add` - Add plot thread
- `novel plot list` - List plot threads
- `novel plot add-beat <id>` - Add a plot beat
- `novel plot add-arc` - Add a story arc
- `novel plot add-conflict` - Add a conflict

### Worldbuilding
- `novel world location-create` - Create a location
- `novel world lore-add` - Add lore entry
- `novel world item-add` - Add an item
- `novel world rule-add` - Add a world rule

### Memory & Search
- `novel memory query <text>` - Search entities
- `novel memory hint` - Get context hints
- `novel memory graph` - Export as DOT graph

### AI Assistance
- `novel ai suggest` - Get writing suggestions
- `novel ai ask <question>` - Ask about your story
- `novel ai character <id>` - Get character insights

### Export
- `novel export compile` - Compile manuscript
- `novel export stats` - Show statistics
- `novel export backup` - Create backup

## Project Structure

All novels are stored in `~/novels/` by default (configurable):

```
~/novels/my-novel/
├── .novelrc          # Project configuration
├── characters/       # Character profiles (YAML)
├── chapters/         # Chapter content (YAML)
├── plots/            # Plot threads (YAML)
├── locations/        # World locations (YAML)
├── lore/             # Worldbuilding (YAML)
├── items/            # Important items (YAML)
├── rules/            # World rules (YAML)
├── exports/          # Generated exports
└── backups/          # Project backups
```

## Configuration

Edit `.novelrc` to customize:

```yaml
name: My Novel
author: Your Name
target_word_count: 80000
ai_enabled: true
ai_provider: ollama  # or openai, anthropic
ai_model_name: llama2
```

## Typical Workflow

```bash
# Start interactive shell
novel shell

# In the shell:
My Novel ❯ character create --name "Elena" --occupation "Archaeologist"
My Novel ❯ character create --name "Marcus"
My Novel ❯ character connect elena marcus --relation romantic

My Novel ❯ world location --name "Crystal Palace"
My Novel ❯ world lore --title "The Ancient Order"

My Novel ❯ plot add --title "Main Quest"
My Novel ❯ plot beat main-quest "Elena finds the map"

My Novel ❯ chapter new --title "The Discovery"
My Novel ❯ write                          # Opens editor

My Novel ❯ status
My Novel ❯ lint
My Novel ❯ export compile
```

## License

MIT
