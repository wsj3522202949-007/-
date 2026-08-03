---
id: tool-01685
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: LOVR
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/arts-hcs/lovr
created: 2026-07-18
updated: 2026-07-18
no: 1685
category: 二、网文 / 长篇 AI 写作系统 库
repo: Arts-HCS/LOVR
stars: 1
url: https://github.com/arts-hcs/lovr
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Arts-HCS/LOVR

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/arts-hcs/lovr
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：ai, full-stack, google-apis, nextjs, openai, prisma, productivity, student-tools
- **GitHub 描述**：LOVR is an AI-powered academic platform that generates content without prompts, learns from the users' writing styles and automatically organizes assignments in a calendar
- **本地描述**：LOVR is an AI-powered academic platform that generates content without prompts, learns from the users' writing styles and automatically organizes assignments in a calendar
- **拉取时间**：2026-07-23 23:28:10

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# LOVR

LOVR is a student productivity platform designed to make academic life easier.  
Instead of forcing users to manually manage tasks in a rigid calendar, LOVR lets them add things naturally, almost like talking to someone.

You can write something like:

> "Entregar la cosa de historia para el siguiente martes"

and LOVR will understand it, create the task, and place it on the correct day.  
From there, you can add context, generate academic content, export it to Google Docs with MLA or APA formatting, or turn the response into slides.

LOVR also lets you build your own writing models by importing your own documents or texts, so generated content matches your style instead of sounding like generic AI.

## Features

- Smart calendar with natural-language task input
- Task context support for organizing all the material you need
- AI-powered content generation
- Export to Google Docs
- MLA and APA formatting support
- Slide generation from generated content
- Custom writing models based on your own texts
- Google API integration
- OpenAI API integration

## Tech Stack

- **Frontend:** Next.js
- **Database:** MySQL, later migrated to PostgreSQL
- **ORM:** Prisma
- **APIs:** Google APIs, OpenAI API, REST APIs
- **Language:** JavaScript / TypeScript

## Project Goal

The goal of LOVR is to reduce friction in student workflow.

Instead of:
- opening a calendar,
- selecting a date manually,
- typing tasks in a strict format,
- rewriting content in different tools,

LOVR lets users enter information naturally and then turns it into something useful.

## How It Works

### 1. Add tasks naturally
Users type tasks in plain language. LOVR interprets the date and task automatically.

### 2. Add context
Each task can store extra context such as:
- notes
- copied text
- instructions
- images
- reference material

### 3. Generate output
LOVR uses the stored context to generate structured responses that can be exported to:
- Google Docs
- Slides

### 4. Match the user’s style
Users can create LOVR models from their own writing so the generated text sounds more personal and less like AI.

## Getting Started

### Prerequisites
Make sure you have:
- Node.js installed
- a database running
- API keys for Google and OpenAI

### Installation

```bash
git clone https://github.com/Arts-HCS/LOVR.git
cd lovr
npm install
```

### Environment Variables
Create a .env file in the root of the project and add your variables:
```bash
DATABASE_URL="your-database-url"
GOOGLE_CLIENT_ID="your-google-client-id"
GOOGLE_CLIENT_SECRET="your-google-client-secret"
GOOGLE_REDIRECT_URI="your-google-redirect-uri"
OPENAI_API_KEY="your-openai-api-key"
```

### Database Setup
If you're using Prisma:
```bash
npx prisma generate
npx prisma migrate dev
```

### Run the project
```bash
npm run dev
```

## Future Improvements

- Better task parsing  
- Improved AI context handling  
- More export formats  
- Better slide customization  
- Stronger model training for writing style  
- Collaboration features  
- Mobile-friendly improvements  

## Contributing

This project is currently developed by a single creator, but suggestions and feedback are always welcome.

Areas where contributions would be especially valuable:

- Adding support for modifying the date and time of existing tasks  
- Expanding features within the LOVR panel  
- Improving data handling, validation, and overall data flow  
- Enhancing performance and scalability  
- Improving UI/UX consistency across the platform  

If you plan to contribute, consider opening an issue first to discuss the change before submitting a pull request.

## Contact

Created by Arturo Sandoval Cervantes  
www.linkedin.com/in/arturo-sandoval-cervantes-67a892377



