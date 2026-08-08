---
id: tool-05227
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: Ai_slop_detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/krgkaushik/ai_slop_detector
created: 2026-07-18
updated: 2026-07-18
no: 5227
category: 一、去 AI 味 / Humanizer 库
repo: krgkaushik/Ai_slop_detector
stars: 0
url: https://github.com/krgkaushik/ai_slop_detector
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: dcc4acda93baf364
  - methods/改稿润色指令库.md
---

# krgkaushik/Ai_slop_detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/krgkaushik/ai_slop_detector
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：krgkaushik/Ai_slop_detector
- **拉取时间**：2026-07-25 18:10:46

---

# AI Slop Detector

A Python-based data collection tool for building datasets used in AI-generated text detection. This project scrapes random Wikipedia articles and extracts paragraphs that can later be used for training or evaluating AI text detection models.

## Features

- Scrapes random Wikipedia articles.
- Extracts clean paragraph text.
- Saves scraped data in JSONL format.
- Easily extendable for dataset generation and preprocessing.

---

## Project Structure

```
AI_slop_detector/
│
├── scraping/
│   ├── src/
│   ├── main.py
│   └── random_list.py
│
├── scrapes/
│   └── scrape_1763655781666449000.jsonl
│
├── .gitignore
├── .gitattributes
├── .python-version
├── pyproject.toml
├── uv.lock
├── LICENSE
└── README.md
```

---

## Requirements

- Python 3.11+
- uv (recommended) or pip

Install dependencies:

```bash
uv sync
```

or

```bash
pip install -r requirements.txt
```

---

## Running the Scraper

Navigate to the scraping directory and run:

```bash
cd scraping
python main.py
```

The scraper will:

- Fetch random Wikipedia pages.
- Extract paragraph text.
- Save the results inside the `scrapes/` directory.

Example output:

```
scrapes/
└── scrape_1763655781666449000.jsonl
```

---

## Output Format

Each line in the JSONL file represents one scraped paragraph.

Example:

```json
{
  "title": "Artificial intelligence",
  "paragraph": "Artificial intelligence (AI) is intelligence demonstrated by machines..."
}
```

---

## Technologies Used

- Python
- Requests
- BeautifulSoup
- JSON Lines (JSONL)

---

## Future Improvements

- Dataset cleaning
- Duplicate removal
- AI text generation pipeline
- Model training for AI text detection
- Web interface for text classification

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## License

This project is licensed under the MIT License.
