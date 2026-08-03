---
id: tool-01326
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: AI-story-board-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/whargrove671-droid/ai-story-board-generator
created: 2026-07-18
updated: 2026-07-18
no: 1326
category: 二、网文 / 长篇 AI 写作系统 库
repo: whargrove671-droid/AI-story-board-generator
stars: 1
url: https://github.com/whargrove671-droid/ai-story-board-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# whargrove671-droid/AI-story-board-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/whargrove671-droid/ai-story-board-generator
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：whargrove671-droid/AI-story-board-generator
- **拉取时间**：2026-07-23 23:17:46

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI Story Generator

A private Next.js web application that generates AI-powered stories with stunning images. Enter a story idea, and watch as AI creates a complete 5-scene narrative with custom images for each scene.

## Features

- **Secure Authentication**: Email/password authentication powered by Supabase
- **AI Story Generation**: OpenAI GPT-4 generates detailed 5-scene narratives
- **AI Image Generation**: Together AI creates 16:9 cinematic images for each scene
- **Story Management**: View all your generated stories in a clean, organized dashboard
- **Real-time Updates**: Watch as your stories and images are generated in real-time
- **Responsive Design**: Beautiful UI built with Tailwind CSS and shadcn/ui components

## Tech Stack

- **Framework**: Next.js 13+ (App Router)
- **Database**: Supabase (PostgreSQL)
- **Authentication**: Supabase Auth
- **AI Services**:
  - OpenAI GPT-4 Mini (Story generation)
  - Together AI FLUX.1 (Image generation)
- **Styling**: Tailwind CSS
- **UI Components**: shadcn/ui

## Prerequisites

Before you begin, you'll need to obtain API keys from:

1. **OpenAI API Key**
   - Visit https://platform.openai.com/api-keys
   - Create a new API key
   - Copy and save it securely

2. **Together AI API Key**
   - Visit https://api.together.xyz/settings/api-keys
   - Create a new API key
   - Copy and save it securely

## Getting Started

### 1. Configure Environment Variables

The Supabase configuration is already set up. You just need to add your API keys to the `.env` file:

```bash
# The file already has these values:
NEXT_PUBLIC_SUPABASE_URL=https://rgysjpyqxdrynzrwdhfj.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# Add your API keys:
OPENAI_API_KEY=sk-your-openai-key-here
TOGETHER_API_KEY=your-together-api-key-here
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Run the Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### 4. Create an Account

1. Click "Sign up" on the login page
2. Enter your email and password
3. You'll be automatically redirected to the dashboard

## How to Use

1. **Generate a Story**:
   - Enter your story idea in the text area (e.g., "A brave knight embarks on a quest to find a magical crystal")
   - Click "Generate Story"
   - Wait while AI creates your 5-scene narrative

2. **View Generated Scenes**:
   - Each story will display 5 scenes
   - Each scene includes:
     - A detailed script
     - A cinematic 16:9 image
     - The image generation prompt used

3. **Manage Your Stories**:
   - All your stories are displayed on the dashboard
   - Stories are ordered by creation date (newest first)
   - Each story card shows the generation status

## Database Schema

The application uses three main tables:

- **stories**: Stores story metadata (title, status, timestamps)
- **scenes**: Stores individual scenes with scripts and image prompts
- Row Level Security (RLS) ensures users can only access their own data

## API Routes

- `/api/generate-story`: Generates 5-scene narratives using OpenAI
- `/api/generate-images`: Creates images for each scene using Together AI

## Security

- All database tables are protected with Row Level Security (RLS)
- Users can only access their own stories and scenes
- Authentication is required for all protected routes
- API keys are stored securely in environment variables

## Troubleshooting

**Images not generating?**
- Check that your TOGETHER_API_KEY is correct in the `.env` file
- Verify your Together AI account has available credits

**Stories not generating?**
- Check that your OPENAI_API_KEY is correct in the `.env` file
- Verify your OpenAI account has available credits

**Authentication issues?**
- Clear your browser cookies and try again
- Check that the Supabase environment variables are correct

## Production Deployment

For production deployment:

1. Build the application:
   ```bash
   npm run build
   ```

2. Deploy to your preferred hosting platform (Vercel, Netlify, etc.)

3. Add environment variables to your hosting platform's settings

## License

This project is private and for personal use only.
