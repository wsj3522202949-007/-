---
id: tool-00317
type: tool
area: 库
status: active
tags: [协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: n8n-AI-Content-Automation-Pipeline
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/lxmachado/n8n-ai-content-automation-pipeline
created: 2026-07-18
updated: 2026-07-18
no: 317
category: 二、网文 / 长篇 AI 写作系统 库
repo: LXMachado/n8n-AI-Content-Automation-Pipeline
stars: 0
url: https://github.com/lxmachado/n8n-ai-content-automation-pipeline
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 00ba31dec2bfeaa1
  - methods/最强写作方法论_全球最强综合版.md
---

# LXMachado/n8n-AI-Content-Automation-Pipeline

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/lxmachado/n8n-ai-content-automation-pipeline
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：A simple n8n workflow that automates social content creation by pulling product data from Google Sheets, generating captions and hashtags via the OpenRouter API, and writing the results back into the sheet. Demonstrates practical experience with workflow automation, API integration, and AI-powered content generation.
- **本地描述**：A simple n8n workflow that automates social content creation by pulling product data from Google Sheets, generating captions and hashtags via the OpenRouter API, and writing the results back into the sheet. Demonstrates practical experience with workflow automation, API integration, and AI-powered content generation.
- **拉取时间**：2026-07-23 22:48:18

---

# n8n AI Social Captions Workflow

This repository contains a N8N workflow that showcases how I combine n8n, Google Sheets, and OpenRouter to automate AI-powered social captions. The automation pulls product rows that still need copy, calls an AI model for short-form captions + hashtag strings, writes the results back to the same sheet, and can optionally alert marketing once everything is ready.

## Architecture at a Glance

Trigger → Get Products → Filter Needs Caption → (optional) Batch → Generate Caption (OpenRouter) → Parse AI Result → Update Row → Notify

- **Trigger:** Manual (during build) or Cron (for scheduled runs).
- **Source of truth:** Google Sheet named `Social_Content`, columns `ProductName, ShortDescription, Link, Status, Caption, Hashtags`.
- **AI generation:** OpenRouter `google/gemini-flash-1.5` endpoint with JSON-only output enforced in the prompt.
- **Writeback:** Google Sheets Update operation, preserving row numbers from the initial fetch.
- **Notification (optional):** Email/Slack to let marketing know new captions are available.

## Prerequisites

1. n8n (cloud or self-hosted) with access to Google Sheets and HTTP Request nodes.
2. Google account with a sheet titled `Social_Content` using the column layout above.
3. OpenRouter account + API key (store as an n8n credential, never in plain JSON).
4. Optional: SMTP/Slack credential for notifications.

## Google Sheet Setup

Create a sheet called `Social_Content` with the headers in row 1:

| ProductName | ShortDescription | Link | Status | Caption | Hashtags |
| --- | --- | --- | --- | --- | related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
--- |
| Manuka MGO 550+ | Premium raw Manuka honey from NZ. | https://example.com/manuka-550 | Needs Caption |  |  |
| Honey & Lemon | Soothing blend for winter wellness. | https://example.com/honey-lemon | Needs Caption |  |  |

The workflow fills `Caption`, `Hashtags`, and flips `Status` to `Ready` once AI output is saved.

## Workflow Instructions

1. **Manual Trigger** – start with the Manual Trigger node for iterative testing. Add a Cron node later for automation.
2. **Get Products (Google Sheets)** – `Read` operation against range `Social_Content!A:F`. Ensure the node returns metadata that includes the row number (enable the “Data starts at row 2” setting or similar so n8n attaches `rowNumber`).
3. **Filter Needs Caption (IF)** – Condition checks whether the `Status` field equals `Needs Caption`. True branch continues; false branch is ignored.
4. **Split In Batches** *(optional but recommended)* – Limit to batches of 5–10 to avoid AI rate limits.
5. **Generate Caption (HTTP Request)** – POST `https://openrouter.ai/api/v1/chat/completions` with headers:
   - `Authorization: Bearer {{$credentials.openrouterApiKey}}`
   - `Content-Type: application/json`
   - `HTTP-Referer: https://yourdomain.example`
   - `X-Title: n8n-ai-social-workflow`

   Sample body:

   ```json
   {
     "model": "google/gemini-flash-1.5",
     "messages": [
       {
         "role": "system",
         "content": "You help a premium honey and wellness brand write short, natural-sounding social captions."
       },
       {
         "role": "user",
         "content": "Product: {{$json[\"ProductName\"]}}\nDescription: {{$json[\"ShortDescription\"]}}\n\nWrite:\n1) One short Instagram caption (max 2 sentences) with a warm, natural tone.\n2) One line with 8-12 relevant hashtags, space-separated.\n\nReturn ONLY valid JSON:\n{\n  \"caption\": \"...\",\n  \"hashtags\": \"...\"\n}"
       }
     ]
   }
   ```

6. **Parse AI Result (Function)** – Convert the nested JSON string into fields:

   ```javascript
   return items.map(item => {
     const raw = item.json.choices[0].message.content;
     let parsed = {};

     try {
       parsed = JSON.parse(raw);
     } catch (error) {
       parsed = {
         caption: raw,
         hashtags: ""
       };
     }

     return {
       json: {
         ...item.json,
         aiCaption: parsed.caption || "",
         aiHashtags: parsed.hashtags || ""
       }
     };
   });
   ```

7. **Update Product Row (Google Sheets)** – Use the stored `rowNumber` to update columns:
   - `Caption` → `={{ $json["aiCaption"] }}`
   - `Hashtags` → `={{ $json["aiHashtags"] }}`
   - `Status` → `Ready`

8. **Notification (Optional)** – Send an email/slack message summarizing how many captions were generated in the current run.

## Exporting and Sharing

- Export the final workflow as `workflow.json` via n8n → *Workflow → Download*.
- Take a zoomed-out screenshot of the full workflow and save it as `screenshots/workflow-overview.png`.

## Repository Contents

```
README.md                ← Overview + build instructions
workflow.json            ← Exported n8n workflow (import directly)
screenshots/             ← Put workflow-overview.png here
```
