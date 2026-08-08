---
id: tool-07198
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: ao3-fic-recommendation
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/cosqf/ao3-fic-recommendation
created: 2026-07-18
updated: 2026-07-18
no: 7198
category: 画龙补充 / 扩容入库 — 补充源
repo: cosqf/ao3-fic-recommendation
stars: 6
url: https://github.com/cosqf/ao3-fic-recommendation
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls: []
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 8635a5e7ef0faf17
  - methods/QUICK_START.md
---

# cosqf/ao3-fic-recommendation

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/cosqf/ao3-fic-recommendation
- **Stars**：6
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：An AO3 scrapper that logs in, reads your history, and recommends a fanfic.
- **本地描述**：ao3-fic-recommendation
- **拉取时间**：2026-07-25 19:13:52

related:
  - methods/QUICK_START.md
---

# ao3-fic-recommendation
A web scrapper that processes your Archive of Our Own (AO3) reading history, provides reading statistics, and recommends fanfiction based on a user-specified ship.

**Login to AO3 is required for history access.**

## Features

* **Reading History Analysis:** Generates statistics from your AO3 reading history.
* **Personalized Fanfic Recommendations:** Suggests new, unread fanfics based on your historical reading patterns.

## How it Works

The project constructs a user profile from your AO3 reading history. This profile incorporates features derived from:

* **Content Descriptors:** Descriptors such as fandoms, ships and tags are converted into numerical vectors using **TF-IDF**.
* **Numerical Attributes:** Fanfic word counts are normalized using **MinMaxScaler**.
* **Engagement Metrics:** Recency of historical reading activity and bookmark status are applied as weights. Bookmarked works and works read more recently contribute a higher weight to the user profile.

For generating recommendations based on a user-provided ship:
1.  New, unread fanfics relevant to the specified ship are collected from AO3.
2.  A recommendation score for each unread fanfic is calculated.
3.  Fanfics are ranked by their recommendation score, and the top-scoring items are presented.

## How to Run

### Using Google Collab
Access and run the project online via this [link](https://colab.research.google.com/drive/1fIdHS0ceLlHEKqSwpPvVoWh7-quhbq3x).

### Locally
1.  Clone the repository: `git clone https://github.com/cosqf/ao3-fic-recommendation`
2.  Set up a virtual environment (recommended): `python -m venv venv`
    * On Windows: `.\venv\Scripts\activate`
    * On macOS/Linux: `source venv/bin/activate`
4.  Install dependencies:  
    `pip install -r requirements.txt`  
    `playwright install`
5.  Run the application:
    `python main.py`

