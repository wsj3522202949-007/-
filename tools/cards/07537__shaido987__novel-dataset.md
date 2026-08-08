---
id: tool-07537
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 本地写作]
title: novel-dataset
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/shaido987/novel-dataset
created: 2026-07-18
updated: 2026-07-18
no: 7537
category: 画龙补充 / 扩容入库 — 补充源
repo: shaido987/novel-dataset
stars: 59
url: https://github.com/shaido987/novel-dataset
tier: "A"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: ff59d5b001697ec1
  - methods/QUICK_START.md
---

# shaido987/novel-dataset

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/shaido987/novel-dataset
- **Stars**：59
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：dataset, dataset-generation, hacktoberfest, novels, novelupdates, translated-novels
- **GitHub 描述**：Dataset with 10k+ novels.
- **本地描述**：novel-dataset
- **拉取时间**：2026-07-25 19:24:57

---

<p align="center">
  <img
    src="https://github.com/shaido987/novel-dataset/blob/master/assets/graph.png"
    alt="Graph illustration of the novels">
</p>

related:
  - methods/QUICK_START.md
---

Creates a dataset from novelupdates (https://www.novelupdates.com) containing information about translated novels.
The dataset contains translated English novels from eight original languages (Chinese, Japanese, Korean, Malaysian, Filipino, Indonesian, Khmer, and Thai). There is currently a total of **24,639** novels.  

Both individual novel statistics such as the number of chapters and ranking as well as relations to other novels are available.

Current Version: 0.1.5  
Updated on 2025-08-21


Dataset columns:
* General Information
  * Novel ID
  * Name
  * Novel Type
  * Cover Image URL
  * Associated Names
  * Original Langauge	
  * Author / Authors
  * Genres
  * Tags
* Publishing Information
  * Start Year
  * Licensed
  * Original Publisher
  * English Publisher
* Chapter Information
  * Number of Chapters (original language)
  * Completed (original language)
  * Number of Chapters (translation)
  * Completed (translation)
* Release Information (translation)
  * Release Frequency
  * Activity Weekly Rank
  * Activity Monthly Rank
  * Activity All-time Rank
* Community Information (translation)
  * On Number of Reading Lists
  * Reading List Monthly Rank
  * Reading List All-time Rank
  * Rating
  * Rating Votes
* Related Series Information
  * Related Series IDs
  * Recommended Series IDs
  * Recommendation List IDs
