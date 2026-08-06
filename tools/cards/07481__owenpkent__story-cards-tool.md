---
id: tool-07481
type: tool
area: 库
status: active
tags: [HTML, 协议宽松, 本地优先, 英文文档, 本地写作]
title: story-cards-tool
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/owenpkent/story-cards-tool
created: 2026-07-18
updated: 2026-07-18
no: 7481
category: 画龙补充 / 扩容入库 — 补充源
repo: owenpkent/story-cards-tool
stars: 0
url: https://github.com/owenpkent/story-cards-tool
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/QUICK_START.md
---

# owenpkent/story-cards-tool

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/owenpkent/story-cards-tool
- **Stars**：0
- **语言**：HTML
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：story-cards-tool
- **拉取时间**：2026-07-25 19:23:14

---

# Cinematic Blueprint

**Open Source Edition**

A visual story planning tool for writers, filmmakers, and content creators. Organize story beats with drag-and-drop, plan scenes across acts and subplots, and create visual storyboards with shot descriptions and reference images.

🌐 **Website:** [cinematicblueprint.com](https://cinematicblueprint.com)

---

## About This Repo

This is the **open source community edition** of Cinematic Blueprint. It contains the full-featured story planning tool that runs entirely in your browser.

- 📖 **Open Source** — MIT licensed, free forever
- 🔌 **Self-hosted** — No server needed, just open the HTML file
- 🤝 **Community-driven** — Contributions welcome!

---

## Quick Start

1. Open `cinematic-blueprint.html` in your browser
2. Switch between **Story Beats**, **Swimlanes**, and **Storyboard** views
3. Edit your content (drag to rearrange, click to edit)
4. Click **Export** → Download your work as `.md` or `.json`
5. To continue later: Click **Load** → Select your saved file

---

## Using the Storyboard

### Creating Shots
1. Click the **Storyboard** button in the toolbar
2. **Drag images** from File Explorer directly onto the storyboard — each image becomes a shot
3. Or click the **+ Add Shot** card to add a shot manually

### Editing Shots (Inline)
Click directly on any field to edit it:
- **Shot number** — e.g., "1", "1A", "2B"
- **Description** — What happens in the shot
- **Camera** — e.g., "Wide", "CU", "Dolly in"
- **Duration** — e.g., "5s"

Press **Enter** to save, **Escape** to cancel.

### Saving & Loading Your Storyboard
1. Click **Export** → Downloads `storyboard.json`
2. Save this file somewhere safe (e.g., your project folder)
3. To continue later: Click **Load** → Select your `storyboard.json` file
4. Your shots, images, and all metadata are restored

> **Important**: The JSON file stores image data, so your images will appear when you reload. Keep the JSON file — it's your save file!

---

## Features

### Story Beats View
- **Acts View** — Columns for each act (drag to reorder acts)
- **Swimlane View** — Rows by subplot, columns by act

### Storyboard View
- **Visual timeline** — Arrange shots in sequence
- **Drag & drop images** — Drop images directly from File Explorer onto the storyboard
- **Inline editing** — Click any field to edit shot number, description, camera notes, duration
- **Reorder shots** — Drag shots to rearrange the sequence
- **Multiple images at once** — Drop several images to create multiple shots

### Editing
- **Click card** — Open edit modal
- **Right-click card** — Context menu (edit, duplicate, move, delete)
- **Right-click empty area** — Add card here
- **Drag cards** — Move between acts/subplots
- **Drag acts** — Reorder act columns

### Templates
17 built-in story structures including:
- Three Act, Save the Cat, Story Circle, Hero's Journey
- Romance, Horror, Mystery genre-specific beats
- See `templates/README.md` for full list

### Settings
- **Light/Dark mode** toggle
- **Custom colors** for status, subplots, and accent

---

## Multi-Project Organization

This tool is designed to be deployed per-project. Recommended structure:

```
my-video-project/
├── cinematic-blueprint.html  # The tool (copy this)
├── project.json              # Project config (auto-created)
├── story-beats/              # Beat card exports
│   ├── story-beats-v1.md
│   └── story-beats-v2.md
├── storyboard/               # Storyboard exports
│   └── storyboard-v1.json
└── images/                   # Reference images for storyboard
    ├── shot-001.jpg
    └── shot-002.png
```

### Deploying to a New Project

1. Copy `cinematic-blueprint.html` to your project folder
2. Create an `images/` folder for reference images
3. Open the HTML file — it auto-creates config on first export

### Image References

The storyboard stores **file paths** or **URLs** to images, not the images themselves:
- Drag images from your file explorer → stores relative path
- Paste image URL → stores the URL
- Images stay in your project's `images/` folder

This keeps your storyboard file small and Git-friendly.

---

## File Locations

| Location | Purpose |
|----------|---------|
| `cinematic-blueprint.html` | The tool |
| `project.json` | Project settings |
| `story-beats/` | Versioned story beat exports |
| `storyboard/` | Storyboard exports (JSON) |
| `images/` | Reference images for storyboard |
| `templates/` | Story structure reference docs |

---

## Keyboard Shortcuts

| Action | How |
|--------|-----|
| Zoom in/out | Slider or +/- buttons |
| Close modal | Click outside or Escape |
| Switch view | Click view buttons in toolbar |

---

## Tips

- **No auto-save** — Export when done rearranging
- Browser warns before leaving with unsaved changes
- Use the **Ideas** column as a parking lot for beat cards
- Right-click for quick actions
- Keep images in the `images/` folder for portable projects
- Git commit your exports for version history

---

## Cloud Features

Cloud save is now available! See [docs/CLOUD_STATUS.md](https://github.com/owenpkent/story-cards-tool/blob/main/docs/CLOUD_STATUS.md) for details.

- ✅ User accounts (Email/Password)
- ✅ Cloud save/sync via Firestore
- 🔲 Multi-project support (planned)
- 🔲 Image uploads (planned)

---

## Documentation

All technical documentation is in the [`docs/`](https://github.com/owenpkent/story-cards-tool/blob/main/docs/) folder:

| Document | Description |
|----------|----------related:
  - methods/QUICK_START.md
---|
| [Progress & Status](https://github.com/owenpkent/story-cards-tool/blob/main/docs/PROGRESS.md) | Current status & roadmap |
| [Cloud Implementation](https://github.com/owenpkent/story-cards-tool/blob/main/docs/CLOUD_STATUS.md) | Firebase setup & deployment |
| [Accessibility](https://github.com/owenpkent/story-cards-tool/blob/main/docs/ACCESSIBILITY.md) | WCAG 2.1 AA compliance |
| [MCP Server](https://github.com/owenpkent/story-cards-tool/blob/main/docs/MCP_SERVER_DESIGN.md) | AI integration |
