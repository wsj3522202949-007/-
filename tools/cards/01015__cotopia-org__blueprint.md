---
id: tool-01015
type: tool
area: 库
status: active
tags: [C#, 协议传染, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: blueprint
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/cotopia-org/blueprint
created: 2026-07-18
updated: 2026-07-18
no: 1015
category: 二、网文 / 长篇 AI 写作系统 库
repo: cotopia-org/blueprint
stars: 4
url: https://github.com/cotopia-org/blueprint
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# cotopia-org/blueprint

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/cotopia-org/blueprint
- **Stars**：4
- **语言**：C#
- **License**：GPL-3.0
- **Topics**：—
- **GitHub 描述**：This project is a Node-Based Process Automation System designed to allow users to automate their workflows without writing any code. The system provides an intuitive interface where users can create and manage their processes using a graphical node-based approach.
- **本地描述**：This project is a Node-Based Process Automation System designed to allow users to automate their workflows without writing any code. The system provides an intuitive interface where users can create and manage their processes using a graphical node-based approach.
- **拉取时间**：2026-07-23 23:08:37

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Blueprint
## Overview
This system is designed as a versatile workflow automation platform that allows users to create and manage automated workflows between various applications, services, and data sources. It empowers users to streamline processes and reduce manual intervention by connecting different tools in a cohesive, automated manner.

## Entities
### 1) Blueprint
A blueprint refers to a space where a set of nodes is located and is triggered by an event. During this process, a series of operations are performed. 
### 2) Node
A node is a fundamental component within the system. It represents an entity with its own data fields and associated scripts that collectively produce a specific output. Each node can have one or more outputs, allowing it to interact with other nodes and contribute to complex workflows. Nodes are designed to encapsulate specific functions or operations, making it easier to build and manage automated processes by connecting and configuring these components.
### 3) Process
Each blueprint, after being triggered by a webhook, pulse, delay, or manually, is converted into a process. Depending on the use case, processes can either remain active for a long time or be terminated quickly after the process is completed.
### 4)Account 
An account refers to a person who can create, manage, and modify blueprints and nodes in the system.

## Script language
In this system, the popular JavaScript language is used to create node code. This approach gives the system the ability to create or modify nodes without needing to restart the service.
