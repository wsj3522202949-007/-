---
id: tool-01910
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 中文友好, 大纲规划, 多Agent, 灵感创意]
title: storyboard-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/soyooaitools/storyboard-generator
created: 2026-07-18
updated: 2026-07-18
no: 1910
category: 二、网文 / 长篇 AI 写作系统 库
repo: soyooAiTools/storyboard-generator
stars: 0
url: https://github.com/soyooaitools/storyboard-generator
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# soyooAiTools/storyboard-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/soyooaitools/storyboard-generator
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI storyboard generator
- **本地描述**：AI storyboard generator
- **拉取时间**：2026-07-23 23:34:40

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Storyboard Generator

AI 分镜生成器 — 上传策划文档，自动生成分镜配图。

## 功能
- 📄 上传策划文档（PDF/图片）
- 🎬 AI 解析文案 → 自动生成分镜帧（GPT-5.4）
- 🎨 AI 自动生成配图（GPT-image-1，帧间一致性）
- ✏️ 分镜帧编辑/重新生成
- 📥 PDF 导出
- 🗺 分镜 → V4 实体蓝图转换

## 技术栈
- 后端：Node.js (CJS) + 原生 HTTP
- 前端：React + Vite
- AI：GPT-5.4 (分镜解析) + GPT-image-1 (配图) + Gemini (编辑 fallback)
- Python 3.8 (AI 调用 subprocess)

## 部署
```bash
npm install
cd frontend && npm install && npx vite build && cd ..
cp .env.example .env  # 填入 API keys
pm2 start server.cjs --name storyboard-gen
```

## 环境变量
- `PORT` — 服务端口（默认 3903）
- `OPENAI_API_KEY` — OpenAI API Key（GPT-5.4 + gpt-image-1）
- `GEMINI_API_KEY` — Gemini API Key（编辑 fallback）
- `GOOGLE_GEMINI_BASE_URL` — Gemini 中转地址

## 关联项目
- [blueprint](https://github.com/soyooAiTools/blueprint) — 蓝图编辑器（"有分镜"模式）
