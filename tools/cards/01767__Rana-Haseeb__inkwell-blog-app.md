---
id: tool-01767
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: inkwell-blog-app
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/rana-haseeb/inkwell-blog-app
created: 2026-07-18
updated: 2026-07-18
no: 1767
category: 二、网文 / 长篇 AI 写作系统 库
repo: Rana-Haseeb/inkwell-blog-app
stars: 0
url: https://github.com/rana-haseeb/inkwell-blog-app
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

# Rana-Haseeb/inkwell-blog-app

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/rana-haseeb/inkwell-blog-app
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Inkwell is a full-stack blog platform built with Next.js, where users can write and publish posts using a rich-text editor with an AI writing assistant, engage through likes, comments, and follows, and track performance via a built-in analytics dashboard.
- **本地描述**：Inkwell is a full-stack blog platform built with Next.js, where users can write and publish posts using a rich-text editor with an AI writing assistant, engage through likes, comments, and follows, and track performance via a built-in analytics dashboard.
- **拉取时间**：2026-07-23 23:30:32

---

<div align="center">

<img src="https://img.shields.io/badge/-%E2%9C%92%EF%B8%8F_Inkwell-1a1a2e?style=for-the-badge&logoColor=white" alt="Inkwell" height="42" />

### A production-grade, full-stack blogging platform.
### Write. Publish. Discover. Analyse.

<br/>

