---
id: tool-01641
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: aiStory
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/sudipsharma826/aistory
created: 2026-07-18
updated: 2026-07-18
no: 1641
category: 二、网文 / 长篇 AI 写作系统 库
repo: sudipsharma826/aiStory
stars: 2
url: https://github.com/sudipsharma826/aistory
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# sudipsharma826/aiStory

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/sudipsharma826/aistory
- **Stars**：2
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI-powered storybook generator that creates personalized illustrated and narrated stories using Next.js, OpenAI, ElevenLabs, and Redis.
- **本地描述**：AI-powered storybook generator that creates personalized illustrated and narrated stories using Next.js, OpenAI, ElevenLabs, and Redis.
- **拉取时间**：2026-07-23 23:26:54

---

# 🌟 aiStoryGenerator

**aiStoryGenerator** is a **full-stack AI-powered storybook generator** that lets users create, review, and share **interactive, illustrated, and narrated storybooks** — all powered by advanced AI services.  
It combines a beautiful UI, modern architecture, and secure authentication for a seamless creative experience.

---

## 🚀 Features

- 🧩 **Full-Stack Architecture**  
  Built with **Next.js (App Router)** and **TypeScript**, using **Server Actions** for scalable and modern development.

- 🔐 **Authentication**  
  Secure login via **NextAuth.js**, supporting **Google** and **GitHub** providers.

- ✍️ **AI Story Generation**  
  Create stories with customizable **tone**, **genre**, **title**, and **moral**, powered by **OpenAI**, **Gemini**, **Groq**, and **OpenRouter**, orchestrated via **Inngest** and **AgentKit**.

- 🎙️ **AI Voice Narration**  
  Generate dynamic story voiceovers using **ElevenLabs**, with a fallback to system-generated voices.

- 🖼️ **AI Cover Image Generation**  
  Automatically produce unique cover images for every story.

- ⚡ **Caching**  
  Integrated **Redis** for efficient caching and faster performance.

- 🗃️ **Database & Storage**  
  Persistent storage with **PostgreSQL** and **Prisma ORM**, plus **Supabase** for file management and scalability.

- 📧 **Email Notifications**  
  Automated notifications using **Resend**.

- ⭐ **Story Review System**  
  Readers can post text reviews and give star ratings.

- 📚 **Dashboard & Sharing**  
  Manage your stories with a personal dashboard and control public/private visibility.

- 📖 **Realistic Book Flip Animation**  
  Immersive reading experience using **`react-pageflip`**.

- 🧾 **Form Handling**  
  Robust and validated forms using **React Hook Form**.

- 🎨 **Modern UI/UX**  
  Fully responsive design with **Tailwind CSS**, custom loaders, toasts, and reusable components.

---

## 🧠 Tech Stack

| Category           | Technologies                                                    |
| ------------------ | --------------------------------------------------------------- |
| **Frontend**       | Next.js (App Router), TypeScript, Tailwind CSS, React Hook Form |
| **Backend**        | Next.js API Routes, Server Actions, Inngest, AgentKit           |
| **AI Services**    | OpenAI, Gemini, Groq, OpenRouter, ElevenLabs                    |
| **Database**       | PostgreSQL, Prisma ORM                                          |
| **Caching**        | Redis                                                           |
| **Authentication** | NextAuth.js (Google, GitHub)                                    |
| **Email**          | Resend                                                          |
| **Storage**        | Supabase Bucket                                                 |
| **UI/UX**          | Tailwind CSS, React PageFlip, custom loaders/toasts             |

---

## Folder Structure

- `app/` - Next.js app directory (pages, API routes, layouts)
- `components/` - Reusable React components (UI, forms, book pages, etc.)
- `lib/` - Utility libraries (auth, database, AI agents, actions)
- `prisma/` - Prisma schema and migrations
- `public/` - Static assets

## Getting Started

1.  **Clone the repository**

    ```sh
    git clone <repo-url>
    cd my-app
    ```

2.  **Install dependencies**

    ```sh
    npm install
    # or
    yarn install
    ```

3.  **Set up environment variables**

        Create a .env.local file in the root directory and add the required environment variables.

    Use the .env.example file as a reference.

4.  **Run database migrations**

    ```sh
    npx prisma migrate dev
    ```

5.  **Start the development server**

    ```sh
    npm run dev
    # or
    yarn dev
    ```

6.  **Open the app**

    Visit [https://aistory.sudipsharma.com.np](https://aistory.sudipsharma.com.np) in your browser.

## Usage

- Sign in with Google or GitHub.
- Generate a new story by selecting tone, genre, and other options.
- Review, rate, and share your stories.
- Enjoy book-style reading with flip animation and AI voice narration.
- Manage your stories from the dashboard.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements and bug fixes.

## License

MIT License

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

**aiStoryGenerator** – Create, narrate, and share AI-powered storybooks with ease!
