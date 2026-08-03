---
id: tool-01058
type: tool
area: 库
status: active
tags: [文风迁移, JavaScript, 协议未明, 本地优先, 英文文档, 改稿润色, 本地写作]
title: PromptSphere
summary: 风格微调/文风迁移
source: https://github.com/bekcodingaddict/promptsphere
created: 2026-07-18
updated: 2026-07-18
no: 1058
category: 二、网文 / 长篇 AI 写作系统 库
repo: BekCodingAddict/PromptSphere
stars: 0
url: https://github.com/bekcodingaddict/promptsphere
tier: "C"
use_case: "风格微调/文风迁移"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# BekCodingAddict/PromptSphere

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/bekcodingaddict/promptsphere
- **Stars**：0
- **语言**：JavaScript
- **License**：None
- **Topics**：nextjs, ssr, tailwindcss
- **GitHub 描述**：A Share Prompts Next.js app is a web application built using the Next.js framework, designed for sharing, discovering, and managing various prompts. These prompts could be related to creative writing, coding challenges, design ideas, or other areas where users seek inspiration or guidance.
- **本地描述**：A Share Prompts Next.js app is a web application built using the Next.js framework, designed for sharing, discovering, and managing various prompts. These prompts could be related to creative writing, coding challenges, design ideas, or other areas where users seek inspiration or guidance.
- **拉取时间**：2026-07-23 23:09:51

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# PromptSphere

> [!NOTE]
> A PromptSphere Next.js app is a web application built using the Next.js framework, designed for sharing, discovering, and managing various prompts. These >prompts could be related to creative writing, coding challenges, design ideas, or other areas where users seek inspiration or guidance.

## Features ⚙:

### ✍️ Prompt Sharing

- Users can submit their own prompts for others to use.

### 🔍 Exploration and Discovery

- A user-friendly interface to browse and explore prompts across various categories.

### 🔧 Search and Filter Options

- Advanced filters and search functionalities to easily find prompts by keywords, categories, or tags.

### 💬 Community Interaction

- Options to like, comment on, and discuss prompts, promoting community engagement.

### 👤 User Profiles

- Personalized profiles where users can view their submitted prompts, saved prompts, and interaction history.

### 📱 Responsive Design

- Ensures the app works well across desktops, tablets, and mobile devices.

### 🔐 Authentication

- Secure login, often using OAuth or similar methods, allowing users to manage their contributions and interactions securely.

### 🛠️ Content Management

- Backend management for reviewing and moderating user-generated prompts.

## What I learned 📚:
- Create API endpoing using Next.js and How to comunicate Front-end with back-end using HTTP Methods(GET,PUT,PATCH,POST,DELETE etc.)
- Creating Reusable component and code
- Next-Auth Authentication and session controlling

### Spesifically: Creating and using Lambda function

I have learned during this project declare and using javascript lambda function. I used it lambda function to connect my app to Mongodb.

This is my mongodb connection logic:

<details>
<summary><code>database.js</code></summary>
  
```js
import mongoose from "mongoose";

let isConnected = false; //track the connection

export const connectToDB = async () => {
  mongoose.set("strictQuery", true);

  if (isConnected) {
    console.log("MongoDB is already connected!");
    return;
  }

  try {
    await mongoose.connect(process.env.MONGODB_URL, {
      dbName: "PromptSphere",
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });

    isConnected = true;
    console.log("MongoDB Connected!");
  } catch (error) {
    console.log(error);
  }
};
```
</details>

This is my api route in next.js app . You can see here connectToDB() fuunction is connect and do task and after that it do not keep running.

<details>
<summary><code>route.js</code></summary>
  
```js
import Prompt from "@models/prompt";
import { connectToDB } from "@utils/database";

export const POST = async (req) => {
  const { userId, prompt, tag } = await req.json();
  try {
    await connectToDB();
    const newPrompt = new Prompt({
      creator: userId,
      prompt,
      tag,
    });
    await newPrompt.save();
    return new Response(JSON.stringify(newPrompt), { status: 201 });
  } catch (error) {
    console.log(error);
  }
};
```
</details>

## Problems & Challanges
| Error & Problem Title | Status | Difficult | Date |
|--|--|--|--|
|[🔄 params should be awaited ](https://github.com/BekCodingAddict/PromptSphere/blob/master/error-archive/params-should-be-awaited.md) | ![solved](https://img.shields.io/badge/solved-blue) | low | Jan 14, 2025 |
|[🔄 Missing Suspense boundary ](https://github.com/BekCodingAddict/PromptSphere/blob/master/error-archive/Suspense-boundary.md) | ![solved](https://img.shields.io/badge/solved-blue) | low | Jan 14, 2025 |
|[🖼️ Cannot use import statement outside a module](https://github.com/BekCodingAddict/PromptSphere/blob/master/error-archive/SyntaxError.md) | ![solved](https://img.shields.io/badge/solved-blue) | low | Jan 12, 2025 |
|[🗑️  Module exports error](https://github.com/BekCodingAddict/PromptSphere/blob/master/error-archive/module.exports-error.md) | ![solved](https://img.shields.io/badge/solved-blue) | low | Jan 13, 2025 |
