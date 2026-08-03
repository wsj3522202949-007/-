---
id: tool-01200
type: tool
area: 库
status: active
tags: [HTML, 协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: ZeroOffice
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/darkenamber/zerooffice
created: 2026-07-18
updated: 2026-07-18
no: 1200
category: 二、网文 / 长篇 AI 写作系统 库
repo: DarkenAmber/ZeroOffice
stars: 8
url: https://github.com/darkenamber/zerooffice
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# DarkenAmber/ZeroOffice

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/darkenamber/zerooffice
- **Stars**：8
- **语言**：HTML
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：ZeroOffice — Free office tools that run in your browser. PDF merger, image editor, AI writing assistant and more. No account, no file uploads, no ads.
- **本地描述**：ZeroOffice — Free office tools that run in your browser. PDF merger, image editor, AI writing assistant and more. No account, no file uploads, no ads.
- **拉取时间**：2026-07-23 23:14:04

---

# 🗂️ ZeroOffice
### Work with Documents. One File. No Installation.
### by DarkenAmber

> Everything you need to work with documents. PDF tools, image editor, AI writing assistant. No account, no uploads, no tracking, no installation. Open and use.

**Live:** [darkenamber.github.io/ZeroOffice](https://darkenamber.github.io/ZeroOffice/)

---

## What is ZeroOffice?

ZeroOffice is a single HTML file. Open it in any browser — no installation, no backend, no server, no account. Everything runs locally on your device.

One file. Zero setup. Full office toolkit.

---

## Tools

### 📄 PDF Tools
| Tool | Description |
|------|-------------|
| PDF Merger | Combine multiple PDFs into one. Drag to reorder. |
| PDF Splitter | Extract pages, split all, or split into chunks. |
| PDF Compressor | Reduce file size. Best for scanned documents. |
| PDF ↔ Images | Convert images to PDF or extract pages as PNG/JPG. |
| PDF Watermark | Add permanent text watermark to every page. |

### 🖼️ Image Tools
| Tool | Description |
|------|-------------|
| Image Compressor | Compress JPG/PNG/WEBP with quality slider. Batch support. |
| Image Resizer | Resize by pixels, percentage, or preset (HD, 4K, Instagram...). |
| Image Converter | Convert between PNG, JPG, and WEBP. |
| Image Editor | Rotate, flip, brightness, contrast, saturation, blur. |

### 📝 Text & Data
| Tool | Description |
|------|-------------|
| Word Counter | Words, characters, sentences, reading time, top words. |
| Case Converter | UPPER, lower, Title, camelCase, snake_case, kebab-case and more. |
| Text Diff | Compare two texts and highlight differences line by line. |
| CSV Tools | View CSV as table, search, sort. Convert CSV ↔ JSON. |
| Chart Builder | CSV → Bar, Line, Pie, Doughnut charts. Export PNG/SVG/Excel/HTML. |

### 🛠️ Utilities
| Tool | Description |
|------|-------------|
| Meeting Cost | Live cost counter for meetings. |
| Security & Privacy | Full transparency about data practices. |

### 🔄 Converters
| Tool | Description |
|------|-------------|
| Currency | Live exchange rates. Cached 1 hour. No API key needed. |
| Unit Converter | Length, weight, temperature, area, volume, speed, data. |

### ✨ AI Tools — Claude API key? Unlock superpowers.
| Tool | Description |
|------|-------------|
| Excel Formula Generator | Describe what you need → get the formula. Excel & Google Sheets. |
| Invoice Generator | Fill in details → AI generates a professional invoice. |
| OCR + AI Cleanup | Upload a photo → get clean, structured text. |
| Email Rewriter | Rewrite, improve, shorten, fix grammar. Choose tone and language. |
| Document Summarizer | Paste any document → key points, TL;DR, or action items. |
| Contract Analyzer | Plain-language explanation of contracts with risk highlights. |
| Letter Writer | Describe what you need → AI writes a professional business letter. |

---

## Privacy

- **Your files never leave your device** — all processing is local in your browser
- No account, no registration, no email required
- No ads, no data selling
- AI tools send data directly to Anthropic API — ZeroOffice is not in the middle
- No analytics, no tracking scripts, no data collection of any kind

---

## AI Tools Setup

AI tools use the [Claude API](https://www.anthropic.com) by Anthropic.

1. Create an account at [console.anthropic.com](https://console.anthropic.com)
2. New accounts receive **~$5 in free credits** — no credit card required
3. Go to API Keys → create a key
4. In ZeroOffice open **AI Setup** and paste your key
5. Key is stored only in your browser's localStorage — we never see it

---

## Architecture

```
zerooffice/
└── index.html    ← the entire product (~480KB, single file)
```

- No build step, no npm, no Docker
- No backend, no server, no database
- 3 themes: Dark (default), Light, Retro 8-bit
- EN/RU bilingual interface
- Works offline (except Currency Converter and AI tools)

### Libraries (CDN, loaded on demand)
- [pdf-lib](https://pdf-lib.js.org/) — PDF manipulation
- [PDF.js](https://mozilla.github.io/pdf.js/) — PDF rendering
- [JSZip](https://stuk.github.io/jszip/) — ZIP creation
- [Chart.js](https://www.chartjs.org/) — Charts
- [ExcelJS](https://github.com/exceljs/exceljs) — Excel export

---

## Part of DarkenAmber Ecosystem

| Product | Description | Link |
|---------|-------------|------|
| 🛠️ IT Tools | Developer and IT utilities | [darkenamber.github.io/DarkenAmber-it-tools](https://darkenamber.github.io/DarkenAmber-it-tools/) |
| 🗂️ ZeroOffice | Document tools for everyone | This repo |
| 📱 Social Tools | AI social media content creation | Coming soon |

---

## Support

If ZeroOffice saves you time:

[![Ko-fi](https://img.shields.io/badge/Ko--fi-Buy%20me%20a%20coffee-FF5E5B?style=flat&logo=ko-fi)](https://ko-fi.com/darkenamber)
[![Patreon](https://img.shields.io/badge/Patreon-Support%20%243%2Fmonth-FF424D?style=flat&logo=patreon)](https://www.patreon.com/cw/DarkenAmber)

---

## License

MIT — see [LICENSE](LICENSE)

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

*Built with ❤️ by [DarkenAmber](https://github.com/DarkenAmber)*
