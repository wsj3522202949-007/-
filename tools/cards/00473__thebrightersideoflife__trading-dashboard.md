---
id: tool-00473
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: trading-dashboard
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/thebrightersideoflife/trading-dashboard
created: 2026-07-18
updated: 2026-07-18
no: 473
category: 二、网文 / 长篇 AI 写作系统 库
repo: thebrightersideoflife/trading-dashboard
stars: 1
url: https://github.com/thebrightersideoflife/trading-dashboard
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: de419ee44c2e4cab
  - methods/最强写作方法论_全球最强综合版.md
---

# thebrightersideoflife/trading-dashboard

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/thebrightersideoflife/trading-dashboard
- **Stars**：1
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A mini trading analytics engine with backend API without writing a server, and a data pipeline powering charts + calendar
- **本地描述**：A mini trading analytics engine with backend API without writing a server, and a data pipeline powering charts + calendar
- **拉取时间**：2026-07-23 22:52:53

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Trading Dashboard

A high-performance trading journal built with React, Supabase, and Recharts.

## Architecture

- **API**: Supabase (PostgreSQL)
- **Styling**: Custom CSS Architecture (found in `src/assets/styles/`)
- **Charts**: Recharts for Equity Curve & Gauges
- **Hooks**: Custom hooks for Auth and Data fetching

## Setup

1. `npm install`
2. Create `.env` with `VITE_SUPABASE_URL` and `VITE_SUPABASE_ANON_KEY`.
3. `npm run dev`
