---
id: tool-00429
type: tool
area: 库
status: active
tags: [文风迁移, Python, 协议宽松, 本地优先, 英文文档, 大纲规划, 改稿润色, 本地写作]
title: LongLM-Eyas
summary: 搭大纲/分卷/节拍
source: https://github.com/indexfziq/longlm-eyas
created: 2026-07-18
updated: 2026-07-18
no: 429
category: 二、网文 / 长篇 AI 写作系统 库
repo: IndexFziQ/LongLM-Eyas
stars: 4
url: https://github.com/indexfziq/longlm-eyas
tier: "B"
use_case: "搭大纲/分卷/节拍"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# IndexFziQ/LongLM-Eyas

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/indexfziq/longlm-eyas
- **Stars**：4
- **语言**：Python
- **License**：Apache-2.0
- **Topics**：chinese-nlp, long-texts, narrative, nlp, sentence-ordering, story, storytelling, t5
- **GitHub 描述**：Implement of IIE-NLP-Eyas@OutGen: Chinese Outline-guided Story Generation via a Progressive Plot-Event-Story Framework
- **本地描述**：Implement of IIE-NLP-Eyas@OutGen: Chinese Outline-guided Story Generation via a Progressive Plot-Event-Story Framework
- **拉取时间**：2026-07-23 22:51:36

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# LongLM-Eyas

**IIE-NLP-Eyas@OutGen: Chinese Outline-guided Story Generation via a Progressive Plot-Event-Story Framework** [[PDF]()]

**Team Members:** *Yuqiang Xie, Yunpeng Li, Wei Peng, Ping Guo and Luxi Xing.* 

**Org.:** Institute of Information Engineering, Chinese Academy of Sciences, Beijing, China.

**Codes are contributed by:**
- Yuqiang Xie (Baselines, Data Pre-processing, Event Generation)
- Yunpeng Li (Event Ranking)
- Wei Peng (LCS).

## Plot-Event-Story (PES)

**Outline:**
- Plot (Step 1-2)
- Event (Step 3-4)
- Story (Step 5-8)

### A Simple Guide:

#### Step 1:

convert train/val/test.jsonl into events of each plot

`python ./tools/split_kw_sent.py`

-> train/val/test_split.jsonl

#### Step 2:

convert train/val/test_split.jsonl into bart format (source and target)

`python ./tools/convert_bartio.py`

-> train/val/test.source/target

#### Step 3:

Train/Eval/Test using LongLM-small model

`bash ./longlm/finetune_deepspeed_iie.sh`

The best model will be in ./save_model

#### Step 4:

Generating stories by Top-p sampling:

`python ./baselines/generation/gen.py`

-> result_of_val/test.txt

#### Step 5:

convert each event into one line with ‘/t’ splitting

`python ./tools/event2data.py`

-> result4rank_of_val/test.txt

#### Step 6:

perform ranking

`python ./tools/outline_reranking.py`

-> train/val_reranking.jsonl

`python ./tools/process_nsp_data.py`

-> train/val_nsp.txt

`python ./tools/story_nsp.py`

-> rerank_test.txt


#### Step 7:

del repetitive words

`python ./tools/data4lcs.py`

-> result4lcs.txt

`python ./tools/lrc.py`

-> final_result.txt


#### Step 8:

`python ./tools/source2jsonl.py`

-> submission.jsonl


### Parameters for Baselines and Event Generation:

```
learning rate: 3e-5
epoch: {5, 10}
top-k: K=40
K's temperature: 0.9
batch size: 8
```
 
## Acknowledgement

Thanks for the baseline model [LongLM](https://github.com/thu-coai/LOT-Benchmark).


