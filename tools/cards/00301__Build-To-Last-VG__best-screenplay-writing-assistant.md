---
id: tool-00301
type: tool
area: 库
status: active
tags: [RAG, JavaScript, 协议未明, 需API密钥, 英文文档, 人物设定]
title: best-screenplay-writing-assistant
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/build-to-last-vg/best-screenplay-writing-assistant
created: 2026-07-18
updated: 2026-07-18
no: 301
category: 二、网文 / 长篇 AI 写作系统 库
repo: Build-To-Last-VG/best-screenplay-writing-assistant
stars: 0
url: https://github.com/build-to-last-vg/best-screenplay-writing-assistant
tier: "C"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Build-To-Last-VG/best-screenplay-writing-assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/build-to-last-vg/best-screenplay-writing-assistant
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A tool to help you write screenplays for tv and movie and novels. and its landings page (with framer?), seo optimized. and the agent system to control it all. tech stack: tailwind, apis mcps for marketing
- **本地描述**：A tool to help you write screenplays for tv and movie and novels. and its landings page (with framer?), seo optimized. and the agent system to control it all. tech stack: tailwind, apis mcps for marketing
- **拉取时间**：2026-07-23 22:47:51

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Stomo — From the story in your heart to the people who need to hear it

A web app for screenwriters, novelists, and TV creators to:
- Answer guided questions about their story
- Generate a beautiful Story Bible
- Export and save their work

**Live at:** stomo-write.com

## Quick Start

1. **Deploy to Vercel**
   ```bash
   git push
   # Vercel auto-deploys
   ```

2. **Configure Supabase**
   - Create a project at supabase.com
   - Run SQL schema from schema.sql
   - Add API keys to Vercel environment variables

3. **Set Environment Variables in Vercel**
   - VITE_SUPABASE_URL: https://vdtiqjwatlxjunqunlyk.supabase.co
   - VITE_SUPABASE_ANON_KEY: [your publishable key]
   - VITE_BUFFER_API_KEY: [your buffer key]

## Files

- `src/App.jsx` - React app with Supabase integration
- `schema.sql` - Database schema (run in Supabase)
- `brand-config.json` - Brand colors and guidelines
- `index.html` - Vite entry point
- `vite.config.js` - Build configuration
- `vercel.json` - Deployment config

## Brand

- **Domain:** stomo-write.com
- **Colors:** Amber (#D97706), Dark Blue (#1E3A8A), Old Paper (#FAF8F3)
- **Tagline:** From the story in your heart to the people who need to hear it

## Next Steps

1. Run schema.sql in Supabase
2. Deploy on Vercel (auto-deploys on git push)
3. Test: Sign up → Create story → Save

## Agent System (Next Weekend)

Marketing, Reach, Product, Tech, and Finance agents to:
- Generate and post content to Buffer
- Track SEO and discoverability
- Manage paid ads (Google, Facebook)
- Monitor infrastructure
- Track metrics and growth

See brand-config.json for marketing guidelines.
