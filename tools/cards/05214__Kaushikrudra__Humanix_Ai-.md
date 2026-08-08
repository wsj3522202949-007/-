---
id: tool-05214
type: tool
area: 库
status: active
tags: [去AI味, TypeScript, 协议未明, 需API密钥, 英文文档]
title: Humanix_Ai-
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/kaushikrudra/humanix_ai-
created: 2026-07-18
updated: 2026-07-18
no: 5214
category: 一、去 AI 味 / Humanizer 库
repo: Kaushikrudra/Humanix_Ai-
stars: 1
url: https://github.com/kaushikrudra/humanix_ai-
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 8afee9fdd4de0ad7
  - methods/改稿润色指令库.md
---

# Kaushikrudra/Humanix_Ai-

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/kaushikrudra/humanix_ai-
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：HumanixAI: An all-in-one platform featuring AI Content Generation, AI Text Humanizer, Paraphraser, and AI Pattern Detector. Powered by Next.js, Express, Prisma, and Gemini 2.5.
- **本地描述**：HumanixAI: An all-in-one platform featuring AI Content Generation, AI Text Humanizer, Paraphraser, and AI Pattern Detector. Powered by Next.js, Express, Prisma, and Gemini 2.5.
- **拉取时间**：2026-07-25 18:10:19

---

# HumanixAI - AI Content Optimization Suite

HumanixAI is a professional, full-stack web application designed for content creators to generate, humanize, paraphrase, and check text for AI patterns with high-precision custom options.

## 🚀 Key Features

* **Content Generator:** Create structured article outlines and copy drafts on any topic.
* **AI Humanizer:** Rewrite AI-generated text to sound conversational and bypass automated detection.
* **Paraphraser:** Rephrase sentences to enhance readability, flow, and clarity.
* **AI Pattern Detector:** Analyze text structure and return detailed human-vs-AI probability score breakups.
* **Advanced Settings:** Granular control over **Tone** (Professional, Casual, Academic, Creative), **Creativity levels**, and **Target word limits**.
* **Generation History:** Interactive logs to view, copy outputs, or delete past items.
* **Demo Auth & Simulation:** Smooth test-mode environment with credit quota upgrades simulator.
* **Premium UI:** Dynamic split-screen layout, dark theme glow accents, and responsive design.

---

## 🛠️ Technology Stack

* **Frontend:** Next.js 16 (App Router), React 19, Tailwind CSS, Lucide Icons, Axios.
* **Backend:** Node.js, Express, TypeScript, tsx.
* **Database & ORM:** PostgreSQL, Prisma ORM.
* **AI Engine:** Google Generative AI (Gemini 2.5 models).

---

## 📁 Project Structure

```text
Humanix_Ai/
├── backend/
│   ├── prisma/             # Database schemas & migrations
│   └── src/
│       ├── middleware/     # Auth & validation middlewares
│       ├── routes/         # AI models & user account endpoints
│       └── index.ts        # Express server entry point
├── frontend/
│   └── src/
│       ├── app/            # Next.js pages & auth wrappers
│       └── components/     # UI design elements
├── package.json            # Workspaces & running scripts config
└── .gitignore              # Files omitted from git tracking
```

---

## ⚡ Local Setup

### 1. Clone the repository & Install Dependencies
```bash
# Install dependencies for both workspaces
npm install
```

### 2. Configure Environment Variables
Create a `.env` file at the project root:
```env
# Database configuration
DATABASE_URL="postgresql://<user>:<password>@localhost:5432/humanix_ai?schema=public"

# NextAuth secrets
NEXTAUTH_SECRET="super_secret_session_key"
NEXT_PUBLIC_API_URL="http://localhost:5000"

# AI Key
GEMINI_API_KEY="your-gemini-api-key"
```

Create a `.env` file inside the `frontend` folder:
```env
NEXT_PUBLIC_API_URL="http://localhost:5000"
NEXTAUTH_URL="http://localhost:3000"
```

### 3. Generate Database Client
```bash
npm run prisma:generate
```

### 4. Run the Development Server
```bash
npm run dev
```
* **Frontend:** `http://localhost:3000`
* **Backend:** `http://localhost:5000`

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## 📄 License
This project is licensed under the MIT License.
