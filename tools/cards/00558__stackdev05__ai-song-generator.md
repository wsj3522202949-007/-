---
id: tool-00558
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: ai-song-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/stackdev05/ai-song-generator
created: 2026-07-18
updated: 2026-07-18
no: 558
category: 二、网文 / 长篇 AI 写作系统 库
repo: stackdev05/ai-song-generator
stars: 26
url: https://github.com/stackdev05/ai-song-generator
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
content_hash: 0f876b7ce8db4065
  - methods/最强写作方法论_全球最强综合版.md
---

# stackdev05/ai-song-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/stackdev05/ai-song-generator
- **Stars**：26
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI Song Generator – from story to full song with lyrics, vocals, and music.
- **本地描述**：AI Song Generator – from story to full song with lyrics, vocals, and music.
- **拉取时间**：2026-07-23 22:55:19

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Story Chord

Turn your stories into beautiful music with AI-powered song generation.

## Features

- 🎵 Generate custom songs from personal stories
- ✍️ AI-powered lyrics creation
- 🎼 Multiple musical styles and moods
- 🎨 Beautiful, responsive UI
- 🌙 Dark/Light mode support
- 📱 Mobile-friendly design
- 🔌 RESTful API endpoints for integration
- 💳 **Integrated Stripe payment processing**
- 🛒 **Secure checkout and purchase management**
- 📊 **Purchase status tracking**

## API Endpoints

The application provides several API endpoints for song generation and payment processing:

### Song Generation APIs
- `POST /api/v1/assist-story` - Generate story content from user queries
- `POST /api/v1/assist-style` - Determine musical style from story content
- `POST /api/v1/generate-lyrics` - Create lyrics based on story and style
- `POST /api/v1/generate-song` - Generate audio songs from lyrics and style
- `GET /api/v1/check-progress` - Check song generation progress

### Payment APIs
- `POST /api/v1/stripe/checkout` - Create Stripe checkout session for song purchase
- `GET /api/v1/stripe/status` - Check purchase status for a specific song

## Tech Stack

- **Frontend**: Next.js 15, React 19, TypeScript
- **Styling**: Tailwind CSS
- **UI Components**: Radix UI, Lucide Icons
- **Package Manager**: pnpm
- **Payment Processing**: Stripe API
- **State Management**: Cookie-based purchase tracking

## Getting Started

1. **Install dependencies**
   ```bash
   pnpm install
   ```

2. **Configure environment variables**
   ```bash
   cp env.example .env.local
   ```
   
   Add your API keys:
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   TOPMEDIA_API_KEY=your_topmedia_api_key
   STRIPE_SECRET_KEY=your_stripe_secret_key
   NEXT_PUBLIC_APP_URL=http://localhost:3000
   ```

3. **Run development server**
   ```bash
   pnpm dev
   ```

4. **Build for production**
   ```bash
   pnpm build
   ```

5. **Start production server**
   ```bash
   pnpm start
   ```

## Payment Integration

Story Chord includes a complete Stripe payment system:

- **Secure Checkout**: Stripe-hosted checkout pages for secure payment processing
- **Purchase Tracking**: Cookie-based system to track purchased songs
- **Status Verification**: Real-time purchase status checking
- **Success Handling**: Automatic redirects and purchase confirmation

### Payment Flow
1. User generates a song using the AI APIs
2. User initiates purchase via checkout endpoint
3. Stripe handles payment processing securely
4. **Direct redirect** to song page with automatic purchase verification
5. Purchase status is tracked and stored
6. User gains access to full song features

**Note**: The payment flow has been optimized for better performance and reliability in production environments.

## Testing

### API Testing

Test all API endpoints using the provided test script:

```bash
node scripts/test-api.js
```

The test script will:
- Verify all API endpoints are working
- Test the complete song generation flow
- Display detailed responses and error information
- Ensure your development server is running on port 3000

**Note**: Make sure your development server is running (`pnpm dev`) before executing the test script.

### Payment Testing

For payment testing, use Stripe's test mode:
- Test card numbers: 4242 4242 4242 4242 (Visa)
- Test mode automatically enabled in development
- No real charges will be processed

## License

Private project - All rights reserved.
