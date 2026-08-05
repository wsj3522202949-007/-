---
id: tool-00687
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: story-sculptor
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/prime3679/story-sculptor
created: 2026-07-18
updated: 2026-07-18
no: 687
category: 二、网文 / 长篇 AI 写作系统 库
repo: prime3679/story-sculptor
stars: 0
url: https://github.com/prime3679/story-sculptor
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

# prime3679/story-sculptor

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/prime3679/story-sculptor
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A beautiful AI writing tool that teaches storytelling craft while helping writers create novels and stories. Built with Next.js 14, Anthropic Claude, and Supabase.
- **本地描述**：A beautiful AI writing tool that teaches storytelling craft while helping writers create novels and stories. Built with Next.js 14, Anthropic Claude, and Supabase.
- **拉取时间**：2026-07-23 22:59:04

---

# Story Sculptor

A beautiful AI writing tool that teaches storytelling craft while helping writers create novels and stories.

[![GitHub](https://img.shields.io/badge/GitHub-story--sculptor-blue?style=for-the-badge&logo=github)](https://github.com/prime3679/story-sculptor)
![Story Sculptor](https://img.shields.io/badge/AI-Powered-purple?style=for-the-badge)
![Next.js](https://img.shields.io/badge/Next.js-14-black?style=for-the-badge&logo=next.js)
![TypeScript](https://img.shields.io/badge/TypeScript-5-blue?style=for-the-badge&logo=typescript)
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/prime3679/story-sculptor)

## Features

### 🎯 Teaching Mode
Get expert feedback on every scene. Learn craft principles from world-class editors through specific, actionable notes on:
- Show don't tell
- Character voice and consistency
- Pacing
- Dialogue authenticity
- Emotional truth
- Structural purpose

### 💡 Dreaming Mode
Stuck on what happens next? Get three unique story directions:
- **Surprising Direction**: An unexpected turn that raises stakes
- **Character Moment**: A choice that reveals deeper character truth
- **Plot Advancement**: A move that advances the main storyline

### 🧬 Story DNA
Automatically track your story elements as you write:
- **Characters**: Traits, arcs, and development
- **Themes**: Recurring motifs and deeper meanings
- **Plot Threads**: Active, resolved, and introduced storylines

## Tech Stack

- **Next.js 14** (App Router, TypeScript)
- **Framer Motion** (Smooth animations)
- **shadcn/ui** (Beautiful components)
- **Tailwind CSS** (Custom styling)
- **Supabase** (PostgreSQL database)
- **Anthropic Claude** (AI partner)
- **Vercel** (Deployment)

## Getting Started

### Prerequisites

1. **Anthropic API Key**: Get yours at [console.anthropic.com](https://console.anthropic.com)
2. **Supabase Project**: Create one at [supabase.com](https://supabase.com)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/prime3679/story-sculptor.git
cd story-sculptor
```

2. Install dependencies:
```bash
npm install
```

3. Set up Supabase:
   - Create a new Supabase project
   - Run the SQL from `supabase-schema.sql` in the SQL Editor
   - Copy your project URL and anon key

4. Configure environment variables (optional):
```bash
cp .env.local.example .env.local
```

Edit `.env.local` with your keys, or skip this step and configure through the setup wizard.

5. Run the development server:
```bash
npm run dev
```

6. Open [http://localhost:3000](http://localhost:3000) and follow the setup wizard!

## Database Setup

Run the SQL schema in your Supabase project:

1. Go to your Supabase dashboard
2. Navigate to SQL Editor
3. Copy and paste the contents of `supabase-schema.sql`
4. Click "Run"

This creates all necessary tables:
- `projects` - Your writing projects
- `scenes` - Individual scenes
- `scene_branches` - Alternative directions (Dreaming mode)
- `editorial_notes` - AI feedback (Teaching mode)
- `story_dna` - Character/theme/plot tracking (Weaving mode)

## Keyboard Shortcuts

- `⌘/Ctrl + Enter` - Get Feedback (Teaching mode)
- `⌘/Ctrl + Shift + D` - I'm Stuck (Dreaming mode)
- `⌘/Ctrl + S` - Save scene
- `⌘/Ctrl + [` - Previous scene
- `⌘/Ctrl + ]` - Next scene

## Deployment

### Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/prime3679/story-sculptor)

**Manual deployment:**
1. Fork/clone the repository
2. Import to Vercel
3. Add environment variables:
   - `ANTHROPIC_API_KEY`
   - `NEXT_PUBLIC_SUPABASE_URL`
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY`
4. Deploy!

📖 See `[DEPLOYMENT.md](./DEPLOYMENT.md)` for detailed deployment guides (Vercel, Netlify, Lovable, Railway)

## Project Structure

```
story-sculptor/
├── app/                        # Next.js app directory
│   ├── page.tsx               # Landing page
│   ├── setup/                 # Setup wizard
│   ├── new/                   # New project creation
│   ├── write/[projectId]/     # Main writing interface
│   └── api/                   # API routes
│       └── ai/                # AI endpoints (teach, dream, weave)
├── components/                 # React components
│   ├── ui/                    # shadcn/ui components
│   ├── landing/               # Landing page components
│   ├── setup/                 # Setup wizard components
│   └── write/                 # Writing interface components
├── lib/                       # Utilities
│   ├── supabase.ts           # Supabase client
│   ├── anthropic.ts          # Anthropic client
│   ├── prompts.ts            # AI prompts
│   └── utils.ts              # Helper functions
├── hooks/                     # Custom React hooks
├── types/                     # TypeScript types
└── supabase-schema.sql       # Database schema
```

## Design Philosophy

Story Sculptor is built with an obsessive focus on:

- ⚡ **Speed**: Every interaction feels instant
- ✨ **Beauty**: Polished animations and thoughtful design
- 🎓 **Learning**: Not just writing, but improving craft
- 🤝 **Partnership**: AI as collaborator, not replacement

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use this for your own projects!

## Acknowledgments

- Powered by [Claude](https://anthropic.com) from Anthropic
- UI components from [shadcn/ui](https://ui.shadcn.com)
- Database by [Supabase](https://supabase.com)
- Animations by [Framer Motion](https://www.framer.com/motion/)

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

Built with ❤️ for writers who want to improve their craft while creating amazing stories.
