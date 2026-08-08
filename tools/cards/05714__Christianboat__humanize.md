---
id: tool-05714
type: tool
area: 库
status: active
tags: [去AI味, 协议宽松, 本地优先, 英文文档, 本地写作]
title: humanize
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/christianboat/humanize
created: 2026-07-18
updated: 2026-07-18
no: 5714
category: 一、去 AI 味 / Humanizer 库
repo: Christianboat/humanize
stars: 0
url: https://github.com/christianboat/humanize
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 986574756f5864fb
  - methods/改稿润色指令库.md
---

# Christianboat/humanize

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/christianboat/humanize
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：agent-skill, ai-detection, ai-humanizer, claude-skill, gptzero, humanizer, llm, opencode
- **GitHub 描述**：Humanize: an AI-text humanizer agent skill. 29-pattern detection, adversarial refinement, and a guaranteed zero em dashes.
- **本地描述**：Humanize: an AI-text humanizer agent skill. 29-pattern detection, adversarial refinement, and a guaranteed zero em dashes.
- **拉取时间**：2026-07-25 18:28:54

---

<h1 align="center">
  ✍️ Humanize
</h1>

<p align="center">
  <b>An AI-text humanizer skill that actually removes the tells</b><br>
  <i>29-pattern detection + adversarial refinement + a guaranteed zero em dashes</i>
</p>

<p align="center">
  <a href="#-the-motivation-why-humanize">Why?</a> •
  <a href="#-features">Features</a> •
  <a href="#-how-it-works">How It Works</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-license">License</a>
</p>

<p align="center">
  <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green.svg">
  <img alt="Type: Agent Skill" src="https://img.shields.io/badge/Type-Agent%20Skill-blue.svg">
  <img alt="Em dashes" src="https://img.shields.io/badge/Em%20dashes-zero-critical.svg">
</p>

---

## 💡 The Motivation: Why Humanize?

Most "humanizers" do one of two things. Some run a list of word swaps and call it a day, which leaves the structure screaming AI. Others paraphrase the whole thing through another model, which flattens your voice and still trips detectors.

This skill came out of merging two separate tools that each did half the job. One was a 29-category pattern framework, built from Wikipedia's WikiProject AI Cleanup research, that knew exactly *what* makes text read as machine-written. The other was an adversarial ML pipeline that scored text on perplexity, burstiness, and trigram diversity, and iterated until the numbers looked human. Running them back to back worked, but it was two steps, and both of them kept leaving em dashes everywhere.

**Humanize** is the single skill that came out of fusing them, with one hard rule added on top: the final text contains **zero em dashes**. Not "one per paragraph." None.

---

## ✨ Features

- **29-pattern detection.** Catches significance inflation, copula avoidance, negative parallelisms, the rule of three, signposting, sycophantic tone, and 24 more concrete tells.
- **Adversarial refinement loop.** Up to 10 iterations of transform, re-score, and keep-or-discard, guided by perplexity, burstiness, and trigram diversity.
- **Voice calibration.** Give it a writing sample and it matches your rhythm, vocabulary level, and punctuation habits instead of imposing a generic voice.
- **Zero em dashes, guaranteed.** A mandatory final pass strips every em dash, en dash, and double hyphen, and picks the right replacement for each.
- **Tool-agnostic.** A plain `SKILL.md`, so it runs in Claude Code, OpenCode, and Claude.ai with no code or dependencies.
- **Open source.** MIT licensed. Fork it, tune the pattern list, ship your own.

---

## ⚙️ How It Works

The skill runs a fixed five-phase pipeline on every piece of text.

| Phase | What it does |
| :--- | :--- |
| **1. Pattern Pass** | Scans against all 29 AI-tell categories and rewrites every match. |
| **2. Scoring Pass** | Rates the draft on perplexity, burstiness, trigram diversity, and pattern recurrence. |
| **3. Adversarial Loop** | Applies 2 to 3 random transformations per round, keeping only changes that lower AI probability. |
| **4. Self-Audit** | Asks what still reads as AI and fixes the remaining tells. |
| **5. Em-Dash Elimination** | Mandatory final pass. Removes every em dash and substitutes the punctuation that fits. |

> [!NOTE]
> Phase 5 is never skipped. If a single em dash survives, the skill loops the pass again before it returns anything.

---

## 📦 Installation

Pick your tool. In every case you are just placing the `humanize` folder where the tool looks for skills.

### Claude Code

```bash
git clone https://github.com/Christianboat/humanize.git
mkdir -p ~/.claude/skills
cp -r humanize ~/.claude/skills/humanize
```

On Windows the target is `C:\Users\<you>\.claude\skills\humanize`.

### OpenCode

```bash
git clone https://github.com/Christianboat/humanize.git
mkdir -p ~/.config/opencode/skills
cp -r humanize ~/.config/opencode/skills/humanize
```

### Claude.ai (web)

1. Download this repository as a ZIP, or zip the `humanize` folder yourself.
2. In Claude.ai, open **Settings > Capabilities** and enable code execution / files.
3. Under **Skills**, choose **Upload skill** and select the ZIP.

> [!TIP]
> The uploaded ZIP must contain a top-level `humanize/` folder with `SKILL.md` inside, and the internal paths must use forward slashes. The Windows "Send to > Compressed folder" option uses backslashes, which Claude.ai rejects.

---

## 🚀 Usage

Once installed, the skill activates on its own when you ask the assistant to humanize text. You can also call it by name.

```text
Humanize this draft. Here is a sample of my writing so you can match my voice:
<your sample>

Text to rewrite:
<your text>
```

What you get back:

- A rewrite with the 29 patterns removed and your voice preserved.
- No em dashes anywhere in the output.
- Optionally, a short list of which patterns it caught and which transformations it applied.

---

## 🛠️ Customizing

Everything lives in `SKILL.md`. The two parts most worth editing:

- **The 29 pattern categories.** Add tells specific to your domain, or relax ones you do not care about.
- **The Linguistic Arsenal.** Tune the contraction list, the sentence merge and split thresholds, and the persona injections (undergrad, professional, casual).

The Phase 5 em-dash rule is intentionally strict. Loosen it only if you actually want em dashes back.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. New pattern categories and better replacement heuristics are especially useful. Open an issue or a pull request.

---

## 📄 License

[MIT](https://github.com/Christianboat/humanize/blob/main/LICENSE). Use it, fork it, ship it.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

<div align="center">
  <sub>Built by merging two humanizers into one. This README contains zero em dashes, on purpose.</sub>
</div>
