---
id: tool-05103
type: tool
area: 库
status: active
tags: [去AI味, Claude插件, Python, 协议宽松, 需API密钥, 英文文档]
title: eames
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/sunnyallana/eames
created: 2026-07-18
updated: 2026-07-18
no: 5103
category: 一、去 AI 味 / Humanizer 库
repo: sunnyallana/eames
stars: 0
url: https://github.com/sunnyallana/eames
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 7521fba38765e3ec
  - methods/改稿润色指令库.md
---

# sunnyallana/eames

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/sunnyallana/eames
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Eames is a Claude Code skill that rewrites AI-generated text into prose that reads as human-written, and proves it worked by scoring the output against   three open-source AI detectors before and after the rewrite. One /humanize command, three layers, real before/after numbers in the reply.
- **本地描述**：Eames is a Claude Code skill that rewrites AI-generated text into prose that reads as human-written, and proves it worked by scoring the output against   three open-source AI detectors before and after the rewrite. One /humanize command, three layers, real before/after numbers in the reply.
- **拉取时间**：2026-07-25 18:06:13

---

<div align="center">

```
   ███████╗ █████╗ ███╗   ███╗███████╗███████╗
   ██╔════╝██╔══██╗████╗ ████║██╔════╝██╔════╝
   █████╗  ███████║██╔████╔██║█████╗  ███████╗
   ██╔══╝  ██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║
   ███████╗██║  ██║██║ ╚═╝ ██║███████╗███████║
   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝
```

**A Claude Code skill that studies AI prose, learns its tells, and rewrites it in a human voice.**

*Named after Eames, the Forger from Inception — the one who studies targets, mimics them precisely, and slips past every detector in the room.*

<!--
  Recording a demo gif? Drop it at docs/hero.gif and uncomment the line below.
  Suggested: ~10s of /humanize in action, ~700px wide, with the before/after
  detection numbers visible at the end. Tools that work well: charmbracelet/vhs,
  asciinema, or ttyrec + ttygif.
-->
<!-- <img src="docs/hero.gif" alt="Eames demo" width="720" /> -->

</div>

---

## What it is

Eames is a `/humanize` skill for [Claude Code](https://claude.com/claude-code). You type the command, paste AI-generated text, and Claude runs the text through three layers:

1. **A writing-craft prompt** — 400+ lines of rules drawn from published anti-LLM-style guidance (em-dash bans, copula-avoidance fixes, paragraph-arc heuristics, vocabulary watchlists). Claude follows these when rewriting.
2. **A TypeScript pattern pass** — `analyze.ts` scans for known AI tells; `transform.ts` auto-rewrites the mechanical ones (`utilize` → `use`, removes "I hope this helps" sentences, fixes curly quotes, flattens em-dashes).
3. **A Python detection pass** — runs the text through three open-source AI detectors (Zippy, RADAR, Binoculars) **before** and **after** the rewrite, so you can see whether the humanizer actually helped.

Each layer is independent. Use one, two, or all three.

---

## Install

### macOS / Linux

```bash
git clone https://github.com/sunnyallana/eames.git
cd eames
bash install.sh
```

### Windows (PowerShell)

```powershell
git clone https://github.com/sunnyallana/eames.git
cd eames
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

The installer:
- Drops the skill into `~/.claude/skills/humanize/` (or the Windows equivalent).
- Backs up any prior install to `~/.claude/skill-backups/` outside the skills tree (so Claude Code won't load the backup as a phantom skill).
- Optionally installs the Node CLI deps (ts-node, typescript) and the Python detection deps (Zippy by default, RADAR and Binoculars on opt-in).

Re-run any time to update.

---

## Use

In a Claude Code session:

```
/humanize
```

Then paste your AI-written text. Claude will run the protocol end-to-end and show you a final detection score line at the bottom.

Or run the pieces from the terminal directly:

```bash
# Scan
npx ts-node ~/.claude/skills/humanize/scripts/analyze.ts draft.txt

# Auto-rewrite mechanical patterns
npx ts-node ~/.claude/skills/humanize/scripts/transform.ts draft.txt --fix-dashes -o clean.txt

# Detection sweep
python ~/.claude/skills/humanize/scripts/detect/detect.py draft.txt --json
```

---

## A real before-and-after

This is verbatim output from the included `demo/` files.

**Input** — 855 chars of generic AI prose:

> *In the ever-evolving landscape of artificial intelligence, it is crucial to delve into the multifaceted intricacies that underpin modern systems. Furthermore, the vibrant interplay between data and algorithms serves as a testament to the pivotal role that machine learning plays in today's fast-paced world. Additionally, this groundbreaking technology showcases the seamless integration of cutting-edge methodologies, fostering an environment that enhances productivity and empowers users to harness valuable insights. The system boasts state-of-the-art capabilities that leverage robust frameworks, underscoring its potential to revolutionize the industry. It is important to note that, while challenges remain, the future looks bright. I hope this helps clarify how transformative these solutions can be. Let me know if you have any other questions!*

**Output** — 560 chars after the full pipeline:

> *AI right now is mostly machine learning under the hood. That's the part doing pattern-recognition on data, and it's the part that explains both why these systems are useful and why they fail the way they do.*
>
> *What works: integrating ML into things that were already structured. Document review, customer support routing, code completion. The speedup is real and people are willing to pay for it.*
>
> *What's still rough: when the same speed gets treated as confidence. Faster output is not better output, and the gap is where the headline failures keep happening.*

**Scores:**

| Check                | Before              | After                  |
| -------------------- | ------------------- | ---------------------- |
| `analyze.ts` issues  | **25**              | **0**                  |
| Zippy verdict        | AI (score 0.03)     | Human (score 0.01)     |

(RADAR and Binoculars were not installed for this demo. With them enabled you'd see two more rows.)

---

## How it works

```
        ┌──────────────────────────────┐
your    │  /humanize  (Claude Code)    │
text →  │                              │
        │  1. write input to tempfile  │
        │  2. detect.py  → BASELINE    │ ───► zippy / radar / binoculars
        │  3. analyze.ts → JSON report │
        │  4. transform.ts → mechanical│
        │     auto-rewrite             │
        │  5. Claude applies the       │
        │     writing-craft rules to   │
        │     what's left (vocabulary, │
        │     rhythm, voice, structure)│
        │  6. detect.py  → FINAL       │ ───► zippy / radar / binoculars
        │  7. show you before / after  │
        └──────────────────────────────┘
                       │
                       ▼
                  rewritten text
                  + score delta
