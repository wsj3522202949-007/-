---
id: tool-07528
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: wnovelarchiver
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/safirex/wnovelarchiver
created: 2026-07-18
updated: 2026-07-18
no: 7528
category: 画龙补充 / 扩容入库 — 补充源
repo: safirex/wnovelarchiver
stars: 28
url: https://github.com/safirex/wnovelarchiver
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls: []
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 50f0232dbedde13b
  - methods/QUICK_START.md
---

# safirex/wnovelarchiver

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/safirex/wnovelarchiver
- **Stars**：28
- **语言**：Python
- **License**：MIT
- **Topics**：japanese-novel, kakuyomu, novel, python, python-script, python3, scraper, syosetu, web, webnovel, webscraper
- **GitHub 描述**：python script to download and keep to date web novels
- **本地描述**：wnovelarchiver
- **拉取时间**：2026-07-25 19:24:39

related:
  - methods/QUICK_START.md
---

note: ripping is bad, don't do it   

# WNovelArchiver
A simple python script to easily download and keep up to date raw web-novels on syosetu and kakuyomu  
If you have another WN site (JP/CN/KR/...) which you would like to be usable, feel free to put an issue.  
If your connection isn't stable, the script may (will) crash while downloading.
### Features:
* batch download (1 to max) from the input.txt
* update chapters of all the novels in the /novel_list/ directory
* generate a status file recording for every novel the last chapter ddl-ed
* compressing each novel in a zip of its own (not accessible by commands atm)

### Sites featured:
* Syosetu ncode and novel18
* Kakuyomu
* Wuxiaworld.com

## Instructions
##### more details in https://github.com/safirex/WNovelArchiver/wiki
The input.txt is used to give the script the entries to download.  
It should be written in csv style (code;novelname):  
The novel name can be let empty, in this case the script will fetch the novel name from the site  
![r](https://image.prntscr.com/image/8AY0wQWOQfqTNRfqg9Lejg.png)  
With n5947eg being the code of the novel accessed by https://ncode.syosetu.com/n5947eg/

codes:
* syosetsu    : code of the novel
* syosetsu 18+: <code>n18</code>code of the novel
* kakyomu     : code of the novel
* wuxiaworld  : Name-Of-The-Novel
