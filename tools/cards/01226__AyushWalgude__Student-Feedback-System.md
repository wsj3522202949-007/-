---
id: tool-01226
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Student-Feedback-System
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/ayushwalgude/student-feedback-system
created: 2026-07-18
updated: 2026-07-18
no: 1226
category: 二、网文 / 长篇 AI 写作系统 库
repo: AyushWalgude/Student-Feedback-System
stars: 0
url: https://github.com/ayushwalgude/student-feedback-system
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
content_hash: 9e4d639071fe40e4
  - methods/最强写作方法论_全球最强综合版.md
---

# AyushWalgude/Student-Feedback-System

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ayushwalgude/student-feedback-system
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A full-stack Student Feedback System built with Streamlit, Python, and MySQL. Features role-based authentication (Admin & Student), student self-registration, 5-category feedback ratings, real-time analytics dashboard, and complete CRUD management — all without writing HTML/CSS.
- **本地描述**：A full-stack Student Feedback System built with Streamlit, Python, and MySQL. Features role-based authentication (Admin & Student), student self-registration, 5-category feedback ratings, real-time analytics dashboard, and complete CRUD management — all without writing HTML/CSS.
- **拉取时间**：2026-07-23 23:14:51

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Student-Feedback-System
A full-stack Student Feedback System built with Streamlit, Python, and MySQL. Features role-based authentication (Admin &amp; Student), student self-registration, 5-category feedback ratings, real-time analytics dashboard, and complete CRUD management — all without writing HTML/CSS.
# 🎓 Student Feedback System

A full-stack web application for collecting and managing student feedback on faculty, built entirely in Python using Streamlit and MySQL.

## ✨ Features
- 🔐 Role-based authentication (Admin & Student portals)
- 📝 Student self-registration with ID verification
- ⭐ 5-category feedback ratings (Teaching, Communication, Punctuality, Knowledge, Overall)
- 📊 Admin dashboard with stats, top-rated teachers, and analytics charts
- 🗑️ Full CRUD — add/view/delete students, teachers, feedback, and admins
- 🚫 Duplicate feedback prevention per student-teacher pair

## 🛠️ Tech Stack
- **Frontend:** Streamlit (pure Python, no HTML/CSS)
- **Backend:** Python
- **Database:** MySQL

## 🚀 Quick Start
bash<br>
pip install -r requirements.txt<br>
mysql -u root -p < database.sql<br>
streamlit run app.py<br>


## 📁 Project Structure

student_feedback/<br>
├── app.py            # Main entry point<br>
├── db.py             # Database connection<br>
├── auth.py           # Login & registration<br>
└── pages/            # Modular page components<br>


## 📄 Documentation
Full project documentation available in `StudentFeedbackSystem_Documentation.docx`

## NOTE
login first with admin's id and password which is add in database.
