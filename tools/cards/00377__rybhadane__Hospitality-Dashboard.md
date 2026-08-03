---
id: tool-00377
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Hospitality-Dashboard
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/rybhadane/hospitality-dashboard
created: 2026-07-18
updated: 2026-07-18
no: 377
category: 二、网文 / 长篇 AI 写作系统 库
repo: rybhadane/Hospitality-Dashboard
stars: 0
url: https://github.com/rybhadane/hospitality-dashboard
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# rybhadane/Hospitality-Dashboard

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/rybhadane/hospitality-dashboard
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Built an end-to-end hospitality analytics solution for Atliq Grand Hotels as part of my Data Analytics training at ExcelR Institute. Worked across 7 properties in Mumbai, Bangalore, Hyderabad, and Delhi writing 20+ SQL queries to extract KPIs. Data model built on Star Schema with Fact and Dimension tables.
- **本地描述**：Built an end-to-end hospitality analytics solution for Atliq Grand Hotels as part of my Data Analytics training at ExcelR Institute. Worked across 7 properties in Mumbai, Bangalore, Hyderabad, and Delhi writing 20+ SQL queries to extract KPIs. Data model built on Star Schema with Fact and Dimension tables.
- **拉取时间**：2026-07-23 22:50:06

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Hospitality-Dashboard

## Data Model 
Our dataset follows a star schema model where fact tables contain transactional data and dimension tables provide descriptive information. This structure improves analytical efficiency and reporting.

<img width="706" height="653" alt="image" src="https://github.com/user-attachments/assets/693f3a55-ee7e-4083-9866-ff5fe052b13f" />

## Business Requirement

<img width="982" height="844" alt="image" src="https://github.com/user-attachments/assets/9f6ae6eb-d449-41fa-9a9c-030c186cb79e" />

## Data Modelling

<img width="1282" height="638" alt="image" src="https://github.com/user-attachments/assets/3a94366c-8d47-4a2d-b6a8-eed198e35f36" />

## Observations
1. Revenue vs Bookings: High revenue (₹1.7B) vs bookings (134,590) suggests healthy ADR; validate with RevPAR and length-of-stay.
2. Cancellations & No-shows: 33,420 cancellations and 6,759 no-shows represent a sizable leakage. Segment by channel to prioritize interventions.
3. Guest Rating: 3.62 average indicates room for CX improvements; correlate with cancellations and negative feedback.

## Excel Dashboard

<img width="1195" height="515" alt="Screenshot 2026-06-25 144057" src="https://github.com/user-attachments/assets/2242a6e1-9c6c-4bf8-b345-9f7bf0c5a7db" />

<img width="1050" height="585" alt="image" src="https://github.com/user-attachments/assets/07480d65-163d-48f4-8adc-299766faf0c6" />

## Tableau Dashboard

<img width="1880" height="764" alt="image" src="https://github.com/user-attachments/assets/0a3df4c9-7aa2-451f-9d75-02d64c0754f1" />

## PowerBI Dashboard

- Management Centric
<img width="1178" height="669" alt="image" src="https://github.com/user-attachments/assets/a721950b-f207-45be-a8a7-9740c881b937" />

- Customer Centric
<img width="1179" height="670" alt="image" src="https://github.com/user-attachments/assets/f91b6640-ccd7-493c-931f-036554f3e35f" />

## Conclusion 
This project demonstrates how data analytics can transform hospitality operations. The dashboard enables AtliQ Grands to:
- Improve revenue management
- Enhance customer satisfaction
- Optimize room pricing
- Reduce cancellations
- Support strategic decision-making

By leveraging analytics, AtliQ Grands can strengthen its competitive position in the hospitality industry.














