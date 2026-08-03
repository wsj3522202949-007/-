---
id: tool-00923
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 需API密钥, 中文友好, 大纲规划, 多Agent, 灵感创意]
title: StoryArchitectAI
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/ou-jiajian/storyarchitectai
created: 2026-07-18
updated: 2026-07-18
no: 923
category: 二、网文 / 长篇 AI 写作系统 库
repo: ou-jiajian/StoryArchitectAI
stars: 0
url: https://github.com/ou-jiajian/storyarchitectai
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# ou-jiajian/StoryArchitectAI

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ou-jiajian/storyarchitectai
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：An AI-powered tool for novel writing
- **本地描述**：An AI-powered tool for novel writing
- **拉取时间**：2026-07-23 23:05:59

---

# 项目规划：Story Architect AI (故事架构师AI)

这是一个旨在利用大型语言模型（LLM）辅助小说创作的工具。它通过结构化的方式，引导用户从核心概念到最终章节的完整创作流程，并提供一致性校验，确保故事的逻辑严谨性。

---

### 核心架构

项目采用前后端分离的架构，并支持连接多个主流 AI 提供商。

1.  **前端 (Frontend):** 一个纯粹的单页面应用 (`index.html`)，负责用户界面、项目管理和 AI 设置。它通过调用后端 API 来管理项目数据。
2.  **后端 (Backend):** 一个基于 Python FastAPI 的 API 服务器，负责处理项目文件的增删改查，并作为调用各种大模型服务的统一网关。
3.  **数据存储 (Data):** 所有故事项目都以独立的 `.json` 文件形式存储在 `data/` 目录中，实现了简单、可靠的持久化。

---

### 一、功能模块

#### 1. 前端 (Client-Side)

-   **项目仪表盘:** 以卡片形式展示所有故事项目，提供创建、查看、删除功能。
-   **AI 设置面板 (Settings):**
    -   允许用户在不同的 AI 提供商（如 Google, OpenAI, Anthropic 等）之间进行选择。
    -   用户在此输入自己的 API 密钥。
    -   **关键机制:** 用户的设置（提供商和密钥）被安全地存储在**浏览器的 `localStorage`** 中，不会永久保存在后端服务器，确保了用户密钥的安全。
-   **项目创建/查看:** 通过模态框（Modal）提供非侵入式的用户体验。

#### 2. 后端 (Server-Side API)

-   **项目管理 API:**
    -   `GET /api/projects`: 获取所有项目的元数据列表。
    -   `POST /api/projects`: 创建一个新项目。这是核心的 AI 调用入口。
    -   `GET /api/projects/{project_id}`: 获取单个项目的完整数据。
    -   `DELETE /api/projects/{project_id}`: 删除一个项目。
-   **AI 提供商网关 (AI Gateway):**
    -   `create_project` 端点会接收前端传来的 `provider` 和 `api_key`。
    -   后端根据 `provider` 参数，动态地选择相应的 SDK（如 `google-generativeai`, `openai`, `anthropic`）和适配的 Prompt 来调用 AI 模型。
    -   这种设计将 API 调用的复杂性和适配逻辑统一放在了后端，使前端可以轻松支持新的 AI 模型。

---

### 二、技术栈 (Tech Stack)

-   **前端:** Vanilla JavaScript (ES6+), HTML5, CSS3。无框架，以保持轻量和简单。
-   **后端:** Python 3, FastAPI, Uvicorn。
-   **AI SDKs:** `google-generativeai`, `openai`, `anthropic`。
-   **数据存储:** JSON 文件系统。

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

### 三、如何运行

1.  **安装依赖:**
    ```bash
    # 进入后端目录
    cd backend
    # 创建并激活虚拟环境
    python3 -m venv .venv
    source .venv/bin/activate
    # 安装所有需要的库
    pip install -r requirements.txt 
    ```
    *(注意: 我们需要创建一个 `requirements.txt` 文件)*

2.  **启动后端服务:**
    ```bash
    # 确保你在 backend 目录下并且虚拟环境已激活
    uvicorn main:app --reload
    ```
    服务将运行在 `http://127.0.0.1:8000`。

3.  **打开前端页面:**
    - 在你的网页浏览器中直接打开 `frontend/index.html` 文件。

4.  **配置 AI 提供商:**
    - 在页面右上角点击 "Settings"。
    - 选择你希望使用的 AI 提供商，并填入你自己的 API 密钥。
    - 点击 "Save Settings"。

5.  **开始创作!**
