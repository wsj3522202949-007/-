---
id: tool-07546
type: tool
area: 库
status: active
tags: [协议传染, 本地优先, 英文文档, 本地写作]
title: wattpad_analysis
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/simonerebora/wattpad_analysis
created: 2026-07-18
updated: 2026-07-18
no: 7546
category: 画龙补充 / 扩容入库 — 补充源
repo: simonerebora/wattpad_analysis
stars: 3
url: https://github.com/simonerebora/wattpad_analysis
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 1d2ca301e7663061
  - methods/QUICK_START.md
---

# simonerebora/wattpad_analysis

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/simonerebora/wattpad_analysis
- **Stars**：3
- **语言**：None
- **License**：GPL-3.0
- **Topics**：—
- **GitHub 描述**：Scripts and (sample) corpus for the analysis of the Wattpad platform 
- **本地描述**：wattpad_analysis
- **拉取时间**：2026-07-25 19:25:14

related:
  - methods/QUICK_START.md
---

# Wattpad_analysis
[![DOI](https://zenodo.org/badge/191598695.svg)](https://zenodo.org/badge/latestdoi/191598695)<br/>
**Author:** Simone Rebora<br/> 
**License:** [GPL-3](https://opensource.org/licenses/GPL-3.0)<br/>
<br/>
Scripts and (sample) corpus for the analysis of the Wattpad platform (www.wattpad.com)<br/>

## Content
The <b>Sample_wattpad_corpus.csv</b> file contains a sample corpus (with anonymized usernames and artificially-generated comments)<br/>
In the <b>Wattpad_network_preparation.Rmd</b> file is the Rmarkdown to prepare the network analysis of the sample corpus (visualizations should be realized with Gephi: https://gephi.org/)<br/>
In the <b>Wattpad_sentiment_analysis.Rmd</b> file is the Rmarkdown for runnning sentiment analysis on the sample corpus, via the syuzhet package: https://github.com/mjockers/syuzhet<br/>
In the <b>reverse_engineering_syuzhet.Rmd</b> file is the Rmarkdown for evaluating the relevance of single words in generating a section of the sentiment analysis graph<br/>
All .Rmd files are accompanied by .md files (easier to read in Github).<br/> 

## References
Rebora, Simone, and Federico Pianzola. 2018. "A New Research Programme for Reading Research: Analysing Comments in the Margins on Wattpad." DigitCult - Scientific Journal on Digital Cultures 3 (2): 19–36. https://doi.org/10.4399/97888255181532.<br/>
Pianzola, Federico, Simone Rebora, and Gerhard Lauer. in press. "Wattpad as a resource for literary studies in the 21st century. Quantitative and qualitative examples of the importance of digital social reading and readers' comments in the margins." PLOS ONE.

