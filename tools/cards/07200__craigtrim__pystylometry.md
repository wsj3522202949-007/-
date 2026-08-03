---
id: tool-07200
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: pystylometry
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/craigtrim/pystylometry
created: 2026-07-18
updated: 2026-07-18
no: 7200
category: 画龙补充 / 扩容入库 — 补充源
repo: craigtrim/pystylometry
stars: 3
url: https://github.com/craigtrim/pystylometry
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls: []
related:
  - methods/QUICK_START.md
---

# craigtrim/pystylometry

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/craigtrim/pystylometry
- **Stars**：3
- **语言**：Python
- **License**：MIT
- **Topics**：ai-detection, ai-detection-bypasser, authorship-attribution, computational-linguistics, digital-humanities, forensic-linguistics, lexical-diversity, natural-language-processing, nlp, readability, stylometry, text-analysis
- **GitHub 描述**：Comprehensive Python toolkit for stylometry
- **本地描述**：pystylometry
- **拉取时间**：2026-07-25 19:13:56

---

# pystylometry

[![PyPI version](https://badge.fury.io/py/pystylometry.svg)](https://badge.fury.io/py/pystylometry)
[![Downloads](https://static.pepy.tech/badge/pystylometry)](https://pepy.tech/project/pystylometry)
[![Downloads/Month](https://static.pepy.tech/badge/pystylometry/month)](https://pepy.tech/project/pystylometry)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-1022%20passed-brightgreen)]()

Stylometric analysis and authorship attribution for Python. 50+ metrics across 11 modules, from vocabulary diversity to AI-generation detection.

## Install

```bash
pip install pystylometry              # Core (lexical metrics)
pip install pystylometry[all]         # Everything
```

## Modules

| Module | Metrics | Description |
|--------|---------|----------related:
  - methods/QUICK_START.md
---|
| [**lexical**](https://github.com/craigtrim/pystylometry/tree/master/pystylometry/lexical) | TTR, MTLD, Yule's K/I, Hapax, MATTR, VocD-D, HD-D, MSTTR, function words, word frequency | Vocabulary diversity and richness |
| [**readability**](https://github.com/craigtrim/pystylometry/tree/master/pystylometry/readability) | Flesch, Flesch-Kincaid, SMOG, Gunning Fog, Coleman-Liau, ARI, Dale-Chall, Fry, FORCAST, Linsear Write, Powers-Sumner-Kearl | Grade-level and difficulty scoring |
| [**syntactic**](https://github.com/craigtrim/pystylometry/tree/master/pystylometry/syntactic) | POS ratios, sentence types, parse tree depth, clausal density, passive voice, T-units, dependency distance | Sentence and parse structure (requires spaCy) |
| [**authorship**](https://github.com/craigtrim/pystylometry/tree/master/pystylometry/authorship) | Burrows' Delta, Cosine Delta, Zeta, Kilgarriff chi-squared, MinMax, John's Delta, NCD | Author attribution and text comparison |
| [**stylistic**](https://github.com/craigtrim/pystylometry/tree/master/pystylometry/stylistic) | Contractions, hedges, intensifiers, modals, punctuation, vocabulary overlap (Jaccard/Dice/Cosine/KL), cohesion, genre/register | Style markers and text similarity |
| [**character**](https://github.com/craigtrim/pystylometry/tree/master/pystylometry/character) | Letter frequencies, digit/uppercase ratios, special characters, whitespace | Character-level fingerprinting |
| [**ngrams**](https://github.com/craigtrim/pystylometry/tree/master/pystylometry/ngrams) | Word/character/POS n-grams, Shannon entropy, skipgrams | N-gram profiles and entropy |
| [**dialect**](https://github.com/craigtrim/pystylometry/tree/master/pystylometry/dialect) | British/American classification, spelling/grammar/vocabulary markers, markedness | Regional dialect detection |
| [**consistency**](https://github.com/craigtrim/pystylometry/tree/master/pystylometry/consistency) | Sliding-window chi-squared drift, pattern classification | Intra-document style analysis |
| [**prosody**](https://github.com/craigtrim/pystylometry/tree/master/pystylometry/prosody) | Syllable stress, rhythm regularity, sentence syllable patterns, pattern repetition | Prose rhythm (requires cmudict) |
| [**viz**](https://github.com/craigtrim/pystylometry/tree/master/pystylometry/viz) | Timeline, scatter, report (PNG + interactive HTML) | Drift detection visualization |

## Development

```bash
git clone https://github.com/craigtrim/pystylometry && cd pystylometry
pip install -e ".[dev,all]"
make test       # 1022 tests
make lint       # ruff + mypy
make all        # lint + test + build
```

## License

MIT

## Author

Craig Trim -- craigtrim@gmail.com
