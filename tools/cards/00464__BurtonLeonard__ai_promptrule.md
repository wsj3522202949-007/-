---
id: tool-00464
type: tool
area: 库
status: active
tags: [HTML, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: ai_promptrule
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/burtonleonard/ai_promptrule
created: 2026-07-18
updated: 2026-07-18
no: 464
category: 二、网文 / 长篇 AI 写作系统 库
repo: BurtonLeonard/ai_promptrule
stars: 0
url: https://github.com/burtonleonard/ai_promptrule
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: ab2f5ebdf8f67ebd
  - methods/最强写作方法论_全球最强综合版.md
---

# BurtonLeonard/ai_promptrule

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/burtonleonard/ai_promptrule
- **Stars**：0
- **语言**：HTML
- **License**：MIT
- **Topics**：ai-humanizer, aigc, chinese-writing, frontend-demo, humanize-text, privacy-first, text-humanizer, writing-tools
- **GitHub 描述**：Privacy-first frontend demo for AI text style review and natural writing workflows
- **本地描述**：Privacy-first frontend demo for AI text style review and natural writing workflows
- **拉取时间**：2026-07-23 22:52:37

---

# AI PromptRule - AI text humanizer frontend demo for natural writing workflows

### Privacy-first open-source interface demo for AI humanizer, humanize text, text humanizer, Chinese writing tools and AI writing style review

<div align="center">

![Frontend](https://img.shields.io/badge/frontend-HTML%20%2B%20CSS%20%2B%20JavaScript-2563EB?style=for-the-badge)
![Privacy](https://img.shields.io/badge/privacy-no%20text%20upload-16A34A?style=for-the-badge)
![Backend](https://img.shields.io/badge/backend-not%20included-64748B?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-F97316?style=for-the-badge)

</div>

> A public frontend demo for AI text style review and natural writing workflows. The repository shows the interface, responsive layout, SEO structure and privacy boundary. It does **not** publish production prompts, rewrite rules, model calls, scoring logic, databases or commercial configuration.

---

## Why this repository exists

Many AI writing tools are presented as a black box. You paste text, click a button, and hope the page does something sensible.

This repository opens a narrower layer: the frontend. It shows how a small AI writing product can explain itself, keep the interaction simple, and state its limits without exposing the private implementation behind a production service.

The boundary is deliberate:

```text
PUBLIC REPOSITORY
  -> landing page
  -> responsive editor interface
  -> character counter
  -> local-only demo interaction
  -> SEO documentation

NOT INCLUDED
  -> production prompts
  -> rewrite strategies
  -> model provider calls
  -> scoring or ranking logic
  -> database and license system
  -> deployment configuration
```

For example, enter a paragraph and click **Run demo**. The page displays a fixed sample response. It does not upload your text and it does not pretend that the sample came from a hidden algorithm.

---

## What you can study

| Area | Included | Notes |
| --- | --- | --- |
| AI writing tool landing page | Yes | Hero, keywords, CTA, project scope and FAQ |
| Text editor workspace | Yes | Mode selection, text input, counter, clear button and demo result |
| Responsive design | Yes | Desktop and mobile layout |
| Privacy-first interaction | Yes | Browser-only demo with no API request |
| SEO metadata | Yes | Description, keyword coverage, Open Graph metadata and README structure |
| Production text processing | No | Intentionally private |
| Prompt engineering rules | No | Intentionally private |
| Server, database and billing | No | Intentionally private |

---

## How the public demo works

The public edition has one job: demonstrate the product interface without leaking the product engine.

```text
User enters text
      |
      v
Browser updates local character count
      |
      v
User clicks "Run demo"
      |
      v
Browser shows a fixed, clearly labeled placeholder example
```

There is no network request in that flow.

This matters. A frontend demo should be inspectable. If someone searches the source for `fetch`, a private API endpoint, model credentials or a worker URL, they should find none of them.

---

## Features

### 1. AI humanizer-style product interface

The page uses the familiar text-tool pattern: input on the left, scope notes on the right, and a result area below the editor. It is easy to understand in a few seconds.

### 2. Local-only interaction

Typing updates the character counter in the browser. Clicking the button shows a fixed sample. No analytics script, ad script, login system or backend endpoint is bundled into this repository.

### 3. Explicit placeholder behavior

The page says exactly what happened. It does not quietly return a canned answer and let visitors assume the code contains a production AI pipeline.

### 4. Search-friendly documentation

The README includes terms developers and product builders commonly use when researching this category:

- `AI humanizer`
- `humanize text`
- `text humanizer`
- `AI writing style review`
- `Chinese writing tools`
- `natural writing workflow`
- `AIGC text style`
- `frontend demo`
- `privacy-first writing tool`

### 5. Public leak check

The repository includes a small verification script. It fails when files or strings associated with private backend code appear in the public directory.

For example, if a future edit accidentally adds a production API path, `npm test` stops immediately and reports the offending file.

---

## Run locally

No installation is required for the UI.

### Option A: open the file directly

Open `index.html` in a browser.

### Option B: run the public repository check

```powershell
npm test
```

Expected output:

```text
公开仓库检查通过：... 个文件，未发现私有处理逻辑或生产配置。
```

---

## Project structure

```text
ai_promptrule/
├── index.html                     # public page structure and SEO metadata
├── styles.css                     # responsive layout and visual system
├── app.js                         # local-only placeholder interaction
├── scripts/
│   └── verify-public-demo.mjs     # private leak check
├── ARCHITECTURE.md                # file responsibilities and decisions
├── CONTEXT.md                     # current public project status
├── LICENSE                        # MIT license
└── README.md                      # project documentation
```

---

## Design notes

The interface is intentionally calm: trust-blue accents, light borders, readable cards and a direct demo area. The goal is not to recreate a full dashboard. It is to make the public scope obvious.

| Design choice | Reason |
| --- | --- |
| Blue primary color | Familiar for productivity and SaaS interfaces |
| One-page structure | Search visitors can understand the project quickly |
| Browser-only demo | No accidental text upload |
| Clear public/private cards | Readers know what is open source and what is not |
| Reduced-motion support | Basic accessibility for users who prefer less animation |

---

## Public repository policy

This project is a frontend reference, not a source dump of a commercial service.

Do not add:

- real prompts or rewrite recipes
- private model routing
- API keys or environment variables
- production domains or analytics identifiers
- database files
- payment, license or account implementation
- backend worker code

Before publishing changes, run:

```powershell
npm test
```

---

## FAQ

### Is this a complete AI text humanizer?

No. It is an open-source frontend demo. The page illustrates a natural writing workflow, but production text processing is intentionally absent.

### Does the demo upload text?

No. The public JavaScript contains no API request. Text remains in the current browser page.

### Is this repository for academic cheating?

No. The public project is framed as a writing-style interface demo. It does not include detector bypass logic or claims that it can defeat academic review systems.

### Why include terms like `AI humanizer` and `humanize text`?

Those are common category keywords. They help developers find a relevant frontend reference when researching AI writing products.

### Can I use this UI as a starting point?

Yes. The frontend code is published under the MIT license. Keep your own backend, credentials and product logic outside the public repository.

---

## Search record

The project documentation was shaped after reviewing public references. This section avoids repeating the same research later.

| Source | Link | Useful observation |
| --- | --- | --- |
| skills.sh AI Humanizer | [skills.sh/smithery/ai/ai-humanizer](https://skills.sh/smithery/ai/ai-humanizer) | Category language includes AI patterns, robotic text and natural-sounding revision |
| blader/humanizer | [github.com/blader/humanizer](https://github.com/blader/humanizer) | A strong README explains the goal early and includes concrete usage examples |
| GitHub humanize-text topic | [github.com/topics/humanize-text](https://github.com/topics/humanize-text) | Useful repository topics include `ai-humanizer`, `humanize-text`, `writing-tools` and `text-humanizer` |

---

## Completed

- [x] Static landing page
- [x] Responsive editor demo
- [x] Local-only placeholder interaction
- [x] SEO metadata
- [x] Detailed GitHub README
- [x] Automated private leak check
- [x] Architecture notes

## Todo

- [ ] Add a screenshot after the public repository is published
- [ ] Add the final GitHub Pages URL if GitHub Pages is enabled later

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## License

MIT. See [LICENSE](https://github.com/BurtonLeonard/ai_promptrule/blob/main/LICENSE).
