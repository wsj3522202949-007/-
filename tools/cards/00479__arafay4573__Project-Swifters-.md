---
id: tool-00479
type: tool
area: 库
status: active
tags: [TTS, JavaScript, 协议未明, 需API密钥, 英文文档]
title: Project-Swifters-
summary: 小说转语音/有声书
source: https://github.com/arafay4573/project-swifters-
created: 2026-07-18
updated: 2026-07-18
no: 479
category: 二、网文 / 长篇 AI 写作系统 库
repo: arafay4573/Project-Swifters-
stars: 0
url: https://github.com/arafay4573/project-swifters-
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# arafay4573/Project-Swifters-

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/arafay4573/project-swifters-
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Ai story generator
- **本地描述**：Ai story generator
- **拉取时间**：2026-07-23 22:53:02

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Project Swifters – AI Story Video Generator

This is a full-stack application that allows users to generate personalized AI-based stories for kids and convert them into short animated videos with background music and narration.

## Features

-   **AI Story Generation:** Uses OpenAI's GPT-4 to generate personalized stories.
-   **AI Voice Generation:** Uses a Text-to-Speech API to create voice narrations.
-   **AI Video Generation:** Creates animated videos from the story and audio.
-   **User Authentication:** JWT-based authentication for user registration and login.
-   **Subscription Plans:** Free and Pro plans with Stripe integration.
-   **Cloud Storage:** Media files are stored in AWS S3.

## Tech Stack

-   **Frontend:** React, Vite, Tailwind CSS, Framer Motion
-   **Backend:** Node.js, Express.js (Vercel Serverless Functions)
-   **APIs:** OpenAI, Stripe, AWS S3

## Getting Started

### Prerequisites

-   Node.js (v18 or higher)
-   MongoDB account
-   OpenAI API key
-   Stripe account and API keys
-   AWS account and S3 bucket credentials

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/project-swifters.git
    cd project-swifters
    ```

2.  **Install backend dependencies:**
    ```bash
    cd api
    npm install
    ```

3.  **Install frontend dependencies:**
    ```bash
    cd ../frontend
    npm install
    ```

### Configuration

Create a `.env` file in the `api` directory and add the following variables:

```
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret
OPENAI_API_KEY=your_openai_api_key
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_REGION=your_aws_region
AWS_BUCKET_NAME=your_aws_bucket_name
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_WEBHOOK_SECRET=your_stripe_webhook_secret
CLIENT_URL=http://localhost:3000
```

### Running the Application

1.  **Start the backend server:**
    ```bash
    cd api
    npm start
    ```

2.  **Start the frontend development server:**
    ```bash
    cd ../frontend
    npm run dev
    ```

## Deployment (Vercel)

1.  Create a new project on Vercel and connect your GitHub repository.
2.  Vercel will automatically detect the monorepo configuration from the `vercel.json` file.
3.  Add your environment variables in the project settings.
4.  Deploy!
