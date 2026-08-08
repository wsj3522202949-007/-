---
id: tool-00305
type: tool
area: 库
status: active
tags: [Jupyter Notebook, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Education-Analytics-Dashboard-
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/paulandreavargas/education-analytics-dashboard-
created: 2026-07-18
updated: 2026-07-18
no: 305
category: 二、网文 / 长篇 AI 写作系统 库
repo: Paulandreavargas/Education-Analytics-Dashboard-
stars: 0
url: https://github.com/paulandreavargas/education-analytics-dashboard-
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 77096e0b96c80ae0
  - methods/最强写作方法论_全球最强综合版.md
---

# Paulandreavargas/Education-Analytics-Dashboard-

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/paulandreavargas/education-analytics-dashboard-
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：Analyzes the impact of ethnicity, test preparation, and parental education on grades across math, reading, writing, and science. Uses Python, SQL, and Tableau for data cleaning, visualization, and insights. Ideal for educators, policymakers, and data enthusiasts.
- **本地描述**：Analyzes the impact of ethnicity, test preparation, and parental education on grades across math, reading, writing, and science. Uses Python, SQL, and Tableau for data cleaning, visualization, and insights. Ideal for educators, policymakers, and data enthusiasts.
- **拉取时间**：2026-07-23 22:47:57

---

# Education Performance Analytics  
**Data Wrangling Final Project**

This project explores how **demographic and socioeconomic factors** influence students’ academic performance.  
It applies **data wrangling**, **exploratory data analysis (EDA)**, and **visual storytelling** using Python, uncovering insights about education outcomes and the variables that most affect learning success.

---

## Project Overview

The dataset contains information on students’ test scores in **Math, Reading, and Writing**, along with features such as:
- Gender  
- Parental education level  
- Lunch type  
- Test preparation course status  
- Race/ethnicity  

The goal is to identify **patterns and correlations** between these factors and overall student performance through a complete data-wrangling workflow.

---

## Tools and Libraries
- **Python** (Pandas, NumPy, Matplotlib, Seaborn)
- **Jupyter Notebook**
- **Scipy** for statistical testing
- **Tableau** (optional visualization layer)
- **GitHub** for version control and collaboration

---

## Repository Structure

```
Education-Performance-Analytics-for-Data-Wrangling-Final-Project/
│
├── Python/
│   └── Analysis.ipynb          # Main notebook with data wrangling and EDA
│
├── data/
│   ├── raw/                    # Original dataset (add link or upload)
│   └── processed/              # Cleaned data after wrangling
│
├── reports/
│   └── figures/                # Exported plots and charts
│
├── requirements.txt            # Required libraries
├── .gitignore                  # Ignored files and folders
├── LICENSE (optional)
└── README.md                   # Project documentation 

```
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Installation & Setup
To reproduce this project locally:

```bash
# Clone repository
git clone https://github.com/Paulangwiedergoerner/Education-Performance-Analytics-for-Data-Wrangling-Final-Project.git

# Navigate into project folder
cd Education-Performance-Analytics-for-Data-Wrangling-Final-Project

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
