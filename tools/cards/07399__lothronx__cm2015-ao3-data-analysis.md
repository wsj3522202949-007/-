---
id: tool-07399
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 本地写作]
title: cm2015-ao3-data-analysis
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/lothronx/cm2015-ao3-data-analysis
created: 2026-07-18
updated: 2026-07-18
no: 7399
category: 画龙补充 / 扩容入库 — 补充源
repo: lothronx/cm2015-ao3-data-analysis
stars: 0
url: https://github.com/lothronx/cm2015-ao3-data-analysis
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# lothronx/cm2015-ao3-data-analysis

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/lothronx/cm2015-ao3-data-analysis
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：📚 Digital Humanities meets Data Science: Analyzing 20,000+ Les Misérables fan fictions to uncover what makes stories popular in the digital age
- **本地描述**：cm2015-ao3-data-analysis
- **拉取时间**：2026-07-25 19:20:44

---

# 📚 What Makes a Fan Fiction Popular: A Digital Humanities Analysis

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![NLTK](https://img.shields.io/badge/NLTK-Natural%20Language%20Processing-purple.svg)](https://www.nltk.org/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-yellow.svg)](https://beautiful-soup-4.readthedocs.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange.svg)](https://pandas.pydata.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-red.svg)](https://scikit-learn.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-green.svg)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-lightblue.svg)](https://seaborn.pydata.org/)
[![WordCloud](https://img.shields.io/badge/WordCloud-Text%20Visualization-teal.svg)](https://github.com/amueller/word_cloud)

> _"Where literature meets algorithms, stories become data, and data tells stories." An interdisciplinary exploration of fanfiction popularity through computational literary analysis and data science_

## 🎯 Project Overview

<div align="center">

![Word Cloud](https://github.com/lothronx/cm2015-ao3-data-analysis/blob/main/img/output_1.png)

</div>

This project sits at the fascinating intersection of **literature studies** and **computer science**, analyzing what makes fan fiction popular in digital communities. Using Archive of Our Own (AO3) as a case study, I scraped and analyzed metadata from 20,800 English fanfictions in the Les Misérables fandom to uncover patterns in reader engagement and content preferences.

### 🔍 Research Questions

- Does frequent updating increase fanfiction popularity?
- What is the optimal length for popular fanfiction?
- How do content ratings affect reader engagement?
- Does publication timing after major canon events matter?
- What themes and character depictions resonate most with readers?

## 🌟 Why This Project Matters

### From a Literature Studies Perspective

- **Digital Literary Communities**: Explores how traditional literary analysis applies to user-generated content
- **Reader Response Theory**: Investigates how audiences actively shape and interpret texts
- **Cultural Studies**: Examines how fan communities create meaning and express contemporary values through transformative works

### From a Computer Science Perspective

- **Web Scraping**: Demonstrates responsible data collection from complex web structures
- **Natural Language Processing**: Applies text analysis techniques to understand semantic patterns in tags
- **Data Visualization**: Uses statistical modeling to reveal trends in large datasets
- **Machine Learning**: Employs regression models to predict popularity factors

## 🛠️ Technical Implementation

### Data Collection

- **Web Scraping**: Custom Python scripts using BeautifulSoup to extract metadata from 1,040 pages
- **Ethical Considerations**: Implemented rate limiting and followed platform guidelines
- **Data Structure**: Collected 10 key variables including engagement metrics and descriptive tags

### Analysis Pipeline

- **Data Cleaning**: Handled missing values, outliers, and inconsistent formatting
- **Statistical Modeling**: Linear and polynomial regression analysis
- **Text Processing**: NLP techniques for tag analysis and word frequency
- **Visualization**: Created compelling charts and word clouds to communicate findings

## 📊 Key Findings

1. **💡 Updates Don't Equal Popularity**: Contrary to intuition, frequent updates don't necessarily increase popularity on archive platforms
2. **📝 Optimal Length**: ~10,000 words is the sweet spot, with different patterns for different content ratings
3. **🔞 Rating Matters**: Higher-rated content tends to be more popular
4. **⏰ Timing is Everything**: Publishing immediately after major canon events provides initial boost, but quality content emerges gradually
5. **🏳️‍🌈 Modern Themes Dominate**: Fans prefer contemporary settings that allow exploration of current social issues

## 🎓 What I Learned

This project taught me invaluable lessons about:

- **Bridging Disciplines**: How computational methods can enhance traditional humanities research
- **Ethical Data Science**: The importance of responsible web scraping and considering community impact
- **Digital Communities**: How online spaces create new forms of literary culture and reader engagement
- **Methodological Rigor**: Balancing quantitative analysis with qualitative interpretation
- **Storytelling with Data**: Translating complex statistical findings into accessible insights

The intersection of literature and technology revealed that fan communities are sophisticated ecosystems where readers actively participate in cultural production, challenging traditional author-reader dynamics.

## 📁 Project Structure

```
├── What-makes-a-fan-fiction-popular.ipynb  # Main analysis notebook
├── fanfic_data.csv                          # Scraped dataset (20,800 works)
├── requirements.txt                         # Python dependencies
├── img/                                     # Visualizations and figures
│   ├── figure_1.png
│   └── figure_2.jpg
└── README.md                               # This file
```

## 🚀 Getting Started

1. **Clone the repository**

   ```bash
   git clone [repository-url]
   cd PwDMidterm_210312838
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the analysis**
   ```bash
   jupyter notebook What-makes-a-fan-fiction-popular.ipynb
   ```

## 📈 Visualizations

The project includes various data visualizations:

- Statistical correlation plots
- Word clouds showing popular themes
- Time series analysis of publication patterns
- Distribution charts of engagement metrics

## 🔬 Future Research Directions

- Cross-platform analysis comparing different fanfiction archives
- Sentiment analysis of reader comments and reviews
- Network analysis of author-reader relationships
- Machine learning models for predicting viral content

## 📝 Academic Context

This research contributes to the growing field of digital humanities, specifically:

- Computational literary studies
- Fan studies and transformative works research
- Digital community analysis
- Data-driven content strategy research

---

## 🤝 Connect With Me

**Yue Wu** - Exploring the intersection of literature, technology, and digital communities

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue.svg)](https://www.linkedin.com/in/yuewuxd/)

related:
  - methods/QUICK_START.md
---

_This project was completed as part of CM2015: Programming With Data coursework, demonstrating the application of computational methods to humanities research questions._
