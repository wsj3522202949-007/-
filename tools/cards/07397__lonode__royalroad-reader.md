---
id: tool-07397
type: tool
area: 库
status: active
tags: [Python, 协议传染, 本地优先, 英文文档, 本地写作]
title: royalroad-reader
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/lonode/royalroad-reader
created: 2026-07-18
updated: 2026-07-18
no: 7397
category: 画龙补充 / 扩容入库 — 补充源
repo: lonode/royalroad-reader
stars: 16
url: https://github.com/lonode/royalroad-reader
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
  - "⚠️ 仓库疑似停更/归档，bug 不会修、依赖可能过期"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: e2179f33249f8044
  - methods/QUICK_START.md
---

# lonode/royalroad-reader

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/lonode/royalroad-reader
- **Stars**：16
- **语言**：Python
- **License**：GPL-3.0
- **Topics**：ebook, epub, fanfiction, python, royalroad, webfiction, webnovel
- **GitHub 描述**：Simple python script to fetch a story from royalroad.com and convert it to epub ebook format.
- **本地描述**：royalroad-reader
- **拉取时间**：2026-07-25 19:20:40

related:
  - methods/QUICK_START.md
---

# ARCHIVE NOTICE

This repository is archived and is now included in the more useful and more complete https://github.com/lonode/royalroad-fetchAndConvert 
A feature is added : Conversion and push to your selected device

# royalroad-reader
Simple python script to fetch a story/web novel from https://www.royalroad.com and convert it to epub ebook format.

# Features

* Retrieve automatically all the chapters of the given story
* Support table of content for ebook conversion
* Support author note at both end and start of the chapter
* Support images
* Support CSS rules for different stories (e.g. "Everybody Love Large Chest")
* Very low memory and performance footprint


# Libraries used

This script uses requests_html python package. https://html.python-requests.org/. Install it :  

	pip install requests

# Usage

    fetch_book.py url_of_chapter number_of_chapters name_of_ebook

Parameters :  

* url_of_chapter : The URL of the chapter (not of the story homepage!)
* number_of_chapters : You guessed. If you want the whole book, just enter something like 99999
* name_of_ebook : The name of the ebook, .html extension will be added when the file is written on the filesystem. 

It reads the chapter content of the URL given ( url_of_chapter ) and goes to the next chapter, and it loops number_of_chapters times.  
name_of_ebook is the name of the file where the HTML source will be stored.  

## Example  

If you want to fetch the best rated story Mother of Learning from the first chapter, execute the following command :

    python fetch_book.py https://www.royalroad.com/fiction/21220/mother-of-learning/chapter/301778/1-good-morning-brother 102 MOL
  
In the example above, MOL.html is written a the working directory.

*Note : this script has been primaly designed to fetch the story "Everybody Love Large Chest", so different stories could be appears wrong in the final file. In particular CSS-designed structure.*

# Conversion to ebook

To convert to your preferred ebook format (AZW3,MOBI,EPUB..) you need to use Calibre : https://en.wikipedia.org/wiki/Calibre_(software).  
Simply import the html file into Calibre (it automatically creates an epub ebook) and you will be able to convert it to your preferred format.  
PS : To have all the images in your kindle, you need to download them manually (otherwise they will be in URL format in the kindle, and you will need an internet connexion to view them). To do so, in calibre, convert the ebook to your format, edit the book, and then tools->download ressources.
