---
id: tool-05367
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: saya-bullshit-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/sozlabs/saya-bullshit-detector
created: 2026-07-18
updated: 2026-07-18
no: 5367
category: 一、去 AI 味 / Humanizer 库
repo: sozlabs/saya-bullshit-detector
stars: 0
url: https://github.com/sozlabs/saya-bullshit-detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# sozlabs/saya-bullshit-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/sozlabs/saya-bullshit-detector
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：scroll your feed without the bullshit and ai slop
- **本地描述**：scroll your feed without the bullshit and ai slop
- **拉取时间**：2026-07-25 18:15:58

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Saya Bullshit Detector

LinkedIn feed extension. Reads posts, decides **water** (blur it) vs **signal** (leave it). Runs on your machine — no backend, no API keys, no "send my feed to OpenAI" nonsense.

## What it actually does

- Hooks into **linkedin.com** feed
- Fast **heuristics** catch obvious engagement bait
- Local classifier runs in the background — nothing leaves your browser
- Overlay with a custom title + roast line; the words in the roast are what the model actually latched onto, not a fixed buzzword list

## Before you whine that it doesn't build

The **big model file is not in git**. You export it yourself:

```bash
cd ../dataset
pip install onnxscript onnxruntime "optimum[onnxruntime]==1.23.3"
python scripts/export_onnx.py
```

Then in this repo:

```bash
cp .env.example .env.local   # optional overrides
npm install
npm run build
```

`npm run build` copies runtime files into `build/chrome-mv3-prod` and runs a sanity check. If you skip it and load a half-built folder — that's on you.

Load unpacked in Chrome from:

```
build/chrome-mv3-prod
```

Not `build/`. Not the repo root. Not mid-build while the bundler is still wiping files — Chrome will cry about a missing manifest.

After reload: **hard refresh LinkedIn** (F5). Otherwise you get ghost errors from a dead content script.

## Env

Defaults live in `.env`. Override in `.env.local` if you need to.

Main knobs: LinkedIn URL match, classify threshold, timeouts. Full list in `.env.example`.

`PLASMO_PUBLIC_*` values are **baked into the bundle at build time**. Don't put secrets there — there is nothing to secret anyway, it's all local.

## Status

Work in progress. Selectors break when LinkedIn moves DOM again. First analysis per post can be slow. Visual stuff (Saya eye, motion) is **proprietary** — not part of any hypothetical open drop.

## Don't commit

- `.env.local`
- `assets/model/**/*.onnx`
- `build/`

## License / sharing

Repo visibility is your call. If you open-source anything later, plan to strip or keep private the UI assets. The classifier pipeline and extension logic are separable from the eye candy.
