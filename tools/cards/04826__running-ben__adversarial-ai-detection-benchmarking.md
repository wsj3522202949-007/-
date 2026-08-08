---
id: tool-04826
type: tool
area: 库
status: active
tags: [去AI味, Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: adversarial-ai-detection-benchmarking
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/running-ben/adversarial-ai-detection-benchmarking
created: 2026-07-18
updated: 2026-07-18
no: 4826
category: 一、去 AI 味 / Humanizer 库
repo: running-ben/adversarial-ai-detection-benchmarking
stars: 0
url: https://github.com/running-ben/adversarial-ai-detection-benchmarking
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: cf795f6214699fcb
  - methods/改稿润色指令库.md
---

# running-ben/adversarial-ai-detection-benchmarking

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/running-ben/adversarial-ai-detection-benchmarking
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Benchmarking adversarial robustness of AI text detectors (RoBERTa, GPTZero, Binoculars) against four-layer attacks
- **本地描述**：Benchmarking adversarial robustness of AI text detectors (RoBERTa, GPTZero, Binoculars) against four-layer attacks
- **拉取时间**：2026-07-25 17:55:49

---

﻿# Benchmarking Trustworthy AI Detection on Multilingual Text

 Benchmarking adversarial robustness of AI-generated text detectors (RoBERTa, GPTZero, Binoculars) against four-layer attacks (character / word / sentence / LLM paraphrase) on Chinese text.

## Key Findings

| Attack | RoBERTa | GPTZero | Binoculars |
|--------|:-------:|:-------:|:----------:|
| Character | <2% ASR | 19–41% ASR | **47–63% ASR**  |
| Word | <2% ASR | 13–25% ASR | 13–33% ASR |
| Sentence | <2% ASR | 5–10% ASR | 22–30% ASR |
| LLM | **51–100% ASR**  | 53–66% ASR | 16–26% ASR |

- **RoBERTa**: immune to surface attacks but fully collapses under LLM paraphrase
- **Binoculars**: vulnerable to character-level perturbation but relatively robust against LLM rewrites
- **Complementary weaknesses** suggest ensemble detection as a practical defense

## Defenses Explored

| Strategy | Char | Word | Sentence | LLM |
|----------|:----:|:----:|:--------:|:related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---:|
| Input sanitization (ZWC) | -23% ASR | — | — | — |
| Confidence shift monitor | 75.6% alert | 32.6% | 55.0% | 37.8% |
| SDP semantic consistency | **ASR 0.9%** | **ASR 1.9%** | **ASR 2.7%** | ASR 14.4% |

## Structure

```
attacks/       — 4-layer attack scripts (char/word/sentence/llm) + evaluator
detectors/     — RoBERTa, GPTZero, Binoculars detection modules
paper_figures/ — Visualization plots (ASR heatmap, radar, bar charts)
```

## Papers

- `Benchmarking_Trustworthy_AI_Detection_on_Multilingual_Text.pdf`
- `adversarial_detection_paper_v2.docx` (with confidence shift analysis)
- See `defense_experiments/` for supplementary results

## Citation

```bibtex
@article{zhou2026benchmarking,
  title={Benchmarking Trustworthy AI Detection on Multilingual Text},
  author={Zhou, Zhenglin},
  year={2026}
}
```
