---
id: tool-01518
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: skills
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/xjsongphy/skills
created: 2026-07-18
updated: 2026-07-18
no: 1518
category: 二、网文 / 长篇 AI 写作系统 库
repo: xjsongphy/skills
stars: 6
url: https://github.com/xjsongphy/skills
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# xjsongphy/skills

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/xjsongphy/skills
- **Stars**：6
- **语言**：Python
- **License**：None
- **Topics**：academic-writing, agent-skills, ai-agents, automation, claude-code, claude-skills, developer-tools, latex, markdown, prompt-engineering
- **GitHub 描述**：A collection of custom skills for academic writing, automation, specialized workflows, and more to come.
- **本地描述**：A collection of custom skills for academic writing, automation, specialized workflows, and more to come.
- **拉取时间**：2026-07-23 23:23:21

---

# Claude Code Skills

`[中文版 README](README_zh.md)`

A collection of specialized skills for Claude Code to enhance AI performance on specific tasks.

## Overview

These skills provide professional guidance for Claude Code in specific domains, ensuring outputs meet expected format, style, and quality requirements.

## Available Skills

### latex-textbook-writer

**Purpose**: Write professional mathematics textbooks using XeLaTeX

**Features**:
- Definition/theorem box styles
- Correct color scheme (definitions in green, theorems in orange, examples in blue)
- Academic narrative style (explanation before definition)
- English and Chinese template support

**Use Cases**: Mathematics textbook chapters, LaTeX paper formatting, academic documents

**Invoke**: `/latex-textbook-writer`

---

### md-report-writer

**Purpose**: Write professional Markdown reports

**Features**:
- Narrative flow (explanation before technical content)
- Coherent explanations (not step-by-step lists)
- Direct, professional tone (no conversational filler)
- Bold emphasis (no italics)
- Embed code snippets and cite literature
- Simple code: annotate variables; complex code: explain logic in detail

**Use Cases**: Technical reports, progress reports, project documentation, meeting notes

**Invoke**: `/md-report-writer`

---

### update-skill

**Purpose**: Update existing skills based on conversation feedback

**Workflow**:
1. Generate output with a skill
2. Refine through conversation until satisfied
3. Call `/update-skill <skill-name>` to update the skill
4. Next invocation applies the improvements automatically

**Use Cases**: Any situation where skill output needs iterative refinement

**Invoke**: `/update-skill <skill-name>`

---

### syncthing-cleanup

**Purpose**: Clean up unexpected items in Syncthing sync folders

**Features**:
- Automatically identify and clean conflict files (`.sync-conflict-*`)
- Delete empty directories in encrypted folders
- Clean temporary files (`*.swp`, `*~`, `.DS_Store`, `Thumbs.db`, `*.tmp`)
- Remove broken symbolic links
- Integrated with Syncthing REST API for automatic rescan after cleanup
- Includes executable Python cleanup script
- Supports dry-run mode to preview deletions
- Cross-platform support (Linux, macOS, Windows WSL)

**Use Cases**: Syncthing showing unexpected items, sync conflicts, periodic cleanup of sync folders

**Invoke**: `/syncthing-cleanup`

**Script Usage**:
```bash
# Interactive mode
python3 scripts/cleanup_syncthing.py

# Preview mode
python3 scripts/cleanup_syncthing.py --dry-run

# Automatic cleanup
python3 scripts/cleanup_syncthing.py --yes

# Clean specific folders
python3 scripts/cleanup_syncthing.py --folders ~/Develop ~/Codes
```

---

### experiment-report-writer

**Purpose**: Professional LaTeX experiment report writing assistant for physics and engineering

**Features**:
- Narrative flow (explanation before technical content)
- Define-before-use principle for variables and units
- Professional academic tone with complete sentences
- Structured report format with proper section ordering
- LaTeX best practices (equations, figures, tables, units)
- Todo-driven breakdown strategy for multi-section reports

**Use Cases**: Physics experiment reports, engineering lab reports, academic LaTeX documents

**Invoke**: `/experiment-report-writer`

---

### browser

**Purpose**: Control Chrome browser via REST API for browser automation tasks

**Features**:
- Full Selenium control via HTTP endpoints
- Anti-detection (background playback, automation hiding)
- Element find/click/input/screenshot/JS execution
- Window management (switch/close)
- Auto random delays to simulate human behavior

**Use Cases**: Web automation, auto-login, course watching, form filling, web scraping with browser

**Invoke**: `/browser`

**Server Project**: `D:\Develop\AgentInBrowser`

---

## Repository Structure

```
skills/
├── latex-textbook-writer/    # LaTeX textbook writing
│   └── SKILL.md
├── md-report-writer/         # Markdown report writing
│   └── SKILL.md
├── update-skill/             # Skill update utility
│   └── SKILL.md
├── syncthing-cleanup/        # Syncthing cleanup utility
│   ├── SKILL.md
│   ├── scripts/
│   │   ├── cleanup_syncthing.py
│   │   └── test_skill.py
│   ├── references/
│   │   └── implementation_details.md
│   └── evals/
│       └── evals.json
└── README.md                 # This file
```

## Usage

### Invoking a Skill

Use the command directly in Claude Code:

```
/skill-name
```

Examples:
```
/latex-textbook-writer
/md-report-writer
```

### Updating a Skill

When a skill's output needs adjustment:

1. Provide feedback in the conversation
2. Once satisfied, call:
   ```
   /update-skill skill-name
   ```
3. AI analyzes the conversation and updates the skill file
4. Changes are automatically committed to git

## Development

### Adding a New Skill

1. Create a new folder under `skills/`
2. Create `SKILL.md` with:
   - Frontmatter (name, description)
   - Detailed usage guidelines
   - Examples and best practices
3. Commit to git

### Skill File Format

```markdown
---
name: skill-name
description: Brief description
---

# Skill Title

Detailed skill documentation...

## When to Use
...

## Core Principles
...

## Examples
...
```

## Contributing

These skills are customized for personal use. To modify:
1. Edit the corresponding `SKILL.md` file directly
2. Commit to git
3. Or use `/update-skill` to iteratively improve through conversation

## License

MIT License

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

**Author**: xjsongphy
**Repository**: [github.com:xjsongphy/skills.git](https://github.com/xjsongphy/skills)
