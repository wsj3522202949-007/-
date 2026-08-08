---
id: tool-07604
type: tool
area: 库
status: active
tags: [大纲规划, Claude插件, JavaScript, 协议宽松, 本地优先, 英文文档, 本地写作]
title: obsidian-screenwriter
summary: 搭大纲/分卷/节拍
source: https://github.com/wesswart77/obsidian-screenwriter
created: 2026-07-18
updated: 2026-07-18
no: 7604
category: 画龙补充 / 扩容入库 — 补充源
repo: wesswart77/obsidian-screenwriter
stars: 0
url: https://github.com/wesswart77/obsidian-screenwriter
tier: "C"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: dd13445a0c5b9c23
  - methods/QUICK_START.md
---

# wesswart77/obsidian-screenwriter

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/wesswart77/obsidian-screenwriter
- **Stars**：0
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Develop screenplays in Obsidian: treatments, outlines, character arcs, scene cards, and beat sheets.
- **本地描述**：obsidian-screenwriter
- **拉取时间**：2026-07-25 19:27:00

---

# Screenwriter

An Obsidian plugin for developing screenplays: treatments, outlines, character arcs, scene cards, and beat sheets.

## Features

- **New Screenplay Project** — Creates a project folder with 5 pre-structured files: Treatment, Outline, Characters, Beat Sheet (Blake Snyder's 15 beats), and Notes
- **New Character** — Add a character entry (archetype, want, need, flaw, arc) to any project's Characters.md
- **New Scene Card** — Add a scene card (scene number, location, time of day, characters, action, purpose) to the project's Outline.md
- **Projects Sidebar** — Lists all projects with format badge, status badge, and scene count

## Usage

Open the command palette (`Ctrl/Cmd+P`) and search for:
- `Screenwriter: New Screenplay Project`
- `Screenwriter: New Character`
- `Screenwriter: New Scene Card`
- `Screenwriter: Open Screenwriter Sidebar`

## Project Structure

Each project creates:
```
Screenwriting/
  My Project/
    Treatment.md
    Outline.md
    Characters.md
    Beat Sheet.md   ← Blake Snyder's 15 beats pre-filled
    Notes.md
```

## Settings

| Setting | Default | Description |
|---------|---------|----------related:
  - methods/QUICK_START.md
---|
| Projects Folder | `Screenwriting` | Root folder for all screenplay projects |

## License

MIT © 2026 Wesley Swart
