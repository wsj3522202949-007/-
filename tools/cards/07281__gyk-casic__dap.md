---
id: tool-07281
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: dap
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/gyk-casic/dap
created: 2026-07-18
updated: 2026-07-18
no: 7281
category: 画龙补充 / 扩容入库 — 补充源
repo: gyk-casic/dap
stars: 0
url: https://github.com/gyk-casic/dap
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/QUICK_START.md
---

# gyk-casic/dap

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/gyk-casic/dap
- **Stars**：0
- **语言**：Python
- **License**：Apache-2.0
- **Topics**：—
- **GitHub 描述**：Official resources of "DAP: Enhancing AI-generated Text Detection via Dynamic Adversarial Paraphrasing"
- **本地描述**：dap
- **拉取时间**：2026-07-25 19:16:31

---

# DAP
Code of "Dynamic Adversarial Paraphrasing via Multi-Objective Fusion for Robust AI-Generated Text Detection"

> **DAP** is a co‑evolving framework that alternately improves a *detector* and a *generator* so that the detector becomes robust against dynamically generated adversarial paraphrasings.

---

## 1  Environment
```bash
pip install -r requirements.txt     # install all dependencies (tested with Python 3.11 & CUDA 12.0)
```

---

## 2  Datasets
Our datasets are in the following directories:
```
dataset/tweepfake   # TweepFake
dataset/roc         # ROCStories
```
Each folder should contain:
```
train_warmup.json     # 10% subset to warm‑up the detector
train_rl.json         # 90% subset for adversarial training
test.json             
```

---

## 3  Pipeline (one dataset at a time)

### 3.1  Detector warm‑up
```bash
python 01_train_original.py                       # trains on train_warmup.json
```

### 3.2  Adversarial round *t* (repeat as needed)
1. **Generate paraphrased AI-generated text + Fine-grained Scoring**
   ```bash
   python scripts/00_generation_and_scoring.py
   ```
2. **Fine‑tune detector** on original and selected paraphrases
   ```bash
   python scripts/01_train_original.py            # original AI-generated text
   python scripts/02_train_paraphrase.py          # paraphrased AI-generated text
   ```
3. **DPO training for generator** (LoRA)
   ```bash
   cd scripts/03_LLaMA-Factory
   llamafactory-cli train training_args.yaml
   cd -
   ```

### 3.3  Evaluation
```bash
python scripts/04_inference.py                    # reports AUROC / Accuracy (FPR 1%) on test.json
```

---

## 4  Acknowledgments and Citations
This project borrows or uses code from the following project, for which we are grateful:

- [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) - Implements Direct Preference Optimization (DPO).
- [Tweepfake](https://github.com/tizfa/tweepfake_deepfake_text_detection) - Used for constructing training and testing data.
- [ROCStories](http://cs.rochester.edu/nlp/rocstories) - Used for constructing training and testing data.

related:
  - methods/QUICK_START.md
---

## 5  Citation
```bibtex
  @article    {dap2026,
  title     = {Dynamic Adversarial Paraphrasing via Multi-Objective Fusion for Robust AI-Generated Text Detection},
  year      = {2026}
}
```

Licensed under the Apache 2.0 license.
