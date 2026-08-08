---
id: tool-01331
type: tool
area: 库
status: active
tags: [协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: SEO-Content-Automation-using-N8N
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/parvez-kabir/seo-content-automation-using-n8n
created: 2026-07-18
updated: 2026-07-18
no: 1331
category: 二、网文 / 长篇 AI 写作系统 库
repo: Parvez-kabir/SEO-Content-Automation-using-N8N
stars: 0
url: https://github.com/parvez-kabir/seo-content-automation-using-n8n
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 13af9324f3ec2237
  - methods/最强写作方法论_全球最强综合版.md
---

# Parvez-kabir/SEO-Content-Automation-using-N8N

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/parvez-kabir/seo-content-automation-using-n8n
- **Stars**：0
- **语言**：None
- **License**：Apache-2.0
- **Topics**：—
- **GitHub 描述**：An automated n8n workflow that researches SEO keywords, generates a full-length legal blog article with AI, creates a matching featured image, and publishes it as a draft post to WordPress — end to end, every day, with no manual keyword research or writing required.
- **本地描述**：An automated n8n workflow that researches SEO keywords, generates a full-length legal blog article with AI, creates a matching featured image, and publishes it as a draft post to WordPress — end to end, every day, with no manual keyword research or writing required.
- **拉取时间**：2026-07-23 23:17:55

---

# SEO-Content-Automation-using-N8N
An automated n8n workflow that researches SEO keywords, generates a full-length legal blog article with AI, creates a matching featured image, and publishes it as a draft post to WordPress — end to end, every day, with no manual keyword research or writing required.
<img width="1280" height="632" alt="image" src="https://github.com/user-attachments/assets/55e282db-6a0e-4460-a63a-d6ae1826710b" />

# SEO Content Automation (n8n Workflow)

An automated **n8n workflow** that researches SEO keywords, generates a full-length legal blog article with AI, creates a matching featured image, and publishes it as a **draft** post to WordPress — end to end, every day, with no manual keyword research or writing required.

Built for a law firm's content marketing (Italian legal niche), but the logic is generic enough to adapt to any WordPress site and any content vertical.

> ⚠️ **This repo contains the workflow JSON with all credentials stripped out.** You must connect your own credentials in n8n before running it. See [Setup](#setup) below.

---

## What it does

Every day at **08:00 (Rome time)**, the workflow:

1. **Finds a keyword** — Queries the SEOZoom API for keyword ideas around a topic, scores them by opportunity/difficulty/volume/search intent, and picks the best one. Falls back to a Google Sheet keyword pool if needed.
2. **Checks existing content** — Pulls existing published WordPress posts so the new article can reference them for internal linking (and avoid duplicating topics).
3. **Writes the article** — Sends the keyword + context to an OpenAI model (via an LLM Chain node) with a detailed prompt: Italian language, 1500+ words, H1, 4+ H2 sections, FAQ section, a call-to-action, and no auto-inserted disclaimer.
4. **Validates the output** — Parses the AI's JSON response and checks word count, H2 count, FAQ count, required fields, and basic on-page SEO (keyword in title/H1/body). Trims meta title/description to safe lengths and sanitizes the slug.
5. **AI quality review** — A second AI pass reviews the article for tone, legal-content quality, SEO, structure, and publish-readiness, returning a quality score and reviewer notes.
6. **Adds legal disclaimer** — Appends a standard disclaimer to the final HTML content.
7. **Generates a featured image** — Creates an infographic-style featured image prompt (icons, illustrated scene, brand color palette) and generates the image via OpenAI image generation.
8. **Publishes to WordPress** — Uploads the image, then creates the post via the WordPress REST API.
   **The post status is hard-coded to `draft` everywhere in the workflow** — it will never auto-publish. There's also a runtime safety check that throws an error if WordPress ever returns a non-`draft` status.
9. **Logs everything** — Writes results (draft link, keyword used, word count, quality score, warnings) to Google Sheets, and logs any failures at each stage to a separate error sheet.
10. **Notifies by email** — Sends a success email with the draft preview/edit link, or a failure alert to the admin if any step breaks (SEOZoom failure, OpenAI failure, WordPress failure).

There's also a secondary trigger path that watches a Google Sheet for manually-added "pending" keyword rows and processes those the same way.

---

## Workflow architecture

```
Daily Trigger (08:00 Rome)
        │
        ▼
Workflow Config (central settings node)
        │
        ▼
SEOZoom - Fetch Keyword Metrics ──► SEOZoom OK? ──(no)──► Log Error + Notify Admin
        │ (yes)
        ▼
Select Best Legal Keyword
        │
        ▼
WordPress - Get Existing Posts ──► Prepare Internal Links Context
        │
        ▼
Basic LLM Chain (writes article) ──► OpenAI Article OK? ──(no)──► Log Error + Notify Admin
        │ (yes)
        ▼
Parse & Validate Article
        │
        ▼
OpenAI - AI Quality Review ──► Process QA Review Result
        │
        ▼
Append Disclaimer + Build Final Content
        │
        ▼
Generate an image ──► Image Generated OK? ──(no)──► Log Warning (non-blocking)
        │ (yes)
        ▼
WordPress - Upload Image
        │
        ▼
Build WordPress Post Body ──► WordPress - Create Draft ──► Draft Created OK? ──(no)──► Log Error + Notify Admin
        │ (yes)
        ▼
Extract Draft Details
        │
        ▼
Sheets - Log Draft / Log Used Keyword / Log Article History
        │
        ▼
Send Success Notification (email with draft link)
```

---

## Requirements

| Service | Used for |
|---|---|
| [n8n](https://n8n.io) (self-hosted or cloud) | Running the workflow |
| [SEOZoom](https://www.seozoom.com/) API key | Keyword research / metrics |
| WordPress site with REST API enabled | Publishing draft posts |
| OpenAI API key | Article writing, QA review, image generation |
| Google account (Sheets + Gmail) | Logging and email notifications |

---

## Setup

1. **Import the workflow**
   In n8n: *Workflows → Import from File* and select `SEO_Content_Automation.json`.

2. **Connect credentials**
   Every node that talks to an external service needs its credential re-selected in n8n (they are intentionally removed from this export):
   - `WordPress - Get Existing Posts`, `WordPress - Create Draft` → HTTP Header Auth (Application Password, Base64-encoded `user:app_password`)
   - `WordPress - Upload Image` → HTTP Basic Auth (or Header/Bearer, depending on your WP auth setup)
   - `OpenAI Chat Model`, `OpenAI Chat Model1`, `Generate an image` → OpenAI API credential
   - `Sheets - Log Draft`, `Sheets - Log Used Keyword`, `Sheets - Log Article History`, `Log Error - *`, `Get row(s) in sheet*`, `Update row in sheet` → Google Sheets OAuth2
   - `Notify Admin - *`, `Send Success Notification` → Gmail OAuth2

3. **Set your SEOZoom API key**
   In the `SEOZoom - Fetch Keyword Metrics` node, replace the `api_key` query parameter (currently `YOUR_SEOZOOM_API_KEY`) with your real key.

4. **Edit the `Workflow Config` node**
   This single Code node centralizes all the settings — edit it before going live:

   ```js
   seozoom_endpoint: '...',          // confirm with SEOZoom docs
   seozoom_country: 'it',
   seozoom_language: 'it',
   wordpress_url: 'https://your-site.com',
   wordpress_post_status: 'draft',   // never change to 'publish'
   content_language: 'italiano',
   content_min_words: 900,
   content_min_h2_count: 3,
   content_min_faq_count: 3,
   firm_name: '...',
   firm_phone: '...',
   firm_email: '...',
   admin_email: '...',
   from_email: '...',
   google_sheet_id: '...',
   max_retries: 3
   ```

5. **Set up the Google Sheet**
   Create a spreadsheet with tabs for: keyword pool, error log, draft log, and article history. Update `google_sheet_id` in the config and point each Google Sheets node at the matching tab.

6. **Test with a manual run** before turning on the schedule trigger — check that the created post lands in WordPress as a `draft`, never `publish`.

---



related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---


