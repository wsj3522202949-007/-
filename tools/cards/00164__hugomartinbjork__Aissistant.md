---
id: tool-00164
type: tool
area: 库
status: active
tags: [互动叙事, TypeScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: Aissistant
summary: 互动叙事/聊天写故事
source: https://github.com/hugomartinbjork/aissistant
created: 2026-07-18
updated: 2026-07-18
no: 164
category: 二、网文 / 长篇 AI 写作系统 库
repo: hugomartinbjork/Aissistant
stars: 1
url: https://github.com/hugomartinbjork/aissistant
tier: "B"
use_case: "互动叙事/聊天写故事"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# hugomartinbjork/Aissistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/hugomartinbjork/aissistant
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：ai, django, nextjs, openai, python, react, typescript
- **GitHub 描述**：Aissistant is a GitHub repository that showcases my website built using Next.js and React as the frontend technologies, and Django as the backend framework. The website features a Trello board integration along with a writing assistant powered by the ChatGPT API, providing users with enhanced writing assistance and productivity tools.
- **本地描述**：Aissistant is a GitHub repository that showcases my website built using Next.js and React as the frontend technologies, and Django as the backend framework. The website features a Trello board integration along with a writing assistant powered by the ChatGPT API, providing users with enhanced writing assistance and productivity tools.
- **拉取时间**：2026-07-23 22:43:48

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Functional Specification:

## Title:

Web application for optimal productivity by utilizing chatbot assistant.

## Vision:

Our goal is to combine the highly relevant concept of text generating AI models with a clever UI for planning, structuring and optimizing your daily workflow. The solution shall offer image scanning for text generation using OCR (optical character recognition).

## Core functions:

- Automated writing assistant.
- An OCR feature that allows users to easily extract text from images and convert them into editable documents.
- A summarization tool that helps users quickly digest large amounts of text.
- An automatic language translation tool that enables users to communicate with people in other countries and cultures.
- An overview tool that helps users organize and prioritize their tasks, using an intuitive KanBan-inspired UI. This board can be customized to meet your exact needs.

# Technological Specification

## Client framework:

- Next.js
- React (TypeScript)

## Server framework/backend service setup:

- Django (REST framework)
- OpenAI API
- OCR library (Tesseract.js for example)

## Technology Choices:

React is a highly popular front end framework. To build the react app using TypeScript instead of plain JavaScript provides easy debugging and stability, something we value since the app also integrates third party API:s. Furthermore, instead of a normal React app we have chosen Next.js, mostly because it comes with index routing which simplifies code structure and project configuration. It is also great for optimizing client side performance and thereby improving the scalability of the project.

Django is out server site framework of choice for several reasons, the most important ones being:

- Robust backend structure that allows us to use a SQL database.
- High security with the Django REST framework authentication system.

## Deployment:

The web application will be deployed to a cloud platform such as Heroku. Continuous integration and deployment (CI/CD) will be implemented using gitlab version handling and Heroku built in support.
