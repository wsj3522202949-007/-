---
id: tool-00611
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 中文友好, 大纲规划, 多Agent, 灵感创意]
title: choose-your-script-mvp
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/030611/choose-your-script-mvp
created: 2026-07-18
updated: 2026-07-18
no: 611
category: 二、网文 / 长篇 AI 写作系统 库
repo: 030611/choose-your-script-mvp
stars: 1
url: https://github.com/030611/choose-your-script-mvp
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 5385c91d60f8cc44
  - methods/最强写作方法论_全球最强综合版.md
---

# 030611/choose-your-script-mvp

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/030611/choose-your-script-mvp
- **Stars**：1
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI interactive web novel generator with questionnaire, story choices, fallback mode, and image prompts.
- **本地描述**：AI interactive web novel generator with questionnaire, story choices, fallback mode, and image prompts.
- **拉取时间**：2026-07-23 22:56:53

---

﻿# 选择你的剧本 MVP

AI 互动爽文生成器。答问卷 → 生成主角画像 → 选剧本赛道 → 分支阅读 → 名场面配图。

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 功能清单

- DeepSeek 生成主角画像（含原型命名）
- DeepSeek 推荐匹配剧本（3选1）
- DeepSeek 生成分支章节，每章第 5 幕触发名场面
- 结构化 choices：每个选项含 title / desc / subtitle，体验更沉浸
- localStorage 存档：关闭页面不丢进度，下次打开自动提示继续
- 图片生成：配置 LiblibAI 后可直接生成名场面图片；未配置时自动回退为 Prompt
- 故事记忆摘要（memory）：跨章节保持剧情一致性
- 剧本模板 **43 个赛道**，覆盖都市/娱乐圈/校园/修仙/赛博/无限流/轻松喜剧/原生家庭/恋综/悬疑/治愈等全类型

## 剧本赛道一览（43个）

**逆袭打脸类**：娱乐圈逆袭、校园重生、穿书觉醒、都市系统、医术逆袭、军旅传承、练习生逆袭、职场爽文、悬疑犯罪、刑侦卧底

**重生穿越类**：穿书觉醒、校园重生、时间循环、轻松穿越、沙雕穿越、萌宠穿书、医术逆袭

**轻松喜剧类**：恋综对照组、霸总家的猫、刺客蹲坑、早八知识卷京城、整顿职场、黑道教父独女、土味视频冠军、猫咖猫霸、假结婚弄假成真

**甜宠恋爱类**：豪门联姻恋爱脑、契约新娘、假结婚先婚后爱、破镜重逢、久别重逢

**都市/职业类**：都市系统、商业博弈、医术逆袭、离婚律师、网安黑客、电竞NPC、记者暗访、猫咖治愈、超级英雄反差

**悬疑惊悚类**：时间循环、悬疑犯罪、精神病院失踪、灵异凶宅、都市怪谈

**世界观奇幻类**：修仙玄幻、古代宫斗、古代美食、地府临时工、赛博未来、末世异能、黑白两道

## 配置

复制 `.env.example` 为 `.env`，填入：

```text
DEEPSEEK_API_KEY=你的key
DEEPSEEK_MODEL=deepseek-chat
PORT=5173

# 可选：LiblibAI 图片生成，不配置时仅展示图片 Prompt
LIBLIB_ACCESS_KEY=你的Liblib AccessKey
LIBLIB_SECRET_KEY=你的Liblib SecretKey
LIBLIB_API_BASE=https://openapi.liblibai.cloud
LIBLIB_TEXT2IMG_PATH=/api/generate/webui/text2img/ultra
LIBLIB_STATUS_PATH=/api/generate/webui/status
LIBLIB_TEMPLATE_UUID=5d7e67009b344550bc1aa6ccbfa1d7f4
LIBLIB_ASPECT_RATIO=portrait
LIBLIB_STEPS=30
```

## 启动

```bash
node server.js
```

打开：

```text
http://localhost:5173
```

健康检查：

```text
http://localhost:5173/api/health
```

## 文件结构

```
.
├── index.html       页面入口
├── styles.css       样式
├── state.js         前端状态 / 存档工具
├── app.js           前端主逻辑（UI / 事件 / 阅读流程）
├── questions.js     问卷配置（14题）
├── templates.js     剧本模板（43个赛道）
├── api.js           API 调用封装
├── fallback.js      本地兜底逻辑（无 API Key 时启用）
├── server.js        Node.js 后端入口（DeepSeek / LiblibAI / 路由）
└── server/          后端配置与 HTTP 工具
```

## 图片生成

目前仅生成图片 Prompt，存储在 `imagePrompt` 字段。

接入图像模型后，将 `imagePrompt.prompt` 字段直接传给图像模型即可。

推荐图像模型：
- OpenAI GPT-Image / GPT-Image-2
- Flux 1.1 Pro
- 阿里通义万相
- Midjourney（通过 API）

## 存档说明

进度自动存入 `localStorage`，key 为 `choose-your-script-state`。
重新打开页面时自动检测，有存档则弹出「继续阅读 / 重新开始」选择。


