---
id: tool-07207
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: lrdiff
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/czy-code/lrdiff
created: 2026-07-18
updated: 2026-07-18
no: 7207
category: 画龙补充 / 扩容入库 — 补充源
repo: czy-code/lrdiff
stars: 6
url: https://github.com/czy-code/lrdiff
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls: []
related:
  - methods/QUICK_START.md
---

# czy-code/lrdiff

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/czy-code/lrdiff
- **Stars**：6
- **语言**：Python
- **License**：Apache-2.0
- **Topics**：—
- **GitHub 描述**：Low-rank Structure Guided Diffusion for Shaanxi Temple Mural Restoration.
- **本地描述**：lrdiff
- **拉取时间**：2026-07-25 19:14:09

related:
  - methods/QUICK_START.md
---

# Low-rank Structure Guided Diffusion for Shaanxi Temple Mural Restoration

## Installation

1. Download source code and dataset:
    
    * `git clone https://github.com/CZY-Code/LRDiff.git`
    * Download the dataset of from the [link](https://drive.google.com/file/d/1Twzrkkb9jEInpsrdrabB6RAcHagwZCVP/view?usp=drive_link)
   

3.  Pip install dependencies:
    * OS: Ubuntu 20.04.6
    * nvidia :
        - cuda: 12.1
        - cudnn: 8.5.0
    * python == 3.9.18
    * pytorch >= 2.1.0
    * Python packages: `pip install -r requirements.txt`

4.  Dataset Preparation:

    * You can set the mask/LQ/GT path in [tdm/options/test/ir-sde-td.yml](https://github.com/CZY-Code/LRDiff/blob/a950d090ff1ce918910198205630b24207eb28eb/tdm/options/test/ir-sde-td.yml#L25)

5. Download the weight of network from the [link](https://drive.google.com/file/d/1cdDZu_F752hmG-fNR1XWxDt4uUJpcUZR/view?usp=drive_link) and move it into the path which setted in [tdm/options/test/ir-sde-td.yml](https://github.com/CZY-Code/LRDiff/blob/530432b32b39e26db4c9c8f18ccf845f0ffd57eb/tdm/options/test/ir-sde-td.yml#L52)

6. Run the following command to test performance:

    `python tdm/test.py`
    
## Acknowledgement
This implementation is based on / inspired by:

* [https://github.com/Algolzw/image-restoration-sde](https://github.com/Algolzw/image-restoration-sde) (Image Restoration SDE)
* [https://github.com/andreas128/RePaint](https://github.com/andreas128/RePaint) (RePaint)
* [https://github.com/htyjers/StrDiffusion](https://github.com/htyjers/StrDiffusion) (StrDiffusion)
