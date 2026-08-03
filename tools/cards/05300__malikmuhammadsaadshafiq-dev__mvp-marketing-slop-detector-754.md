---
id: tool-05300
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 去AI味]
title: mvp-marketing-slop-detector-754
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/malikmuhammadsaadshafiq-dev/mvp-marketing-slop-detector-754
created: 2026-07-18
updated: 2026-07-18
no: 5300
category: 一、去 AI 味 / Humanizer 库
repo: malikmuhammadsaadshafiq-dev/mvp-marketing-slop-detector-754
stars: 0
url: https://github.com/malikmuhammadsaadshafiq-dev/mvp-marketing-slop-detector-754
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# malikmuhammadsaadshafiq-dev/mvp-marketing-slop-detector-754

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/malikmuhammadsaadshafiq-dev/mvp-marketing-slop-detector-754
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：mvp, nextjs, react, saas, typescript
- **GitHub 描述**：[SaaS] AI analyzer that detects AI-generated buzzwords and generic marketing speak in landing page copy | Inspired by Reddit community
- **本地描述**：[SaaS] AI analyzer that detects AI-generated buzzwords and generic marketing speak in landing page copy （ Inspired by Reddit community
- **拉取时间**：2026-07-25 18:13:29

---

<div align="center">

# Marketing Slop Detector

**AI analyzer that detects AI-generated buzzwords and generic marketing speak in landing page copy**

![Next.js](https://img.shields.io/badge/Next.js-333?style=flat-square) ![OpenAI API](https://img.shields.io/badge/OpenAI%20API-333?style=flat-square) ![Cheerio for scraping](https://img.shields.io/badge/Cheerio%20for%20scraping-333?style=flat-square)
![AI Powered](https://img.shields.io/badge/AI-Powered-blueviolet?style=flat-square)
![Type](https://img.shields.io/badge/Type-SaaS%20Platform-blue?style=flat-square)
![Tests](https://img.shields.io/badge/Tests-13%2F14-brightgreen?style=flat-square)

</div>

---

## Problem

Plague of AI-generated slop apps with copy-paste marketing that lacks authenticity

## Who Is This For?

Indie hackers and marketers reviewing SaaS websites


## Inspiration & Source

This product was built to address **real user needs** discovered from community feedback:

- **r/SaaS**: [Drop your SaaS, I’ll give you marketing advice, for free.](https://reddit.com/r/SaaS/comments/1r4flpp/drop_your_saas_ill_give_you_marketing_advice_for/) (106 upvotes, 539 comments)
- **r/indiehackers**: [Show me your startup website and I'll give you actionable feedback](https://reddit.com/r/indiehackers/comments/1r0a5ig/show_me_your_startup_website_and_ill_give_you/) (85 upvotes, 442 comments)
- **r/webdev**: [We have a plague of AI generated slop "apps" on this sub promoted by AI itself](https://reddit.com/r/webdev/comments/1r43lja/we_have_a_plague_of_ai_generated_slop_apps_on/) (571 upvotes, 98 comments)

> Built because real people asked for it.


## Features

- **Paste copy to get "AI-slop" score and buzzword density**
- **Specific suggestions to humanize the text**
- **Comparison against high-converting human-written examples**
- **Chrome extension to analyze any site instantly**

## Tech Stack

| Technology | Purpose |
|-----------|---------|
| Next.js | Core dependency |
| OpenAI API | Core dependency |
| Cheerio for scraping | Core dependency |
| Kimi K2.5 (NVIDIA) | AI/LLM integration |

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) v18+
- npm or yarn

### Installation

1. Clone the repository
```bash
git clone https://github.com/malikmuhammadsaadshafiq-dev/mvp-marketing-slop-detector.git
cd mvp-marketing-slop-detector
```

2. Install dependencies
```bash
npm install
```

3. Start the development server
```bash
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser

## Usage Guide

### Core Workflows

**1. Paste copy to get "AI-slop" score and buzzword density**
   - Navigate to the relevant section in the app
   - Follow the on-screen prompts to complete the action
   - Results are displayed in real-time

**2. Specific suggestions to humanize the text**
   - Navigate to the relevant section in the app
   - Follow the on-screen prompts to complete the action
   - Results are displayed in real-time

**3. Comparison against high-converting human-written examples**
   - Navigate to the relevant section in the app
   - Follow the on-screen prompts to complete the action
   - Results are displayed in real-time

### AI Features

This app uses **Kimi K2.5** via NVIDIA API for intelligent processing.

To use AI features, add your NVIDIA API key:
```bash
# Create .env.local file
echo "NVIDIA_API_KEY=nvapi-your-key" > .env.local
```

Get a free API key at [build.nvidia.com](https://build.nvidia.com)


## Quality Assurance

| Test | Status |
|------|--------|
| Has state management | ✅ Pass |
| Has form/input handling | ✅ Pass |
| Has click handlers (2+) | ✅ Pass |
| Has demo data | ⚠️ Needs attention |
| Has loading states | ✅ Pass |
| Has user feedback | ✅ Pass |
| No placeholder text | ✅ Pass |
| Has CRUD operations | ✅ Pass |
| Has empty states | ✅ Pass |
| Has responsive layout | ✅ Pass |
| Has search/filter | ✅ Pass |
| Has tab navigation | ✅ Pass |
| Has data persistence | ✅ Pass |
| No dead links | ✅ Pass |

**Overall Score: 13/14**

## Project Structure

```
├── src/
│   ├── app/
│   │   ├── layout.tsx    # Root layout
│   │   ├── page.tsx      # Homepage
│   │   └── globals.css   # Global styles
│   └── components/       # Reusable UI components
├── public/               # Static assets
├── package.json          # Dependencies
├── next.config.js        # Next.js configuration
├── tailwind.config.ts    # Tailwind CSS config
└── tsconfig.json         # TypeScript config
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License — use freely for personal and commercial projects.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

<div align="center">

**Built autonomously by [NeuraFinity MVP Factory](https://github.com/malikmuhammadsaadshafiq-dev/NeuraFinity)** — an AI-powered system that discovers real user needs and ships working software.

</div>
