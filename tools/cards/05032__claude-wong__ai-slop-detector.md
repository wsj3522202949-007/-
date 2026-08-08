---
id: tool-05032
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 去AI味]
title: ai-slop-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/claude-wong/ai-slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5032
category: 一、去 AI 味 / Humanizer 库
repo: claude-wong/ai-slop-detector
stars: 0
url: https://github.com/claude-wong/ai-slop-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: d1f668d2e66862a7
  - methods/改稿润色指令库.md
---

# claude-wong/ai-slop-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/claude-wong/ai-slop-detector
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Chrome extension that detects AI-generated content in GitHub repositories and gists
- **本地描述**：Chrome extension that detects AI-generated content in GitHub repositories and gists
- **拉取时间**：2026-07-25 18:03:36

---

# AI Slop Detector

Chrome extension that detects AI-generated content in GitHub repositories and gists. Designed to quickly evaluate whether a PoC is worth investigating or is just AI slop.

## How It Works

The extension runs automatically when you visit a GitHub repo or gist page. It analyzes the content and author, then displays a floating score badge in the bottom-right corner.

### Scoring (0-100%)

Three signal categories are combined into a weighted score:

- **Content Analysis (60%)** - Local heuristic pattern matching:
  - AI boilerplate phrases ("certainly!", "I'll help you", ChatGPT artifacts)
  - Prompt remnants left in comments
  - Comment-to-code ratio and redundant commenting patterns
  - README analysis: emoji density, buzzwords, generic features, over-structured layout
  - Code structure: placeholder values, over-engineered file trees, config file overload
  - Hallucination detection: commonly hallucinated npm packages, wrong API endpoints

- **Author Reputation (30%)** - GitHub profile analysis:
  - Account age
  - Repo quality and star counts
  - Contribution activity
  - Fork ratio (original vs forked repos)
  - Profile completeness
  - Follower ratio
  - Commit history depth (single-commit repos = red flag)

- **AI Analysis (10%, optional)** - Send code to an LLM for deeper analysis:
  - Ollama (local, free)
  - Claude (Anthropic)
  - OpenAI

### Classifications

| Score | Label | Color |
|-------|-------|----related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| 0-25% | Likely Legit | Green |
| 26-50% | Mixed Signals | Yellow |
| 51-75% | Suspicious | Orange |
| 76-100% | AI Slop | Red |

## Install

```bash
git clone https://github.com/YOUR_USERNAME/ai-slop-detector.git
cd ai-slop-detector
npm install
npm run build
```

Then load in Chrome:
1. Go to `chrome://extensions/`
2. Enable **Developer mode**
3. Click **Load unpacked** and select the `dist/` folder

## Configuration

Click the extension icon > **Settings** to configure:

- **GitHub PAT** - Personal access token for higher API rate limits (5000/hr vs 60/hr). No special scopes needed for public repos.
- **AI Provider** - Optional LLM analysis:
  - **Ollama** - Runs locally, no API key needed. Set the URL (default `http://localhost:11434`) and model name (default `llama3.2`).
  - **Claude** or **OpenAI** - Requires an API key. Costs apply per analysis.
- **Scoring Weights** - Adjust how much each category contributes.
- **Cache TTL** - How long to cache results (default 24 hours).

## Build

```bash
npm run build    # Type-check + build to dist/
```

The build uses esbuild for the content script (IIFE, single file to avoid CSP issues on GitHub) and the service worker, plus Vite for the popup and options HTML pages.

## Project Structure

```
src/
├── analysis/           # Scoring engine
│   ├── contentAnalyzer.ts
│   ├── authorAnalyzer.ts
│   ├── aiAnalyzer.ts
│   ├── scorer.ts
│   └── patterns/       # Heuristic pattern matchers
├── background/         # Service worker
│   ├── analysisOrchestrator.ts
│   ├── cache.ts
│   └── api/            # GitHub API, scraper, AI API clients
├── content/            # Content script (page detection + DOM extraction)
├── content-ui/         # React modal overlay (Shadow DOM)
├── options/            # Settings page
├── popup/              # Extension popup
└── shared/             # Types, constants, utilities
```

## License

MIT
