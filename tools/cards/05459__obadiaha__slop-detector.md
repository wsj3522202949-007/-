---
id: tool-05459
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: slop-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/obadiaha/slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5459
category: 一、去 AI 味 / Humanizer 库
repo: obadiaha/slop-detector
stars: 0
url: https://github.com/obadiaha/slop-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# obadiaha/slop-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/obadiaha/slop-detector
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：🔍 Is your website AI slop? Scan any URL for AI-generated design patterns, copy clichés, and template fatigue. Free tool at godigitalapps.com/tools/slop-detector
- **本地描述**：🔍 Is your website AI slop? Scan any URL for AI-generated design patterns, copy clichés, and template fatigue. Free tool at godigitalapps.com/tools/slop-detector
- **拉取时间**：2026-07-25 18:19:29

---

# 🔍 Slop Detector

**Is your website AI slop?** Paste any URL and get a 0–100 score analyzing AI-generated design patterns, copy clichés, and template fatigue.

**[Try it free →](https://godigitalapps.com/tools/slop-detector)**

## What It Detects

### DOM & CSS Analysis
- Tailwind default class detection (indigo-500 energy)
- ShadCN/UI component fingerprinting
- Cookie-cutter layout patterns (Hero → Features → Pricing → Testimonials → FAQ → CTA)
- 3-column grid detection
- Gradient cliché spotting

### Copy Analysis
- AI phrase detection ("revolutionize your workflow", "seamless integration")
- Em-dash density scoring (AI uses 3-5x more em-dashes than humans)
- Filler metric detection (unverifiable "10,000+ users" claims)
- Fake testimonial name spotting (Sarah Chen, Alex Rodriguez)
- Buzzword density analysis

### Typography
- Default AI font detection (Inter, system-ui, Roboto)
- Single-font-family detection
- Font pairing analysis

### Visual Design
- Generic gradient backgrounds
- Indigo/purple color scheme detection
- Card hover-lift patterns
- Missing favicon detection

## The Slop Scale

| Score | Label | Meaning |
|-------|-------|---------|
| 0–20 | 🏆 Artisanally Crafted | Hand-crafted with taste and intention |
| 21–40 | 👀 Suspiciously Human | Mostly original, minor template vibes |
| 41–60 | 🤷 Template-Curious | Default patterns showing through |
| 61–80 | 🤖 Peak AI Energy | Clearly AI-assisted, little customization |
| 81–100 | 💀 ChatGPT Sneezed On This | Maximum slop detected |

## Tech Stack

- **Next.js 14** — React framework
- **Tailwind CSS** — Styling
- **Server-side HTML parsing** — No Playwright needed, Vercel-compatible
- **Heuristic analysis engine** — Pattern matching across 100+ AI-slop signals

## Run Locally

```bash
git clone https://github.com/obadiaha/slop-detector.git
cd slop-detector
pnpm install
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000).

## How It Works

1. **Fetch** — Server-side HTTP fetch of the target URL's HTML
2. **Parse** — Extract CSS classes, text content, fonts, sections, and meta tags via regex parsing
3. **Analyze** — Run 5 analysis layers: Layout, Visual Design, Copy, Typography, Interactivity
4. **Score** — Weighted scoring across all categories produces a 0–100 slop score
5. **Report** — Detailed findings with severity levels and specific fix recommendations

## API

```bash
curl -X POST https://godigitalapps.com/api/scan \
  -H "Content-Type: application/json" \
  -d '{"url": "example.com"}'
```

Returns a JSON object with the scan ID and full analysis result.

## Contributing

Found a new AI-slop pattern? PRs welcome. Add detection rules to:
- `lib/slop-detector/analyzer/dom-css.ts` — DOM/CSS patterns
- `lib/slop-detector/analyzer/copy.ts` — Copy/text patterns

## License

MIT

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

Built by [Go Digital Apps](https://godigitalapps.com) — tools for builders who ship.