```

Each step is deterministic where it can be (regex, JSON-parseable scanner, compression-ratio detector) and contextual where it has to be (vocabulary that needs context, structural patterns, voice calibration).

---

## The three detection tiers

The detection layer runs whichever tiers you've installed. Missing ones report `available: false` in the JSON and never block the rest of the pipeline.

| Tier | Detector | Disk | First-run | Hardware | Strength |
|------|---|---|---|---|---|
| 1 | [Zippy](https://github.com/thinkst/zippy) | ~5 MB | 0 | CPU | Compression-ratio heuristic. Fast, ~50× faster than RoBERTa-based detectors. Coarse but always works. |
| 2 | [RADAR](https://huggingface.co/TrustSafeAI/RADAR-Vicuna-7B) | ~600 MB | ~500 MB model | CPU OK, GPU faster | RoBERTa-large trained adversarially against a paraphraser. Robust to rewrites — the closest stress-test for what a humanizer like this does. |
| 3 | [Binoculars](https://github.com/ahans30/Binoculars) | ~14 GB+ | Falcon-7B pair | GPU strongly recommended | State-of-the-art zero-shot detection (ICML 2024). Beats GPTZero in the paper's benchmarks. |

Install commands the installer prints:

```bash
pip install thinkst-zippy                                           # Tier 1
pip install transformers torch                                      # Tier 2
pip install git+https://github.com/ahans30/Binoculars.git           # Tier 3
```

Closed-source detectors (Turnitin, GPTZero, Originality.ai, Pangram) don't publish their models, so no one can replicate them exactly. The open-source tiers above are the closest available proxy.

---

## Layout

```
eames/
├─ install.sh                 macOS / Linux installer
├─ install.ps1                Windows installer
├─ LICENSE                    MIT
├─ README.md
├─ demo/                      sample input + before / after files used above
└─ skill/                     ← everything in here is copied to ~/.claude/skills/humanize/
   ├─ SKILL.md                writing-craft guide + auto-invocation protocol
   └─ scripts/
      ├─ analyze.ts           pattern scanner
      ├─ transform.ts         mechanical auto-rewriter
      ├─ patterns.json        rule sets (edit to customize)
      ├─ package.json
      ├─ tsconfig.json
      └─ detect/
         ├─ detect.py         zippy + radar + binoculars orchestrator
         ├─ requirements.txt
         └─ README.md         detection-layer docs
