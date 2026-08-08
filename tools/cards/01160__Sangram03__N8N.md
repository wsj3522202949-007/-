---
id: tool-01160
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: N8N
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/sangram03/n8n
created: 2026-07-18
updated: 2026-07-18
no: 1160
category: 二、网文 / 长篇 AI 写作系统 库
repo: Sangram03/N8N
stars: 1
url: https://github.com/sangram03/n8n
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 48872cf2fb39f548
  - methods/最强写作方法论_全球最强综合版.md
---

# Sangram03/N8N

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/sangram03/n8n
- **Stars**：1
- **语言**：None
- **License**：None
- **Topics**：n8n, n8n-automation, n8n-community-node-package, n8n-nodes, n8n-tutorial, n8n-webhook, n8n-workflow
- **GitHub 描述**：n8n (Node-N-Node) is an open-source workflow automation platform that allows you to connect applications, APIs, and databases to automate tasks without writing full code. It uses a visual, node-based editor where each block (node) performs an action like sending an email, calling an API, reading a database, or processing data.
- **本地描述**：n8n (Node-N-Node) is an open-source workflow automation platform that allows you to connect applications, APIs, and databases to automate tasks without writing full code. It uses a visual, node-based editor where each block (node) performs an action like sending an email, calling an API, reading a database, or processing data.
- **拉取时间**：2026-07-23 23:12:52

---

# ⭐ **n8n in Details (Beginner to Advanced Explanation)**

---

## Create your account here
https://n8n-cg6a.onrender.com

## Rule For Used
https://github.com/Sangram03/N8N/blob/main/Rule%20zFor%20used.md

## Create your own n8n automation tools
https://github.com/Sangram03/N8N/blob/main/CreateYourOwnN8N.md

# ✅ **What is n8n?**

**n8n (node-n-node)** is an **open-source workflow automation tool** that allows you to connect apps, APIs, databases, and AI tools **without writing full code**.

It is similar to **Zapier, Make.com**, but more powerful because:

* Completely **free & open-source**
* You can **self-host**
* Supports **JavaScript functions**
* Connects to **APIs, databases, webhooks, triggers**

You create **workflows** using **nodes** (blocks).

<img  alt="image" src="https://github.com/user-attachments/assets/26c645b6-bdf3-4895-8f74-aba058c6ad2c" />




---

# 🧩 **Key Components of n8n**

Here are the **core building blocks**:

## 1️⃣ **Trigger Nodes**

Start the workflow automatically.

Examples:

* Webhook Trigger
* Cron Trigger
* Gmail Trigger
* Discord Trigger
* Schedule trigger

## 2️⃣ **Regular Nodes (Action Nodes)**

Perform tasks like:

* Send email
* Insert DB entries
* Fetch API
* If condition
* Split data
* Merge data

## 3️⃣ **Credentials**

Secure login info for apps:

* API keys
* OAuth tokens
* Database credentials

## 4️⃣ **Workflow Execution Engine**

This runs your workflow step by step.

## 5️⃣ **n8n Editor UI**

Drag-and-drop interface where you design workflows.

## 6️⃣ **Database**

Stores:

* workflows
* credentials
* execution history

(Default = SQLite, but supports Postgres/MySQL)

---

# 📦 **n8n Detailed Architecture Diagram (Explained)**

---

## 🔥 **Architecture Overview**

### **1. Frontend (n8n Editor UI)**

* Built in Vue.js
* Displays nodes, connections, history
* Sends workflow design changes → backend

### **2. Backend (n8n Core Engine)**

* Executes workflows
* Handles triggers
* Stores credentials securely
* Runs node logic (API calls, functions, automation steps)

### **3. Trigger System**

* Webhooks
* Cron jobs
* Event triggers (Gmail, Slack, GitHub etc.)

### **4. Worker Process (optional in scalable setup)**

Used in production to run workflows parallelly.

### **5. Message Queue (Redis)**

Used when scaling horizontally.

### **6. Database**

Stores:

* workflows
* execution logs
* users
* credentials (encrypted)

### **7. External Services**

n8n interacts with:

* APIs
* Databases
* SaaS tools (Gmail, Stripe, GitHub)
* AI/LLMs (OpenAI, Gemini, Claude)
* Custom scripts

---

# 🔄 **n8n Internal Workflow Execution Flow**

---

### **Step-by-step:**

1. **Trigger activates**
   Example: webhook receives data.

2. **Backend receives event**
   n8n engine starts workflow execution.

3. **Node 1 executes**
   Node runs API/database/logic.

4. **Node passes output to next node**
   Every node receives **JSON** input and returns **JSON output**.

5. **Continue until last node**
   Task completed.

6. **Execution log saved**
   You can view executions later.

---

# 🏗️ **n8n Deployment Structure**

There are 3 major ways to run n8n:

## ✔️ 1. **Cloud**

* Easiest
* Fully managed

## ✔️ 2. **Self-Hosted (Docker)**

Most popular.

Architecture:

```
User → Browser (UI)
        |
        v
Nginx → n8n Server → Redis (optional)
                      |
                      v
                    Database (Postgres)
```

## ✔️ 3. **Kubernetes (Scalable Enterprise)**

Used by big companies.

---

# 🎯 **Summary for Interviews**

Here is a short summary you can use:

> **n8n is an open-source, node-based workflow automation platform.
> It connects APIs, databases, and services using triggers and nodes.
> It has a modular architecture including UI editor, workflow engine, triggers, worker processes, and database storage.
> Workflows execute step-by-step with JSON data passing between nodes.
> It supports self-hosting, API integration, and scale-out processing using Redis + multiple workers.**

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# ✅ Want me to create a **custom diagram** for you?

I can create a full **PNG diagram** showing:

* Nodes
* Trigger
* Engine
* Database
* Workers
* API flow

Just tell me:

**“Make a clean n8n architecture diagram for my notes”** or
**“Create a workflow diagram for n8n automation.”**
