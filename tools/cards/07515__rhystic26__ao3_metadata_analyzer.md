---
id: tool-07515
type: tool
area: 库
status: active
tags: [Java, 协议未明, 本地优先, 英文文档, 本地写作]
title: ao3_metadata_analyzer
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/rhystic26/ao3_metadata_analyzer
created: 2026-07-18
updated: 2026-07-18
no: 7515
category: 画龙补充 / 扩容入库 — 补充源
repo: rhystic26/ao3_metadata_analyzer
stars: 0
url: https://github.com/rhystic26/ao3_metadata_analyzer
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 261716620674f7b1
  - methods/QUICK_START.md
---

# rhystic26/ao3_metadata_analyzer

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/rhystic26/ao3_metadata_analyzer
- **Stars**：0
- **语言**：Java
- **License**：None
- **Topics**：—
- **GitHub 描述**：A program to analyze tag density and fanfiction metadata from Archive of Our Own.
- **本地描述**：ao3_metadata_analyzer
- **拉取时间**：2026-07-25 19:24:15

related:
  - methods/QUICK_START.md
---

# AO3 Metadata Analyzer
A program to analyze tag density and fanfiction metadata from Archive of Our Own. Made by Rhystic26 and jan-Pansoki.

## Overview
This package is a command-line tool that can perform analysis on CSV files of Archive of Our Own (Ao3) metadata. The package comes bundled with a starter dataset (every General Audiences-rated fanfiction under the 'Chess' tag), but if you want to create your own dataset check out this fantastic project by radiolarian: https://github.com/radiolarian/AO3Scraper.

## Requirements
- OpenJDK Runtime Environment Corretto-11.0.23 or later

## Installation
1. `git clone` the repository to your machine.
2. Open a terminal and `cd` to the repository.
3. `mkdir bin`
4. `javac -d bin Ao3Analyzer/*.java`
5. (Optional) To use a custom dataset, rename it to 'fanfics.csv' and put it in the root folder of the repository (erasing the starter dataset).


## Usage
To use the program, run `java -cp bin Ao3Analyzer.FicFunctions` from the repository's root folder.

## Commands
The following commands can be run from within the program:

[1] - Get metadata for a specific fic - given a fanfiction ID number, this returns the work's name, author(s), views, and tags.

[2] - Get metadata for a specific tag - given a tag, this returns the number of fics with that tag and the most popular fic from that tag in the dataset.

[3] - Get most popular fics for a specific tag - given a tag and a number `n`, this returns the n most popular works for that tag in the dataset.

[4] - Get most popular tags for this data - given a number `n`, this returns the n most popular fics in the dataset.

[5] - Delete all fics with a specific tag - given a tag, this deletes all fics containing that tag from the **active** dataset (it will not delete them from the CSV file - this is useful if you want to see the effects of large-scale changes to the dataset without permanently altering your data).
