---
id: tool-01377
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: lovestory-builder
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/afarabee/lovestory-builder
created: 2026-07-18
updated: 2026-07-18
no: 1377
category: 二、网文 / 长篇 AI 写作系统 库
repo: afarabee/lovestory-builder
stars: 1
url: https://github.com/afarabee/lovestory-builder
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: ba258c7aa429407c
  - methods/最强写作方法论_全球最强综合版.md
---

# afarabee/lovestory-builder

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/afarabee/lovestory-builder
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered User Story Generator for Agile Teams
- **本地描述**：AI-powered User Story Generator for Agile Teams
- **拉取时间**：2026-07-23 23:19:16

---

# 💜 AI-Assisted User Story Generator

AI-assisted tool for generating, refining, and exporting Agile user stories into Azure DevOps (ADO).  
Built with **React + TypeScript + Vite**, styled with **Tailwind**, and extended with custom AI refinement logic.  

---

## 🚀 Features

### 🆕 New User Story Flow
- Start fresh with **raw input fields** (Role, Action, Goal, Benefit).  
- Confirmation modal appears before wiping a draft.  
- When confirmed → all fields cleared, chat reset, UI returns to fullscreen raw input.  

### 📖 User Story Generation
- **Generate User Story** button reveals:
  - User Story Details (Title, Description, Acceptance Criteria)  
  - Developer Notes  
  - Push to ADO section  
  - Story Refinement Chat (expanded by default)  
- Story Points auto-suggested but editable.  

### 💬 Story Refinement Chat
- Suggestions limited to **actions supported in UI** (update title, description, AC).  
- **Apply Suggestion** only shows when actionable.  
- **Undo Suggestion** reverts last change.  
- Auto-scrolls to latest message, with sticky **Scroll to Bottom** button.  
- Filters out repetitive phrases like *“I understand you want to refine…”*.  
- Accepts nonsense input but still returns mock refinement suggestions.  

### 🧪 Test Data
- Hidden by default; toggleable via sidebar.  
- Displays **sample inputs, edge cases, and mock API responses**.  
- Updates when suggestions are applied.  
- No “test data updated” pop-ups.  

### 🕰️ Version History
- **Sidebar only** (redundant right-hand card removed).  
- New snapshot created:
  - On field edits (Title, Description, AC).  
  - Or via optional autosave interval.  
- Each version includes:
  - Timestamp  
  - Diff view (shows all field changes, not just description)  
  - Restore button  

### ⚙️ Project Settings Modal
- Accessed via top-right header only.  
- Opens as modal (not full page).  
- Fields include:
  - Project metadata  
  - Prompt behavior toggles  
  - GitHub repo integration (Dev Notes & static project context)  

---

## 🛠️ Tech Stack

- [React](https://react.dev/) + [TypeScript](https://www.typescriptlang.org/)  
- [Vite](https://vitejs.dev/)  
- [Tailwind CSS](https://tailwindcss.com/)  
- [Lucide Icons](https://lucide.dev/)  
- [Lovable](https://lovable.dev/) for prototyping  

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## ⚡ Getting Started

### Prerequisites
- Node.js v18+  
- npm v9+  

### Installation
```bash
# Clone repo
git clone https://github.com/afarabee/lovestory-builder.git

# Enter folder
cd lovestory-builder

# Install dependencies
npm install
