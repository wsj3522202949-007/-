---
id: tool-00668
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: Natural-Language-Database-Query-Assistant
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/syednihal32/natural-language-database-query-assistant
created: 2026-07-18
updated: 2026-07-18
no: 668
category: 二、网文 / 长篇 AI 写作系统 库
repo: syednihal32/Natural-Language-Database-Query-Assistant
stars: 0
url: https://github.com/syednihal32/natural-language-database-query-assistant
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# syednihal32/Natural-Language-Database-Query-Assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/syednihal32/natural-language-database-query-assistant
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：ChatSQL DB is an interactive project that connects natural language with MySQL databases. It allows users to query their data in plain English without writing SQL commands. Powered by LangChain, it translates human language into SQL queries behind the scenes. A simple yet effective tool to make database interactions smarter and user-friendly.
- **本地描述**：ChatSQL DB is an interactive project that connects natural language with MySQL databases. It allows users to query their data in plain English without writing SQL commands. Powered by LangChain, it translates human language into SQL queries behind the scenes. A simple yet effective tool to make database interactions smarter and user-friendly.
- **拉取时间**：2026-07-23 22:58:31

---

**# Natural-Language-Database-Query-Assistant**
ChatSQL DB is an interactive project that connects natural language with MySQL databases. It allows users to query their data in plain English without writing SQL commands. Powered by LangChain, it translates human language into SQL queries behind the scenes. A simple yet effective tool to make database interactions smarter and user-friendly.

**Chat with SQL Database using LangChain**

**📌 Project Overview**

This project demonstrates how to build a chat-based interface to interact with SQL databases using LangChain.
It allows users to enter queries in plain English, which are then converted into SQL queries automatically.
The results are fetched from either a local SQLite database (student.db) or a MySQL database, depending on the user’s choice.

The project also includes a Streamlit UI where users can chat with the database directly.

**Features**
Query SQL databases in natural language.

Supports SQLite (local student.db) and MySQL.

Uses LangChain Agents for SQL query generation.

Simple Streamlit-based chat interface.

Configurable with Groq API key for LLM responses.

**📂 Project Structure**

ChatSQL-Assistant/
│── app.py              # Main Streamlit app (chat interface)  
│── sqlite.py           # Script to create SQLite DB and insert student data  
│── student.db          # SQLite database file  
│── requirements.txt    # Python dependencies  
│── README.md           # Documentation  



**🛠️ Tech Stack**

Python 3.10+

LangChain

SQLite3 / MySQL

Streamlit (for UI)

Groq LLM (LLaMA3)

**⚙️ Setup Instructions**

1️⃣ Clone the Repository
git clone https://github.com/syednihal32/Natural-Language-Database-Query-Assistant.git
cd ChatSQL-Assistant

2️⃣ Install Dependencies
pip install -r requirements.txt


3️⃣ Create SQLite Database

Run sqlite.py once to generate student.db with a STUDENT table:

python sqlite.py

This will create a student.db file and insert sample student records.

4️⃣ Run the Application
streamlit run app.py


**🎯 Usage**

Open the Streamlit UI in your browser (default: http://localhost:8501).

Choose between:

SQLite (student.db)

MySQL (enter host, username, password, and DB name)

Enter your Groq API Key in the sidebar.

Start chatting with the database in plain English.

Example Queries:

“Show all students from Data Science class”

“Get the names of students who scored more than 80 marks”

“List all students in section A”

| NAME   | CLASS        | SECTION | MARKS |
| ------ | ------------ | ------- | --related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
--- |
| Krish  | Data Science | A       | 90    |
| John   | Data Science | B       | 100   |
| Mukesh | Data Science | A       | 86    |
| Jacob  | DevOps       | A       | 50    |
| Dipesh | DevOps       | A       | 35    |

👨‍💻 Author

**SYED NIHAL**


**✅ Future Improvements**

Add support for multiple databases simultaneously.

Build an authentication system for database connections.

Extend to handle complex queries and visualizations.
