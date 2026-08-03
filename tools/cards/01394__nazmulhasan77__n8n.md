---
id: tool-01394
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: n8n
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/nazmulhasan77/n8n
created: 2026-07-18
updated: 2026-07-18
no: 1394
category: 二、网文 / 长篇 AI 写作系统 库
repo: nazmulhasan77/n8n
stars: 0
url: https://github.com/nazmulhasan77/n8n
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# nazmulhasan77/n8n

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/nazmulhasan77/n8n
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：An open-source workflow automation platform built with n8n. Design, execute, and manage automated workflows connecting apps, APIs, and services without writing extensive code. Includes user authentication, secure data storage, and custom integrations.
- **本地描述**：An open-source workflow automation platform built with n8n. Design, execute, and manage automated workflows connecting apps, APIs, and services without writing extensive code. Includes user authentication, secure data storage, and custom integrations.
- **拉取时间**：2026-07-23 23:19:46

---

# n8n
## **1. Install via npm (Node.js required)**

### **Step 1: Install Node.js**

n8n requires **Node.js 18 or 20** (LTS recommended). Since you’re on macOS:

```bash
brew install node@20
```

Or download from [Node.js official site](https://nodejs.org/).

Check version:

```bash
node -v
npm -v
```

---

### **Step 2: Install n8n globally**

```bash
npm install -g n8n
```

Check installation:

```bash
n8n --version
```

---

### **Step 3: Run n8n**

```bash
n8n
```

By default, it runs on:

```
http://localhost:5678
```

Open in your browser to access the UI.

---

## **2. Install via Docker (recommended for isolation)**

If you have Docker installed:

```bash
docker run -it --rm \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

* `-p 5678:5678` → maps the port
* `-v ~/.n8n:/home/node/.n8n` → saves workflow data

---

## **3. Optional: Start n8n as a service (auto start)**

For macOS using `brew services`:

```bash
brew install n8n
brew services start n8n
```

Or use **pm2** to keep it running:

```bash
npm install -g pm2
pm2 start n8n
pm2 save
```

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

✅ After this, n8n will be running and you can start building automation workflows.
