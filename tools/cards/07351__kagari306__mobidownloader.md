---
id: tool-07351
type: tool
area: 库
status: active
tags: [Python, 协议传染, 本地优先, 中文友好, 本地写作]
title: mobidownloader
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/kagari306/mobidownloader
created: 2026-07-18
updated: 2026-07-18
no: 7351
category: 画龙补充 / 扩容入库 — 补充源
repo: kagari306/mobidownloader
stars: 4
url: https://github.com/kagari306/mobidownloader
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 02b60c012799a294
  - methods/QUICK_START.md
---

# kagari306/mobidownloader

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/kagari306/mobidownloader
- **Stars**：4
- **语言**：Python
- **License**：GPL-3.0
- **Topics**：acgn, acgn-download, anime, bangumi, downloader, light-novel, light-novels, mobinovels, webnovel, webnovels
- **GitHub 描述**：A light novel file downloader
- **本地描述**：mobidownloader
- **拉取时间**：2026-07-25 19:19:14

related:
  - methods/QUICK_START.md
---

# MOBIDownloader

用于从 [魔笔小说](https://mobinovels.com/) 下载轻小说的脚本

## 设置

`main.py` 中第八行和第九行为下载设置

```
PASSCODE = 6195
FORMAT = "MOBI" # MOBI/EPUB
```

其中 `PASSCODE` 为ctfile密码，默认为6195(网站公告有标)

`FORMAT` 为下载格式，在MOBI和EPUB里面二选一，我要塞到Kindle里面所以选了MOBI

## 使用方法

### 下载一个系列

直接将url作为第一个参数传入，比如

```
python3 main.py "https://mobinovels.com/mushoku-tensei/"
```

### 下载多个系列

在项目目录下新建一个 `lists.txt` 然后将多个链接丢进去, 一行一个, 比如

```
https://mobinovels.com/mushoku-tensei/
https://mobinovels.com/classroom-of-the-elite/
https://mobinovels.com/gj-club/
https://mobinovels.com/aria-the-scarlet-ammo/
```

然后执行

```
python3 main.py
```

## Links

[Matrix Group](https://matrix.to/#/#kagari306-official:matrix.org)
