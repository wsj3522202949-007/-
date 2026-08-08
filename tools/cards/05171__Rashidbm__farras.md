---
id: tool-05171
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: farras
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/rashidbm/farras
created: 2026-07-18
updated: 2026-07-18
no: 5171
category: 一、去 AI 味 / Humanizer 库
repo: Rashidbm/farras
stars: 1
url: https://github.com/rashidbm/farras
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
  - "⚠️ 仓库疑似停更/归档，bug 不会修、依赖可能过期"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: bd1988cf9792eaf0
  - methods/改稿润色指令库.md
---

# Rashidbm/farras

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/rashidbm/farras
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：فرّاس — Arabic AI Text Detector | Detecting AI-generated Arabic text with 97.27% accuracy
- **本地描述**：فرّاس — Arabic AI Text Detector （ Detecting AI-generated Arabic text with 97.27% accuracy
- **拉取时间**：2026-07-25 18:08:44

---

<div align="center">

# فرّاس — Arabic AI Text Detector

**An open-source tool for detecting AI-generated Arabic text**

[Live Demo](https://farras.app) &nbsp;|&nbsp; [Model on HuggingFace](https://huggingface.co/Rashidbm/farras-xlmr-arabic-ai-detector) &nbsp;|&nbsp; [Research Report (v1)](https://github.com/Rashidbm/farras/blob/main/v1-hybrid/Arabic_AI_Text_Detection_Report.pdf)

</div>

---

## Overview

Farras (فرّاس) is a detection system for identifying AI-generated Arabic text. The project went through two major iterations, each informed by the limitations of the previous one.

| Version | Base Model | Training Data | Accuracy | Status |
|---------|-----------|---------------|----------|--------|
| **v1** | AraBERTv2 + XGBoost + N-grams | Custom Gemini-only (12,796 samples) | 93.16% (internal), 86% (external) | Archived |
| **v2** | XLM-RoBERTa | KFUPM-JRCAI multi-generator (28,098 samples) | **97.27%** | **Deployed** |

## The Journey

### v1: Hybrid Ensemble (Dec 2025)

The first version explored whether stylistic and structural cues could outperform deep transformers for Arabic AI detection. Five approaches were compared:

- **Naive Bayes** baseline (55.7% accuracy)
- **Character N-grams** with logistic regression (87.0%)
- **Farasa morphological features** with XGBoost (81.2%)
- **AraBERTv2** fine-tuning (85.2%)
- **Hybrid ensemble** combining N-grams + linguistic features (93.2%)

Key finding: the hybrid model that combined surface-level patterns with linguistic features outperformed the deep transformer. The full analysis is in the [research report](https://github.com/Rashidbm/farras/blob/main/v1-hybrid/Arabic_AI_Text_Detection_Report.pdf).

**Limitations identified:**
- Dataset was Gemini-only — the model had never seen GPT-4, Llama, or Jais outputs
- AraBERT's aggressive Arabic normalization (diacritics removal, alef normalization) was destroying detection signals
- External evaluation dropped to 86% accuracy, confirming poor generalization

### v2: XLM-RoBERTa (Feb 2026)

Informed by the [AraGenEval 2025 shared task](https://arxiv.org/abs/2503.18234) results and the v1 limitations, the second version made three key changes:

1. **Switched to XLM-RoBERTa** — the AraGenEval findings showed `xlm-roberta-base` outperforms AraBERT for Arabic AI detection (F1=0.770 vs ~0.618)
2. **Multi-generator training data** — used KFUPM-JRCAI datasets covering 4 generators (ALLaM, Jais, Llama 3.1, GPT-4) across 2 domains (academic abstracts + social media)
3. **No Arabic normalization** — following the BUSTED team's finding that text normalization destroys stylistic cues that differentiate AI from human writing

**Results:**

| Class | Precision | Recall | F1 |
|-------|-----------|--------|-related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| Human | 0.93 | 0.94 | 0.93 |
| AI | 0.98 | 0.98 | 0.98 |
| **Overall Accuracy** | | | **97.27%** |

## Architecture

```
farras.app (Next.js on Vercel)
    ↓ API calls via @gradio/client
HuggingFace Space (Gradio backend)
    ↓ loads model at startup
HuggingFace Hub (XLM-RoBERTa weights, 1.1GB)
```

## Repository Structure

```
farras/
├── v1-hybrid/                        # First iteration (archived)
│   ├── Arabic_AI_Text_Detection_Report.pdf   # Full research report
│   ├── app.py                        # Gradio app (ensemble backend)
│   ├── hybrid_model/                 # N-gram + linguistic feature code
│   └── finetuned_model/              # AraBERTv2 fine-tuning notebook
│
├── v2-xlmr/                          # Current deployed version
│   ├── app.py                        # Gradio app (XLM-RoBERTa backend)
│   ├── train_xlmr.py                 # Training script
│   └── requirements.txt
│
└── web/                              # Landing page (Next.js)
```

## Quick Start

### Run the detector locally

```bash
cd v2-xlmr
pip install -r requirements.txt
# Download model from HuggingFace Hub
python -c "from transformers import AutoModel, AutoTokenizer; AutoTokenizer.from_pretrained('Rashidbm/farras-xlmr-arabic-ai-detector'); AutoModel.from_pretrained('Rashidbm/farras-xlmr-arabic-ai-detector')"
python app.py
```

### Train from scratch

```bash
cd v2-xlmr
python train_xlmr.py
```

Requires the KFUPM-JRCAI datasets in `Datasets/KFUPM-JRCAI/`.

## Known Limitations

- Struggles with short texts (<50 words) — training data averages 110-879 words per sample
- Optimized for Modern Standard Arabic and common dialects; may underperform on very niche dialects
- Detection accuracy may degrade as LLMs improve their Arabic generation

## Links

- **Live app**: [farras.app](https://farras.app)
- **Model weights**: [Rashidbm/farras-xlmr-arabic-ai-detector](https://huggingface.co/Rashidbm/farras-xlmr-arabic-ai-detector)
- **HF Space**: [Rashidbm/farras-ai-detector](https://huggingface.co/spaces/Rashidbm/farras-ai-detector)

## Authors

- Rashid Binkulaib
- Mohammed Alomar
- Nawaf Alwazrah

## License

MIT
