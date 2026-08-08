---
id: tool-07525
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 中文友好, 本地写作]
title: narou-scraper
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/rw21/narou-scraper
created: 2026-07-18
updated: 2026-07-18
no: 7525
category: 画龙补充 / 扩容入库 — 补充源
repo: rw21/narou-scraper
stars: 0
url: https://github.com/rw21/narou-scraper
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: d8960a56161a2e46
  - methods/QUICK_START.md
---

# rw21/narou-scraper

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/rw21/narou-scraper
- **Stars**：0
- **语言**：Python
- **License**：NOASSERTION
- **Topics**：—
- **GitHub 描述**：小説家になろうをスクレイピングするスクリプト
- **本地描述**：narou-scraper
- **拉取时间**：2026-07-25 19:24:34

related:
  - methods/QUICK_START.md
---

# narou-scraper
```
usage: main.py [-h] [--reset] [--start-from START_FROM] [--end-with END_WITH]
               [--log-file LOG_FILE] [--skip-r18 SKIP_R18] [--nid NID]
               [--skip-content] [--skip-impression]

    This script will scrape narou novels.
    It will save the files in a sqlite database named novels.db.
    See models.py for the fields it can scrape.
    
    Example Usage:
    1. To scrape a range of novels, specify the starting and ending nids:
    python3 main.py --start-from N1955HZ --end-with N1955HZ 

    2. To scrape a specific novel, specify its nid:
    python3 main.py --nid n6879ig 

    3. To skip scraping R18 novels:
    python3 main.py --skip-r18 true 

    4. To specify the location of the log file:
    python3 main.py --log-file ./logs/scrape.log 
    
    このスクリプトはなろう小説をスクレイピングします。
    novels.dbという名前のsqliteデータベースに保存されます。
    取得できるフィールドは、models.pyを参照してください。
    
    使用例:
    1. 小説の範囲を指定し、スクレイピングするには、開始と終了のnidを設定します:
    python3 main.py --start-from N1955HZ --end-with N1955HZ 

    2. 特定の小説をスクレイピングするには、そのnidを指定します:
    python3 main.py --nid n6879ig 

    3. R18の小説のスクレイピングをスキップするには:
    python3 main.py --skip-r18 true 

    4. ログファイルの場所を指定するには:
    python3 main.py --log-file ./logs/scrape.log 
    
    

optional arguments:
  -h, --help            show this help message and exit
  --reset               Reset scrape history (default: False)
  --start-from START_FROM
                        The starting nid, inclusive (default: N9999ZZ)
  --end-with END_WITH   The ending nid, inclusive (default: N0000AA)
  --log-file LOG_FILE   Location of log file (default: scrape.log)
  --skip-r18 SKIP_R18   Whether to skip R18 novels (default: False)
  --nid NID             The nid to scrape, if this is set, --start-from and --end-with are ignored
  --skip-content        When this is enabled, it will skip scraping novel content (default: False)
  --skip-impression     When this is enabled, it will skip scraping novel impression(default: False)

    

```
