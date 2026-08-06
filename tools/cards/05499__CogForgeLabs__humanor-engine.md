---
id: tool-05499
type: tool
area: 库
status: active
tags: [去AI味, 互动叙事, TypeScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: humanor-engine
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/cogforgelabs/humanor-engine
created: 2026-07-18
updated: 2026-07-18
no: 5499
category: 一、去 AI 味 / Humanizer 库
repo: CogForgeLabs/humanor-engine
stars: 0
url: https://github.com/cogforgelabs/humanor-engine
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# CogForgeLabs/humanor-engine

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/cogforgelabs/humanor-engine
- **Stars**：0
- **语言**：TypeScript
- **License**：NOASSERTION
- **Topics**：—
- **GitHub 描述**：Open-source text humanizer and AI-text detection engine (TypeScript). The engine behind HumanOR.
- **本地描述**：Open-source text humanizer and AI-text detection engine (TypeScript). The engine behind HumanOR.
- **拉取时间**：2026-07-25 18:20:58

---

# HumanOR Engine

Open-source engine for **humanizing text** and **detecting AI-generated text**.
This is the brain behind [human-or.cognitive-industries.org](https://human-or.cognitive-industries.org);
the website is a separate (private) repo that runs this engine **server-side** —
the engine and its models are never shipped to a browser.

- **Humanizer** — removes the mechanical "signs of AI writing" (em dashes, curly
  quotes, decorative emoji, filler phrases, chatbot artifacts, and a curated set
  of "AI vocabulary" words) with deterministic, explainable edits. No model, no
  network.
- **Detector** — scores how AI-like a passage is using transparent stylometric
  signals (AI-vocabulary density, burstiness, punctuation tells, connector
  density, formulaic structure, filler density). Every point of the score traces
  to a named signal.

Text is implemented today. Image and audio detection are on the roadmap (see
[Roadmap](#roadmap)); the website stubs those endpoints until the models land.

## Why heuristics first

The baseline detector is a glass box, not a classifier you have to trust blindly.
It is grounded entirely in **human-authored** research on how LLM prose differs
from human prose:

- Wikipedia, *Signs of AI writing* (WikiProject AI Cleanup)
- Kobak et al., *Delving into ChatGPT usage in academic writing through excess
  vocabulary* (arXiv:2406.07016)
- The FSU focal-word study, *Why Does ChatGPT "Delve" So Much?* (arXiv:2412.11385)
- Editor/journalist write-ups on AI tells (Washington Post, 2025)

Trained text/image/audio classifiers will slot in behind the same
`DetectSignal` interface without changing the API. See [docs/METHOD.md](https://github.com/CogForgeLabs/humanor-engine/blob/main/docs/METHOD.md).

## Install

```bash
npm install @humanor/engine
```

## Usage

```ts
import { humanizeText, detectTextAI } from "@humanor/engine";

const { text, edits } = humanizeText(
  'In order to utilize this — it is important to note that you should delve in.',
  { aggressive: false },          // minConfidence, categories also available
);
// text: "To use this, you should delve in."  (+ structured `edits`)

const result = detectTextAI("In today's evolving landscape, this stands as a testament...");
// { aiScore: 0..100, label: "likely-ai" | "uncertain" | "likely-human",
//   summary, signals: [...explainable...], stats }
```

### API

| Function | Returns |
|----------|------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| `humanizeText(text, options?)` | `{ text, edits }` — rewritten text + applied edits |
| `humanizeEdits(text, options?)` | `Edit[]` — proposed edits without applying |
| `detectTextAI(text)` | `DetectResult` — score, label, signals, stats |
| `humanizeRules()` | the compiled rule catalog (for inspection/UI) |

`HumanizeOptions`: `minConfidence` (default 0.6), `aggressive` (default false),
`categories` (`punctuation` \| `filler` \| `vocabulary` \| `chatbot`).

## Develop

```bash
npm install      # also builds (prepare script)
npm test         # vitest
npm run build    # tsc -> dist/
```

## Roadmap

- [x] Text humanizer (deterministic, rule-based)
- [x] Text AI-detector (explainable stylometry)
- [ ] Trained text classifier (HuggingFace), behind the same interface
- [ ] Image AI-detection model
- [ ] Audio AI-detection model
- [ ] Python bindings + HuggingFace model cards

Models will be published under the same org on
[GitHub](https://github.com/cognitive-industries) and
[HuggingFace](https://huggingface.co/cognitive-industries).

## License

Apache-2.0. Use it, build on it, ship it — including commercially.
