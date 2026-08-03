---
id: tool-00859
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Customer-Data-Automation-Filtering-Using-n8n-and-Google-Sheets
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/saadhere123/customer-data-automation-filtering-using-n8n-and-google-sheets
created: 2026-07-18
updated: 2026-07-18
no: 859
category: 二、网文 / 长篇 AI 写作系统 库
repo: Saadhere123/Customer-Data-Automation-Filtering-Using-n8n-and-Google-Sheets
stars: 0
url: https://github.com/saadhere123/customer-data-automation-filtering-using-n8n-and-google-sheets
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Saadhere123/Customer-Data-Automation-Filtering-Using-n8n-and-Google-Sheets

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/saadhere123/customer-data-automation-filtering-using-n8n-and-google-sheets
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：This project showcases an end-to-end customer data processing workflow built using n8n (open-source automation tool) and Google Sheets. The main objective of this workflow is to retrieve customer records, clean and transform the data, generate derived fields, and filter records based on specific conditions without writing traditional backend code.
- **本地描述**：This project showcases an end-to-end customer data processing workflow built using n8n (open-source automation tool) and Google Sheets. The main objective of this workflow is to retrieve customer records, clean and transform the data, generate derived fields, and filter records based on specific conditions without writing traditional backend code.
- **拉取时间**：2026-07-23 23:04:04

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

Customer Data Automation & Filtering Using n8n and Google Sheets
📌 Project Overview

This project showcases an end-to-end customer data processing workflow built using n8n (open-source automation tool) and Google Sheets. The main objective of this workflow is to retrieve customer records, clean and transform the data, generate derived fields, and filter records based on specific conditions without writing traditional backend code.

The workflow is designed to run on a local (free) n8n setup, making it ideal for learners, students, and professionals who want to understand real-world data automation and ETL (Extract, Transform, Load) concepts.

📂 Dataset Description

The dataset represents customer information stored in a Google Sheet. Each row corresponds to one customer and includes the following fields:

Field Name	Description
row_number	Row index of the record in Google Sheets
id	Unique numeric identifier for each customer
first_name	Customer’s first name
last_name	Customer’s last name
email	Customer’s email address
gender	Gender identity of the customer
Country	Country of residence
🔹 Sample Data
id: 1
first_name: Constantina
last_name: Adelsberg
email: cadelsberg0@ebay.co.uk
gender: Female
Country: Argentina


The dataset contains diverse records from multiple countries such as China, Brazil, Indonesia, Russia, Argentina, and many others, allowing meaningful filtering and segmentation.

🔄 Workflow Architecture

The workflow is built using multiple n8n nodes, each performing a specific task in the data pipeline.

1️⃣ Manual Trigger

The workflow starts using the Manual Trigger node.

This allows the user to execute the workflow on demand during testing and development.

2️⃣ Customer Datastore

Retrieves customer records from an internal datastore.

Acts as the initial data source before enrichment from Google Sheets.

3️⃣ Google Sheets – Get Rows

Fetches rows from a connected Google Sheet.

Reads thousands of records in a structured JSON format.

Ensures data is dynamically pulled and updated.

4️⃣ Edit Fields (Data Transformation)

This step is responsible for cleaning and restructuring the data.

🔹 Fields Created / Mapped:

Fullname (String)

{{ $json.first_name }} {{ $json.last_name }}


Combines first and last names into a single readable field.

email (String)

{{ $json.email }}


Country (String)

{{ $json.Country }}


id (Number)

{{ $json.id }}


This step ensures that only the required fields are passed forward in a clean and consistent format.

5️⃣ IF Node – Conditional Filtering

The IF node is used to apply business logic and segment the data.

🔹 Condition Applied:
Country is equal to "China"


True Output → Customers from China

False Output → Customers from all other countries

This allows easy customer segmentation for analytics, reporting, or further automation.

6️⃣ Output Separation

Customers matching the condition are sent to a dedicated processing path.

Remaining customers are routed separately.

This structure can be extended to:

Store filtered data

Send emails

Push records to databases

Generate reports

🎯 Key Features

No-code / low-code automation

Real-world ETL workflow

Dynamic Google Sheets integration

Data transformation using expressions

Conditional logic for segmentation

Runs on free localhost n8n

🧠 Learning Outcomes

This project helps in understanding:

How automation tools replace manual data handling

Practical use of IF conditions in workflows

Field mapping and data normalization

Handling large datasets efficiently

Preparing structured data for analytics or CRM systems

🛠️ Tools & Technologies

n8n (Self-hosted / Localhost)

Google Sheets API

JSON Field Mapping

Conditional Logic

Manual Trigger for Testing

🚀 Use Cases

Customer data cleaning

Country-wise customer segmentation

Data preparation for dashboards

CRM data automation

Learning automation tools like n8n

📌 Future Enhancements

Store filtered data in a database

Add email notifications

Export filtered data to CSV

Integrate with BI tools like Power BI

Add error handling and logging
