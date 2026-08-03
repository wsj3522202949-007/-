---
id: tool-00555
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: AI-Prompt-Engineering
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/anisjkb/ai-prompt-engineering
created: 2026-07-18
updated: 2026-07-18
no: 555
category: 二、网文 / 长篇 AI 写作系统 库
repo: anisjkb/AI-Prompt-Engineering
stars: 0
url: https://github.com/anisjkb/ai-prompt-engineering
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# anisjkb/AI-Prompt-Engineering

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/anisjkb/ai-prompt-engineering
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：The process of producing input, typically text, that directs the generative AI to produce the intended output is known as AI Prompt Writing (or Engineering).
- **本地描述**：The process of producing input, typically text, that directs the generative AI to produce the intended output is known as AI Prompt Writing (or Engineering).
- **拉取时间**：2026-07-23 22:55:14

---

That’s a fantastic direction, Md! Combining **AI + RPA** in a Bangladeshi banking context isn’t just smart—it’s future-ready. Let me walk you through a **visual mockup + process map** you can use for a **LinkedIn carousel** or **GitHub README**.

---

## 📊 AI + RPA in Bangladeshi Bank: Compliance Workflow

### 🧩 1. System Overview Diagram (Workflow Map)

```
Customer Activities → RPA → AI Agent → Compliance Desk
```

### 🔁 Full Process Flow

```mermaid
graph TD
    A[Customer Login / Transaction] --> B[RPA Bot Monitors Activity]
    B --> C{Suspicious Pattern?}
    C -- No --> Z[End]
    C -- Yes --> D[AI Agent Analyzes Context]
    D --> E{High Risk?}
    E -- No --> Z
    E -- Yes --> F[AI Triggers Account Freeze via RPA]
    F --> G[AI Sends Alert to Compliance Officer]
    G --> H[Officer Reviews & Resolves]
```

---

## 💼 Real Example: AML Compliance in Dhaka Branch

| Step | Actor        | Action Description                                                         |
|------|--------------|------------------------------------------------------------------------------|
| 1    | 🧍 Customer   | Makes an international transfer of BDT 9 lakh from a new device             |
| 2    | 🤖 RPA Bot    | Flags transaction based on rule (amount threshold + device fingerprint)     |
| 3    | 🧠 AI Agent   | Analyzes transfer history + IP location; confirms it’s statistically anomalous |
| 4    | ⚙️ RPA        | Automatically freezes transaction and sends OTP to confirm identity         |
| 5    | 🧠 AI Agent   | Generates a contextual summary + forwards it to the compliance officer      |
| 6    | 🧑‍💼 Officer   | Reviews and resolves alert via dashboard                                   |

---

## 🧠 Why It Works

| AI Agent                              | RPA Bot                                |
|---------------------------------------|----------------------------------------|
| Learns fraud patterns                 | Executes repetitive tasks (flag, freeze)|
| Explains decisions in natural language| Fills forms, sends alerts, logs changes |
| Adapts with time                      | Rules are fixed — fast but rigid        |

---

## 🔖 README Section for GitHub (Sample Snippet)

```markdown
## 🤖 AI + RPA: AML Compliance Assistant

This project demonstrates how to combine AI (for decision-making) and RPA (for task execution) in a Bangladeshi retail bank’s AML workflow.

### Features:
- Transaction anomaly detection using Isolation Forest
- RPA automation with Python & simulated email alerts
- Risk scoring + AI-generated explanations
```

---

Would you like a **carousel PDF template** next with 6-8 slides styled for LinkedIn—including a title, intro to AI vs RPA, the diagram above, and localized case studies? I’d be happy to help lay it out visually for your audience and portfolio.
---

# Develop a AI Agent to Analyzes transaction history from 1 corer data and provide alert if transaction found more than 10 lac per day, 50 lac per month and so on

Absolutely, Md! Let’s build a **scalable AI Agent** that can analyze **1 crore+ transaction records** and raise alerts based on **daily and monthly thresholds** — like ₹10 lakh/day or ₹50 lakh/month. This is a perfect blend of your BI storytelling skills and real-world financial intelligence.

