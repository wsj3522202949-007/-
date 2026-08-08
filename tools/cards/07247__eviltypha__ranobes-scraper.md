---
id: tool-07247
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: ranobes-scraper
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/eviltypha/ranobes-scraper
created: 2026-07-18
updated: 2026-07-18
no: 7247
category: 画龙补充 / 扩容入库 — 补充源
repo: eviltypha/ranobes-scraper
stars: 24
url: https://github.com/eviltypha/ranobes-scraper
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls: []
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: f2ed6c04297ee674
  - methods/QUICK_START.md
---

# eviltypha/ranobes-scraper

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/eviltypha/ranobes-scraper
- **Stars**：24
- **语言**：Python
- **License**：MIT
- **Topics**：ebook, epub, lightnovel, python3, webnovel, webscraper, wuxiaworld
- **GitHub 描述**：Scrapes webnovels from https://ranobes.net/ and saves them in .epub format
- **本地描述**：ranobes-scraper
- **拉取时间**：2026-07-25 19:15:26

related:
  - methods/QUICK_START.md
---

# Ranobes Scraper

This Python script scrapes novels from [Ranobes](https://ranobes.net/) and saves them into .epub format with an optional conversion into .pdf format

### Features

- Regular updates
- No 'In preparation, Keguan...' for chapters
- 10,000+ novels to scrape
- Terminal based and simple to use
- Scraping progress can be monitored

### Getting Started

Install the latest version of [Python](https://www.python.org/). It may work with older versions but has not been tested.

### Prerequisites

This script depends on bs4, ebooklib, progress and pdfkit. To install these navigate to the project folder and run

```
pip install -r requirements.txt
```

### Usage

Navigate to the project folder and run

```
python main.py
```
to start the script

Now copy and paste the URL of the novel you wish to scrape from [Ranobes](https://ranobes.net/).

<img src = "images/Demo/novel_webpage.PNG" alt = "novel_webpage">


It will start extracting the chapter list.

<img src = "images/Demo/extract_index.PNG" alt = "extract_index">


After that, select the chapter range and it will start scraping the chapters.

<img src = "images/Demo/chapter_range.PNG" alt = "chapter_range">


Now save the file. The file gets saved in .epub format

<img src = "images/Demo/save_file.PNG" alt = "save_file">


Enjoy your read!


### Lithium: EPUB Reader

Personally, I prefer the [Lithium: EPUB Reader](https://play.google.com/store/apps/details?id=com.faultexception.reader) due to its simplicity and ease of use to read .epub files.

<table>
    <tr>
        <td><img src = "images/Lithium/lithium_1.png" height = 400 width = 180 alt = "lithium_1"></td>
        <td><img src = "images/Lithium/lithium_2.png" height = 400 width = 180 alt = "lithium_2"></td>
        <td><img src = "images/Lithium/lithium_3.png" height = 400 width = 180 alt = "lithium_3"></td>
        <td><img src = "images/Lithium/lithium_4.png" height = 400 width = 180 alt = "lithium_4"></td>
    </tr>
</table>

### Finally

Feel free to open an issue if you face any bugs or have any suggestions.
