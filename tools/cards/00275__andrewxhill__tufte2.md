---
id: tool-00275
type: tool
area: 库
status: active
tags: [CSS, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: tufte2
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/andrewxhill/tufte2
created: 2026-07-18
updated: 2026-07-18
no: 275
category: 二、网文 / 长篇 AI 写作系统 库
repo: andrewxhill/tufte2
stars: 1
url: https://github.com/andrewxhill/tufte2
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# andrewxhill/tufte2

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/andrewxhill/tufte2
- **Stars**：1
- **语言**：CSS
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：A Tufte-inspired CSS library for vibe coders building calm, legible interfaces for writing, charts, dashboards, and analytical websites.
- **本地描述**：A Tufte-inspired CSS library for vibe coders building calm, legible interfaces for writing, charts, dashboards, and analytical websites.
- **拉取时间**：2026-07-23 22:47:06

---

# Graphics Press CSS

A typographic and data-visualization CSS library derived from the books of Edward Tufte, the cartographic color principles of Eduard Imhof, and the typographic standards of Robert Bringhurst.

**[Live Demo & Documentation](https://andrewxhill.github.io/tufte2)**

## Features

- **ET Book typeface** -- Tufte's open-source Bembo digitisation
- **Sidenotes & margin notes** -- CSS-only, no JavaScript required
- **Data visualization components** -- dot charts, dumbbell charts, sparklines, bullet graphs, heat tables, slopegraphs, parallel coordinates, and more
- **Narrative map framing** -- reusable slippy-map container, inset legend panel, and map annotation chrome for MapLibre/Leaflet examples
- **Analytical briefing blocks** -- strategy headers, metric strips, tab rows, analytic cards, app-shell primitives, reusable research rows, and editorial spread layouts for research apps
- **Analytics application guidance** -- treemap framing, ranked-bar patterns, workspace shells, and table/chart rules informed by real dashboard integration work
- **Chart interop tokens** -- semantic chart colors and axis/grid variables for D3, Recharts, ECharts, and hand-rolled SVG
- **Editorial spread layouts** -- dual-column analysis blocks with deliberate chart/timeline breakout rows
- **Theme-aware by default** -- follows `prefers-color-scheme`; manual override via `.dark`, `.light`, or `[data-theme]`
- **Responsive** -- fluid typography, mobile sidenote toggles, adaptive chart layouts
- **Print styles** -- optimized for paper output
- **CSS layers** -- `@layer` for specificity-safe cascade; override without `!important`
- **oklch() colors** -- perceptually uniform categorical palette per Imhof's equal-weight principle

## Install

### CDN

```html
<link rel="stylesheet" href="https://unpkg.com/@andrewxhill/graphics-press-css@4.7.2/css/graphics-press.css">
```

### npm

```bash
npm install @andrewxhill/graphics-press-css
```

```css
@import '@andrewxhill/graphics-press-css';
```

### Tailwind CSS

```bash
npm install @andrewxhill/graphics-press-css tailwindcss
```

```js
// tailwind.config.js
module.exports = {
  plugins: [
    require('@andrewxhill/graphics-press-css/tailwind'),
  ],
}
```

## Quick Start

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://unpkg.com/@andrewxhill/graphics-press-css@4.7.2/css/graphics-press.css">
</head>
<body>
  <article>
    <h1>Your Title</h1>
    <p class="subtitle">Your subtitle here</p>
    <section>
      <h2>Section heading</h2>
      <p>Your content with a sidenote.<label for="sn-1" class="sidenote-toggle sidenote-number"></label>
        <input type="checkbox" id="sn-1" class="sidenote-toggle">
        <span class="sidenote">This appears in the margin on wide screens.</span>
      </p>
    </section>
  </article>
</body>
</html>
```

## Components

| Component | Class | Description |
|-----------|-------|----------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| Sidenotes | `.sidenote` | Numbered margin notes |
| Margin notes | `.marginnote` | Unnumbered margin content |
| Figures | `.figure-full`, `.figure-margin` | Column, full-width, or margin figures |
| Tables | booktabs default | Three-rule tables in Gill Sans |
| Sparklines | `.sparkline` | Word-sized inline charts |
| Dot chart | `.dot-chart` | Tufte's bar chart replacement |
| Dumbbell | `.dumbbell` | Before/after connected dots |
| Strip plot | `.strip-plot` | One-way scatter |
| Bullet graph | `.bullet-graphs` | Gauge replacement |
| Heat table | `.heat-table` | Color-encoded cell values |
| Ranked table | `.ranked-table` | Dotted leaders, recessive ranks |
| Small multiples | `.small-multiples` | Grid of comparable charts |
| Timeline | `.timeline` | Events and periods |
| Slopegraph | `.slopegraph-wrap` | Two-point comparison |
| Parallel coords | `.parallel-coords` | Multi-variable SVG |
| Slippy map | `.gp-map-block`, `.gp-map-frame`, `.gp-map-panel` | Narrative map embed with overlay panel and key |
| Strategy brief | `.brief-backlink`, `.brief-header`, `.metric-strip`, `.tab-nav--filled`, `.analytic-grid`, `.activity-timeline` | Analytical dashboard framing for research and trading apps |
| App UI | `.gp-app-shell`, `.gp-app-main--detail`, `.gp-app-main--detail-wide`, `.gp-workspace`, `.gp-workspace__tabs`, `.gp-workspace__header`, `.gp-workspace__toolbar`, `.gp-toolbar`, `.gp-btn`, `.gp-input`, `.gp-panel`, `.gp-kpi-grid`, `.gp-data-table`, `.gp-card-grid`, `.gp-progress`, `.gp-meter`, `.gp-rank-list`, `.gp-rank-card`, `.gp-record-list`, `.gp-chart-frame`, `.gp-spread`, `.gp-treemap`, `.gp-treemap__tooltip` | Tufte-compatible operational UI layer for analytics apps, research lists, ranked bar views, chart wrappers, editorial spreads, wide workspace shells, treemaps, tooltips, and quantitative table cells |
| Bar chart | `.bar-chart` | Minimal tick or filled bars |
| Pull stat | `.pull-stat` | Large featured numbers |
| Stat grid | `.stat-grid` | Multiple metrics under one rule |
| Evidence | `.evidence` | Image + analysis layout |

## Themes

Default behavior is automatic via system preference. Manual override is also supported:

```js
document.documentElement.dataset.theme = 'dark';  // or 'light'
// `.dark` / `.light` classes also work
```

## Font Variations

The default library voice is still serif-forward. If you want a cleaner application mode, `tufte2` also supports an `Inter + JetBrains Mono` variation driven by `next/font/google`.

```tsx
import { Inter, JetBrains_Mono } from "next/font/google";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
  display: "swap",
});