```

---

## Customizing

**Vocabulary and replacements** — edit `skill/scripts/patterns.json` (before install) or `~/.claude/skills/humanize/scripts/patterns.json` (after install). The four lists are `ai_words`, `puffery`, `replacements`, and `chatbot_artifacts`. Auto-rewrite mappings live in `replacements`; setting a value to `""` deletes the match.

**Writing rules** — edit `skill/SKILL.md`. It's plain markdown that Claude reads when you invoke `/humanize`. Add domain-specific guidance, your own voice samples, or genre conventions. Re-run the installer to push the change to the live skill.

**Detection thresholds** — `detect.py` reports raw scores rather than applying a hard threshold. The default label cutoff is 0.5 for RADAR; Zippy and Binoculars use their upstream defaults. Modify `detect.py` if you want different thresholds.

---

## Caveats

- Open-source detectors are a proxy for commercial ones, not a guarantee. A rewrite that passes Zippy / RADAR / Binoculars will *usually* pass Turnitin or GPTZero, but no detector landscape is stable for long.
- The Python detection layer is optional. The `/humanize` skill still runs without it; you just lose the before / after score line.
- RADAR is licensed for non-commercial use only. Check the upstream model card before using it in a commercial product.
- This tool removes the surface patterns AI text *tends* to have. It cannot make false claims true, fix bad arguments, or paper over thin content. The honest use case is restoring a voice that's already there, not laundering output you couldn't have written yourself. Follow your school's, employer's, or platform's policies.

---

## Acknowledgments

This project is mostly a thoughtful assembly of other people's work. Credit where it's due.

### Detection layer

- **[Zippy](https://github.com/thinkst/zippy)** by Thinkst Applied Research — MIT-licensed compression-ratio AI text detector. ~200 lines of Python that punch well above their weight. Their [blog post](https://blog.thinkst.com/2023/06/meet-zippy-a-fast-ai-llm-text-detector.html) explaining the technique is worth reading.
- **[RADAR-Vicuna-7B](https://huggingface.co/TrustSafeAI/RADAR-Vicuna-7B)** by TrustSafeAI — RoBERTa-large fine-tuned via adversarial learning against a paraphraser, NeurIPS 2023. [Paper](https://arxiv.org/abs/2307.03838). Non-commercial license.
- **[Binoculars](https://github.com/ahans30/Binoculars)** by Hans, Schwarzschild, Cherepanova, Kazemi, Saha, Goldstein, et al. — Apache-2.0. ICML 2024. The state-of-the-art zero-shot detector this project measures against. [Paper](https://arxiv.org/abs/2401.12070).
- **[MGTEval / MGTD benchmark](https://github.com/datamllab/awsome-LLM-generated-text-detection)** — curated index of detection research that helped narrow down which tiers to support.

### Runtime

- **[Claude Code](https://claude.com/claude-code)** by Anthropic — the runtime that loads `SKILL.md` and follows the auto-invocation protocol. Without it this is just a doc and three scripts.
- **[Hugging Face Transformers](https://github.com/huggingface/transformers)** — Apache-2.0. Powers the RADAR detector.
- **[PyTorch](https://github.com/pytorch/pytorch)** — BSD. Powers RADAR and (optionally) Binoculars.
- **[ts-node](https://github.com/TypeStrong/ts-node)** + **[TypeScript](https://github.com/microsoft/TypeScript)** — MIT. Run the pattern scripts.
- **[Brotli](https://github.com/google/brotli)** — used inside Zippy.

### Writing-craft guidance

The rules in `skill/SKILL.md` are an assembled distillation of published anti-LLM-style writing guidance from across the open web — em-dash bans, copula-avoidance fixes, vocabulary watchlists, paragraph-shape heuristics. None of the rules are original to this project; the contribution is wiring them into a runnable skill alongside the detection layer.

### Name

**Eames** is the Forger in Christopher Nolan's *Inception* (2010), played by Tom Hardy. Inside the shared-dream architecture the heist team uses, Eames's job is to study a target's voice and manner thoroughly enough to impersonate them — convincingly enough that the target's own subconscious doesn't notice the seam. He treats it as a craft, not a trick. The name was picked because that's the closest description of what this skill is doing to AI-generated prose: studying the tells, learning the voice, and replacing the seam.

> *"You mustn't be afraid to dream a little bigger, darling."* — Eames

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## License

MIT. See [LICENSE](https://github.com/sunnyallana/eames/blob/main/LICENSE).
