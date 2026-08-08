---
id: tool-07621
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: ao3-stats
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/xodarap/ao3-stats
created: 2026-07-18
updated: 2026-07-18
no: 7621
category: 画龙补充 / 扩容入库 — 补充源
repo: xodarap/ao3-stats
stars: 0
url: https://github.com/xodarap/ao3-stats
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 55aff7b3b67e4639
  - methods/QUICK_START.md
---

# xodarap/ao3-stats

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/xodarap/ao3-stats
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：ao3-stats
- **拉取时间**：2026-07-25 19:27:58

related:
  - methods/QUICK_START.md
---

# ao3-stats

A small scraper that sums the kudos for specific AO3 relationship (ship) tags.

## Usage

Run the scraper for your chosen relationship tags. To keep load on AO3 reasonable,
the default configuration only fetches a single page (20 works) per tag.

```
python -m ao3_stats "Aldebaran | Al*s*Priscilla Barielle" --pages 2
```

Use `--pages` to inspect more works per tag, `--delay` to adjust the pause between
requests, and `--json` for machine-readable output. You can also restrict results to
works posted within a specific time range with `--start-date` and `--end-date`.

### Batch scraping from CSV

To recreate the 2025 ship stats with kudos totals, first populate `data/ships_2025.csv`
with the relationships you want to analyse (a header row named `relationship` followed
by one ship per line). Then run the batch scraper, which resumes automatically if it is
interrupted:

```
python -m ao3_stats.csv_kudos data/ships_2025.csv data/ship_kudos_2025.csv --delay 1
```

The command writes results incrementally to `data/ship_kudos_2025.csv`, storing the
total kudos and works for each relationship tag.

## Visualising Viktor/Jayce share over time

To recreate the Viktor/Jayce share plot that weights the relationship by kudos, hits,
bookmarks, comments, words, and raw work counts—and to compare the top Arcane ships by
the naive average of those metrics—first ensure the `data/created_dates.csv` dataset from
the `data` branch is present locally. Then run:

```
python analysis/viktor_jayce_share.py
```

The script writes `figures/viktor_jayce_share.png` with the percentage of Viktor/Jayce
works per month under each weighting, `figures/top_ships_naive_average.png` with the
naive-average share for the top five ships (by average across the supplied metrics), and
`figures/total_hits.png` with the total number of hits across all Arcane works per month.
Use `--top-n` to change how many ships appear on the naive-average chart, and `--viktor-output`,
`--top-output`, or `--total-hits-output` to customise the output paths. Generated figures are not
tracked in the repository; regenerate them locally as needed.
