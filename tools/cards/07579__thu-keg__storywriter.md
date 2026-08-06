---
id: tool-07579
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: storywriter
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/thu-keg/storywriter
created: 2026-07-18
updated: 2026-07-18
no: 7579
category: 画龙补充 / 扩容入库 — 补充源
repo: thu-keg/storywriter
stars: 45
url: https://github.com/thu-keg/storywriter
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# thu-keg/storywriter

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/thu-keg/storywriter
- **Stars**：45
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：storywriter
- **拉取时间**：2026-07-25 19:26:12

---

# StoryWriter

**StoryWriter** is a multi-agent framework for generating high-quality **long stories** with logical coherence and engaging plots—two major challenges that remain unsolved for most current large language models (LLMs).

---

## ✨ Highlights

Long story generation is hard due to:

1. **Discourse Coherence**
   Maintaining consistency, logic, and completeness throughout the story.

2. **Narrative Complexity**
   Crafting engaging, interwoven plots across characters and events.

To tackle these, we introduce **`StoryWriter`**, a **multi-agent story generation framework** with the following components:

* **🧠 Outline Agent**
  Produces event-based outlines rich in plots, characters, and inter-event relationships.

* **🗂️ Planning Agent**
  Breaks down the outline into chapter-wise plans, ensuring an engaging, interwoven narrative.

* **✍️ Writing Agent**
  Dynamically compresses the story history to generate coherent new content aligned with the current event.

---

## 📊 Results

We conduct both human and automatic evaluations, and **StoryWriter** significantly **outperforms** existing baselines in:
![image](https://github.com/user-attachments/assets/a23eb560-1870-4661-ad10-27d378ca470f)



---

## 📚 Dataset

We use StoryWriter to generate a large-scale long story dataset:

* **\~5,000 stories**
* **Average length: 8,000 words/story**

related:
  - methods/QUICK_START.md
---

## 📥 Get Started

* **📖 Read Sample Stories**
  Download generated stories here:
  👉 [Tsinghua huggingface Link](https://github.com/thu-keg/storywriter/blob/main/[https://cloud.tsinghua.edu.cn/f/6173850b58114951ab7e/](https://huggingface.co/datasets/THU-KEG/LongStory))

* **🛠️ Train Your Own Model**
  Use [LongWriter](https://github.com/THUDM/LongWriter/tree/main) to train on our dataset.
  Replace the original raw file with our training JSON.
