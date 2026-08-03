---
id: tool-04896
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: AI-Content-Detector-Extension
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/learntocodefree/ai-content-detector-extension
created: 2026-07-18
updated: 2026-07-18
no: 4896
category: 一、去 AI 味 / Humanizer 库
repo: learntocodefree/AI-Content-Detector-Extension
stars: 0
url: https://github.com/learntocodefree/ai-content-detector-extension
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# learntocodefree/AI-Content-Detector-Extension

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/learntocodefree/ai-content-detector-extension
- **Stars**：0
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A free and open-source browser extension that detects AI-generated content on web pages, helping users quickly identify AI-written text while browsing. Built for transparency, privacy, and the LearnToCodeFree open-source ecosystem.
- **本地描述**：A free and open-source browser extension that detects AI-generated content on web pages, helping users quickly identify AI-written text while browsing. Built for transparency, privacy, and the LearnToCodeFree open-source ecosystem.
- **拉取时间**：2026-07-25 17:58:29

---

# AI Content Detector Extension

A lightweight, open-source browser extension that helps identify AI-generated content across the web.

Whether you're reading blogs, news articles, documentation, or social media posts, the extension analyzes the visible text, images, and metadata to provide an estimated AI-generated probability directly in your browser.

> **Part of the LearnToCodeFree Open Source ecosystem.**

---

## Features

* **Text Analysis** - Detect AI-generated text using phrase detection, vocabulary richness, sentence uniformity, entropy analysis, and filler word detection
* **AI Model Detection** - Identify likely AI models: ChatGPT, Claude, Gemini, GPT-4, Llama, Midjourney, DALL-E, Stable Diffusion
* **Image Analysis** - Scan images for AI-generated content using URL patterns, alt text analysis, and spectral analysis
* **Metadata Detection** - Check page metadata for AI generator tags and mentions
* **Score Breakdown** - Visual breakdown of Text, Image, and Metadata scores with weighted overall score
* **Full Dashboard** - Detailed analysis with tabs for Overview, Text Analysis, Images, Paragraphs, and History
* **Paragraph-by-Paragraph Analysis** - See which specific paragraphs are likely AI-generated
* **Dark Mode** - Toggle between light and dark themes
* **Scan History** - Track previous scans with score distribution chart
* **Badge Score** - Extension icon badge shows AI score for current page
* **Auto-Scan** - Automatically analyzes pages on load and updates badge
* **Privacy-first** - No tracking, no ads, no unnecessary data collection
* **Free and Open Source** - MIT licensed, easy to modify and extend

---

## Why?

As AI-generated content becomes increasingly common, it can be difficult to distinguish between human-written and AI-assisted writing.

This extension provides an additional signal to help users evaluate online content. It is designed for:

* Students
* Researchers
* Journalists
* Content creators
* Recruiters
* Developers
* Anyone curious about AI-generated text

> **Note:** AI detection is probabilistic, not definitive. No AI detector can guarantee 100% accuracy.

---

## Supported Browsers

* Google Chrome
* Microsoft Edge
* Brave
* Opera
* Any Chromium-based browser

(Firefox support may be added in the future.)

---

## Installation

### From Source

```bash
git clone https://github.com/learntocodefree/ai-content-detector-extension.git
```

Then:

1. Open your browser.
2. Navigate to the Extensions page.
3. Enable **Developer Mode**.
4. Select **Load unpacked**.
5. Choose the project folder.

---

## Project Structure

```text
.
├── manifest.json        # Extension manifest (Manifest V3)
├── popup.html           # Extension popup UI
├── popup.js             # Popup logic and scan display
├── content.js           # Content script for page analysis
├── background.js        # Service worker for history and settings
├── dashboard.html       # Full dashboard page
├── dashboard.js         # Dashboard rendering and history
├── gen-icons.cjs        # Icon generator script
├── icons/               # Extension icons (16px, 48px, 128px)
├── LICENSE
└── README.md
```

---

## How It Works

### Text Analysis
The extension analyzes page text using 7 detection methods:
1. **AI Phrase Detection** - Matches against 70+ known AI phrases and patterns
2. **Model Signatures** - Identifies specific AI model fingerprints
3. **Vocabulary Richness** - Measures word diversity (lower = more AI-like)
4. **Sentence Burstiness** - Analyzes sentence length uniformity
5. **Filler Word Detection** - Counts transition words and phrases
6. **Entropy Analysis** - Measures text predictability
7. **Repetition Patterns** - Detects unusual word repetition

### Image Analysis
Scans all page images for:
- URL patterns from AI generators (Midjourney, DALL-E, Stable Diffusion, etc.)
- AI mentions in alt text or title attributes
- Stock photo sources
- Canvas-based spectral analysis for visual patterns

### Score Calculation
The overall score combines three components:
- **Text Score** (50-70% weight)
- **Image Score** (0-30% weight)
- **Metadata Score** (20-30% weight)

---

## Contributing

Contributions are always welcome.

You can help by:

* Improving detection accuracy
* Fixing bugs
* Improving UI/UX
* Optimizing performance
* Supporting additional browsers
* Improving documentation

Please open an issue before submitting major changes.

---

## Roadmap

* Firefox support
* Safari support
* Custom API integration
* Multiple detection providers
* Offline inference
* Batch analysis
* Export results to CSV/JSON
* Custom phrase lists

---

## Privacy

Your privacy matters.

This extension is designed with privacy in mind.

* No tracking
* No advertisements
* No unnecessary permissions
* No hidden analytics
* Open source for complete transparency

All analysis is performed locally in your browser. No data is sent to external servers.

---

## Disclaimer

AI content detection is an estimation, not proof of authorship.

Results should be treated as guidance rather than factual evidence.

Always use your own judgment before making academic, professional, or legal decisions based on detection results.

---

## License

This project is licensed under the MIT License.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## LearnToCodeFree

This project is maintained as part of the **LearnToCodeFree** open-source initiative.

Our goal is to build high-quality, free, developer-friendly tools that anyone can use, learn from, and contribute to.

If you find this project useful, consider:

* Starring the repository
* Forking it
* Reporting issues
* Suggesting new features
* Contributing code

Together, we can build better open-source tools for everyone.