[![Next.js](https://img.shields.io/badge/Next.js_15-black?style=flat-square&logo=next.js&logoColor=white)](https://nextjs.org/)
[![React](https://img.shields.io/badge/React_19-149ECA?style=flat-square&logo=react&logoColor=white)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript_5-3178C6?style=flat-square&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Prisma](https://img.shields.io/badge/Prisma_7-2D3748?style=flat-square&logo=prisma&logoColor=white)](https://www.prisma.io/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_v4-38BDF8?style=flat-square&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![Auth.js](https://img.shields.io/badge/Auth.js_v5-purple?style=flat-square&logo=auth0&logoColor=white)](https://authjs.dev/)
[![OpenRouter](https://img.shields.io/badge/OpenRouter_AI-FF6B35?style=flat-square&logoColor=white)](https://openrouter.ai/)

<br/>

[Features](#-features) · [Tech Stack](#️-tech-stack) · [Getting Started](#-getting-started) · [Project Structure](#️-project-structure) · [Deployment](#-deployment)

</div>

---

**Inkwell** is a full-stack blog platform built end-to-end on the **Next.js 15 App Router**. It pairs a polished writing experience with everything a modern reader expects — and wraps it in a fast, accessible, dark-mode-ready UI.

> No separate REST or GraphQL API. Every data operation is a **React Server Component** or **Server Action** — type-safe from database to browser.

<br/>

## ✨ Features

<details open>
<summary><strong>🔐 Authentication & Accounts</strong></summary>

<br/>

- **Email + password** sign-up and login with bcrypt-hashed credentials
- **Google OAuth** one-click sign-in via Auth.js v5
- **Role-based access control** — `USER` / `ADMIN` with middleware + server-side enforcement
- **Full profile management** — name, bio, avatar, password change
- **JWT sessions** — stateless, edge-compatible
- **Rate limiting** on registration, commenting, liking, and AI usage

</details>

<details open>
<summary><strong>🛡️ Admin Dashboard</strong></summary>

<br/>

- Protected `/admin` area — role-checked at the middleware **and** server level
- Platform overview: total users, posts, comments, likes
- **User management** — promote/demote roles, remove accounts
- **Post moderation** — unpublish or delete any post
- **Comment moderation** — remove any comment

</details>

<details open>
<summary><strong>✍️ Writing & Publishing</strong></summary>

<br/>

- **Rich-text editor** (TipTap) — headings, bullet & ordered lists, links, inline images
- **AI writing assistant** (OpenRouter, free-tier fallback chain):
  - ✦ Improve a selected passage in-place
  - ✦ Generate 5 title suggestions from your draft
  - ✦ Write a summary automatically
  - ✦ Suggest relevant tags
- **Cover images & in-editor image uploads** via UploadThing
- **Chip-style tag input** — tags are auto-created and reused across posts
- **Draft → Publish** workflow — toggle live from the editor footer
- Auto **slug generation** and **reading-time** estimate on save
- Author- and admin-scoped **edit / delete** authorization

</details>

<details open>
<summary><strong>📚 Reading & Discovery</strong></summary>

<br/>

- **Infinite-scroll feed** with cursor-based pagination — no page refreshes
- **Full-text search** across titles and summaries
- **Tag filter pages** (`/blog/tag/[slug]`) for topic browsing
- **Related stories** — same-tag / same-author suggestions on every post
- **Auto-generated table of contents** from post headings
- **Reading-progress bar** that tracks scroll position
- **Public author profiles** (`/author/[id]`) with bio and published work

</details>

<details open>
<summary><strong>💬 Engagement & Social</strong></summary>

<br/>

- **Likes** and **bookmarks** with optimistic UI (no spinner, instant feedback)
- **Personal Bookmarks page** to save stories for later
- **Threaded comments** with nested replies
- **Inline comment editing** with an "edited" marker
- **Follow authors** and a personalised **Following feed**
- **In-app notifications** — bell dropdown for likes, comments, replies, and follows
- **View counter** per post, tracked with a time-series event model
- **Share buttons** — X (Twitter), LinkedIn, and copy-link

</details>

<details open>
<summary><strong>📊 Analytics & SEO</strong></summary>

<br/>

- **Author analytics dashboard** — 30-day views, likes, and comments charted with [Recharts](https://recharts.org/)
- **Timestamped view tracking** (`PostView` events) powering the time-series; a denormalised `viewCount` counter keeps headline numbers fast
- **Top posts table** with per-post engagement breakdown
- **Dynamic `sitemap.xml`** — static pages, published posts, tags, and authors; revalidates hourly
- **`robots.txt`** that keeps `/dashboard`, `/admin`, and `/api/` out of the index
- **RSS feed** at `/feed.xml` — the 30 most recent posts; advertised via `<link rel="alternate">`

</details>

<details open>
<summary><strong>🎨 Experience & Accessibility</strong></summary>

<br/>

- **Light / Dark / System** theme switching (next-themes)
- Fully **responsive** across mobile, tablet, and desktop
- Accessible UI built on **shadcn/ui** (Base UI primitives)
- **Toast notifications** (Sonner) for every action
- Graceful **loading**, **error**, and **not-found** states throughout
- Per-page **SEO metadata**, Open Graph, and Twitter card tags

</details>

<br/>

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Framework** | [Next.js 15](https://nextjs.org/) — App Router, RSC, Server Actions, Middleware |
| **Language** | [TypeScript 5](https://www.typescriptlang.org/) · [React 19](https://react.dev/) |
| **Database** | [PostgreSQL](https://www.postgresql.org/) · [Prisma 7](https://www.prisma.io/) (driver adapter) |
| **Auth** | [Auth.js v5 / NextAuth](https://authjs.dev/) — Credentials + Google OAuth |
| **Styling** | [Tailwind CSS v4](https://tailwindcss.com/) · [shadcn/ui](https://ui.shadcn.com/) (Base UI) |
| **Editor** | [TipTap](https://tiptap.dev/) |
| **AI** | [OpenRouter](https://openrouter.ai/) — free model fallback chain (`gpt-oss-120b` → `gpt-oss-20b` → `llama-3.3-70b`) |
| **Charts** | [Recharts](https://recharts.org/) |
| **Uploads** | [UploadThing](https://uploadthing.com/) |
| **Validation** | [Zod v4](https://zod.dev/) |
| **Toasts** | [Sonner](https://sonner.emilkowal.ski/) |
| **Rate limiting** | In-memory sliding-window (per-route, per-user) |

<br/>

## 🚀 Getting Started

### Prerequisites

- **Node.js 18.18+**
- A **PostgreSQL** database — local, [Neon](https://neon.tech), or [Supabase](https://supabase.com)

### 1. Clone & install

```bash
git clone https://github.com/<your-username>/inkwell.git
cd inkwell
npm install
```

### 2. Configure environment

```bash
cp .env.example .env
```

Open `.env` and fill in every value — see the table below:

| Variable | Where to get it |
|---|---|
| `DATABASE_URL` | Your PostgreSQL connection string |
| `NEXTAUTH_URL` | `http://localhost:3000` in dev; your domain in prod |
| `NEXTAUTH_SECRET` | `openssl rand -base64 32` |
| `AUTH_GOOGLE_ID` | [Google Cloud Console](https://console.cloud.google.com/apis/credentials) |
| `AUTH_GOOGLE_SECRET` | Google Cloud Console |
| `UPLOADTHING_TOKEN` | [UploadThing dashboard](https://uploadthing.com/dashboard) |
| `OPENROUTER_API_KEY` | [openrouter.ai/keys](https://openrouter.ai/keys) *(optional — AI features hide when unset)* |

### 3. Set up the database

```bash
npm run db:migrate   # apply all migrations
npm run db:seed      # seed 10 demo users + 30 posts
```

### 4. Start the dev server

```bash
npm run dev
```

Open **[http://localhost:3000](http://localhost:3000)** 🎉

### 🔑 Demo credentials

After seeding you can sign in with any of the 10 demo accounts. Two to start with:

| Email | Password | Role |
|---|---|---|
| `alice@inkwell.dev` | `password123` | **Admin** |
| `bob@inkwell.dev` | `password123` | User |

All 10 accounts share the password `password123`. Emails follow the pattern `<name>@inkwell.dev` — alice, bob, carol, david, emma, farah, george, hana, ivan, julia.

<br/>

## 📜 Available Scripts

| Script | Description |
|---|---|
| `npm run dev` | Start the development server (with Turbopack) |
| `npm run build` | Create an optimised production build |
| `npm run start` | Run the production server |
| `npm run lint` | Lint with ESLint |
| `npm run db:migrate` | Create & apply a new migration |
| `npm run db:seed` | Seed the database with demo data |
| `npm run db:studio` | Open Prisma Studio (visual DB browser) |
| `npm run db:reset` | Drop, re-migrate, and re-seed (destructive) |

<br/>

## 🗂️ Project Structure

```
inkwell/
├── prisma/
│   ├── schema.prisma          # Full data model (User, Post, Tag, Comment, Like, …)
│   ├── migrations/            # Versioned SQL migration history
│   └── seed.ts                # 10 users · 30 posts · follows · bookmarks · analytics
│
├── src/
│   ├── actions/               # Server Actions
│   │   ├── posts.ts           # CRUD, view tracking (dual-write)
│   │   ├── comments.ts        # Create, edit, delete (threaded)
│   │   ├── engagement.ts      # Likes, bookmarks, follows
│   │   ├── profile.ts         # Avatar, bio, password change
│   │   └── ai.ts              # AI generation actions (rate-limited)
│   │
│   ├── app/
│   │   ├── (auth)/            # /login, /register (route group)
│   │   ├── admin/             # Admin dashboard — users, posts, comments
│   │   ├── api/               # Auth.js & UploadThing route handlers
│   │   ├── author/[id]/       # Public author profiles
│   │   ├── blog/              # Feed, post detail, search, tag pages
│   │   ├── dashboard/         # Create/edit, bookmarks, profile, analytics
│   │   ├── feed.xml/          # RSS 2.0 route handler
│   │   ├── sitemap.ts         # Dynamic sitemap.xml
│   │   └── robots.ts          # robots.txt
│   │
│   ├── components/
│   │   ├── auth/              # Login & register forms
│   │   ├── blog/              # PostCard, InfiniteFeed, CommentSection, …
│   │   ├── dashboard/         # DashboardHeader, AnalyticsChart
│   │   ├── editor/            # RichTextEditor, PostEditorForm, AIAssist, TagInput
│   │   ├── layout/            # Navbar, Footer, ThemeToggle
│   │   └── ui/                # shadcn/ui primitives (Button, Card, Input, …)
│   │
│   ├── lib/
│   │   ├── prisma.ts          # Singleton Prisma client (driver adapter)
│   │   ├── auth.ts            # Auth.js session helpers
│   │   ├── analytics.ts       # getAuthorAnalytics — time-series aggregation
│   │   ├── openrouter.ts      # OpenRouter client + fallback chain
│   │   ├── rate-limit.ts      # Sliding-window rate limiter
│   │   ├── site.ts            # SITE_NAME, getSiteUrl()
│   │   ├── utils/             # cn(), extractPlainText(), content helpers
│   │   └── validations/       # Zod schemas (posts, auth, ai, …)
│   │
│   ├── types/                 # Shared TypeScript types & interfaces
│   ├── auth.ts                # Auth.js v5 configuration
│   └── middleware.ts          # Route protection + role gating
```

<br/>

## ☁️ Deployment

### Recommended: Vercel + Neon (both free tiers)

**1. Neon — free PostgreSQL**

1. Create a free project at [neon.tech](https://neon.tech)
2. Copy the connection string — it looks like:
   ```
   postgresql://user:pass@ep-xxx.neon.tech/neondb?sslmode=require
   ```

**2. Vercel — free hosting**

1. Push this repo to GitHub
2. Import the repo at [vercel.com/new](https://vercel.com/new)
3. Add every variable from `.env.example` in **Project → Settings → Environment Variables**
4. Set `NEXTAUTH_URL` to your assigned Vercel domain (e.g. `https://inkwell.vercel.app`)
5. Deploy — Prisma generates the client automatically via `postinstall`

**3. Migrate & seed production**

Run once against your Neon database:
```bash
DATABASE_URL="<neon-url>" npx prisma migrate deploy
DATABASE_URL="<neon-url>" npx prisma db seed
```

> Any Node-compatible host works too — **Railway**, **Render**, **Fly.io** — just provision PostgreSQL and set the same environment variables.

**Google OAuth in production**

In [Google Cloud Console](https://console.cloud.google.com/apis/credentials) add your Vercel domain to:
- **Authorised JavaScript origins** — `https://your-app.vercel.app`
- **Authorised redirect URIs** — `https://your-app.vercel.app/api/auth/callback/google`

<br/>

## 🧭 Roadmap

| Status | Feature |
|---|---|
| 🔲 | Password reset & email verification via [Resend](https://resend.com) |
| 🔲 | Multi-instance rate limiting & AI quotas via [Upstash Redis](https://upstash.com) |
| 🔲 | Real-time notifications (WebSockets / SSE) |
| 🔲 | Post scheduling — set a future publish date |
| 🔲 | Newsletter / email digest for followers |

<br/>

## 📄 License

Released under the **MIT License** — free to use, learn from, and build upon.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<div align="center">

Built with ❤️ using Next.js 15, Prisma 7, and TypeScript.

</div>
