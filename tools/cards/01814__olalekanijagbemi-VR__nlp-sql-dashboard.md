---
id: tool-01814
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: nlp-sql-dashboard
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/olalekanijagbemi-vr/nlp-sql-dashboard
created: 2026-07-18
updated: 2026-07-18
no: 1814
category: 二、网文 / 长篇 AI 写作系统 库
repo: olalekanijagbemi-VR/nlp-sql-dashboard
stars: 0
url: https://github.com/olalekanijagbemi-vr/nlp-sql-dashboard
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# olalekanijagbemi-VR/nlp-sql-dashboard

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/olalekanijagbemi-vr/nlp-sql-dashboard
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：NLP to SQL Analytics Dashboard - An intelligent database query system that converts natural language questions to executable SQL. Features include multi-table JOIN queries, auto-generated visualizations, query history, and real-time results. Built for non-technical users to explore data without writing SQL
- **本地描述**：NLP to SQL Analytics Dashboard - An intelligent database query system that converts natural language questions to executable SQL. Features include multi-table JOIN queries, auto-generated visualizations, query history, and real-time results. Built for non-technical users to explore data without writing SQL
- **拉取时间**：2026-07-23 23:31:56

---

# 🐘 AI-Powered SQL Analytics Dashboard

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Groq](https://img.shields.io/badge/Groq-FF6B00?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)

**Ask questions in plain English • Get SQL results + charts instantly • Enterprise-grade PostgreSQL**

---

## 🚀 Live Demo

> **Try it yourself:** [Your Streamlit Cloud URL here]

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **Natural Language to SQL** | Ask questions in plain English, AI generates SQL automatically |
| 📊 **Auto Charts** | Visualizations generated instantly from query results |
| 🔗 **Multi-Table JOINs** | Query across 4 normalized tables with relationships |
| 🐘 **PostgreSQL** | Enterprise-grade database with Supabase cloud hosting |
| 📜 **Query History** | Save and reuse previous queries with one click |
| 💡 **Example Questions** | Pre-built queries to get started immediately |
| 📥 **CSV Export** | Download any query result with one click |
| 🔒 **Security** | SQL injection protection and safe query execution |
| 🎨 **Professional UI** | Clean, responsive design with dark/light mode support |

---

## 📁 Database Schema

| Table | Rows | Description | Key Columns |
|-------|------|-------------|-------------|
| **sales** | 10,000 | Transaction data | transaction_id, sale_date, customer, product, revenue |
| **customers** | 100 | Customer details | customer_id, customer_name, email, customer_segment |
| **products** | 10 | Product information | product_id, product_name, category, supplier, cost |
| **regions** | 5 | Region management | region_id, region_name, manager, office |

### Entity Relationship Diagram

---

## 🛠️ Tech Stack

### Frontend & Backend
- **Framework:** Streamlit 1.35.0
- **Language:** Python 3.12
- **Database:** PostgreSQL (Supabase)
- **AI/LLM:** Groq API (Llama 3.1 8B)
- **Visualization:** Plotly 5.19.0
- **Data Processing:** Pandas 2.2.0, NumPy 1.26.4

### Deployment
- **Frontend Hosting:** Streamlit Cloud
- **Database Hosting:** Supabase (PostgreSQL)
- **Version Control:** Git / GitHub

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 🏃‍♂️ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/olalekanijagbemi-VR/nlp-sql-dashboard.git
cd nlp-sql-dashboard
