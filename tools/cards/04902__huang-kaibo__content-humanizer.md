---
id: tool-04902
type: tool
area: 库
status: active
tags: [去AI味, Claude插件, 协议未明, 需API密钥, 中文友好]
title: content-humanizer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/huang-kaibo/content-humanizer
created: 2026-07-18
updated: 2026-07-18
no: 4902
category: 一、去 AI 味 / Humanizer 库
repo: huang-kaibo/content-humanizer
stars: 0
url: https://github.com/huang-kaibo/content-humanizer
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# huang-kaibo/content-humanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/huang-kaibo/content-humanizer
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Use when AI-generated Chinese text needs to sound human — rewrite to remove template patterns, clichés, and over-structuring. Other content-producing Skills should call this before publishing.
- **本地描述**：Use when AI-generated Chinese text needs to sound human — rewrite to remove template patterns, clichés, and over-structuring. Other content-producing Skills should call this before publishing.
- **拉取时间**：2026-07-25 17:58:43

---

[🇨🇳 中文版](./README.zh-CN.md)

# Content Humanizer

A [Claude Code](https://docs.anthropic.com/en/docs/claude-code) Skill that rewrites AI-generated Chinese text to sound like a real person wrote it — removing template patterns, clichés, and over-structuring.

Other content-producing Skills can call this as a final pass before publishing.

## What It Does

```
AI draft → Break structure → Colloquialize → Inject emotion → Add detail → Ban-list scan → Self-check → Info integrity check → AI-tell score → Deliver
```

### Five Core Principles

1. **Cut filler** — remove openers, filler words, vague attributions
2. **Break formulas** — dismantle binary contrasts, dramatic segmenting, rhetorical build-ups
3. **Vary rhythm** — mix long and short sentences, two beats over three, diverse paragraph endings
4. **Trust the reader** — state facts directly, skip softening, justification, and hand-holding
5. **Kill quotables** — if it sounds like an inspirational quote, rewrite it

## Usage

In Claude Code:

```
/content-humanizer
帮我去AI味
改得像人写的
活人感校准
```

### Input Contract

| Field | Required | Description |
|-------|----------|-------------|
| Text | Yes | AI-generated content to rewrite |
| Platform | If available | Xiaohongshu, WeChat, Zhihu, etc. — affects colloquial level |
| Persona | If available | Casual user, expert, student, etc. — affects tone and word choice |
| Protected fields | If available | Brand names, prices, event info that must stay unchanged |

## Quality Controls

### Over-Humanization Brake

Humanizing doesn't mean dumbing down:

- Every core info point from the original must be traceable in the rewrite
- Industry-standard terms (dish names, place names, product specs) stay as-is
- Rewrite must not exceed 1.3x the original word count
- Specific numbers stay specific — "about" and "roughly" only where the original was already imprecise
- Protected fields remain untouched

### Ban List (instant rework triggers)

- Cliché connectors: "首先...其次...最后", "综上所述", "值得注意的是"
- High-frequency AI tells: "说白了", "本质上", "换句话说", "这意味着"
- Punctuation: colons, em-dashes, double quotes (use「」instead)
- Vague attribution: "专家认为", "行业报告显示"
- Synonym cycling, copula avoidance, fake range ("从X到Y"), binary contrasts ("不是…而是…")

### AI-Tell Score (0–100)

Post-rewrite assessment of "how much does this read like AI wrote it":

| Score | Verdict |
|-------|------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| 0–20 | Pass — reads human, ready to publish |
| 21–40 | Minor traces — acceptable for most readers |
| 41–60 | Needs local fixes — specific paragraphs flagged |
| 61–80 | Major rework needed — all issues listed |
| 81–100 | Rejected — start over |

Scoring dimensions: structure, word choice, rhythm, emotion, detail, punctuation (0–15 each).

## Scope

- Chinese text only
- Not for code, config files, or structured data
- Not for formal/academic/official tone requirements

## References

- `references/xhs-adaptation.md` — Xiaohongshu-specific platform rules (auto-loaded when platform is Xiaohongshu)

## License

Apache 2.0