const jetbrainsMono = JetBrains_Mono({
  subsets: ["latin"],
  variable: "--font-jetbrains-mono",
  display: "swap",
});

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html
      lang="en"
      className={`${inter.variable} ${jetbrainsMono.variable} gp-font-inter`}
    >
      <body>{children}</body>
    </html>
  );
}
```

You can also switch the variation with an attribute instead of a class:

```tsx
<html
  lang="en"
  className={`${inter.variable} ${jetbrainsMono.variable}`}
  data-gp-font="inter"
>
```

That setup keeps font loading inside Next.js and avoids external font `<link>` tags entirely.

## Analytics Guidance

- Make hierarchy loud and decoration quiet. Grouping, proportion, spacing, and line weight should orient the reader before color does.
- Keep app shells wide and figures disciplined. Workspace headers can hold tabs, KPIs, and filters; the actual evidence should still read like charts, tables, and annotated figures, not rounded widgets.
- Use semantic chart tokens everywhere. Read `--gp-chart-positive`, `--gp-chart-negative`, `--gp-chart-accent-1`, `--gp-chart-axis`, `--gp-chart-grid`, and `--gp-chart-surface` from CSS and reuse them across D3, Recharts, ECharts, or SVG.
- In dense treemaps, let category blocks carry the hierarchy and keep micro-cells quiet. Strong borders on every tiny tile create shimmer.
- In tables, keep the number visible and let the visual encoding support it. `gp-meter` is for compact quantitative cells, not for hiding the value.

## License

MIT

## Release Flow

Releases are CI-driven with Changesets.

For any PR that should publish a new package version:

```bash
npx changeset
```

Choose the release type:

- `patch` for fixes and polish
- `minor` for new backwards-compatible components or tokens
- `major` for breaking changes

When changesets land on `main`:

- GitHub Actions opens or updates a release PR
- merging that PR bumps the version and creates the release commit
- CI tags the release, publishes to npm, creates the GitHub release, and republishes `gh-pages`

Do not hand-create version tags or GitHub releases for normal package publishing.
