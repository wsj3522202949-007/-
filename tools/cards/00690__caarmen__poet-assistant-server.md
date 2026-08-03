---
id: tool-00690
type: tool
area: 库
status: active
tags: [Kotlin, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: poet-assistant-server
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/caarmen/poet-assistant-server
created: 2026-07-18
updated: 2026-07-18
no: 690
category: 二、网文 / 长篇 AI 写作系统 库
repo: caarmen/poet-assistant-server
stars: 0
url: https://github.com/caarmen/poet-assistant-server
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# caarmen/poet-assistant-server

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/caarmen/poet-assistant-server
- **Stars**：0
- **语言**：Kotlin
- **License**：NOASSERTION
- **Topics**：java, kotlin, rest-api, scala, spring-boot
- **GitHub 描述**：REST API for English-language tools for writing poetry (Spring boot)
- **本地描述**：REST API for English-language tools for writing poetry (Spring boot)
- **拉取时间**：2026-07-23 22:59:09

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Poet Assistant Server

This server contains a read-only embedded database with dictionaries for rhymes, synonyms/antonyms and definitions.

Refer to the [documentation](https://caarmen.github.io/poet-assistant-server)
for the list of endpoints and how to use them.

## Test it out
The app is available on heroku: https://poet-assistant-rest.herokuapp.com/

## Architecture
The app contains the following modules:

<img src="modules/doc/src/main/plantuml/object-diagram.png">

* Bottom:
  - `repository`: Accesses the database and exposes functions to retrieve Entities
* Top:
  - `api`: Defines the REST endpoints
* Middle:
  - `service`:  Contains the business logic required to map Entities to Model objects
* Other:
  - `doc`: Generates documentation
  - `app`: Contains the application class

## Tech stack

The main branch is implemented in Kotlin with Spring Boot and Gradle.

There are other branches of this project, using other implementations. They may not be as up-to-date as the main branch:
* [Scala (Spring Boot, Gradle)](https://github.com/caarmen/poet-assistant-server/tree/scala)
* [Java (Spring Boot, Gradle)](https://github.com/caarmen/poet-assistant-server/tree/java)
