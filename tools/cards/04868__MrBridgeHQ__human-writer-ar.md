---
id: tool-04868
type: tool
area: 库
status: active
tags: [去AI味, Claude插件, Markdown, 协议宽松, 本地优先, 英文文档, 本地写作]
title: human-writer-ar
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/mrbridgehq/human-writer-ar
created: 2026-07-18
updated: 2026-07-18
no: 4868
category: 一、去 AI 味 / Humanizer 库
repo: MrBridgeHQ/human-writer-ar
stars: 0
url: https://github.com/mrbridgehq/human-writer-ar
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# MrBridgeHQ/human-writer-ar

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/mrbridgehq/human-writer-ar
- **Stars**：0
- **语言**：Markdown
- **License**：MIT
- **Topics**：agent-skills, ai-detection, ai-writing, arabic, claude, copywriting
- **GitHub 描述**：Human Writer (Arabic (MSA, RTL)) - AI-text humanizer & 0-100 detector (Claude Code skill). Part of the mr-bridge.com toolkit.
- **本地描述**：Human Writer (Arabic (MSA, RTL)) - AI-text humanizer & 0-100 detector (Claude Code skill). Part of the mr-bridge.com toolkit.
- **拉取时间**：2026-07-25 17:57:28

---

# Human Writer - Arabic

Make Arabic AI text read as human-authored, and audit any Arabic draft with a **deterministic 0-100 AI-detection score** before you publish. A Claude Code Agent Skill.

The Arabic member of the `human-writer` per-language family (English, French, Spanish, Portuguese, German, Arabic, Hindi). Each member installs side by side and activates only on its own language triggers.

## Three modes

- **Write:** produce new Arabic content already engineered to score low-risk.
- **Clean:** rewrite an existing Arabic AI draft to strip detector tells, preserving meaning.
- **Audit:** score a Arabic draft, surface the worst tells, and recommend fixes without rewriting it.

Four content types are supported (marketing long-form, short-form comms, technical docs, editorial-SEO), each with its own tolerances.

## Why it exists

Modern LLM output is fluent enough to ship but carries fingerprints that commercial detectors (Copyleaks, GPTZero, Originality.ai) latch onto: low burstiness, repeated vocabulary, formulaic frames, and typographic tells. A draft rejected at 70 percent or more does not need a rewrite from scratch; it needs a disciplined sweep of the specific tells the detectors weight. This skill encodes that doctrine for Arabic and ships a scorer, targeting sub-25 percent AI-probability on Copyleaks and GPTZero.

## Arabic-specific doctrine

- Latin comma, semicolon, and question mark used where the Arabic marks belong, plus the foreign em-dash (U+2014), which is treated more strictly than in English or French.
- Tatweel (kashida) overuse and waw or fa connector overuse, clitic-aware vocabulary matching, EN-to-AR calques, and formulaic conclusion frames. Modern Standard Arabic, right-to-left.

## The analyzer

`scripts/analyze.py` is a deterministic 0-100 scorer that runs offline (it loads `rules.yaml`; optional live scoring via Copyleaks, GPTZero, or Originality.ai with `--external`).

```bash
python3 skills/human-writer-ar/scripts/analyze.py --input draft.md --lang ar --type marketing --format human
```

Score bands: 0-24 low-risk (ship it), 25-49 medium (apply the top fixes and re-score), 50-74 high, 75-100 critical.

## Installation

```bash
cp -r skills/human-writer-ar ~/.claude/skills/
pip install -r skills/human-writer-ar/requirements.txt   # pyyaml required, httpx optional
```

Or copy `skills/human-writer-ar` into a project's `.claude/skills/` directory.

## Use it

Once installed, the skill auto-activates on Arabic prose requests. Example prompts:

- "Rends ce texte arabe plus humain"
- "Clean this Arabic draft of AI tells"
- "Audit this Arabic text for AI-detection risk"

Force activation: "Use the `human-writer-ar` skill to ...".

## What is inside

The skill lives in `[`skills/human-writer-ar/`](skills/human-writer-ar/)`: a `SKILL.md` (routing, master checklist, anti-patterns), a `references/` library (stylistic, statistical, and structural tells, humanization techniques, and per-content-type adapters), and `scripts/` (`rules.yaml` plus the `analyze.py` 0-100 scorer and its tests).

## License

See `LICENSE`.

---

Part of the **[mr-bridge.com](https://mr-bridge.com)** toolkit for scraping, data, and content automation:
[Scrapers](https://mr-bridge.com/scrapers) · [MCP servers](https://mr-bridge.com/mcp-servers) · [AI workflows](https://mr-bridge.com/ai-workflows) · [Studies](https://mr-bridge.com/studies) · [Articles](https://mr-bridge.com/articles) · [Solutions](https://mr-bridge.com/solutions)

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

*Part of the [MrBridge Agent Skills catalog](https://github.com/MrBridgeHQ/skills). Browse them all at [mr-bridge.com/skills](https://mr-bridge.com/skills).*
