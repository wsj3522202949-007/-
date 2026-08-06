---
id: tool-05441
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ai-content-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/ckorhonen/ai-content-detector
created: 2026-07-18
updated: 2026-07-18
no: 5441
category: 一、去 AI 味 / Humanizer 库
repo: ckorhonen/ai-content-detector
stars: 0
url: https://github.com/ckorhonen/ai-content-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# ckorhonen/ai-content-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ckorhonen/ai-content-detector
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered tool to detect AI-generated content (slop) across images, text, and video
- **本地描述**：AI-powered tool to detect AI-generated content (slop) across images, text, and video
- **拉取时间**：2026-07-25 18:18:46

---

# AI Content Detector

[![CI Pipeline](https://github.com/ckorhonen/ai-content-detector/actions/workflows/ci.yml/badge.svg)](https://github.com/ckorhonen/ai-content-detector/actions/workflows/ci.yml)
[![Deploy](https://github.com/ckorhonen/ai-content-detector/actions/workflows/deploy.yml/badge.svg)](https://github.com/ckorhonen/ai-content-detector/actions/workflows/deploy.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

🤖 AI-powered tool to detect AI-generated content across images and text. Built with React, TypeScript, Hono, and Cloudflare Workers AI.

## ✨ Features

- **📝 Text Analysis**: Detect AI-generated text using advanced language models
- **🖼️ Image Analysis**: Identify AI-generated images and digital art
- **⚡ Real-time Detection**: Fast analysis powered by Cloudflare Workers AI
- **🎯 Confidence Scores**: Get detailed confidence ratings for each analysis
- **🔒 Rate Limiting**: Built-in protection (10 requests per minute per IP)
- **🌐 Edge Computing**: Global deployment with Cloudflare Workers
- **💅 Modern UI**: Beautiful, responsive interface with Tailwind CSS

## 🚀 Quick Start

### Prerequisites

- Node.js 20.x or later
- npm or yarn
- Cloudflare account with Workers AI enabled

### Installation

```bash
# Clone the repository
git clone https://github.com/ckorhonen/ai-content-detector.git
cd ai-content-detector

# Install dependencies
npm install

# Start development server
npm run dev
```

The app will be available at `http://localhost:8787`

## 🔧 Configuration

### Cloudflare Workers Setup

1. **Create a Cloudflare account** at [cloudflare.com](https://cloudflare.com)

2. **Enable Workers AI**:
   - Go to Workers & Pages → AI
   - Enable Workers AI for your account

3. **Create KV Namespace for rate limiting**:
```bash
# Create production KV namespace
wrangler kv:namespace create "RATE_LIMITER"

# Create preview KV namespace for development
wrangler kv:namespace create "RATE_LIMITER" --preview
```

4. **Update wrangler.toml** with your KV namespace IDs:
```toml
[[kv_namespaces]]
binding = "RATE_LIMITER"
id = "your-production-kv-id"
preview_id = "your-preview-kv-id"
```

5. **Deploy to Cloudflare Workers**:
```bash
npm run deploy
```

## 📡 API Documentation

### Base URL
- **Production**: `https://your-worker.workers.dev`
- **Development**: `http://localhost:8787`

### Endpoints

#### POST /api/detect-text

Analyze text content for AI generation.

**Request:**
```json
{
  "text": "Your text content to analyze..."
}
```

**Response:**
```json
{
  "success": true,
  "isAiGenerated": false,
  "confidence": 0.65,
  "reasoning": "Analysis explanation...",
  "type": "text",
  "model": "@cf/meta/llama-2-7b-chat-int8"
}
```

**Validation:**
- Text must be 10-10,000 characters
- Content-Type: application/json

#### POST /api/detect-image

Analyze image content for AI generation.

**Request:**
- Content-Type: multipart/form-data
- Form field: `image` (file upload)

**Response:**
```json
{
  "success": true,
  "isAiGenerated": true,
  "confidence": 0.82,
  "reasoning": "Image shows characteristics of AI-generated content",
  "type": "image",
  "model": "@cf/microsoft/resnet-50",
  "classifications": [
    { "label": "digital art", "score": 0.89 },
    { "label": "computer graphics", "score": 0.76 }
  ]
}
```

**Validation:**
- Maximum file size: 5MB
- Accepted formats: JPEG, PNG, GIF, WebP

#### GET /api/health

Health check endpoint.

**Response:**
```json
{
  "status": "ok",
  "timestamp": "2025-10-17T03:00:00.000Z",
  "version": "1.0.0"
}
```

### Rate Limiting

- **Limit**: 10 requests per minute per IP address
- **Response on limit exceeded** (429):
```json
{
  "error": "Rate limit exceeded. Please try again later.",
  "resetAt": "2025-10-17T03:01:00.000Z"
}
```

## 🛠️ Development

### Available Scripts

| Script | Description |
|--------|-------------|
| `npm run dev` | Start development server |
| `npm run build` | Build for production |
| `npm run deploy` | Deploy to Cloudflare Workers |
| `npm run typecheck` | Run TypeScript type checking |
| `npm run lint` | Run ESLint |
| `npm run lint:fix` | Fix ESLint issues |
| `npm run format` | Format code with Prettier |
| `npm test` | Run unit tests |
| `npm run test:coverage` | Run tests with coverage |

### Environment Variables

No environment variables needed! The app uses Cloudflare Workers AI bindings:
- **AI**: Cloudflare Workers AI binding (configured in wrangler.toml)
- **RATE_LIMITER**: KV namespace for rate limiting (configured in wrangler.toml)

### Project Structure

```
ai-content-detector/
├── src/
│   ├── index.tsx       # Hono API server & routes
│   ├── App.tsx         # React frontend component
│   └── main.tsx        # React entry point
├── wrangler.toml       # Cloudflare Workers config
├── package.json        # Dependencies & scripts
└── tsconfig.json       # TypeScript configuration
```

## 🏗️ Architecture

```
┌─────────────────┐
│   User Browser  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   React UI      │ (Tailwind CSS)
│   (src/App.tsx) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Hono API      │ (Rate Limiting)
│ (src/index.tsx) │
└────────┬────────┘
         │
         ├─────────────────┬─────────────────┐
         ▼                 ▼                 ▼
┌────────────────┐  ┌──────────────┐  ┌──────────────┐
│ Cloudflare AI  │  │  KV Storage  │  │   Bindings   │
│ (Llama-2 &     │  │ (Rate Limit) │  │              │
│  ResNet-50)    │  │              │  │              │
└────────────────┘  └──────────────┘  └──────────────┘
```

### Tech Stack

- **Frontend**: React 18, TypeScript, Tailwind CSS
- **Backend**: Hono (lightweight HTTP framework)
- **Runtime**: Cloudflare Workers (V8 isolates)
- **AI Models**: 
  - Text: `@cf/meta/llama-2-7b-chat-int8`
  - Image: `@cf/microsoft/resnet-50`
- **Storage**: Cloudflare KV (rate limiting)
- **Build**: Vite, TypeScript

## 🚀 Deployment

### Automatic Deployment (Recommended)

The app automatically deploys on every push to `main` branch via GitHub Actions.

**Setup:**
1. Add GitHub secrets:
   - `CLOUDFLARE_API_TOKEN`
   - `CLOUDFLARE_ACCOUNT_ID`

2. Push to main branch
3. Check deployment status in Actions tab

### Manual Deployment

```bash
# Deploy to production
npm run deploy

# Deploy to preview
wrangler deploy --env preview
```

### Production URL

After deployment, your app will be available at:
- `https://ai-content-detector.{your-subdomain}.workers.dev`

## 🧪 Testing

```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Generate coverage report
npm run test:coverage
```

### Testing the API

**Test text detection:**
```bash
curl -X POST https://your-worker.workers.dev/api/detect-text \
  -H "Content-Type: application/json" \
  -d '{"text":"Your test content here..."}'
```

**Test image detection:**
```bash
curl -X POST https://your-worker.workers.dev/api/detect-image \
  -F "image=@/path/to/image.jpg"
```

**Test rate limiting:**
```bash
# Send 11 requests quickly to trigger rate limit
for i in {1..11}; do
  curl -X POST https://your-worker.workers.dev/api/detect-text \
    -H "Content-Type: application/json" \
    -d '{"text":"Test content for rate limiting"}' &
done
```

## 🎯 Use Cases

- **Content Moderation**: Detect AI-generated spam and fake content
- **Academic Integrity**: Identify AI-written essays and assignments
- **Social Media**: Flag potential AI-generated posts and images
- **Journalism**: Verify authenticity of images and text
- **Digital Forensics**: Analyze content for AI generation patterns

## 🔒 Security Features

- **Rate Limiting**: Prevents abuse with IP-based throttling
- **Input Validation**: Strict validation on all inputs
- **File Size Limits**: Maximum 5MB for image uploads
- **Error Handling**: Secure error messages without leaking internals
- **CORS**: Configurable cross-origin policies

## 📊 Performance

- **Cold Start**: < 50ms (Cloudflare Workers)
- **Text Analysis**: ~500-1000ms
- **Image Analysis**: ~1000-2000ms
- **Global Latency**: < 100ms (edge deployment)

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](https://github.com/ckorhonen/ai-content-detector/blob/main/CONTRIBUTING.md) for details.

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting (`npm test && npm run lint`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ckorhonen/ai-content-detector/blob/main/LICENSE) file for details.

## 👤 Author

**Chris Korhonen**
- GitHub: [@ckorhonen](https://github.com/ckorhonen)
- Email: ckorhonen@gmail.com

## 🙏 Acknowledgments

- [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/) - AI inference at the edge
- [Hono](https://hono.dev/) - Lightweight web framework
- [React](https://react.dev/) - UI library
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS

## 📚 Resources

- [Cloudflare Workers Documentation](https://developers.cloudflare.com/workers/)
- [Workers AI Models](https://developers.cloudflare.com/workers-ai/models/)
- [Hono Documentation](https://hono.dev/)
- [Project Issues](https://github.com/ckorhonen/ai-content-detector/issues)

## 🔗 Links

- [Live Demo](https://ai-content-detector.workers.dev)
- [Documentation](https://github.com/ckorhonen/ai-content-detector/blob/main/docs/)
- [API Reference](#-api-documentation)
- [Contributing Guide](https://github.com/ckorhonen/ai-content-detector/blob/main/CONTRIBUTING.md)

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

**Made with ❤️ using Cloudflare Workers AI**

*Keywords: AI detection, content moderation, machine learning, Cloudflare Workers, image analysis, text analysis, deep learning*
