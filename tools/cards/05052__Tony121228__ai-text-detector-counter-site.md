---
id: tool-05052
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 中文友好, 去AI味]
title: ai-text-detector-counter-site
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/tony121228/ai-text-detector-counter-site
created: 2026-07-18
updated: 2026-07-18
no: 5052
category: 一、去 AI 味 / Humanizer 库
repo: Tony121228/ai-text-detector-counter-site
stars: 1
url: https://github.com/tony121228/ai-text-detector-counter-site
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 03cfc607343767cf
  - methods/改稿润色指令库.md
---

# Tony121228/ai-text-detector-counter-site

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/tony121228/ai-text-detector-counter-site
- **Stars**：1
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：你像AI吗 - 文本检测反测站
- **本地描述**：你像AI吗 - 文本检测反测站
- **拉取时间**：2026-07-25 18:04:20

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

﻿# 你像AI吗 - 文本检测反测站

基于 PRD 的完整版 MVP：文本检测 + 风险分级 + 改写建议 + 知识库训练 + 复制 + 事件埋点。

## 功能范围（对齐 PRD）

- 文本输入与字数统计（5000 字限制）
- 敏感词提示/拦截
- AI 概率检测（第三方 API）
- 风险等级（低/中/高）与可视化进度条
- 中高风险自动生成改写建议（1-3 个版本）
- 训练功能：从整篇 AI 文本里提取“AI语句”并写入本地 knowledge-base
- 结果复制、改写复制、改写重生成
- 基础埋点接口 `/api/track`
- 超时与错误处理（检测 10 秒、改写 15 秒）
- 重试策略（服务端 2 次重试，针对 5xx/429）

## 启动

```bash
npm install
npm run dev
```

访问 `http://localhost:3000`

Windows PowerShell 如果直接执行 `npm` 被脚本策略拦截，可改用：

```powershell
npm.cmd install
npm.cmd run dev
```

## 环境变量

- `AI_API_BASE_URL`: 例如 `https://api.deepseek.com`
- `AI_API_KEY`: 第三方 API key
- `AI_DETECT_MODEL`: 检测模型名
- `AI_REWRITE_MODEL`: 改写模型名
- `HTTPS_PROXY`: 可选，HTTP/HTTPS 代理，例如 `http://127.0.0.1:7890`
- `HTTP_PROXY`: 可选，HTTP/HTTPS 代理，例如 `http://127.0.0.1:7890`

说明：项目启动脚本已启用 Node 的 `--use-env-proxy`，会在启动时读取 `.env` 中的代理变量并用于上游 API 请求。

## 接口

- `POST /api/detect`
  - 入参: `{ "text": "..." }`
  - 出参: `probability`, `riskLevel`, `reasons`, `rewrites`, `detectDurationMs` 等

- `POST /api/rewrite`
  - 入参: `{ "text": "..." }`
  - 出参: `rewrites`

- `POST /api/train`
  - 入参: `{ "text": "..." }`
  - 出参: `summary`, `suspiciousSentences`, `knowledge`, `added`, `addedCounts`

- `POST /api/track`
  - 入参: `{ "eventCode": "...", "payload": {} }`

- `GET /health`

## 知识库

- AI 痕迹规则已拆到 `knowledge-base/ai-signals/`
- 目前包含：
  - `cliche-phrases.json`
  - `transitions.json`
  - `direct-hints.json`
  - `emotional-words.json`
  - `suspicious-sentences.json`
- 每次训练还会追加一条 `knowledge-base/training-log.jsonl`
- 后续新增关键语句时，优先维护这些文件，而不是直接改 `server.js`

## 注意

若未配置 `AI_API_KEY`，检测与改写接口会返回认证失败提示。
