---
id: tool-00067
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: inkspec
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/openmoto/inkspec
created: 2026-07-18
updated: 2026-07-18
no: 67
category: 二、网文 / 长篇 AI 写作系统 库
repo: openmoto/inkspec
stars: 0
url: https://github.com/openmoto/inkspec
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
  - "⚠️ 仓库疑似停更/归档，bug 不会修、依赖可能过期"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# openmoto/inkspec

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/openmoto/inkspec
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Specification-Driven Storytelling framework: Apply software engineering discipline to fiction writing. Story specs are the single source of truth, ensuring plot consistency and character authenticity.
- **本地描述**：Specification-Driven Storytelling framework: Apply software engineering discipline to fiction writing. Story specs are the single source of truth, ensuring plot consistency and character authenticity.
- **拉取时间**：2026-07-23 22:40:49

---

# Inkspec

**Specification-Driven Storytelling Framework**

Inkspec applies software engineering discipline to fiction writing. Story specifications are the single source of truth, ensuring plot consistency, character authenticity, and thematic coherence throughout the creative process.

## What is Inkspec?

Inkspec is a collaborative fiction writing framework that uses a spec-first workflow to prevent plot holes, maintain character consistency, and track story development with the same rigor as software projects.

### Core Philosophy

- **Spec-First**: Define characters, plot, and world-building through structured requirements before writing prose
- **Traceability**: Every scene, dialogue, and character action traces back to approved specifications
- **Consistency**: Story specifications are the single source of truth
- **Collaboration**: Designed for human authors working with AI assistants

## Key Features

- **Specification-Driven Storytelling (SDS)**: Three-phase workflow from discovery to published prose
- **OpenSpec Integration**: Change management and version control for story development
- **AI-Assisted Writing**: Configured for Claude Code with mandatory confirmation gates
- **Structured Requirements**: Character profiles, plot outlines, scene specifications, and world-building docs
- **Mobile Idea Capture**: Simple inbox system for capturing inspiration on-the-go

## Three-Phase Workflow

### Phase 1: Story Discovery & Specification
- Clarify central conflict, protagonist goals, themes, and structure
- Create comprehensive story specification
- Define character profiles, plot structure, setting, and style guidelines
- Get author approval before proceeding

### Phase 2: Scene Planning & Implementation
- Create detailed scene outlines with purpose, goals, conflict, and sensory details
- Draft scenes according to approved outlines
- Maintain consistency with character voices and story world

### Phase 3: Revision & Refinement
- Verify story consistency with specifications
- Implement author feedback while maintaining story integrity
- Merge to main manuscript only after final approval

## Getting Started

### Prerequisites
- [Claude Code](https://claude.com/claude-code)
- [OpenSpec CLI](https://github.com/rrkeji/openspec) (bundled)
- Git (for version control)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/openmoto/inkspec.git
cd inkspec
```

2. Open in Claude Code:
```bash
claude-code .
```

3. Start your first story:
```
Ask Claude: "Let's start a new story following the SDS protocol"
```

## Project Structure

```
inkspec/
├── .claude/                    # Claude Code configuration
│   └── commands/               # Custom slash commands
├── openspec/                   # OpenSpec framework
│   ├── AGENTS.md              # OpenSpec workflow instructions
│   ├── project.md             # Project conventions
│   ├── specs/                 # Implemented story capabilities
│   └── changes/               # Active and archived proposals
├── docs/                      # Story specifications
│   └── story-spec/
│       ├── premise/           # Story premises (PR-###)
│       ├── characters/        # Character profiles (CH-###)
│       ├── scenes/            # Scene outlines (SC-###)
│       └── world/             # World-building (WB-###)
├── inbox/                     # Mobile idea capture
│   ├── ideas/                 # Raw ideas from mobile
│   └── processed/             # Converted to specs
├── manuscript/                # Final prose output
├── 00_spec_driven_storytelling_protocol.md
├── CLAUDE.md                  # AI assistant instructions
└── README.md                  # This file
```

## Custom Slash Commands

- `/openspec:proposal` - Create a new story change proposal
- `/openspec:apply` - Implement an approved change
- `/openspec:archive` - Archive completed story work

## Documentation

- **[SDS Protocol](00_spec_driven_storytelling_protocol.md)** - The complete methodology
- **[OpenSpec Guide](openspec/AGENTS.md)** - Change management workflow
- **[Claude Instructions](CLAUDE.md)** - AI assistant configuration

## Story Spec Conventions

### File Naming
- Premises: `PR-###_story_title.md`
- Characters: `CH-###_character_name.md`
- Scenes: `SC-###_scene_description.md`
- World: `WB-###_world_element.md`

### Branch Naming
- `story/[IssueNum]-SC-###-scene-description`
- `revision/[IssueNum]-CH-###-character-development`

### Commit Messages
- `scene(SC-101): add opening confrontation scene`
- `character(CH-205): develop protagonist's backstory reveal`
- `revision(SC-101): strengthen dialogue and conflict`

## Core Principles

1. **Never write prose without approved specifications**
2. **Story specification is the single source of truth**
3. **Character consistency is mandatory**
4. **Show, don't tell**
5. **Collaborative partnership between author and AI**

## Mobile Idea Capture (Inbox)

Inspiration doesn't wait for you to be at your desk. The **Inkspec Inbox** lets you capture ideas anywhere:

### Quick Start
1. Use any notes app that syncs to your computer (Apple Notes, Google Keep, Notion, etc.)
2. Create a file: `inbox/ideas/2025-01-15.md` (or just use `quick-notes.md`)
3. Jot down whatever comes to mind - character ideas, dialogue, plot twists, world-building
4. Later in Claude Code: "Review my inbox and help me process these ideas"

### What to Capture
- Character ideas and personality traits
- Overheard dialogue that feels authentic
- Plot twists and story concepts
- World-building details and settings
- Scene atmospheres and sensory details
- Random creative thoughts

No formatting needed - just capture! Claude will help you convert raw ideas into proper specifications later.

See [inbox/README.md](inbox/README.md) for the complete workflow.

## When to Create OpenSpec Proposals

**Create proposals for:**
- New story arcs or major plot developments
- Character arc changes or additions
- World-building that affects multiple scenes
- Breaking changes to established canon

**Skip proposals for:**
- Minor dialogue revisions
- Typo fixes
- Formatting changes
- Scene polish that doesn't change plot or character

## Contributing

This is a framework for personal or collaborative fiction writing. Feel free to fork and adapt to your own creative process.

## License

[Choose your license - MIT, Creative Commons, etc.]

## Acknowledgments

- Built with [Claude Code](https://claude.com/claude-code)
- Powered by [OpenSpec](https://github.com/rrkeji/openspec)
- Inspired by Test-Driven Development and Spec-Driven Development methodologies

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

**Write with discipline. Create with confidence.**
