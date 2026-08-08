---
id: tool-01758
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: bedtimestories
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/saivanka/bedtimestories
created: 2026-07-18
updated: 2026-07-18
no: 1758
category: 二、网文 / 长篇 AI 写作系统 库
repo: saivanka/bedtimestories
stars: 2
url: https://github.com/saivanka/bedtimestories
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 51d4371ff2940dc3
  - methods/最强写作方法论_全球最强综合版.md
---

# saivanka/bedtimestories

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/saivanka/bedtimestories
- **Stars**：2
- **语言**：TypeScript
- **License**：None
- **Topics**：ai-generator, bedtime-stories, cloudflare-pages, docker, groq, kids-app, n8n, react, tailwind
- **GitHub 描述**：✨ Magical AI-powered bedtime story generator for kids using React, Tailwind, n8n, and Groq GPT-4o. Customizable stories with name, age, and theme.
- **本地描述**：✨ Magical AI-powered bedtime story generator for kids using React, Tailwind, n8n, and Groq GPT-4o. Customizable stories with name, age, and theme.
- **拉取时间**：2026-07-23 23:30:17

---

# 🌙 Magical Bedtime Stories

Create magical AI-powered bedtime stories for kids using your child’s name, age, and favorite story elements.

🟢 **Live App:** [bedtimestories.pages.dev](https://bedtimestories.pages.dev)  
💻 **Source Code:** [GitHub](https://github.dev/theuntoldcreator/bedtimestories)

---

## ✨ Features

- Custom name and age
- Choose story type: Adventure, Horror, Love, Sci-fi, Fairytales
- Pick up to 3 story elements (e.g., dinosaur, rainbow, spaceship)
- Add custom detail (optional)
- AI-generated story via Groq (GPT-4o)
- Clean, mobile-friendly UI
- Hosted on Cloudflare Pages
- Story served via n8n Webhook

---

## 🔧 Tech Stack

| Layer      | Tool                       |
|------------|----------------------------|
| Frontend   | React, Tailwind, Vite      |
| Backend    | n8n + Groq Chat            |
| Hosting    | Cloudflare Pages, GCP VM   |
| AI Cleanup | Regex via `Set` node       |

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 🚀 Quick Start

### 1. Clone the Project

```bash
git clone https://github.com/theuntoldcreator/bedtimestories
cd bedtimestories
```

## 2. Frontend Setup (React)

```bash
npm install
npm run dev         # Local development
``` 

#### Deploy to Cloudflare Pages
Connect this repo to Cloudflare Pages:

Build command: ```npm run build```

Output directory: ```dist```



## 3. Backend Setup (n8n + Groq)
Run n8n in Docker on GCP:
```bash
docker run -d --name n8n \
-p 5678:5678 \
-e N8N_BASIC_AUTH_ACTIVE=false \
-e N8N_CORS_ALLOW_ORIGIN=https://bedtimestories.pages.dev \
-e N8N_CORS_ALLOW_METHODS=GET,POST,OPTIONS \
-e N8N_CORS_ALLOW_HEADERS="Content-Type,Authorization" \
-e WEBHOOK_URL=https://your-domain.com \
n8nio/n8n
```
## 4. Setup n8n Workflow
You can import the full workflow from n8n.json or build it manually with these nodes:

#### A. Webhook – listens to POST from frontend


#### B. AI Agent – receives story prompt


#### C. Groq Chat Model – GPT-4o backend


#### D. Set Node – removes <think>...</think> using:
```bash
{{ $json.output ? $json.output.replace(/<think>[\s\S]*?<\/think>/gi, '').trim() : '' }}
```

#### E. Respond to Webhook – sends JSON back to frontend:
```bash
{
  "post": "Here's your magical bedtime story!",
  "response": "{{ $json.cleanedStory }}"
}
```
✅ Make sure the workflow is active.

🔄 Flow Diagram
![Alt text of the image](https://github.com/theuntoldcreator/bedtimestories/blob/main/workflow.png)

#### 🧪 Common Issues
### ❌ CORS Error?
Make sure N8N_CORS_ALLOW_ORIGIN=https://bedtimestories.pages.dev is set.

### ❌ Webhook Returns Template?
Ensure your Respond node returns proper JSON and not {{$json.output}}.

## 5. 🛠 Future Ideas
🗣️ Add voice (text-to-speech)
📄 Download as PDF
🖼️ AI-generated story art
🧑‍🎓 Add multi-language support
📄 License
MIT © [TheUntoldCreator](https://github.dev/theuntoldcreator)

“Because every child deserves a magical story made just for them.”

