---
id: tool-01790
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: AI-Based-Story-Writer-with-Style-Control
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/tapendra9104/ai-based-story-writer-with-style-control
created: 2026-07-18
updated: 2026-07-18
no: 1790
category: 二、网文 / 长篇 AI 写作系统 库
repo: tapendra9104/AI-Based-Story-Writer-with-Style-Control
stars: 0
url: https://github.com/tapendra9104/ai-based-story-writer-with-style-control
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# tapendra9104/AI-Based-Story-Writer-with-Style-Control

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/tapendra9104/ai-based-story-writer-with-style-control
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered story writing platform with controllable genre, tone, and narrative style, featuring a professional editorial dashboard, story versioning, plot pacing tools, character relationship mapping, and live style comparison.
- **本地描述**：AI-powered story writing platform with controllable genre, tone, and narrative style, featuring a professional editorial dashboard, story versioning, plot pacing tools, character relationship mapping, and live style comparison.
- **拉取时间**：2026-07-23 23:31:13

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Story Foundry

Story Foundry is an AI-based story writing platform that helps users generate, edit, and refine structured narratives while controlling genre, tone, writing style, and pacing. The project combines a FastAPI backend with a professional editorial dashboard designed to feel like a real creative writing workspace rather than a simple text generator.

## Overview

The platform is built for writers, students, and content creators who want more control than a generic prompt-to-text tool provides. Instead of producing flat output, Story Foundry organizes each draft into a narrative structure, supports iterative revision, preserves version history, and exposes visual tools for understanding how the story evolves.

## Core Features

- Prompt-based story generation with configurable genre, tone, writing style, and target length
- Structured narrative output across introduction, conflict development, climax, and resolution
- Iterative refinement prompts for revising specific parts of a draft
- Story version management with editable saved revisions
- Professional editorial dashboard with a focused writing workspace
- Story library for reopening and managing saved drafts
- Download support for generated stories

## Advanced Frontend Features

- Character relationship graph visualization based on the active story draft
- Interactive plot timeline editor for pacing and narrative flow review
- Live style comparison panel for previewing alternate genre, tone, and style combinations
- AI suggestion panel for revision ideas and narrative improvements

## Frontend Dashboard Theme

The interface follows a clean editorial dashboard style inspired by modern writing tools. The layout is organized into three functional zones:

- Left sidebar for navigation, story modules, and session context
- Central workspace for prompt creation, editing, structure review, and comparison
- Right control rail for story settings, refinement prompts, suggestions, and version history

The visual design uses a light neutral background, muted panel surfaces, deep indigo accents, readable typography, and table-based content presentation. The result is a professional product-facing UI intended to look credible in demos, reports, and project evaluations.

## Tech Stack

- Backend: FastAPI
- Frontend: HTML, CSS, and JavaScript served by FastAPI
- Storage: local JSON persistence in `data/stories.json`
- Narrative engine: offline deterministic generator designed to be replaced by a real LLM later
- Testing: Python `unittest`

## API Highlights

- `POST /api/stories/generate` - generate a new story draft
- `POST /api/stories/{story_id}/refine` - revise a story with follow-up instructions
- `POST /api/stories/{story_id}/versions` - save a manual version
- `POST /api/stories/{story_id}/compare-style` - preview alternate style variants
- `GET /api/stories` - list saved stories
- `GET /api/stories/{story_id}` - fetch a single story and its versions

## Project Structure

```text
app/
  main.py
  domain.py
  schemas.py
  storage.py
  services/
    story_engine.py
  static/
    index.html
    styles.css
    app.js
data/
  stories.json
tests/
  test_story_engine.py
docs/
  PROJECT_SUMMARY.md
  screenshots/
    README.md
requirements.txt
README.md
```

## Run Locally

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the development server:

```bash
uvicorn app.main:app --reload
```

4. Open the app in your browser:

```text
http://127.0.0.1:8000
```

## Deploy On Vercel

This project is prepared for Vercel using a root `index.py` FastAPI entrypoint and `public/static/` assets.

1. Install the Vercel CLI if needed:

```bash
npm install -g vercel
```

2. Log in and deploy:

```bash
vercel
```

3. Promote the deployment to production when ready:

```bash
vercel --prod
```

### Important Vercel Note

On Vercel, the app automatically falls back to in-memory story storage because serverless filesystem writes are not persistent. That means generated stories can reset between cold starts or deployments. For durable production storage, replace the local JSON repository with a managed database such as PostgreSQL, MongoDB, or Vercel KV.

## Demo Flow

Use this sequence when presenting the project in a viva, demo, or screen recording:

1. Open the dashboard and start a new story from the prompt panel.
2. Select genre, tone, writing style, and story length from the control rail.
3. Generate a structured story draft and review the introduction, conflict, climax, and resolution.
4. Refine a section with a follow-up prompt and compare the updated version history.
5. Show the plot timeline, character relationship graph, and live style comparison panel.
6. Save the story to the library and reopen it from the dashboard.

## Suggested Screenshots For GitHub

If you want to make the repository look stronger on GitHub, capture these screens and place them in `docs/screenshots/`:

- Dashboard overview with sidebar, editor workspace, and style control rail
- Story generation form with prompt and narrative settings filled in
- Generated story draft showing structured sections
- Character relationship graph panel
- Plot timeline editor and pacing controls
- Side-by-side live style comparison panel
- Story library view with saved drafts

Suggested GIF ideas:

- Prompt to story generation flow
- Refinement prompt creating a new version
- Style comparison switching between two narrative modes

## Current Implementation Notes

- The current story engine is intentionally offline and deterministic, so the project runs end-to-end without external API keys.
- The main extension point for integrating a real model provider is `app/services/story_engine.py`.
- Story data is stored locally in `data/stories.json`.

## Future Enhancements

- Real LLM-backed story generation
- Character consistency tracking across versions
- Collaborative editing workflows
- Multilingual storytelling support
- Export formats such as PDF and Markdown

## Repository Description

AI-powered story writing platform with controllable genre, tone, and narrative style, featuring a professional editorial dashboard, version history, plot pacing tools, character relationship mapping, and live style comparison.

## Suggested GitHub Topics

`fastapi` `ai-writing` `story-generation` `creative-writing` `nlp` `dashboard` `javascript` `frontend` `python` `editor`

## Report Resources

For a project-report-ready summary, see [docs/PROJECT_SUMMARY.md](https://github.com/tapendra9104/AI-Based-Story-Writer-with-Style-Control/blob/main/docs/PROJECT_SUMMARY.md).
