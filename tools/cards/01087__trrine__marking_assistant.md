---
id: tool-01087
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: marking_assistant
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/trrine/marking_assistant
created: 2026-07-18
updated: 2026-07-18
no: 1087
category: 二、网文 / 长篇 AI 写作系统 库
repo: trrine/marking_assistant
stars: 0
url: https://github.com/trrine/marking_assistant
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# trrine/marking_assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/trrine/marking_assistant
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A tool to streamline marking and writing feedback for assignments. Built with Django, TypeScript and SQLite.
- **本地描述**：A tool to streamline marking and writing feedback for assignments. Built with Django, TypeScript and SQLite.
- **拉取时间**：2026-07-23 23:10:41

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Marking Assistant 📝

![image](https://github.com/trrine/marking_assistant/assets/41973043/e0df6aea-1534-47dd-a122-b6d36bb48133)

## Description

Marking Assistant is a practical tool developed to streamline the task of marking assignments and writing feedback for students. It simplifies the process of creating, managing, and marking assignments. With this app, you can:
- Define assignment tasks with total marks and grading criteria.
- Easily mark tasks by selecting met criteria.
- Automatically calculate student marks and generate feedback.
- Temporarily store results during your session.
- Export results to an Excel file.

As a tutor, I designed Marking Assistant to address the challenges I faced in marking assignments efficiently. It is a handy tool that automates certain tedious processes while keeping the human touch intact.

### Built With
- ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
- ![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
- ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## Features

### Adding Assignments
![image](https://github.com/trrine/marking_assistant/assets/41973043/29ab2c97-9c71-4369-a9c4-23a00564da33)

### Manage and Update Existing Assignments
![image](https://github.com/trrine/marking_assistant/assets/41973043/b6ddf322-aa2f-4060-938d-2f78ef90525a)

### Marking Assignment Tasks
![image](https://github.com/trrine/marking_assistant/assets/41973043/392b802e-d2a5-4574-a3e5-d7963c581cec)

### Exporting Marking Results
![image](https://github.com/trrine/marking_assistant/assets/41973043/26da357b-5f20-4a2e-9e70-e541ef301caf)

## Getting Started

### Prerequisites
* [Python ≥ 3.9](https://www.python.org/downloads/)

### Installation 
1. Clone the repo if you have git.
```
git clone https://github.com/trrine/marking_assistant.git
```
Or press Code➝Download ZIP.

2. Navigate to the location of the requirements file on your system and install the requirements.
```
cd PATH_TO_PROJECT
pip install -r requirements.txt
```
3. Run the following commands to setup the database:
```
python manage.py makemigrations
python manage.py migrate
```

## Starting the App
1. Navigate to the project location.
```
cd PATH_TO_PROJECT
```
2. Start the server
```
python manage.py runserver
```
3. Open your browser and go to:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

## TO DO:
- Write more unit and integration tests
- Add input validation
- Make design responsive
- Only display markable tasks with criteria
