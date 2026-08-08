---
id: tool-04973
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: raid-max-v2
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/matman22/raid-max-v2
created: 2026-07-18
updated: 2026-07-18
no: 4973
category: 一、去 AI 味 / Humanizer 库
repo: Matman22/raid-max-v2
stars: 0
url: https://github.com/matman22/raid-max-v2
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 185198fcfd9df6ac
  - methods/改稿润色指令库.md
---

# Matman22/raid-max-v2

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/matman22/raid-max-v2
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：v2 AI-text detector engineered to maximize RAID benchmark score (supervised + adversarial normalization). Companion to Ai-Layered-Detection-Tool.
- **本地描述**：v2 AI-text detector engineered to maximize RAID benchmark score (supervised + adversarial normalization). Companion to Ai-Layered-Detection-Tool.
- **拉取时间**：2026-07-25 18:01:28

---

# raid-max-v2 — AI-text detector engineered for the RAID leaderboard

**Goal (singular):** achieve the highest possible score on the
[RAID benchmark](https://raid-bench.xyz/leaderboard).

This is the **v2** of a larger project. v1
([Ai-Layered-Detection-Tool](https://github.com/Matman22/Ai-Layered-Detection-Tool))
was optimized for *honest generalization* — detecting AI text from sources it had
never seen. It proved that surface stylometry does **not** generalize (cross-domain
AUROC ≈ 0.52, chance) and that a zero-shot language-model signal does (≈ 0.83).

v2 has a different objective. RAID grades **accuracy at a strict 5% false-positive
rate** across 8 domains, 11 generators, and ~11 adversarial attacks — and it hands
you a labeled *training* split drawn from the same distribution as the test set.
So the winning strategy here is **on-distribution specialization**, not generality.

> **Honest framing:** a RAID-tuned model scores higher on this benchmark but
> generalizes *worse* to non-RAID text. That is the intended tradeoff of v2, and
> the reason it lives in a separate repo from the v1 generalist.

---

## Strategy (ordered by expected impact)

1. **Supervised transformer fine-tuned on RAID-train** — DeBERTa-v3 / RoBERTa.
   The single biggest lever: the model learns the exact generator + attack
   distribution it is graded on. Fits a free Colab T4 GPU.
2. **Input-normalization front-end** — strip zero-width chars, map homoglyphs back
   to Latin, collapse trick whitespace *before* the model. Cheaply defeats several
   adversarial attack types. (Ports the v1 forensic layer into an adversarial defense.)
3. **Adversarial data augmentation** — apply paraphrase / synonym / homoglyph
   attacks to training data to harden the weak slices.
4. **Ensemble with a strong zero-shot signal** (Binoculars, or Fast-DetectGPT with
   larger open base models) to hedge against under-represented generators.
5. **Per-slice threshold calibration** to hit the 5%-FPR operating point exactly.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Repo structure

```
data/          RAID train/test splits (not committed — fetched via script)
training/      fine-tuning code (train.py) + notes
detector/      the my_detector(texts) -> list[float] wrapper + normalization front-end
submission/    metadata.json template + RAID PR steps
notebooks/     Colab notebook that runs the whole pipeline on a free GPU
```

## Status

🟡 **Scaffold.** Structure and plan are in place; components are stubs with clear
TODOs. Nothing is trained or submitted yet. Build order follows the strategy list
above — start with `training/train.py` and `detector/detector.py`.

## Cost

Targets **$0**: free Colab T4 GPU for fine-tuning, HuggingFace free datasets for
RAID data, GitHub for hosting. A larger zero-shot ensemble (step 4) is the only
piece that might want Colab Pro (~$10/mo) or a HuggingFace GPU grant.
