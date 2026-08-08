---
id: tool-00020
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: story-framework
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/lordjabez/story-framework
created: 2026-07-18
updated: 2026-07-18
$1124
category: 二、网文 / 长篇 AI 写作系统 库
repo: lordjabez/story-framework
stars: 3
language: null
license: MIT-0
url: https://github.com/lordjabez/story-framework
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: d99a0dad08b85626
  - methods/最强写作方法论_全球最强综合版.md
---

# Story Framework

A structured approach to writing fiction with AI assistance, using markdown files and git for version control.

## Getting Started

1. Clone or copy this folder for your new project
2. Initialize git: `git init`
3. Start developing your story in the planning documents
4. Write your drafts in the `Drafts/` folder
5. Use git commits to track revisions (no need for versioned folders)

## Folder Structure

```
your-story/
├── Characters/
│   └── characters.md      # Character profiles and relationships
├── Plot/
│   ├── outline.md         # Story structure and scene breakdown
│   └── threads.md         # Subplots, foreshadowing, payoffs
├── Themes/
│   └── themes.md          # Central themes, motifs, and symbols
├── Setting/
│   └── world.md           # Locations, time period, world rules
├── Continuity/
│   ├── timeline.md        # Scene-by-scene chronology
│   └── facts.md           # Canonical details (names, descriptions, etc.)
├── Drafts/
│   └── (your story files) # One file per chapter/act, numbered: 01-chapter-one.md
├── Notes/
│   ├── style-guide.md     # Voice, tone, formatting conventions
│   └── editing-markup.md  # How to leave inline edit notes
└── Final/
    └── README.md          # Checklist for finalizing
```

## Workflow

### Planning Phase
1. Fill out character profiles in `Characters/characters.md`
2. Develop your plot structure in `Plot/outline.md`
3. Define themes and motifs in `Themes/themes.md`
4. Build your world in `Setting/world.md`
5. Establish voice and conventions in `Notes/style-guide.md`
6. **Review and approve** all planning docs before moving to drafting

These planning documents are the **source of truth** for your story. Complete them first.

### Continuity Tracking (for novel-length work)

As you write, maintain these documents to prevent inconsistencies:

- `Continuity/timeline.md` - Log each scene's date/time as you write it
- `Continuity/facts.md` - Record canonical details (physical descriptions, addresses, object locations)
- `Plot/threads.md` - Track subplots, foreshadowing, and payoffs

Update these incrementally—don't wait until revision. The AI assistant will reference them to maintain consistency.

### Writing Phase
1. Create one file per chapter/act in `Drafts/`: `01-title.md`, `02-title.md`, etc.
2. Commit regularly with descriptive messages
3. Use `git tag` to mark milestones: `git tag v1-first-draft`

### Revision Phase
1. Add inline edit notes using the markup in `Notes/editing-markup.md`
2. Ask your AI assistant to "process edit notes"
3. Review and approve changes
4. Commit after each revision pass

### Inline Markup

Two markup types keep notes in your drafts:

| Syntax | Purpose | Example |
|--------|---------|---------|
| `[[...]]` | Author notes (context for AI) | `[[POV: Sarah]] [[TIMELINE: Day 3]]` |
| `{{...}}` | Edit notes (revision instructions) | `{{FIX: wrong name}} {{EXPAND: more detail}}` |

- **Author notes** stay in the draft until finalization—use them for POV, timeline, mood, active threads, research notes
- **Edit notes** are processed and removed during revision

See `Notes/editing-markup.md` for full syntax.

### Finalization
1. Follow the checklist in `Final/README.md`
2. Copy approved files to `Final/`
3. Tag the release: `git tag v1-final`

## Creative Collaboration Approaches

The file `creative-approaches.md` defines six distinct modes for human-AI creative collaboration, ordered by degree of human control:

| Approach | AI Role | Best For |
|----------|---------|----------|
| **Author** | Critic only | Getting feedback without AI-generated content |
| **Muse** | Pure executor | Precise control over every detail |
| **Artisan** | Scaffolder | Structure and outlines, you write prose |
| **Debater** | Adversary | Stress-testing creative choices |
| **Creator** | Generative partner | Iterative drafting with AI assistance |
| **Curator** | Option generator | Exploring many possibilities quickly |

**To use:** Tell the AI which mode you want—"Let's work in Author mode" or "Curator mode: give me options." You can switch modes mid-session.

See `creative-approaches.md` for full details on each approach's behaviors and sample prompts.

## Working with AI Assistants

This framework is designed for collaborative writing with AI. Configuration files are included for all major AI coding assistants:

| Tool | Configuration File |
|------|----------------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| Claude Code | `CLAUDE.md` |
| Gemini CLI | `GEMINI.md` |
| Kiro | `.kiro/steering/creative-writing.md` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| Cursor | `.cursorrules` |
| Windsurf | `.windsurfrules` |
| Cline | `.clinerules` |
| Universal fallback | `AGENTS.md` |

All tool-specific files reference `.ai-instructions.md`, which contains the complete guidance. Edit that file to change behavior across all tools.

The AI can:

- Help develop characters, plot, and themes in the planning docs
- Write drafts based on your outlines
- Process edit notes you leave in the text
- Follow the style guide for consistency
- Use git to track all changes

### Key Commands
- "Process edit notes" - Find and address all `{{...}}` markers
- "Show me the diff" - See uncommitted changes
- "Revise [section] to [instruction]" - Make specific edits

## Git Basics (If New to Git)

```bash
# Start tracking your project
git init

# Save your current state
git add .
git commit -m "Description of changes"

# See what's changed
git diff

# See history
git log --oneline

# Mark a milestone
git tag v1-first-draft

# Undo uncommitted changes to a file
git checkout -- filename.md
```

### Writing Good Commit Messages

Commit messages are your revision history. Focus on **why** you made changes, not just what changed—the diff already shows what. Good commit messages let you:

- Understand your creative decisions months later
- Find when and why a passage changed
- Revert to earlier versions with confidence

**Format:**
```
Short summary (50 chars or less)

Longer explanation if needed. Describe your reasoning:
- Why did you cut that scene?
- What feedback prompted this revision?
- What problem were you solving?
```

**Examples:**
```bash
# Good - explains the why
git commit -m "Cut prologue - slowed pacing, info now woven into ch 1"
git commit -m "Rework Sarah's intro to show competence before vulnerability"
git commit -m "Add tension to cafe scene per beta reader feedback"

# Less useful - only describes what
git commit -m "Edited chapter 3"
git commit -m "Fixed typos"
git commit -m "Rewrote dialogue"
```

## Tips

- Commit often with clear messages
- Use tags for major milestones (drafts, revisions, final)
- Keep the style guide updated as you establish patterns
- The planning docs are living documents—update them as the story evolves

