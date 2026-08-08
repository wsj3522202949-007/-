---
id: tool-04798
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: ownpen
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/huangjihua007-rgb/ownpen
created: 2026-07-18
updated: 2026-07-18
$110
category: 一、去 AI 味 / Humanizer 库
repo: huangjihua007-rgb/ownpen
stars: 2
language: HTML
license: null
url: https://github.com/huangjihua007-rgb/ownpen
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 64a3b47bef74b1ee
  - methods/改稿润色指令库.md
---

<p align="center">
  <img src="https://img.shields.io/badge/version-v1.1.0-blue?style=flat-square" alt="version">
  <img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="license">
  <img src="https://img.shields.io/badge/lang-Chinese-red?style=flat-square" alt="chinese">
  <img src="https://img.shields.io/badge/rules-45%2B-orange?style=flat-square" alt="rules">
</p>

<h1 align="center">OwnPen — 亲笔写的</h1>

<p align="center">
  <b>Make it sound like YOU wrote it.</b><br>
  <b>让领导看不出是AI写的。</b><br>
  Detect and fix AI-generated Chinese text. Platform-aware rewriting.
</p>

---

## Install

```bash
# via npx (recommended)
npx skills add huangjihua007-rgb/ownpen

# via ClawHub
clawhub install ownpen

# via SkillHub
skillhub install ownpen
```

---

## What It Does

1. **Diagnose** -- Scan your Chinese text for AI patterns (45+ rules, severity-graded)
2. **Rewrite** -- Transform it into platform-specific human style
3. **Explain** -- Tell you exactly what was wrong and what changed

**Core Principles (3 Don'ts):**
- Don't change formality -- remove AI templates, not professional tone
- Don't change stance or voice -- keep the author's attitude intact
- Colloquial touches break monotony, they're not the goal

---

## Supported Platforms

| Platform | Style | Command |
|----------|-------|---------|
| WeChat Articles | Insight + rhythm + detail | `/ownpen gongzhonghao` |
| Zhihu | Opinion + evidence + depth | `/ownpen zhihu` |
| Xiaohongshu | Diary + details + casual | `/ownpen xiaohongshu` |
| Work Reports | Conclusion-first + data | `/ownpen huibao` |
| WeChat Moments | Short + warm + incomplete | `/ownpen pengyouquan` |
| General | Just remove AI patterns | `/ownpen tongyong` |

---

## Example

**Before (AI-generated):**

> 在当今数字化转型的大背景下，AI正在深刻改变着各行各业。我们不仅需要积极拥抱变革，更要深入思考如何保持核心竞争力。综上所述，未来可期。

**Diagnosis:**

```
[fatal] "在当今...大背景下" -- template opening
[fatal] "不仅...更要..." -- forced parallelism
[fatal] "综上所述...未来可期" -- cliche ending
[fatal] zero personal details, zero specific examples

AI score: HEAVY
```

**After (WeChat Article style):**

> 上周五改PPT改到第三版的时候，旁边实习生说了句："学姐，这个ChatGPT 30秒就能做。"
>
> 五年经验，干不过一个prompt？
>
> 后来我真试了。5分钟搞定了我改一下午的东西。但说个反直觉的事——用了半年AI之后，我反而加薪了。

---

## Why Not humanizer-zh?

| | humanizer-zh | OwnPen |
|---|---|---|
| Rules | Translated from English Wikipedia | Built natively for Chinese |
| Chinese patterns | Detects "-ing endings" (irrelevant) | Detects 体制词/排比/成语/总分总/四字词偏好 |
| Platform styles | None | 5 platform-specific rewrites |
| Core principles | None | 3 Don'ts: no stance/voice/formality change |
| Updates | v1.0.0, never updated | Active development |
| Examples | None | Real before/after samples |

---

## Detection Categories

| Category | Rules | Examples |
|----------|:-----:|---------|
| Vocabulary | 14 | 赋能/闭环/深耕/综上所述/未来可期/四字词偏好 |
| Sentence patterns | 16 | 排比三连/对偶/万能开头/设问自答/分类枚举/括号解释癖 |
| Emotion | 10 | 零立场/假共情/过度正能量 |
| Structure | 8 | 工整病/总分总/段落均匀 |
| Punctuation | 5 | 分号癖/省略号缺失 |

---

## What's New in v1.1.0

- **Brand**: English name `OwnPen`, slug `ownpen`
- **Core Principles**: Added "3 Don'ts" framework (don't change formality / stance / voice)
- **New Rules**: +5 detection patterns (设问自答, 分类枚举, 括号解释癖, 四字词偏好, 递进叠加)
- **Platform Tune**: WeChat Articles emphasize insight over emotion; General mode adds specifics instead of colloquial touches

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Links

- [ClawHub](https://clawhub.ai/skills/ownpen)
- [SkillHub](https://skillhub.cn)
- [GitHub](https://github.com/huangjih
