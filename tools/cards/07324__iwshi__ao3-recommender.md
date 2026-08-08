---
id: tool-07324
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: ao3-recommender
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/iwshi/ao3-recommender
created: 2026-07-18
updated: 2026-07-18
no: 7324
category: 画龙补充 / 扩容入库 — 补充源
repo: iwshi/ao3-recommender
stars: 2
url: https://github.com/iwshi/ao3-recommender
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 02a4cfdc2778999b
  - methods/QUICK_START.md
---

# iwshi/ao3-recommender

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/iwshi/ao3-recommender
- **Stars**：2
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Given a link to a work on AO3, recommends a list of similar works
- **本地描述**：ao3-recommender
- **拉取时间**：2026-07-25 19:17:52

related:
  - methods/QUICK_START.md
---

# Archive Of Our Own (AO3) Work Recommender

To use this program, download the Python file and run it in your terminal. This program utilizes the Beautiful Soup package to parse AO3's HTML.

Given a link to a work on on the fanfiction-sharing website Archive Of Our Own (AO3), this program outputs a list of similar works on AO3. 
All works on AO3 are marked by tags that convey different types of information about the work in question. This program generates recommendations based on
seven types of tags:
- **Rating:** The work's content rating (e.g. Teen and Up)
- **Archive warning:** Warns readers about any one of several Archive-wide warning subjects (e.g. major character death)
- **Category:** The type of relationships featured prominently in the work (e.g. male/male relationships)
- **Fandom:** The name of the fandom that the work is part of
- **Relationship:** The specific relationships featured prominently in the work
- **Character:** The specific characters featured prominently in the work
- **Freeform:** Any additional information the author wants to share; completely user-generated

This program uses several different strategies in order to generate a list of varied recommendations. These strategies include:
- Looking through other works by the original author(s)
- Looking through works bookmarked (i.e. favorited) by the original author(s)
- Looking through works bookmarked by users who also bookmarked the original work
- Looking through the Archive as a whole, taking advantage of the Archive's ability to filter by work tags

Generally speaking, the fandom tag has priority when it comes to generating recommendations. This is so we don't recommend works from a completely
different fandom that the reader may know nothing about. The relationship tag is also of great importance. Many readers of fanfiction are heavily invested
in specific relationships and may even go so far as to totally reject other relationships involving the same characters. As such, we must ensure, as
much as possible, that our recommended works have the same relationship(s) as the original work.

This program also takes advantage of the fact that, for freeform tags, the latter tags tend to be less important than the first few. That is to say, the
first few tags may give you information like "Enemies to Lovers" or "Angst With a Happy Ending" while later tags tend to contain comments from the author
that serve more of a humorous purpose than an informative one. Because of this, it is more important to find other works with the first few tags matching 
the original work's instead of the later tags.

*Code not maintained since July 2022.*
