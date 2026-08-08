---
id: tool-01118
type: tool
area: 库
status: active
tags: [校对, 协议未明, 本地优先, 英文文档, 大纲规划, 改稿润色, 本地写作]
title: novelforge
summary: 搭大纲/分卷/节拍
source: https://github.com/greene-ctrl/novelforge
created: 2026-07-18
updated: 2026-07-18
no: 1118
category: 二、网文 / 长篇 AI 写作系统 库
repo: Greene-ctrl/novelforge
stars: 0
url: https://github.com/greene-ctrl/novelforge
tier: "C"
use_case: "搭大纲/分卷/节拍"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 0136ba0d9ce113fc
  - methods/最强写作方法论_全球最强综合版.md
---

# Greene-ctrl/novelforge

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/greene-ctrl/novelforge
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Local-first browser-based novel writing application. No cloud, no AI — just a sharp tool for a human craft.
- **本地描述**：Local-first browser-based novel writing application. No cloud, no AI — just a sharp tool for a human craft.
- **拉取时间**：2026-07-23 23:11:38

---

# ChapterCauldron

A local-first, browser-based novel writing application built for how novelists actually work — messy, non-linear, and across months of planning, drafting, and revision.

No account required. No cloud dependency. No AI. Just a sharp tool for a human craft.

## Features

### Writing & Editing
- **Manuscript editor** — Tiptap/ProseMirror rich text with chapters, scenes, and drag-and-drop reordering
- **Focus mode** — Hide all chrome and write distraction-free; typewriter-style centered cursor
- **Style editor** — Customize font family, font size, line height, and paragraph spacing per session
- **Stitched mode** — Click a chapter to view all its scenes as continuous prose
- **Inline TODOs** — Annotate text with TODO markers; jump between them with keyboard shortcuts
- **Spellcheck toggle** — Browser spellcheck on/off from the toolbar
- **Autosave** — Debounced saves with visible status indicator; no work is ever lost

### Planning & Structure
- **Timeline view** — Multi-lane D3 visualization with chapter, character, subplot, and status axes
- **Outline view** — Sortable/filterable spreadsheet table of all scenes with columns for title, chapter, synopsis, POV, location, status, word count, subplots, and color
- **Plot templates** — Seven built-in structures (Three-Act, Save the Cat, Hero's Journey, Snowflake, Story Circle, Freytag's Pyramid, Seven-Point) with template picker, beat preview, and context-menu access
- **Subplots** — Named subplot threads with color coding; tag scenes to subplots in metadata

### World-Building
- **Codex (Story Bible)** — Floating, draggable reference panel for characters, locations, factions, items, events, and custom categories
- **Relationship map** — D3 force-directed graph showing connections between codex entries
- **Relationship editor** — Add, remove, and label relationships between any two codex entries
- **Auto-linking** — Codex entry names are automatically recognized in the editor with inline highlights
- **Reference panel** — Pin any codex entry alongside the editor for quick reference while writing
- **Custom categories** — Define your own codex categories beyond the built-in set

### Scene Metadata
- **Scene status** — Track scenes through idea → draft → revised → polished → final with color-coded indicators
- **POV character** — Assign POV from codex characters, with inline dropdowns that can create new entries
- **Location** — Assign location from codex locations
- **Story date** — Set in-world dates for timeline ordering
- **Characters present** — Tag which characters appear in each scene
- **Emotional & plot beats** — Annotate the dramatic purpose of each scene

### Version History & Safety
- **Persistent version history** — Every scene maintains a browsable history of past states
- **Auto-snapshots** — Automatic snapshots every 5 minutes while editing
- **Manual snapshots** — Save a snapshot on demand from the history panel
- **Status change snapshots** — Automatic snapshot before any status transition
- **Trash snapshots** — Automatic snapshot before moving items to trash
- **Content preview** — Preview snapshot content with text excerpts before restoring
- **Safe restore** — Restoring an older version first snapshots the current state, so no work is ever lost

### Safety & Backup
- **Snapshot pruning** — Old edit snapshots automatically pruned (keeps last 50 per scene)
- **Trash & restore** — Soft-delete chapters, scenes, and codex entries with full restore capability
- **Permanent delete** — Hard-delete trashed items with full cleanup of associated data
- **Project backup** — Export your entire project as a `.chaptercauldron.zip` archive
- **Project import** — Import backups with conflict resolution (skip, overwrite, or import as copy)
- **Backup reminders** — Gentle nudge if 24 hours pass without exporting a backup

### Productivity
- **Daily word count goals** — Progress bar, configurable daily target, and 7-day writing stats chart
- **Session warm-up** — Shows where you left off with your parking note when reopening a project
- **Parking notes** — Leave a note about what to write next, visible on your next session
- **Idle nudge** — Gentle writing prompts when you pause
- **TODO panel** — Sidebar panel listing all inline TODOs across the manuscript
- **Global search & replace** — Find and replace text across all scenes in the manuscript

### Project Management
- **Multi-project support** — Welcome screen with project list, create/open/delete
- **Demo project** — Pre-loaded "The Last Lighthouse" manuscript for exploring the app
- **Guided tour** — Interactive 7-step walkthrough for new users, with a post-tour tips modal
- **Multi-format export** — DOCX, EPUB, PDF, and Markdown export from the status bar menu
- **Chapter from Template** — Right-click a chapter or manuscript header to create a new chapter from a plot structure template

