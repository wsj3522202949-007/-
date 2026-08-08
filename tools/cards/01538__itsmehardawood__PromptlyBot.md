---
id: tool-01538
type: tool
area: 库
status: active
tags: [互动叙事, JavaScript, 协议未明, 需API密钥, 英文文档]
title: PromptlyBot
summary: 互动叙事/聊天写故事
source: https://github.com/itsmehardawood/promptlybot
created: 2026-07-18
updated: 2026-07-18
no: 1538
category: 二、网文 / 长篇 AI 写作系统 库
repo: itsmehardawood/PromptlyBot
stars: 0
url: https://github.com/itsmehardawood/promptlybot
tier: "C"
use_case: "互动叙事/聊天写故事"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 7d52fa2e5fcda26d
  - methods/最强写作方法论_全球最强综合版.md
---

# itsmehardawood/PromptlyBot

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/itsmehardawood/promptlybot
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：PromptlyBot is a no-code AI chatbot platform designed specifically for service providers who want to automate communication, streamline customer interactions, and elevate their client experience with just writing a single line of code.
- **本地描述**：PromptlyBot is a no-code AI chatbot platform designed specifically for service providers who want to automate communication, streamline customer interactions, and elevate their client experience with just writing a single line of code.
- **拉取时间**：2026-07-23 23:23:57

---

# **PromptlyBot**

### No-Code AI Chatbot for Service Providers

PromptlyBot is a no-code AI chatbot builder that allows service providers to create and embed an intelligent chatbot on their website without technical skills. Users simply fill out a setup form, add FAQs, and receive a one-line script tag to paste into their website’s `<head>` section.

---

## **How It Works**

1. **Fill Out the Setup Form**
   Enter your business details, chatbot personality, and basic information.

2. **Add FAQs**
   Add common questions and answers your clients normally ask.

3. **Copy Your Script**
   After completing setup, PromptlyBot generates a single one-liner script tag.

4. **Paste Into Your Website**
   Add the script inside your site’s `<head>` tag, and the chatbot appears automatically.

---

## **Tech Stack**

* Next.js
* React
* API Routes / Server Actions
* Vercel (recommended for deployment)

---

## **Development Setup**

Install dependencies:

```bash
npm install
# or
yarn install
# or
pnpm install
# or
bun install
```

Run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open the app:

```
http://localhost:3000
```

Edit the UI by modifying:

```
app/page.js
```

---

## **Environment Variables**

Create `.env.local` and add required keys:

```
NEXT_PUBLIC_API_BASE_URL=https://api.neurovise.co
NEXT_PUBLIC_API_KEY=your_key_here
```

(Add more variables as needed.)

---

## **Deployment**

Deploy easily on Vercel:

* [https://vercel.com](https://vercel.com)
* [https://nextjs.org/docs/app/building-your-application/deploying](https://nextjs.org/docs/app/building-your-application/deploying)

---

## **Project Name**

`promptlybot`

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---
