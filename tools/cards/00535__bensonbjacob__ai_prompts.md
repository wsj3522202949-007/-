---
id: tool-00535
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: ai_prompts
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/bensonbjacob/ai_prompts
created: 2026-07-18
updated: 2026-07-18
no: 535
category: 二、网文 / 长篇 AI 写作系统 库
repo: bensonbjacob/ai_prompts
stars: 0
url: https://github.com/bensonbjacob/ai_prompts
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
content_hash: 1e72b02ffdd73a3c
  - methods/最强写作方法论_全球最强综合版.md
---

# bensonbjacob/ai_prompts

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/bensonbjacob/ai_prompts
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Prompts is a CRUD application built with Next.js, Tailwind CSS, and MongoDB. It allows users to create, discover, and share AI prompts, fostering a collaborative environment for creative writing and ideation. With Prompts, you can unleash your imagination and explore a diverse range of prompts contributed by others.
- **本地描述**：Prompts is a CRUD application built with Next.js, Tailwind CSS, and MongoDB. It allows users to create, discover, and share AI prompts, fostering a collaborative environment for creative writing and ideation. With Prompts, you can unleash your imagination and explore a diverse range of prompts contributed by others.
- **拉取时间**：2026-07-23 22:54:38

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Prompts

[Live App](https://share-prompts-gamma.vercel.app)

Prompts is a CRUD application built with Next.js, Tailwind CSS, and MongoDB. It allows users to create, discover, and share AI prompts, fostering a collaborative environment for creative writing and ideation. With Prompts, you can unleash your imagination and explore a diverse range of prompts contributed by others.

## Features

- Create AI Prompts: Generate and submit your own AI prompts to inspire others and spark their creativity.
- Explore the Feed: Browse through a dynamic feed of AI prompts contributed by users worldwide.
- Search and Filter: Find specific prompts or narrow down your search based on different categories or tags.
- Responsive Design: Enjoy a seamless experience on different devices, thanks to the app's responsive layout.

## Installation

### Clone the repository and install dependencies   

```bash
git clone https://github.com/bensonbjacob/ai_prompts.git
cd ai_prompts
npm install
```

### Configure Environment Variables

1.  Create an .env file
2.  Add the following fields along with your own environment variables

```javascript
GOOGLE_ID=
GOOGLE_CLIENT_SECRET=
MONGODB_URI=
NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_URL_INTERNAL=http://localhost:3000
NEXTAUTH_SECRET=
```

### Start the Development Server

```bash
npm run dev
```
