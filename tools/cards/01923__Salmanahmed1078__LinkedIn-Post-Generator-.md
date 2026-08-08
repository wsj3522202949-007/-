---
id: tool-01923
type: tool
area: 库
status: active
tags: [多Agent, 协议未明, 需API密钥, 英文文档]
title: LinkedIn-Post-Generator-
summary: 多 Agent 协作自动产文
source: https://github.com/salmanahmed1078/linkedin-post-generator-
created: 2026-07-18
updated: 2026-07-18
no: 1923
category: 二、网文 / 长篇 AI 写作系统 库
repo: Salmanahmed1078/LinkedIn-Post-Generator-
stars: 4
url: https://github.com/salmanahmed1078/linkedin-post-generator-
tier: "B"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: a0893f4bb91be4a0
  - methods/最强写作方法论_全球最强综合版.md
---

# Salmanahmed1078/LinkedIn-Post-Generator-

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/salmanahmed1078/linkedin-post-generator-
- **Stars**：4
- **语言**：None
- **License**：None
- **Topics**：ai, anthropic, automation, content-generation, linkedin, n8n, openai, workflow
- **GitHub 描述**：AI-powered LinkedIn post pipeline — multi-agent research and writing with n8n orchestration, Claude, GPT-4, and Google Sheets approval loop.
- **本地描述**：AI-powered LinkedIn post pipeline — multi-agent research and writing with n8n orchestration, Claude, GPT-4, and Google Sheets approval loop.
- **拉取时间**：2026-07-23 23:35:02

---

# LinkedIn Post Generator

