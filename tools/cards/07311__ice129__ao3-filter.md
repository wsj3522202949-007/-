---
id: tool-07311
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: ao3-filter
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/ice129/ao3-filter
created: 2026-07-18
updated: 2026-07-18
no: 7311
category: 画龙补充 / 扩容入库 — 补充源
repo: ice129/ao3-filter
stars: 0
url: https://github.com/ice129/ao3-filter
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# ice129/ao3-filter

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/ice129/ao3-filter
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：ao3-filter
- **拉取时间**：2026-07-25 19:17:26

related:
  - methods/QUICK_START.md
---

# AO3 Filter

A Python tool that scrapes Archive of Our Own (AO3) works and ranks them using AI based on your preferences.

## What It Does

- Scrapes AO3 search results with your filters
- Extracts fic metadata (title, summary, tags, stats, etc.)
- Uses a local AI model (via Ollama) to rank fics based on your search criteria
- Outputs a formatted markdown file with ranked results

## Setup

### Prerequisites

1. **Python 3.7+**
2. **Chrome Browser** (for Selenium)
3. **Ollama** - [Install Ollama](https://ollama.ai)
4. **AI Model** - Pull the model:
   ```bash
   ollama pull goekdenizguelmez/JOSIEFIED-Qwen3:4b
   ```

### Install Dependencies

```bash
pip install selenium beautifulsoup4 aiohttp
```

## How to Use

1. **Configure the script** in `main.py`:
   - Set your AO3 search URL with filters applied
   - Set number of pages to scrape
   - Set your search criteria in natural language

   ```python
   url = "https://archiveofourown.org/works/search?your_filters_here"
   pages = 3
   search_param = "I want long completed fics with happy endings"
   ```

2. **Run the script**:
   ```bash
   python main.py
   ```

3. **View results** in `filtered_fics.md`

## Ranking Methods

The script offers two ranking approaches:

- **Tournament ranking** (default): Uses pairwise comparisons via merge sort - more accurate but slower
- **Scoring system**: Scores each fic independently - faster but less precise

Switch between them by commenting/uncommenting the relevant lines in `main()`.

## Notes

- Be respectful of AO3's servers - the script includes rate limiting
- Processing time depends on the number of fics and ranking method chosen
- You can interrupt ranking with Ctrl+C to proceed with partial results
