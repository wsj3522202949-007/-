---
id: tool-07396
type: tool
area: 库
status: active
tags: [Python, 协议传染, 本地优先, 英文文档, 本地写作]
title: royalroad-fetchandconvert
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/lonode/royalroad-fetchandconvert
created: 2026-07-18
updated: 2026-07-18
no: 7396
category: 画龙补充 / 扩容入库 — 补充源
repo: lonode/royalroad-fetchandconvert
stars: 17
url: https://github.com/lonode/royalroad-fetchandconvert
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 8679e29a5e8d0e1e
  - methods/QUICK_START.md
---

# lonode/royalroad-fetchandconvert

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/lonode/royalroad-fetchandconvert
- **Stars**：17
- **语言**：Python
- **License**：GPL-3.0
- **Topics**：adb, azw3, ebook, epub, fanfiction, kindle, python, royalroad, webfiction, webnovel
- **GitHub 描述**：Automatically download a royalroad story, convert it to kindle format and push it to the device.
- **本地描述**：royalroad-fetchandconvert
- **拉取时间**：2026-07-25 19:20:38

related:
  - methods/QUICK_START.md
---

# royalroad-fetchAndConvert
Automatically download a royalroad story, optionally convert it to kindle format and push it to the device.

![GUI Homepage](https://github.com/lonode/royalroad-fetchandconvert/blob/main/homepage.png)


# Features

* Retrieve automatically all the chapters of the given story
* Support table of content for ebook conversion
* Support author note at both end and start of the chapter
* Support images
* Support CSS rules for different stories (e.g. "Everybody Love Large Chest")
* Convert the story in the azw3 format, and push it to the kindle.


# GUI

## Install

Download the latest [released](https://github.com/lonode/royalroad-fetchAndConvert/releases) graphical version. For now, only the downloading is supported. The ebook generated need to be given to Calibre to convert it & to push it to your device.

## Developpement

The GUI has been developped with Tkinter. Specifically, [customtkinter](https://github.com/tomschimansky/customtkinter). All the front end is inside the file ``gui_rfetcher.py``.

The release is made by following this [official](https://customtkinter.tomschimansky.com/documentation/packaging) tutorial.

# CLI

## Install

Install Python3 on your operating system. 

Install needed libraries : 

	pip install requests-html

Also [Install ADB drivers](https://adb.clockworkmod.com/) if you plan to automatically push the book into your Kindle.



It also uses [calibre](https://github.com/kovidgoyal/calibre) to convert and push the ebook to the kindle. Everything is included here.  

## Usage

## Fetch and convert to AZW3 (Kindle Format)

The following command pull the chapter

	python fetch_book.py url_of_chapter number_of_chapters name_of_ebook

Parameters :  

* url_of_chapter : The URL of the chapter (not of the story homepage!)
* number_of_chapters : You guessed. If you want the whole book, just enter something like 99999
* name_of_ebook : The name of the ebook, .html extension will be added when the file is written on the filesystem.

It reads the chapter content of the URL given ( url_of_chapter ) and goes to the next chapter, and it loops number_of_chapters times.  

This command will give you a file ```name_of_ebook.html``` on your filesystem, that can be used through Calibre to be directly pushed to your Kindle. 


## Fetch, convert, and push to your device : 

	fetchAndCopy.py url_of_chapter number_of_chapters name_of_ebook

This script will download the chapter and push it to the first kindle detected. ```name_of_ebook``` is the name of the ebook which will be visible.


## Example  

If you want to fetch the best rated story Mother of Learning from the first chapter, execute the following command :

    python fetch_book.py https://www.royalroad.com/fiction/21220/mother-of-learning/chapter/301778/1-good-morning-brother 102 Mother_Of_Learning
  
In the example above, MOL.html is written a the working directory.
