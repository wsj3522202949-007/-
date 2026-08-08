---
id: tool-00232
type: tool
area: 库
status: active
tags: [Java, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: AITestCodeGenerator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/manesshakumar/aitestcodegenerator
created: 2026-07-18
updated: 2026-07-18
no: 232
category: 二、网文 / 长篇 AI 写作系统 库
repo: Manesshakumar/AITestCodeGenerator
stars: 0
url: https://github.com/manesshakumar/aitestcodegenerator
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
content_hash: b73af4172e0e2f16
  - methods/最强写作方法论_全球最强综合版.md
---

# Manesshakumar/AITestCodeGenerator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/manesshakumar/aitestcodegenerator
- **Stars**：0
- **语言**：Java
- **License**：None
- **Topics**：—
- **GitHub 描述**：Test Code Generation from User Story
- **本地描述**：Test Code Generation from User Story
- **拉取时间**：2026-07-23 22:45:50

---

# AI-Powered Selenium Test Generator



## Overview
This project automaticall![GIFTestcode](https://github.com/user-attachments/assets/092d63d7-9e36-40dc-a9cc-651fa4aa4915)
y generates **Selenium + TestNG test classes** in Java from user stories using the **Gemini-2.5-Flash** AI model. The generated tests include:

- Screenshots on test failure with attachment
- Clear and maintainable test code with proper **TestNG assertions**.
- One `@Test` method per logical test case.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## How It Works
1. **Write a User Story**  
   Define your user story with acceptance criteria. Example:

   ```text
   As a registered user,
   I want to log in to the website with valid credentials
   so that I can access my dashboard.

   Acceptance Criteria:
   - Navigate to https://opensource-demo.orangehrmlive.com/
   - Verify the Page Title
   - Enter valid username and password
   - Verify successful login by checking dashboard visibility or Page Title
