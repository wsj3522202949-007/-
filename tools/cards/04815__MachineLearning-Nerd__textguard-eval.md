---
id: tool-04815
type: tool
area: 库
status: active
tags: [去AI味, 协议未明, 本地优先, 英文文档, 本地写作]
title: textguard-eval
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/machinelearning-nerd/textguard-eval
created: 2026-07-18
updated: 2026-07-18
no: 4815
category: 一、去 AI 味 / Humanizer 库
repo: MachineLearning-Nerd/textguard-eval
stars: 0
url: https://github.com/machinelearning-nerd/textguard-eval
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# MachineLearning-Nerd/textguard-eval

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/machinelearning-nerd/textguard-eval
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Anti-gaming evaluator that ranks AI-text-detector miners against clean ground truth — Telegraph Protocol hackathon (Track 2).
- **本地描述**：Anti-gaming evaluator that ranks AI-text-detector miners against clean ground truth — Telegraph Protocol hackathon (Track 2).
- **拉取时间**：2026-07-25 17:55:22

---

# textguard-eval

A scoring script for the Telegraph hackathon (Track 2). It takes a bunch of miners
that claim they can spot AI-generated text and figures out which ones are actually
any good.

The catch with these detection tasks is that it's easy to look good on a benchmark
and still be useless. A miner can memorize the test set, always guess "AI" because
the set happens to be AI-heavy, or ace plain ChatGPT output and fall apart the moment
someone runs it through a paraphraser. So most of the work here isn't the scoring
math, it's making the scoring hard to cheat.

## Why bother building the evaluator instead of a detector

Honestly, because it's the less crowded problem. Everyone and their dog is going to
submit a detector miner. Way fewer people want to sit down and build the thing that
grades them fairly. And a bad grader poisons the whole subnet's incentives, so it's
the part that actually matters. Detection is also a moving target (detectors vs
"humanizers" forever), which is a headache if you're the detector but kind of perfect
if you're the one measuring how well detectors hold up.

## What it scores

Nothing fancy, four things:

- **Accuracy** — plain AUC / F1, but on a set mixed across several LLM families, not
  just one model vs Wikipedia. That "vs Wikipedia" version is too easy and hides who's
  actually good.
- **Holding up under evasion** — same detectors, re-run on paraphrased / humanized /
  lightly-edited AI text. This is the one I care about most. A detector that's steady
  here should beat one that's brilliant on raw output and brittle everywhere else.
- **Calibration** — are the confidence numbers honest? Brier score + reliability
  curves. Punishes the ones that scream 0.99 on every guess.
- **Gaming checks** — canaries the miner never sees coming, duplicate/copycat
  detection, catching the "always predict the majority class" trick, distribution-shift
  probes.

Everything gets weighted into one number per miner, plus a breakdown so you can see
*why* it landed where it did.

## How the pieces fit

```
DatasetBuilder  ->  eval set (+ some secret canary samples)
                        |
MinerAdapter  <------related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---+   detect(text) -> {label, confidence}
   |   mock for now, real Telegraph API once the spec drops
   v
predictions  ->  ScoringEngine  +  AntiGamingBattery  ->  ranking  ->  report
```

The `MinerAdapter` bit matters. The real Telegraph submission spec isn't out until
Aug 17, so I'm hiding it behind one small interface and building everything against
fake miners in the meantime. When the spec lands I swap that one file and the rest
shouldn't care.

## Status

Early. Right now it's a README and a plan. The design's in `docs/` (soon). Building the
offline version first, wiring to the real network after that.

## Stack

Python, scikit-learn for the metrics, pandas, pydantic to validate miner responses so a
malformed reply gets penalized instead of crashing the run. No GPU needed — it makes its
own labeled data (real human text + text I generate from a few models), so there's
nothing external to depend on.

## License

MIT
