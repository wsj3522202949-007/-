---
id: tool-00250
type: tool
area: 库
status: active
tags: [协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: wordpress-blog-automation
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/51-shenn/wordpress-blog-automation
created: 2026-07-18
updated: 2026-07-18
no: 250
category: 二、网文 / 长篇 AI 写作系统 库
repo: 51-Shenn/wordpress-blog-automation
stars: 1
url: https://github.com/51-shenn/wordpress-blog-automation
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# 51-Shenn/wordpress-blog-automation

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/51-shenn/wordpress-blog-automation
- **Stars**：1
- **语言**：None
- **License**：MIT
- **Topics**：ai, ai-agents, artificial-intelligence, automation, blog, chatgpt, google-sheets, n8n, n8n-template, n8n-workflow, no-code, openai, seo, seo-friendly, seo-optimized, wordpress, workflow
- **GitHub 描述**：An automated n8n workflow that generates SEO blog articles from Google Sheets and publishes them as drafts to WordPress. Features AI blog writing, relevant image selection from Pexels, preview URL logging, error handling, and email notifications.
- **本地描述**：An automated n8n workflow that generates SEO blog articles from Google Sheets and publishes them as drafts to WordPress. Features AI blog writing, relevant image selection from Pexels, preview URL logging, error handling, and email notifications.
- **拉取时间**：2026-07-23 22:46:23

---

# AI SEO Blog Generator for WordPress

This n8n workflow automates the process of generating SEO-friendly blog articles, selecting relevant featured images from Pexels, uploading drafts to WordPress, and updating Google Sheets with the final publishing details.

The workflow is designed for teams that manage multiple websites and want to reduce manual work in blog writing, image selection, WordPress uploading, and tracking.

<p align="left">
  <img src="https://img.shields.io/badge/n8n-EA4B71?style=for-the-badge&logo=n8n&logoColor=white" alt="n8n" />
  <img src="https://img.shields.io/badge/WordPress-21759B?style=for-the-badge&logo=wordpress&logoColor=white" alt="WordPress" />
  <img src="https://img.shields.io/badge/ChatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white" alt="ChatGPT" />
  <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail" />
  <img src="https://img.shields.io/badge/Google%20Sheets-34A853?style=for-the-badge&logo=google-sheets&logoColor=white" alt="Google Sheets" />
  <img src="https://img.shields.io/badge/Pexels-05A081?style=for-the-badge&logo=pexels&logoColor=white" alt="Pexels" />
</p>

<img width="2160" height="1440" alt="Screenshot 2026-05-27 145659" src="https://github.com/user-attachments/assets/3fc48770-1f7b-4c91-b140-3ba9fea936af" />

<p align="center">
  <strong>
    Live now on
    <a href="https://n8n.io/workflows/15814-generate-seo-blog-drafts-from-google-sheets-to-wordpress-with-openai/">
      n8n.io
    </a>
  </strong>
</p>

## Workflow Preview

The full workflow is large, so this overview image is meant to show the overall structure only. For clearer node-level details, refer to [Screenshots](#screenshots).

<img width="1798" height="983" alt="Screenshot 2026-05-19 215830" src="https://github.com/user-attachments/assets/70ce3dd3-7d1e-48e3-b6f8-9a5c421e676a" />

## What This Workflow Does

This workflow helps you:

- Read blog requirements from **Google Sheets**
- Generate SEO-friendly blog drafts with **OpenAI**
- Select a relevant **Pexels featured image** using a second AI Agent
- Upload the image and draft post to **WordPress**
- Route posts to the correct WordPress site based on the `website` column
- Update Google Sheets with image details, draft/post URL, and completion status
- Send a **Gmail completion email** when all rows are processed

## Who Is This For?

This workflow is useful for:

- **SEO agencies** producing blog drafts for multiple client websites
- **Content teams** managing a publishing queue in Google Sheets
- **WordPress site managers** who want to reduce manual content uploading
- **Freelancers** who prepare draft posts for client review
- Businesses that want **AI-assisted content drafts** without auto-publishing

## Quick Start

1. Download or clone this repository.
2. Import `workflow.json` into n8n.
3. Copy the Google Sheets [template](https://docs.google.com/spreadsheets/d/1ybJrjB6vnHmLUqWLYPXC7CKwcZ6UeoJKjqfrEDivujE/copy).
4. Connect the required credentials in n8n.
5. Select the correct Google Sheet and tabs in all Google Sheets nodes.
6. Update the WordPress routing rules in `Map to WordPress Site`.
7. Add one test row and run the workflow manually.
8. Activate the workflow after testing.

## Google Sheets Setup

Use the provided spreadsheet template and fill in the required fields.

Required input columns include:

| Column | Description |
|---|---|
| `no` | Unique row reference number |
| `website` | Target WordPress website |
| `language` | Blog language |
| `word_count` | Target word count |
| `meta_title` | SEO meta title |
| `meta_desc` | SEO meta description |
| `keyword` | Primary SEO keyword |
| `targeted_url` | Internal link to include in the blog |
| `done` | Processing status |

The workflow will update these columns automatically:

| Column | Description |
|---|---|
| `photo_url` | Selected Pexels image URL |
| `alt_text` | Generated image alt text |
| `photographer` | Pexels photographer name |
| `pexels_url` | Original Pexels image page |
| `wp_url` | WordPress draft/post URL |
| `done` | Updated to `true` after successful processing |

## Setup Guide

1. Copy the Google Sheets template: [Click Here](https://docs.google.com/spreadsheets/d/1ybJrjB6vnHmLUqWLYPXC7CKwcZ6UeoJKjqfrEDivujE/copy)
2. Connect your **Google Sheets** credential in all Google Sheets nodes.
3. For Google Sheets nodes starting with `Log`, select the `Logs` sheet.
4. For the other Google Sheets nodes, select the `Automation` sheet.
5. Connect your **OpenAI** credential in the Blog Article Model and Image Model nodes.
6. Add your **Pexels API key** to the Pexels HTTP Request node using Header Auth.
7. Connect your **Gmail** account and set the email recipient in the Gmail node.
8. Create a **WordPress Application Password** for each WordPress site.
9. Configure the WordPress and HTTP Request credentials for each site.
10. Update the `Map to WordPress Site` Switch node so each domain routes to the correct WordPress node group.
11. Add one test row in Google Sheets.
12. Run the workflow manually and confirm that the post appears as a **draft** in WordPress.
13. Activate the workflow when testing is complete.

## Multi-Site WordPress Setup

The workflow supports **multiple WordPress sites** by routing each row based on the `website` column.

The template includes sample routing for two websites. To add another WordPress site:

1. Duplicate the WordPress node group.
2. Add the new WordPress credentials.
3. Add a new routing rule in the `Map to WordPress Site` node.
4. Match the new rule to the domain used in the Google Sheet.
5. Connect the new Switch output to the duplicated WordPress node group.
6. Connect the error outputs to the existing error logging path.

## Important Notes

- This workflow creates WordPress posts as **drafts**. It does **not publish posts automatically**.
- Review all generated content before publishing.
- Each WordPress site needs its own credentials and routing rule.
- SEO meta title and meta description are generated in the AI output, but extra nodes may be needed to write them into Yoast, Rank Math, or custom SEO fields.
- Use **n8n credentials** for API keys, passwords, and tokens. Do not hardcode secrets inside nodes.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Screenshots

[`back to top`](#seo-blog-article-generation-workflow)

### 1. Google Sheets Input and Row Filtering

<img width="1741" height="1040" alt="Google Sheets input and row filtering nodes in n8n" src="https://github.com/user-attachments/assets/83724202-1490-465c-9c4c-0fc925873763" />


### 2. AI Blog Generation and Image Selection

<img width="1731" height="1123" alt="SEO Blog AI Agent and Pexels image selection workflow nodes" src="https://github.com/user-attachments/assets/be70ed2f-dc1e-4e19-b4ad-da6f3fc87f85" />

### 3. WordPress Upload and Draft Creation

<img width="1490" height="1159" alt="WordPress media upload draft creation and featured image workflow nodes" src="https://github.com/user-attachments/assets/b1b2401c-cef5-4c0c-aeab-c2eb1af25f7a" />
