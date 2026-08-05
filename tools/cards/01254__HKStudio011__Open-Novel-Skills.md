---
id: tool-01254
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Open-Novel-Skills
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/hkstudio011/open-novel-skills
created: 2026-07-18
updated: 2026-07-18
no: 1254
category: 二、网文 / 长篇 AI 写作系统 库
repo: HKStudio011/Open-Novel-Skills
stars: 0
url: https://github.com/hkstudio011/open-novel-skills
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# HKStudio011/Open-Novel-Skills

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/hkstudio011/open-novel-skills
- **Stars**：0
- **语言**：JavaScript
- **License**：MIT
- **Topics**：ai-agents, cli, novel-writing, opennovel, storytelling
- **GitHub 描述**：CLI tool for the OpenNovel novel-writing framework — scaffold project structure and track writing progress
- **本地描述**：CLI tool for the OpenNovel novel-writing framework — scaffold project structure and track writing progress
- **拉取时间**：2026-07-23 23:15:40

---

# OpenNovel Framework 🖋️

AI-assisted novel/story writing framework.

`[:vietnam: Tiếng Việt](README.vi.md)`

Combines a **CLI tool** + **7 agent skills** for AI coding assistants (Claude Code, OpenCode, Codex) — from project scaffolding, story bible, plot outline, chapter writing, review, continuity tracking, to final export.

---

## Features

- **CLI scaffold** — `opennovel init` creates a standardized project structure
- **Story bible** — characters, world rules, secrets, cause-effect chains
- **Plot outline** — chapter briefs, timeline, turning points, hooks
- **AI-assisted writing** — chapters written per brief, in-character
- **Built-in review** — 6-layer quality check (logic → character → plot → pacing → emotion → prose)
- **Continuity tracking** — auto-update story state after each chapter
- **Raw Story Assimilation** — import existing stories, extract bible/outline, rewrite or continue
- **Export** — `.md` → `.txt` / `.html`

---

## Installation

```bash
# Global install
npm install -g @hkstudio011/opennovel

# Or run directly via npx
npx @hkstudio011/opennovel init my-story
```

**Requirements:** Node.js >= 18

---

## Quick Start

```bash
npx @hkstudio011/opennovel init my-story
cd my-story
```

Then load the `opennovel-writing-assistant` skill in your AI coding assistant (Claude Code, OpenCode, Codex...).

### Option 1: New story

Tell the AI:

> "I want to write a story"

The AI will automatically:
1. Fill in project metadata (genre, tone, POV, premise...)
2. Build story bible (characters, world rules, secrets)
3. Create outline (plot structure, chapter briefs)
4. Write each chapter, review, revise, update continuity

### Option 2: Existing story

Paste your story text and tell the AI:

> "Continue this story" / "Rewrite this chapter"

The AI enters **Raw Story Assimilation Mode**:
1. Analyze content → detect characters, plot, secrets
2. Propose Bible Update + Outline Update
3. After your approval, rewrite or continue with continuity tracking

---

## Workflow

```
Bible → Outline → Write → Review → Revise → Continuity
  ↑                                                │
  └───────────────────── Next chapter ─────────────┘
                              │
                              ↓
                          Export
```

Breakdown:
1. **project-init** — scaffold project, fill metadata
2. **bible-builder** — characters, world, rules, secrets
3. **outline-builder** — plot, timeline, chapter briefs
4. **writing-assistant** — write chapter per brief
5. **review** — quality check (diagnosis-only, no edits)
6. **writing-assistant** — fix issues from review (logic first, prose last)
7. **continuity-manager** — update story state (only after chapter finalized)
8. Loop to step 4 for next chapter, or **export** on completion

---

## Skill Inventory

| Skill | Role | When to use |
|---|---|---|
| `opennovel-writing-assistant` | Core orchestration, write/revise | Every writing session — **main entry point** |
| `opennovel-bible-builder` | Characters, world, rules, secrets | Missing context, worldbuilding, or raw text analysis |
| `opennovel-outline-builder` | Plot, timeline, chapter briefs | Missing structure, planning, or raw text analysis |
| `opennovel-continuity-manager` | Track story state | After each finalized chapter |
| `opennovel-review` | Diagnosis-only quality check | Before finalizing a chapter |
| `opennovel-exporter` | .md → .txt / .html | Story complete |

---

## Golden Rules

1. Every chapter needs: **goal** → **conflict** → **mini-climax** → **hook**
2. Review order: logic → character → plot → pacing → emotion → prose
3. Fix order: logic first, prose last
4. Update continuity after every chapter (only after finalized)
5. Never reveal secrets early or break character

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## License

MIT
