---
id: tool-00415
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: flowpilot
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/nikhilrana13/flowpilot
created: 2026-07-18
updated: 2026-07-18
no: 415
category: 二、网文 / 长篇 AI 写作系统 库
repo: nikhilrana13/flowpilot
stars: 0
url: https://github.com/nikhilrana13/flowpilot
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

# nikhilrana13/flowpilot

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/nikhilrana13/flowpilot
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：FlowPilot is an AI-powered workflow automation platform that enables developers to visually build, execute, and monitor API-driven workflows using a drag-and-drop interface.  Instead of writing complex backend automation logic, developers can create reusable workflows, publish them as webhooks, and integrate them into any application with a single 
- **本地描述**：FlowPilot is an AI-powered workflow automation platform that enables developers to visually build, execute, and monitor API-driven workflows using a drag-and-drop interface.  Instead of writing complex backend automation logic, developers can create reusable workflows, publish them as webhooks, and integrate them into any application with a single
- **拉取时间**：2026-07-23 22:51:14

---

# 🚀 FlowPilot

FlowPilot is an AI-powered workflow automation platform that enables developers to visually build, execute, and monitor API-driven workflows using a drag-and-drop interface.

Instead of writing complex backend automation logic, developers can create reusable workflows, publish them as webhooks, and integrate them into any application with a single API call.

Inspired by tools like n8n and Zapier, FlowPilot focuses on simplicity, developer experience, and AI-powered automation.

---

## ✨ Features

### 🎨 Workflow Builder

- Drag & Drop Visual Workflow Builder
- Manual Trigger
- Webhook Trigger
- HTTP Request Node
- Gemini AI Node
- Response Node

### ⚡ Workflow Execution

- Real-Time Execution Progress
- Live Node Status
- Execution Timeline
- Execution Duration
- Success & Failed States
- Detailed Execution Logs
- Node Output Inspector

### 🚀 Platform

- Workspace Management
- JWT Authentication
- Real-Time Updates using Socket.io
- Responsive Dashboard
- Docker Support

---

## 💡 Example Workflow

```text
Webhook Trigger
        │
        ▼
HTTP Request
        │
        ▼
Gemini AI
        │
        ▼
Response
```

---

## 🌐 Webhook Integration

Every published workflow generates a unique webhook endpoint.

Applications can trigger workflows without implementing the automation logic inside their backend.

### Request

```http
POST /api/webhook/{workflowId}
```

```json
{
  "city": "Mohali"
}
```

### Response

```json
{
  "current_weather_summary": "...",
  "clothing_recommendation": "...",
  "carry_umbrella": false
}
```

This allows developers to integrate AI-powered workflows into any application with a simple HTTP request.

---

## 📌 Supported Nodes

- Manual Trigger
- Webhook Trigger
- HTTP Request
- Gemini AI
- Response

More workflow nodes coming soon.

---

## 📊 Execution Monitoring

Each workflow execution provides:

- Live execution progress
- Node execution status
- Execution duration
- Detailed logs
- Node outputs
- Error tracking
- Execution timeline

---

## 🛠 Tech Stack

### Frontend

- Next.js
- React
- React Flow
- Tailwind CSS
- Redux Toolkit
- RTK Query
- React Hook Form
- Socket.io Client

### Backend

- Node.js
- Express.js
- MongoDB
- Mongoose
- Socket.io
- JWT Authentication
- Gemini API

---

## 💼 Use Cases

FlowPilot can be used to build automations such as:

- 🌦 Weather Assistant
- 🤖 AI Content Generator
- 📄 Resume Analyzer
- 📧 Email Summarizer
- 🛍 Product Recommendation
- 📑 Invoice Processing
- 💬 Customer Support Automation
- 🔄 Data Transformation APIs

---


## 🚀 Getting Started

### Clone Repository

```bash
git clone https://github.com/your-username/FlowPilot.git
```

---

### Install Backend

```bash
cd backend
npm install
npm run dev
```

---

### Install Frontend

```bash
cd frontend
npm install
npm run dev --webpack
```

---

## 🐳 Docker

```bash
docker compose up --build
```

---

## 🌍 Environment Variables

### Backend

```env
PORT=
MONGO_URI=
JWT_SECRET=
GEMINI_API_KEY=
FRONTEND_URL=
```

### Frontend

```env
NEXT_PUBLIC_BACKEND_URL=
```

---

## 📈 Roadmap

- Google Sheets Integration
- Scheduler Trigger
- Delay Node
- Conditional Node
- Variables
- Loop Node
- Email Automation
- Slack Integration
- Discord Integration
- Workflow Templates
- Multi-user Collaboration

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Why FlowPilot?

FlowPilot helps developers automate backend workflows without writing repetitive automation logic. Design workflows visually, expose them through webhooks, integrate them into any application, and monitor every execution in real time.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

Made with ❤️ using Next.js, Node.js, Express.js, MongoDB, Socket.io, and Gemini AI.
