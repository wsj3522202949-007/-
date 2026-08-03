---
id: tool-05265
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 大纲规划, 本地写作]
title: entropy-based-text-detector
summary: 搭大纲/分卷/节拍
source: https://github.com/davin11/entropy-based-text-detector
created: 2026-07-18
updated: 2026-07-18
no: 5265
category: 一、去 AI 味 / Humanizer 库
repo: davin11/entropy-based-text-detector
stars: 14
url: https://github.com/davin11/entropy-based-text-detector
tier: "B"
use_case: "搭大纲/分卷/节拍"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# davin11/entropy-based-text-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/davin11/entropy-based-text-detector
- **Stars**：14
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：My solution for the ''LLM - Detect AI Generated Text'' kaggle competition
- **本地描述**：My solution for the ''LLM - Detect AI Generated Text'' kaggle competition
- **拉取时间**：2026-07-25 18:12:10

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

Hi!

Below you can find a outline of how to reproduce my solution for the ''LLM - Detect AI Generated Text'' competition.
If you run into any trouble with the setup/code or have any questions please contact me at davide.cozzolino@unina.it

# ARCHIVE CONTENTS
- train.py   : code to train the one-class svm.
- predict.py : code to generate predictions.
- LICENSE    : license.

# HARDWARE:
- Ubuntu 24GB
- NVIDIA Tesla P100

# SOFTWARE
- Python 3.10
- nvidia drivers 535
- CUDA 12.2
- python packages are detailed in `requirements.txt`

# CODE
Download the files of competition `train_essays.csv` and `test_essays.csv` in this folder.

Run this script for training:
```
python train.py train_essays.csv
```

Run this script to generate predictions:
```
python predict.py test_essays.csv
```

