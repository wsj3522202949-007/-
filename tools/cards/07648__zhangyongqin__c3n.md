---
id: tool-07648
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: c3n
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/zhangyongqin/c3n
created: 2026-07-18
updated: 2026-07-18
no: 7648
category: 画龙补充 / 扩容入库 — 补充源
repo: zhangyongqin/c3n
stars: 5
url: https://github.com/zhangyongqin/c3n
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 109bd7094b25e42e
  - methods/QUICK_START.md
---

# zhangyongqin/c3n

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/zhangyongqin/c3n
- **Stars**：5
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：C3N：Content-Constrained Convolutional Network for Mural Image Completion
- **本地描述**：c3n
- **拉取时间**：2026-07-25 19:28:49

related:
  - methods/QUICK_START.md
---

# C3N：Content-Constrained Convolutional Network for Mural Image Completion

### [Paper](https://link.springer.com/article/10.1007/s00521-022-07806-0)

## Requirements
numpy==1.14.4

Pillow==5.1.0

six==1.11.0

tensorboardX==1.2

torch==0.4.1

torchvision==0.2.1

tqdm==4.23.4

## Preparation works
To generate binary masks, use
```
python generate_data.py
```

To generate the image covered by the mask, that is, generate the simulated damaged image, use
```
python 1test.py
```

## Training and testing
To conduct network model training, use
```
python train.py
```
The image data set and mask data set can be simply modified at the beginning of the code as required.

To generate a repair image, use
```
python 2test.py
```

## Citation

If you find our code or paper useful, please cite the paper:
```bash
@article{PengWZ23,
title = {C3N: Content-constrained convolutional network for mural image completion},
author = {Xianlin Peng, Huayu Zhao, Xiaoyu Wang, Yongqin Zhang, Zhan Li, Qunxi Zhang, Jun Wang, Jinye Peng, Haida Liang},
journal = {Neural Computing and Applications},
volume = {35},
article id = {},
pages = {1959-1970},
year={2023}
}
```
