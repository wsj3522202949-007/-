---
id: tool-04993
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: voight-kampff-clef2026
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/dcondrey/voight-kampff-clef2026
created: 2026-07-18
updated: 2026-07-18
no: 4993
category: 一、去 AI 味 / Humanizer 库
repo: dcondrey/voight-kampff-clef2026
stars: 0
url: https://github.com/dcondrey/voight-kampff-clef2026
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 77d6547186cd1a35
  - methods/改稿润色指令库.md
---

# dcondrey/voight-kampff-clef2026

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/dcondrey/voight-kampff-clef2026
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：ai-generated-text-detection, clef2026, deberta, ensemble, lightgbm, nlp, pan-clef, stylometry
- **GitHub 描述**：PAN@CLEF 2026 Voight-Kampff AI-generated text detector: calibrated DeBERTa + LightGBM + SVM ensemble over 44 domain-portable features (0.891 ROC-AUC).
- **本地描述**：PAN@CLEF 2026 Voight-Kampff AI-generated text detector: calibrated DeBERTa + LightGBM + SVM ensemble over 44 domain-portable features (0.891 ROC-AUC).
- **拉取时间**：2026-07-25 18:02:13

---

# Voight-Kampff: Cross-Genre AI-Generated Text Detection (PAN@CLEF 2026)

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PAN@CLEF 2026](https://img.shields.io/badge/PAN%40CLEF-2026-green.svg)](https://pan.webis.de/clef26/pan26-web/generated-content-analysis.html)

Team `writerslogic-inc` submission to the **PAN@CLEF 2026 Voight-Kampff Generative AI Detection** task — a calibrated ensemble that classifies text as human- or AI-written across genres (essays, news, fiction), emitting a probability in `[0, 1]`.

## Official Result

On the PAN 2026 test set, our best configuration (`large-rank`) scored:

| Metric | Score |
|---|---|
| ROC-AUC | **0.891** |
| C@1 | 0.853 |
| F1 | 0.902 |
| F0.5u | 0.899 |
| **Mean (ranking metric)** | **0.887 — rank 7** |

On the PAN 2025 backward-compatibility test set the same configuration scored **0.979**. We submitted 11 software configurations to TIRA; they share the same trained base models and differ only in ensemble composition (which classifiers are included, stacker vs. weighted-average fusion, isotonic calibration on/off, LightGBM seed-bag size, and the abstention margin).

## Approach

A calibrated ensemble of three complementary classifiers combined by learned stacking:

- **DeBERTa-v2** — fine-tuned, exported to ONNX with INT8 dynamic quantization for CPU inference.
- **Multi-seed LightGBM** — over 44 domain-portable stylometric features, concatenated with truncated-SVD projections of character (3–6) and word (1–2) n-gram TF-IDF, plus GPT-2 perplexity features.
- **Calibrated linear SVM** — Platt-scaled, over raw sparse character/word n-gram TF-IDF.

Component probabilities are combined via a logistic-regression stacker with interaction features (max, min, std, range), followed by isotonic-regression calibration; borderline predictions within a narrow margin of 0.5 abstain.

The 44 features are deliberately **domain-portable**. That choice came from our companion Reasoning Trajectory Detection analysis, where generator- and topic-specific features died under domain shift (0% fire rate out-of-domain) while vocabulary fingerprints and compression measures survived — so every feature here was selected for support overlap across genres, not for training-set effect size.

### Feature groups (44)

| Group | Count | Examples |
|---|---|related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| Document structure | 7 | word/char/sentence/paragraph counts |
| Vocabulary richness | 8 | type-token ratio, hapax ratio, Yule's K, Heaps' exponent, MATTR |
| Sentence structure | 6 | mean length, length CV, sentence-start diversity |
| Readability | 4 | Flesch-Kincaid, Coleman-Liau, avg. syllables |
| Compression/entropy | 4 | zlib ratio, char entropy, repetition ratio |
| Style markers | 9 | punctuation ratio, quote density, contraction ratio |
| Discourse | 4 | transition diversity, connective formality |
| Distributional | 2 | burstiness, intrinsic dimensionality |
| Perplexity (GPT-2) | 4 | log-perplexity, burstiness, rank-1 accuracy, binoculars ratio |

## Quick Start

```bash
pip install -e .
python download_onnx.py            # fetch/convert the quantized DeBERTa ONNX model
python train.py                    # train LightGBM + SVM, fit the stacker + calibrator
python calibrate_ensemble.py       # isotonic calibration of the fused score
python main.py -i input/ -o output/  # predict (writes probabilities)
```

Docker (TIRA):

```bash
docker build -t voight-kampff-clef2026 .
docker run --rm -v /input:/input -v /output:/output voight-kampff-clef2026 -i /input -o /output
```

## Repository Structure

```
features.py             # the 44 domain-portable features + GPT-2 perplexity
train.py                # LightGBM (multi-seed) + SVM training
train_transformer.py    # DeBERTa-v2 fine-tuning
calibrate_ensemble.py   # learned stacking + isotonic calibration
download_onnx.py        # DeBERTa -> ONNX INT8 export
augment.py              # training-data augmentation
main.py                 # inference entrypoint
models/                 # trained base models, stacker, calibrator, vk_config.json
Dockerfile              # CPU/ONNX containerized inference
```

## Citation

```bibtex
@inproceedings{condrey2026pan,
  title     = {Writerslogic at {PAN} 2026: Process over Content for Robust
               Detection under Domain Shift},
  author    = {Condrey, David},
  booktitle = {Working Notes of CLEF 2026 -- Conference and Labs of the Evaluation Forum},
  series    = {CEUR Workshop Proceedings},
  year      = {2026},
  publisher = {CEUR-WS.org},
  note      = {Voight-Kampff is one of three PAN tasks in this paper; to appear}
}
```
