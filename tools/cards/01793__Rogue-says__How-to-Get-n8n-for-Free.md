---
id: tool-01793
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: How-to-Get-n8n-for-Free
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/rogue-says/how-to-get-n8n-for-free
created: 2026-07-18
updated: 2026-07-18
no: 1793
category: 二、网文 / 长篇 AI 写作系统 库
repo: Rogue-says/How-to-Get-n8n-for-Free
stars: 0
url: https://github.com/rogue-says/how-to-get-n8n-for-free
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
content_hash: b1df25e001b65a42
  - methods/最强写作方法论_全球最强综合版.md
---

# Rogue-says/How-to-Get-n8n-for-Free

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/rogue-says/how-to-get-n8n-for-free
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：n8n is an open-source automation tool that lets you connect apps, APIs, and workflows without writing much code. You can self-host it for free and build powerful automatons across tools like Slack, Notion, Google Sheets, and more
- **本地描述**：n8n is an open-source automation tool that lets you connect apps, APIs, and workflows without writing much code. You can self-host it for free and build powerful automatons across tools like Slack, Notion, Google Sheets, and more
- **拉取时间**：2026-07-23 23:31:19

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<!-- Slide number: 1 -->
# Step 1 — Deploy n8n on Render

Go to https://render.com
and create a free account

Click New → Web Service → Existing Image.

Paste this in Docker image

docker.n8n.io/n8nio/n8n

![image alt](https://github.com/Rogue-says/How-to-Get-n8n-for-Free/blob/8406aeab2cc4a175700641d306eb8f848aee3a32/dockerlink%20png.png) 


Choose the region closest to you

Select the Free Plan.

Click Deploy and wait ~2–5 minutes

![image alt](https://github.com/Rogue-says/How-to-Get-n8n-for-Free/blob/8406aeab2cc4a175700641d306eb8f848aee3a32/n8n%20page%20live.png)


Once deployed and live

Render will give you a public URL

Open the link or double click on the link

Create an n8n account

Fill in your details and mails, they will send it to you directly

Check you mail

Click License Key

You’ll receive premium features via email


<!-- Slide number: 2 -->

# Step 2 — Prevent Render from Sleeping (Keep n8n Alive)

Render free services sleep after inactivity. This breaks workflows.

Here’s the fix:

Go to https://cron-job.org

Create an account and verify your email

Create a new cron job

Paste your n8n Render URL

Set it to run every 5 minutes

This continuously pings your server and keeps it awake.
