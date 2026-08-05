---
id: tool-05231
type: tool
area: 库
status: active
tags: [去AI味, Claude插件, JavaScript, 协议宽松, 需API密钥, 英文文档]
title: ai-humanizer
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/viryazheng/ai-humanizer
created: 2026-07-18
updated: 2026-07-18
no: 5231
category: 一、去 AI 味 / Humanizer 库
repo: ViryaZheng/ai-humanizer
stars: 2
url: https://github.com/viryazheng/ai-humanizer
tier: "B"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# ViryaZheng/ai-humanizer

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/viryazheng/ai-humanizer
- **Stars**：2
- **语言**：JavaScript
- **License**：MIT
- **Topics**：academic-writing, agent-skills, ai-detection, anthropic, claude, claude-code, claude-skill, humanizer, plugin, turnitin
- **GitHub 描述**：Detector-guided humanizer skill for Claude Code: lower the AI-detection score of English text while preserving every key term, number, citation, and the original logic. Keyless, agent-as-rewriter.
- **本地描述**：Detector-guided humanizer skill for Claude Code: lower the AI-detection score of English text while preserving every key term, number, citation, and the original logic. Keyless, agent-as-rewriter.
- **拉取时间**：2026-07-25 18:10:55

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# ai-humanizer

A Claude Code skill that **lowers the AI-detection score of English text without changing what it says** — every key term, number, and citation is preserved verbatim, and the original logic stays intact.

It works by *detector-guided surgical paraphrase* (cf. [arXiv:2506.07001](https://arxiv.org/abs/2506.07001)): a detector flags which sentences read as AI, the agent rewrites only those, re-checks, and loops — keeping the best result and never dropping a protected term.

- **No API key.** The baseline detector is the keyless ZeroGPT endpoint; the **agent running the skill is the rewriter**, so there is no separate paraphrase API to configure.
- **Term-safe.** Numbers, percentages, citations, drug/gene names, theorems, standards, and inline notation are extracted and verified character-for-character after every round.
- **Honest.** Real human academic prose scores 0–50% on these detectors, not 0. Saturated topics (clinical, monetary policy, common legal/historical essays) are reported truthfully instead of over-promised. ZeroGPT is treated as a free *proxy* — Turnitin is the ground truth.
- **Reads detector reports.** Hand it a Turnitin / GPTZero / Originality.ai PDF and it uses the report's highlighted spans as the attack list.

> ⚠️ For legitimate use — reducing false positives on your own writing, de-roboticizing AI-assisted drafts, and detector research. Follow your institution's and publisher's policies on AI assistance.

## Install

```
/plugin marketplace add recomby-ai/ai-humanizer
/plugin install ai-humanizer@ai-humanizer
```

Update later with:

```
/plugin marketplace update ai-humanizer
```

<details>
<summary>Manual install (other agents — Codex, Cursor, Gemini CLI)</summary>

The skill is plain Node with no dependencies. Clone the repo (or copy the skill folder) and point your agent at `SKILL.md`:

```bash
git clone https://github.com/recomby-ai/ai-humanizer
# the skill lives at:
#   ai-humanizer/plugins/ai-humanizer/skills/ai-humanizer/
```

Then tell the agent to read `SKILL.md` and follow it. The two scripts run under any Node 18+:

```bash
node scripts/detect.mjs <file>            # AI score + flagged sentences (JSON)
node scripts/terms.mjs extract <file>     # protected factual terms
node scripts/terms.mjs verify <orig> <new> <terms.json>   # term-preservation gate
```
</details>

## How to use it

Trigger phrases (English or Chinese): *"humanize this", "lower the AI score", "降AI率", "降低Turnitin AI率", "make this read human", "reduce GPTZero score"* — or just hand over a draft, optionally with a detector report PDF.

The skill will:

1. Detect a **baseline** score and the flagged sentences.
2. Build the **protected-term** list (deterministic regex + the agent's own domain-entity pass).
3. Rewrite **only the flagged sentences** under a set of surgical rules grounded in measured findings (see `reference/principles.md`).
4. Re-detect and loop (up to ~5 rounds), keeping the best version.
5. **Verify** every protected term survived, then show a **before → after** report with a sentence-level diff.

## Examples

Real before/after runs are in `[`examples/`](examples/)`:

- `[Nursing essay](examples/01-nursing-essay.md)` — normal academic domain, **100% → 11.1%** in one round, 7/7 terms kept.
- `[Clinical meta-analysis](examples/02-clinical-saturated-domain.md)` — a detector-*saturated* domain. Two independent rewrites scored **0%** and **26.5%** under identical rules (14/14 terms kept) — the clearest illustration of why best-of-N matters and why the skill won't over-promise.

## Why these rules (the short version)

The detailed evidence is in `[`reference/principles.md`](plugins/ai-humanizer/skills/ai-humanizer/reference/principles.md)`. The headline findings, measured against ZeroGPT with confirmed-human baselines:

- **The signal is lexical predictability, not connectives.** "Furthermore / Moreover / plays a crucial role" is a false tell — a Band-9 IELTS sample full of them scored 19.6%; a polished AI clinical review with none scored 100%.
- **Fluency is the tell.** Polished, frictionless prose reads as AI. You lower the score by allowing *slight roughness* and longer, idea-dense sentences — not by chopping text into short punchy lines.
- **For academic content, more precision — not more casual.** Swap high-probability defaults for precise, lower-frequency domain vocabulary. "Explain it to a friend" is the wrong move here.
- **Best-of-N is the biggest lever.** Score variance is sampling-dominated (the same input can swing 0–52%). Generate a few independent rewrites and keep the lowest scorer.

## License

`[MIT](LICENSE)` © recomby-ai
