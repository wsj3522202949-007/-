---
id: tool-00943
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: NovelKit
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/georgetw6060/novelkit
created: 2026-07-18
updated: 2026-07-18
no: 943
category: 二、网文 / 长篇 AI 写作系统 库
repo: GeorgeTW6060/NovelKit
stars: 0
url: https://github.com/georgetw6060/novelkit
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: d46bcb38006891d6
  - methods/最强写作方法论_全球最强综合版.md
---

# GeorgeTW6060/NovelKit

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/georgetw6060/novelkit
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：browser-app, dark-ui, localstorage, manuscript-management, novel, novel-writing, text-editor, vanilla-javascript, writing, writing-software, writing-tool
- **GitHub 描述**：A minimalist, browser-based writing environment for novelists. Manage novels, chapters, characters, and world-building with a distraction-free editor, formatting tools, and automatic local storage backup. No external dependencies.
- **本地描述**：A minimalist, browser-based writing environment for novelists. Manage novels, chapters, characters, and world-building with a distraction-free editor, formatting tools, and automatic local storage backup. No external dependencies.
- **拉取时间**：2026-07-23 23:06:34

---

# NovelKit

A comprehensive web-based writing workspace for novelists. NovelKit provides all the tools you need to organize, write, and manage your novel projects in one elegant interface.

## ✨ Features

### 📚 Novel Management
- **Create Multiple Novels** - Start new writing projects with custom titles and genres
- **Genre Selection** - Choose from 10 genres: Thriller, Fantasy, Sci-Fi, Mystery, Romance, Historical, Horror, Contemporary Nonfiction, Adventure/Action, and Dystopian
- **Status Tracking** - Track project progress with five status states: In Progress, Completed Blueprint, Drafting Phase, Editing Workflow, and On Hold
- **Workspace Organization** - Easily switch between multiple novel projects in the sidebar

### ✍️ Advanced Writing Tools
- **Rich Text Editor** - Full-featured editor with formatting controls in the Write tab
- **Formatting Toolbar** - Bold, italic, underline, strikethrough, text styles (headings, quotes), bullet lists, numbered lists, and text alignment
- **Find & Replace** - Built-in find and replace functionality with case-sensitive and whole-word matching options
- **Focus Mode** - Hide the sidebar to minimize distractions while writing (Ctrl+Shift+F)
- **Word Count Tracking** - Real-time word count for each chapter

### 📖 Chapter Management
- **Chapter Organization** - Create and manage multiple chapters within each novel
- **Chapter Titles & Status** - Set custom titles and track individual chapter status (Planned, Drafting, Done)
- **Manuscript Blueprint** - Visual chapter layout view for planning your book structure
- **Direct Chapter Editing** - Seamless navigation between chapters with auto-save

### 👥 Character Development
- **Character Database** - Create and manage a cast of characters for your novel
- **Character Cards** - Organize character information with dedicated card-based interface
- **Color-Coded Avatars** - Visual system for quick character identification

### 📐 Plot & Structure Tools
- **Act-Based Organization** - Break down your story into custom acts with clues and plot points
- **Story Beats** - Track narrative progression and key moments
- **Flexible Act Structure** - Add as many acts as needed for your story

### 🌍 Worldbuilding
- **Lore & Setting** - Comprehensive worldbuilding notes for your story's universe
- **Location Management** - Create and catalog key locations in your world
- **Location Database** - Organized directory of all important places in your story

### 📊 Project Overview
- **Dashboard Stats** - Real-time metrics showing:
  - Total chapter count
  - Completed chapters
  - Character count
  - Words written
- **Story Premise** - Define your narrative with:
  - One-line summary
  - Themes
  - Tone
  - Full synopsis
- **Planning & Schedule** - Set word count goals and project deadlines
- **General Notes** - Brainstorm area for universe rules and important lore

### 💾 Data Management
- **Auto-Save** - All changes are automatically saved to local storage
- **Export Options**:
  - **TXT Export** - Export your entire manuscript as a cleanly formatted text file
  - **JSON Backup** - Save complete project state including all chapters, characters, plot, and settings
- **Import Backups** - Restore projects from previously exported JSON files
- **Drag & Drop Import** - Drop `.json` files anywhere to load projects

## 🚀 Getting Started

### Opening NovelKit
Simply open `index.html` in your web browser. No installation or server required—everything runs locally in your browser.

### Creating Your First Novel
1. Click the **"New novel"** button in the sidebar
2. Enter your novel title
3. Select your genre from the available options
4. Click **"Create project blueprint"**

### Writing Your Novel
1. Select your novel from the sidebar
2. Go to the **Write** tab
3. Create chapters or select existing ones from the left panel
4. Start writing in the rich text editor
5. Use the formatting toolbar to style your text
6. Track your progress with the word count badge

### Organizing Your Story
- **Overview Tab**: Set up your premise, themes, and story summary
- **Chapters Tab**: Plan your manuscript structure and chapter sequence
- **Characters Tab**: Develop your cast of characters
- **Plot Tab**: Define your story's acts and narrative beats
- **World Tab**: Build your story's setting and locations

### Exporting Your Work
1. Click **"Export / Save"** button
2. Choose your export format:
   - **TXT** - For manuscript sharing and reading
   - **JSON** - For complete backup and restoration

## 🎨 Design Features

- **Dark, Professional Theme** - Elegant dark interface with warm accent colors
- **Responsive Layout** - Sidebar navigation with main workspace
- **Intuitive UI** - Clean, organized interface designed for writers
- **Focus Mode** - Distraction-free writing environment
- **Real-time Updates** - Instant feedback as you write and organize

## 💾 Data Storage

NovelKit uses your browser's **localStorage** to save all data locally. This means:
- ✅ Your data stays on your device
- ✅ Works offline
- ✅ No account or login required
- ⚠️ Clearing browser data will delete your projects (use JSON export for backup!)

## 🎯 Tips for Writers

- **Regular Backups**: Export your novel as JSON periodically to ensure you don't lose work
- **Use Focus Mode**: Press Ctrl+Shift+F to hide the sidebar and focus on writing
- **Find & Replace**: Use Ctrl+H to quickly fix repeated text or terminology across chapters
- **Chapter Status**: Toggle chapter status by clicking the status badges to track your progress
- **Organize First**: Spend time in the Overview and Plot tabs to plan before writing

## 📝 Keyboard Shortcuts

- **Ctrl+B** - Bold
- **Ctrl+I** - Italic
- **Ctrl+U** - Underline
- **Ctrl+H** - Find & Replace
- **Ctrl+Shift+F** - Toggle Focus Mode

## 🛠️ Technical Details

- **Pure Frontend** - Runs entirely in the browser with vanilla JavaScript
- **No Dependencies** - No npm packages or build tools required
- **Local Storage** - All data persisted to browser localStorage
- **Responsive Design** - Works on desktop browsers
- **Standards-Based** - Built with HTML5, CSS3, and modern JavaScript

## 📄 License

This project is open source. Feel free to use, modify, and share.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

**Start writing your masterpiece today with NovelKit!**