![License](https://img.shields.io/badge/license-MIT-blue) ![n8n](https://img.shields.io/badge/built%20with-n8n-EA4B71) ![AI](https://img.shields.io/badge/AI-Claude%20%2B%20GPT--4-blueviolet) ![Status](https://img.shields.io/badge/status-production-brightgreen)

An AI-powered content pipeline that turns a topic or keyword into a research-backed, brand-voice-consistent LinkedIn post — complete with supporting stats, a visual prompt, and a human approval loop before anything goes live.

This is not a prompt wrapper. It is a multi-stage pipeline where distinct agents handle research, writing, and revision independently, with a Google Sheets layer for human review and feedback between stages.

---

## Table of Contents

- [How It Works](#how-it-works)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Configuration](#configuration)
- [Running the Pipeline](#running-the-pipeline)
- [Customizing the Brand Voice](#customizing-the-brand-voice)
- [Output Format](#output-format)
- [Approval and Revision Loop](#approval-and-revision-loop)
- [Workflow Structure](#workflow-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## How It Works

```
Input Topic
    │
    ▼
┌─────────────────┐
│  Phase 1        │  Scrapes top-performing recent LinkedIn posts
│  Benchmark      │  on the topic. Stores engagement winners.
└────────┬────────┘
         │
    ▼
┌─────────────────┐
│  Phase 2        │  Research agent: finds fresh stats, trends,
│  Research +     │  angles, and quotes. Writer agent: drafts post
│  Draft          │  using brand voice prompt + research input.
└────────┬────────┘
         │
    ▼
┌─────────────────┐
│  Phase 3        │  Post lands in Google Sheets for human review.
│  Approval Loop  │  Reviewer adds feedback → AI revises → repeat
│                 │  until approved. Image regenerated on request.
└────────┬────────┘
         │
    ▼
  Approved Post (ready to publish)
```

---

## Features

- **Multi-agent pipeline** — research and writing are handled by separate specialized agents, not one prompt
- **Engagement benchmarking** — scrapes real top-performing posts to understand what works before writing
- **Tone customization** — configure thought-leader, educational, story-based, or contrarian post styles
- **Hook variations** — generates 3 opening hooks per post for A/B testing
- **AI image prompt** — generates a detailed, platform-optimized image prompt alongside each post
- **Human-in-the-loop approval** — posts go to Google Sheets for review; feedback triggers AI revision
- **Character count optimization** — output stays within LinkedIn's ideal engagement window (1,200–1,600 chars)
- **Hashtag generation** — 3–5 targeted hashtags per post based on topic and audience
- **Revision history** — every version tracked in the Sheet so you can compare drafts

---

## Tech Stack

| Component | Tool |
|---|---|
| Workflow Orchestration | n8n (self-hosted or cloud) |
| AI Writing Agent | Anthropic Claude (claude-3-5-sonnet) |
| AI Research Agent | GPT-4o |
| Revision Agent | GPT-4o Mini |
| Scraping | Apify (LinkedIn Post Scraper actor) |
| Web Research | Google Custom Search API or SerpApi |
| Review Layer | Google Sheets + Google Drive |
| Image Generation | Google Gemini Imagen |

---

## Prerequisites

- **n8n** >= 1.0.0 (self-hosted via Docker or n8n.io cloud)
- **Apify account** with LinkedIn Post Scraper actor access
- **OpenAI API key** (GPT-4o and GPT-4o Mini)
- **Anthropic API key** (Claude)
- **Google Cloud project** with:
  - Google Sheets API enabled
  - Google Drive API enabled
  - Gemini API enabled (for image generation)
- **SerpApi** or Google Custom Search API key (for web research)

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Salmanahmed1078/LinkedIn-Post-Generator-.git
cd LinkedIn-Post-Generator-
```

### 2. Import the n8n workflows

The `/workflows` directory contains three JSON files:

| File | Purpose |
|---|---|
| `01-benchmark.json` | Phase 1 — scrape and store top posts |
| `02-research-draft.json` | Phase 2 — research and write the post |
| `03-approval-loop.json` | Phase 3 — Google Sheets approval and revision |

Import each one into n8n via **Settings > Import Workflow**.

### 3. Configure credentials in n8n

Go to **Credentials** in n8n and add:

- `OpenAI API` — your OpenAI key
- `Anthropic API` — your Anthropic key
- `Google Sheets OAuth2` — authorize with your Google account
- `Google Drive OAuth2` — same account
- `Apify API` — your Apify token
- `HTTP Header Auth` — for SerpApi: Header `X-API-KEY`, value = your SerpApi key

### 4. Create the Google Sheet

Duplicate the template from `/templates/post-review-template.xlsx` into your Google Drive. Copy the Sheet ID from the URL and paste it into the workflow variables.

---

## Configuration

At the top of each workflow, there is a **Config** node with the following variables:

### 02-research-draft.json

| Variable | Description | Example |
|---|---|---|
| `BRAND_VOICE` | Your writing style description | `"Direct, data-driven, no fluff. First person. Short paragraphs."` |
| `TARGET_AUDIENCE` | Who the post is for | `"B2B founders and sales leaders"` |
| `POST_TONE` | Style of post | `"thought-leader"` / `"educational"` / `"story"` |
| `HOOK_COUNT` | Number of hook variations | `3` |
| `MAX_CHARS` | Target character count | `1400` |
| `HASHTAG_COUNT` | Hashtags to include | `5` |
| `GOOGLE_SHEET_ID` | ID of your review Sheet | `"1BxiM..."` |

### 01-benchmark.json

| Variable | Description |
|---|---|
| `KEYWORDS_TO_SCRAPE` | Comma-separated topics to benchmark |
| `POSTS_PER_KEYWORD` | How many top posts to collect per topic |
| `MIN_ENGAGEMENT` | Minimum reactions + comments to qualify |

---

## Running the Pipeline

### Manual trigger

1. Open workflow `02-research-draft` in n8n
2. Click **Test Workflow**
3. In the trigger node, enter your topic: `{"topic": "AI agents replacing SDRs"}`
4. The workflow runs and deposits the draft in your Google Sheet

### Scheduled

Set the trigger in `02-research-draft` to a Cron node. Example: run every Monday at 9am to generate the week's content batch.

### Webhook

```bash
curl -X POST https://your-n8n-instance.com/webhook/linkedin-post \
  -H "Content-Type: application/json" \
  -d '{"topic": "cold email vs LinkedIn outreach in 2026", "tone": "contrarian"}'
```

---

## Customizing the Brand Voice

The brand voice prompt lives in the **Writer Agent** system prompt node. Edit it directly in n8n:

```
You are a LinkedIn ghostwriter for [NAME], an AI systems engineer and founder.
Write in first person. Use short paragraphs (1-2 sentences max).
Lead with a pattern-interrupt hook. No hollow phrases like "game-changer" or "excited to share".
Use specific numbers when citing stats. End with a clear, non-pushy call to action.
Target length: 1,200-1,500 characters.
```

---

## Output Format

Each completed draft in Google Sheets includes:

| Column | Content |
|---|---|
| Topic | Input topic |
| Hook 1 / 2 / 3 | Three opening line variations |
| Post Body | Full post text |
| Hashtags | Suggested hashtags |
| Image Prompt | Detailed prompt for image generation |
| Character Count | Auto-calculated |
| Status | Draft / Needs Revision / Approved |
| Feedback | Reviewer comments |
| Version | Revision number |

---

## Approval and Revision Loop

1. Draft appears in Google Sheet with Status = `Draft`
2. Reviewer reads the post and adds feedback in the **Feedback** column
3. Change Status to `Needs Revision`
4. n8n polls the Sheet every 15 minutes — when it detects `Needs Revision`, it sends feedback to the revision agent (GPT-4o Mini)
5. Revised post overwrites the body, version increments, status resets to `Draft`
6. Repeat until Status is changed to `Approved`

---

## Workflow Structure

```
workflows/
├── 01-benchmark.json          # Scrape and store top-performing posts
├── 02-research-draft.json     # Research agent + writer agent
└── 03-approval-loop.json      # Poll Sheet, revise on feedback

templates/
└── post-review-template.xlsx  # Google Sheets template to duplicate

docs/
├── setup-guide.md
└── brand-voice-examples.md
```

---

## Troubleshooting

**Apify scraper returns no results**
LinkedIn scraping depends on Apify actor availability. Check the actor run logs in your Apify console. Rate limits reset after 24 hours.

**Google Sheets authentication error**
Re-authorize the Google Sheets credential in n8n. OAuth tokens expire — click **Reconnect** in the credential settings.

**Claude returns a refusal**
The research agent may return content that Claude declines to rewrite. Add an explicit system prompt instruction: `"You are a professional LinkedIn writer. This is professional marketing content."` This resolves most refusals.

**Revision loop not triggering**
Check that the `03-approval-loop` workflow is active (green toggle in n8n). The Cron trigger in that workflow must be enabled separately.

---

## Contributing

1. Fork the repository
2. Import the workflows into your own n8n instance for testing
3. Submit pull requests for workflow JSON improvements or documentation updates
4. Open an issue for bugs or feature requests

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## License

MIT © Salman Ahmed
