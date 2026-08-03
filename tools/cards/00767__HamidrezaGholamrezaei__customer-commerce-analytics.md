---
id: tool-00767
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: customer-commerce-analytics
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/hamidrezagholamrezaei/customer-commerce-analytics
created: 2026-07-18
updated: 2026-07-18
no: 767
category: 二、网文 / 长篇 AI 写作系统 库
repo: HamidrezaGholamrezaei/customer-commerce-analytics
stars: 0
url: https://github.com/hamidrezagholamrezaei/customer-commerce-analytics
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# HamidrezaGholamrezaei/customer-commerce-analytics

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/hamidrezagholamrezaei/customer-commerce-analytics
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：dashboard, data-analysis, data-analytics, data-modeling, etl, etl-pipeline, postgresql, power-bi, python, retail-analytics, sql
- **GitHub 描述**：This project builds a basic customer-centric analytics pipeline on top of raw commerce data. The goal is to make common sales and customer questions easy to answer in Power BI without writing complex SQL each time.
- **本地描述**：This project builds a basic customer-centric analytics pipeline on top of raw commerce data. The goal is to make common sales and customer questions easy to answer in Power BI without writing complex SQL each time.
- **拉取时间**：2026-07-23 23:01:24

---

# Customer Commerce Analytics using PostgreSQL and Power BI
*From raw sales data to decision-ready dashboards.*

This repo is a compact customer commerce analytics project, designed to make it easy to answer common sales questions. It covers the full analytics workflow, including data cleaning and validation, dimensional modeling, and visualizing results in Power BI.

---

## Business Context

E-commerce teams usually have order exports but need to turn them into reliable metrics for:
- What’s actually happening day to day?
- Are we growing buyers, and who’s going inactive?
- What products are leaking margin through refunds?
- How much revenue is “bought” through discounting?

In this project, I built a small analytics stack that helps answer those questions.

---

## Questions this project answers
**Revenue & demand**
- What is our net revenue trend (daily + rolling windows)?
- How do order volume and basket size evolve?
- How does “promo” (discount applied) compare to non-promo performance?

**Customer health**
- How many buyers do we have, and how many are active vs inactive (churn risk)?
- How concentrated is revenue across customers (top X% contribution)?
- What do cohorts show about repeat behavior over time?

**Returns & product performance**
- Which categories/items have the highest return rates?
- Which items drive revenue vs operational risk (returns)?
- How large is the discount footprint and where does it concentrate?

---

## Dataset

- **Name:** Product Sales and Returns  
- **Source:** Kaggle [Product Sales and Returns Dataset](<https://www.kaggle.com/datasets/yaminh/product-sales-and-returns-dataset>) (see `data/README.md`)  
- **Time range:** 2018-11-01 → 2019-04-30  
- **Size:** ~70k rows
- **Scale:** ~25k buyers, ~1k items, ~30k transactions  

---

## What I Built

### 1) PostgreSQL Star Schema
A clean dimensional model designed for BI performance and consistent metrics.

- **Fact:** `c360.fact_sales`
- **Dimensions:** `c360.dim_date`, `c360.dim_item`, `c360.dim_buyer`

Schema diagram: `docs/schema_diagram.png`

### 2) ETL Pipeline (Python)
CSV → clean/standardize → build dimensions → validate fact rows → load to Postgres.

Outputs:
- `data/processed/orders_cleaned.csv`
- `data/processed/dim_*.csv`
- `data/processed/validated_fact_data.csv`
- Optional `data/processed/rejected_rows.csv` (failed validation)

### 3) Analytics Layer (SQL)
SQL views used in Power BI, which includes:
- revenue (daily/monthly + rolling windows)
- customer rollups (active/inactive flag, basic cohorts)
- returns analysis (item/category/buyer return rates)
- promotions (discount share, promo vs non-promo)
- item rankings (revenue, quantity, return rate, discount footprint)


### 4) BI Layer (Semantic Model + Report)
Report pages (screenshots in `docs/screenshots/`):
1. **Executive Overview**
2. **Customer Insights**
3. **Item Performance**

---

## Tech Stack

- **SQL / PostgreSQL**
- **Python**
- **Power BI / Semantic Model**

---

## How to run Locally
1) Download `order_dataset.csv` and place it under `data/raw/` (see `data/README.md`).
2) Create database and schema by running SQL scripts in `sql/`:
- `01_create_database.sql`
- `02_schema.sql`
3) Configure the ETL by updating `etl/etl_config.yaml` with your Postgres connection settings.
4) Run the pipeline:
- `python etl/etl_pipeline.py`
5) Build analytics views by running:
- `03_analytics.sql`
6) Use the views as sources for Power BI reports.

---

## Repository Structure

```text
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
├── docs/
│   ├── schema_diagram.png
│   ├── screenshots/
│   ├── data_dictionary.md
│   ├── dax_measures.md
│   └── insights.md
├── etl/
│   ├── etl_pipeline.py
│   ├── etl_config.yaml
│   └── utils/helpers.py
├── sql/
│   ├── 01_create_database.sql
│   ├── 02_schema.sql
│   └── 03_analytics.sql
├── tests/
│   ├── conftest.py
│   ├── test_helpers.py
│   └── test_pipeline.py
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Notes
- The dataset covers ~6 months, so “churn” is treated as inactivity proxy, not true customer churn.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## License
This project is licensed under the MIT License. For more detailed information, please refer to the LICENSE file.
