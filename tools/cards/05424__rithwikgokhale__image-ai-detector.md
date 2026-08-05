---
id: tool-05424
type: tool
area: 库
status: active
tags: [HTML, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: image-ai-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/rithwikgokhale/image-ai-detector
created: 2026-07-18
updated: 2026-07-18
no: 5424
category: 一、去 AI 味 / Humanizer 库
repo: rithwikgokhale/image-ai-detector
stars: 2
url: https://github.com/rithwikgokhale/image-ai-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# rithwikgokhale/image-ai-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/rithwikgokhale/image-ai-detector
- **Stars**：2
- **语言**：HTML
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Click-to-scan Chrome extension for AI image + text detection. Private local mode by default, optional BYO API key boost mode.
- **本地描述**：Click-to-scan Chrome extension for AI image + text detection. Private local mode by default, optional BYO API key boost mode.
- **拉取时间**：2026-07-25 18:18:07

---

# AI Content Detector for Chrome

Click-to-scan Chrome extension that flags AI-generated **images** and **text** on any page.

- Product website (Netlify publish target): `site/index.html`
- Documentation hub: `site/docs/index.html`
- Architecture overview: `site/docs/architecture.html`

> **Status:** v1 rebuild in progress. The previous v0.1 (in `[/archive/](archive/)`) used a hash-based placeholder for "ML" — it was not a real detector. v1 is a ground-up rewrite with actual ML running locally in the browser.

## What it does (v1, in progress)

- You click the toolbar icon → press **Scan visible images** → AI/Real badges appear on every visible image with a confidence score.
- You select text → right-click → **Detect AI in selection** → highlights flag likely-AI passages with a confidence score.
- All inference runs **on your machine** by default. Nothing about the page leaves your browser unless you explicitly opt into **Boost mode** (below).

## Two tiers

| Tier | How it works | Cost | Accuracy |
|---|---|---|related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| **Local** (default) | A quantized ONNX model runs in the browser via [transformers.js](https://huggingface.co/docs/transformers.js). The model is downloaded once on first use (~50–100 MB) and cached locally forever. No data leaves your machine. | $0 | Good but not perfect. Newer image generators (Flux, SD3, Sora, GPT-Image) and newer LLMs can slip past. |
| **Boost** (opt-in) | You paste your own API key (Google Gemini, OpenAI, or Hugging Face) in Settings. The extension calls that provider directly — never any server we operate. | Whatever your provider charges. Gemini has a generous free tier. | Materially better, especially on text and on newer image generators. |

## Stack

- Chrome MV3 extension (TypeScript + React + Tailwind, built with Vite + [@crxjs/vite-plugin](https://crxjs.dev/))
- ML: [@huggingface/transformers](https://www.npmjs.com/package/@huggingface/transformers) (transformers.js v3) running ONNX Runtime Web in an MV3 offscreen document, WebGPU-accelerated where available
- Boost providers: Google Gemini 2.5 Flash, OpenAI (GPT-4o-mini / GPT-5-mini), Hugging Face Inference API
- No backend. No accounts. No telemetry by default.

For the full architecture see `[ARCHITECTURE.md](ARCHITECTURE.md)`. For the build-out plan see `[ROADMAP.md](ROADMAP.md)`.

## Install (developer mode, during build-out)

The extension is not yet published to the Chrome Web Store. To run a local build:

```bash
npm install
npm run build        # builds extension into dist/
```

Then in Chrome:
1. Visit `chrome://extensions`
2. Toggle **Developer mode**
3. Click **Load unpacked** and select `dist/`

## Privacy

- **Local mode:** image bytes and selected text are processed entirely inside the extension's offscreen document. No network calls beyond a one-time download of the model weights from Hugging Face's CDN (with a GitHub Releases mirror as fallback).
- **Boost mode:** image bytes / text are sent **directly** from your browser to the provider you configured (Google / OpenAI / HF). Their privacy policies apply.
- **Telemetry:** none, unless you explicitly opt into anonymous error reporting in Settings.

## Repository layout

```
ARCHITECTURE.md        # how v1 is built
ROADMAP.md             # what's coming, by phase
CHANGELOG.md           # release notes
CONTRIBUTING.md        # dev guide
AGENTS.md              # guidance for AI agents working on this repo
LICENSE                # MIT
assets/icons/          # extension icons (will be redesigned)
src/                   # v1 source (added in Phase 1)
archive/               # v0.1 code + docs, kept for reference
```

## License

MIT — see `[LICENSE](LICENSE)`.
