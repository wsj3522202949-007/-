---
id: tool-05645
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: slop-edge
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/iyop666/slop-edge
created: 2026-07-18
updated: 2026-07-18
no: 5645
category: 一、去 AI 味 / Humanizer 库
repo: iyop666/slop-edge
stars: 1
url: https://github.com/iyop666/slop-edge
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# iyop666/slop-edge

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/iyop666/slop-edge
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI Content Authenticity Detector — 10-dimension scoring system with Indonesian language support. Detects AI writing patterns, structural tells, and casual authenticity issues.
- **本地描述**：AI Content Authenticity Detector — 10-dimension scoring system with Indonesian language support. Detects AI writing patterns, structural tells, and casual authenticity issues.
- **拉取时间**：2026-07-25 18:26:24

---

# Slop Edge 🎯

**Your competitors use AI too. Make sure yours doesn't sound like it.**

Slop Edge is an AI content detection tool that scores text across 10 dimensions to identify AI-generated writing patterns. It's designed for content creators, bloggers, and developers who want to maintain authentic, human-sounding content.

## 🚀 Live Demo

**https://slop-edge.vercel.app**

## ✨ Features

- **10-Dimension Scoring System** — Vocabulary, Banned Phrases, Structure, Rhythm, Voice, Density, Formatting, Readability, Originality, Specificity
- **Indonesian Language Support** — Full detection for Indonesian AI patterns (ChatGPT, Gemini, Claude)
- **Casual Authenticity Detection** — Detects AI "trying too hard to be casual" in informal Indonesian text
- **Model Fingerprints** — Identifies GPT/Claude/Gemini specific patterns
- **Real-time Analysis** — Instant feedback with detailed issue breakdown
- **Dark Mode UI** — Clean, modern interface built with Next.js + Tailwind

## 🎯 Use Cases

- **Content Creators** — Ensure your blog posts, articles, and social media content sound human
- **Developers** — Check AI-generated documentation and README files
- **Educators** — Detect AI-written student submissions
- **Journalists** — Verify authenticity of submitted articles
- **Indonesian Content** — Specialized detection for Indonesian AI writing patterns

## 🛠️ Tech Stack

- **Frontend**: Next.js 16, React 19, Tailwind CSS
- **Backend**: TypeScript, Node.js
- **Deployment**: Vercel (serverless)
- **Detection Engine**: Custom regex-based pattern matching with tiered severity scoring

## 📊 Scoring System

Each dimension scores 0-10 points:

| Dimension | What It Detects |
|-----------|----------------|
| **Vocabulary** | AI overused words (delve, tapestry, pivotal, etc.) |
| **Banned Phrases** | Throat-clearing, sycophancy, rhetorical patterns |
| **Structure** | Negative parallelism, tricolons, dramatic countdowns |
| **Rhythm** | Sentence uniformity, burstiness, em dash overuse |
| **Voice** | Sycophancy, hedging, performative openers |
| **Density** | Passive voice, filler words, buzzword stacking |
| **Formatting** | Bold-first bullets, formulaic structure |
| **Readability** | Wall-of-text, single-sentence paragraphs |
| **Originality** | Overused metaphors, template patterns |
| **Specificity** | Vague quantifiers, generic examples |

## 🇮🇩 Indonesian Language Features

- **Tier 1-3 AI Words** — Formal/bureaucratic words AI overuses in Indonesian
- **Banned Phrases** — ChatGPT-style openers and closers in Indonesian
- **Structural Patterns** — "Bukan X, melainkan Y", "Tidak hanya X, tetapi juga Y"
- **Casual Authenticity** — Detects register mismatch (formal/scientific mixed with slang)
- **Sambil Chains** — Detects AI stacking simultaneous actions

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/iyop666/slop-edge.git
cd slop-edge

# Install
npm install

# Run
npm run dev

# Build
npm run build
```

## 📈 API Usage

```typescript
import { analyzeText } from '@/lib/scorer';

const result = analyzeText("Your text here...");
console.log(result.total); // Score out of 100
console.log(result.scores); // Per-dimension scores
console.log(result.tier1Hits); // AI word matches
```

## 🌟 Why Slop Edge?

Unlike generic AI detectors that just look for "AI words", Slop Edge uses:

1. **Multi-language pattern matching** — English + Indonesian
2. **Structural analysis** — Detects AI writing patterns, not just vocabulary
3. **Rhythm analysis** — Checks sentence variation and burstiness
4. **Casual authenticity** — Detects when AI tries too hard to sound human
5. **Model fingerprints** — Identifies specific AI model patterns

## 📝 License

MIT License - feel free to use, modify, and distribute.

## 🤝 Contributing

Contributions welcome! Please read the contributing guide first.

## 📧 Contact

Built by [@iyop666](https://github.com/iyop666) — Indonesian developer building AI tools for content authenticity.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

**Live**: https://slop-edge.vercel.app  
**GitHub**: https://github.com/iyop666/slop-edge