### Design
- **Dark theme** — Purpose-built dark UI for distraction-free writing
- **Low-flash design** — Minimized sudden flashes and transitions for writers with sensitivity
- **Offline-first** — All data stored in IndexedDB via Dexie.js; works without internet
- **PWA** — Installable as a Progressive Web App on desktop and mobile
- **Keyboard-driven** — Comprehensive shortcuts for writing, navigation, and TODOs

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | React 19 + TypeScript |
| Editor | Tiptap 2 (ProseMirror) |
| Database | Dexie.js 4 (IndexedDB) + SQLite (server backup) |
| State | Zustand 5 |
| Styling | Tailwind CSS 4 |
| Visualization | D3.js (timeline, relationship map) |
| Build | Vite 6 |
| PWA | vite-plugin-pwa |
| Monorepo | pnpm workspaces |
| Testing | Vitest + Playwright |
| DnD | @dnd-kit |
| Export | docx + JSZip + file-saver |
| Server | Node.js + better-sqlite3 |

## Getting Started

### Development

```bash
# Prerequisites: Node.js 20+, pnpm 9+
pnpm install
pnpm dev
```

Open http://localhost:5173 in your browser.

### Docker (Production)

```bash
docker compose up -d
```

Open http://localhost:3000 in your browser. Data is persisted in a Docker volume.

The container runs a Node.js server that:
- Serves the built SPA
- Backs up all data to SQLite (survives browser data clears)
- Syncs manuscripts as Markdown files to disk
- Manages session locking for multi-tab safety

#### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `3000` | HTTP port |
| `DATA_DIR` | `/data` | SQLite database and file sync directory |

## Project Structure

```
chaptercauldron/
├── apps/web/              # Vite + React web application
│   └── src/
│       ├── components/    # Sidebar, EditorPanel, VersionHistory, TimelineView, OutlineView, PlotTemplatePicker, etc.
│       ├── hooks/         # useNodes, useSubplots, useWritingSessions, useDebouncedNodeSave
│       ├── lib/           # Server sync utilities
│       └── stores/        # Zustand stores (project, session, UI, filter)
├── packages/
│   ├── core/              # Database, types, seed data, export (DOCX/EPUB/PDF/MD/ZIP), word count, snapshots
│   ├── editor/            # Tiptap editor + toolbar + extensions (AutoLink, TodoMarker)
│   └── ui/                # Shared UI primitives (Button, Input, Card, StatusPill, etc.)
└── origins/               # Design docs, requirements, and strategic reference
```

## Scripts

| Command | Description |
|---------|----------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| `pnpm dev` | Start dev server (with SQLite backend) |
| `pnpm build` | Production build |
| `pnpm test` | Run unit tests (92 tests) |
| `pnpm test:e2e` | Run Playwright E2E tests |
| `docker compose up -d` | Build and run the production container |

## Milestone Status

- [x] **M1.0** — Monorepo skeleton (pnpm workspaces, TypeScript, Vite)
- [x] **M1.1** — Sidebar tree with chapters, scenes, bible entries, DnD
- [x] **M1.2** — Tiptap editor with autosave, toolbar, scene breaks
- [x] **M1.3** — Refactoring (makeNode factory, scenesByParent map, dead code removal)
- [x] **M1.4** — Scene metadata panel (status, POV, synopsis, location, story date, characters present)
- [x] **M1.5** — Daily word count goals with progress bar, 7-day stats, settings UI
- [x] **M1.6** — DOCX manuscript export
- [x] **M1.7** — Welcome screen and multi-project management
- [x] **M2.0** — Full schema expansion (series, subplots, drafts, comments, todos, revision layers)
- [x] **M2.1** — State management refactor (filterStore, sessionStore, clean data access layer)
- [x] **M2.2** — Editor extension architecture (registry pattern, CommentMark/TodoMarker/AutoLink)
- [x] **M2.3** — Component library & design system (15+ shared UI primitives)
- [x] **M2.4** — Testing foundation (92 unit tests, Playwright E2E, GitHub Actions CI)
- [x] **M2.5** — Holistic UI/UX improvements (idle nudge, style editor, reference panel, focus mode)
- [x] **M2.6** — Timeline view (D3 multi-lane visualization with chapter/character/subplot/status axes)
- [x] **M2.7** — Outline view (sortable/filterable table of all scenes)
- [x] **M2.7.2** — Plot structure template picker (seven templates with beat preview and apply)
- [x] **M2.8** — Relationship map (D3 force-directed graph for bible entries)
- [x] **M2.9** — Auto-linking (bible entry name recognition in the editor)
- [x] **M3.0** — Persistent version history (snapshots, auto-save, manual save, restore, pruning)
- [x] **M3.1** — Trash & restore (soft-delete with sidebar trash section, permanent delete)
- [x] **M3.2** — Version history polish (timeline slider, diff preview, restore workflow)
- [x] **M3.3** — Multi-format export (EPUB, PDF, Markdown) and unified status bar menu
- [x] **M3.4** — Project backup/restore (ZIP export, import with conflict resolution)
- [x] **M3.5** — Help overlay, guided walkthrough, tips modal, about screen
- [x] **M3.6** — Global search & replace across manuscript
- [x] **M3.7** — PWA support (installable, offline-capable, service worker)
- [x] **M3.8** — Docker deployment (production Node.js server with SQLite backup)
- [ ] **M3.9** — Revision layers (focused editing passes with annotations)

## License

MIT
