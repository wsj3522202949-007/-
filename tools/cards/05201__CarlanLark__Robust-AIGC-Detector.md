---
id: tool-05201
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: Robust-AIGC-Detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/carlanlark/robust-aigc-detector
created: 2026-07-18
updated: 2026-07-18
no: 5201
category: 一、去 AI 味 / Humanizer 库
repo: CarlanLark/Robust-AIGC-Detector
stars: 33
url: https://github.com/carlanlark/robust-aigc-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 32cb2e144fdedee5
  - methods/改稿润色指令库.md
---

# CarlanLark/Robust-AIGC-Detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/carlanlark/robust-aigc-detector
- **Stars**：33
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Code for ACL 2024 long paper: Are AI-Generated Text Detectors Robust to Adversarial Perturbations?
- **本地描述**：Code for ACL 2024 long paper: Are AI-Generated Text Detectors Robust to Adversarial Perturbations?
- **拉取时间**：2026-07-25 18:09:50

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Robust-AIGC-Detector

Code for ACL 2024 long paper: Are AI-Generated Text Detectors Robust to Adversarial Perturbations?

### Environments

```bash
torch==1.11.0
transformers==4.30.2
textattack==0.3.9 
tensorflow==2.9.1 
tensorflow_hub==0.15.0
```


### Data Preparation

```bash
unzip data_in.zip
mkdir data_out
```

### Training
```bash
$ bash train.sh
```

### Checkpoints
The checkpoints of in-domain detector, cross-domain detector, and cross-genre detector can be found in <https://huggingface.co/CarlanLark/AIGT-detector-in-domain>. (These detectors are trained on the same training set and evaluated on different test sets.)

The checkpoint of mixed-source detector can be found in <https://huggingface.co/CarlanLark/AIGT-detector-mixed-source>.

### Robustness Evaluation
```bash
$ bash attack.sh
```

### Citation
If you find our work useful to your research, you can cite the paper below:
```bash
@article{huang2024ai,
  title={Are AI-Generated Text Detectors Robust to Adversarial Perturbations?},
  author={Huang, Guanhua and Zhang, Yuchen and Li, Zhe and You, Yongjian and Wang, Mingze and Yang, Zhouwang},
  journal={arXiv preprint arXiv:2406.01179},
  year={2024}
}
```