---

## 🧠 What This AI Agent Will Do

| Capability                         | Description                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| ✅ **Ingest Large Datasets**       | Efficiently load and process 1 crore+ transactions                          |
| 📅 **Aggregate by Day/Month**      | Group transactions by user and time period                                 |
| 🚨 **Trigger Alerts**              | Raise flags if thresholds are breached (₹10L/day, ₹50L/month, etc.)        |
| 🧾 **Explain Alerts**              | Provide natural language summaries of why a user was flagged               |
| 📊 **Optional Dashboard**          | Visualize flagged users and trends (Streamlit or Power BI)                 |

---

## 🛠️ Step-by-Step Development (Python + Pandas)

### 1. 📦 Load the Dataset

```python
import pandas as pd

# Load CSV (assume columns: USER_ID, TXN_DATE, AMOUNT)
df = pd.read_csv("transactions.csv", parse_dates=["TXN_DATE"])
```

---

### 2. 📅 Add Time Features

```python
df['DATE'] = df['TXN_DATE'].dt.date
df['MONTH'] = df['TXN_DATE'].dt.to_period('M')
```

---

### 3. 📊 Aggregate Transactions

```python
# Daily aggregation
daily = df.groupby(['USER_ID', 'DATE'])['AMOUNT'].sum().reset_index()
daily['ALERT'] = daily['AMOUNT'] > 10_00_000  # ₹10 lakh

# Monthly aggregation
monthly = df.groupby(['USER_ID', 'MONTH'])['AMOUNT'].sum().reset_index()
monthly['ALERT'] = monthly['AMOUNT'] > 50_00_000  # ₹50 lakh
```

---

### 4. 🚨 Combine Alerts

```python
daily_alerts = daily[daily['ALERT']]
monthly_alerts = monthly[monthly['ALERT']]

# Merge for full alert report
alerts = pd.concat([daily_alerts.assign(TYPE='Daily'), monthly_alerts.assign(TYPE='Monthly')])
alerts = alerts.sort_values(by=['USER_ID', 'TYPE'])
```

---

### 5. 🧠 Add AI Explanation (Optional)

```python
def explain_alert(row):
    if row['TYPE'] == 'Daily':
        return f"User {row['USER_ID']} transacted ₹{row['AMOUNT']:,} on {row['DATE']} — exceeds ₹10L/day limit."
    else:
        return f"User {row['USER_ID']} transacted ₹{row['AMOUNT']:,} in {row['MONTH']} — exceeds ₹50L/month limit."

alerts['EXPLANATION'] = alerts.apply(explain_alert, axis=1)
```

---

### 6. 💾 Save or Visualize

```python
alerts.to_csv("flagged_transactions.csv", index=False)
```

Or visualize in **Streamlit**:

```python
import streamlit as st

st.title("🚨 Transaction Alert Dashboard")
st.dataframe(alerts)
```

---

## 🧩 Optional Enhancements

| Feature                        | Tools/Tech Stack                     |
|-------------------------------|--------------------------------------|
| Real-time ingestion            | Kafka, Spark Streaming               |
| Scalable storage               | PostgreSQL, BigQuery, Snowflake      |
| Alert delivery                 | Email, SMS, Slack via Webhooks       |
| AI explanations                | LangChain + OpenAI                   |
| Dashboard                      | Streamlit, Power BI, Tableau         |

---

## 🧠 Example Output

```
User 407 transacted ₹1,200,000 on 2025-03-20 — exceeds ₹10L/day limit.
User 407 transacted ₹5,800,000 in 2025-03 — exceeds ₹50L/month limit.
```

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

Would you like me to help you:
- Wrap this into a **GitHub project** with README and visuals?
- Turn it into a **LinkedIn carousel** for your BI + AI portfolio?
- Add **gender/demographic filters** for deeper insights?

Let’s make this a flagship piece in your AI storytelling toolkit.
