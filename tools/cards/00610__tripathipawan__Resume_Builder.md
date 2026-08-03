---
id: tool-00610
type: tool
area: 库
status: active
tags: [TypeScript, 协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: Resume_Builder
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/tripathipawan/resume_builder
created: 2026-07-18
updated: 2026-07-18
no: 610
category: 二、网文 / 长篇 AI 写作系统 库
repo: tripathipawan/Resume_Builder
stars: 0
url: https://github.com/tripathipawan/resume_builder
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

# tripathipawan/Resume_Builder

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/tripathipawan/resume_builder
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A full-featured, production-grade resume builder built with React, TypeScript, and Redux Toolkit. It comes with an AI writing assistant, live resume preview, 4 customizable templates, PDF export, Firebase-backed authentication, a personal dashboard, and a resume analytics page — all wrapped in a polished dark/light themed UI.
- **本地描述**：A full-featured, production-grade resume builder built with React, TypeScript, and Redux Toolkit. It comes with an AI writing assistant, live resume preview, 4 customizable templates, PDF export, Firebase-backed authentication, a personal dashboard, and a resume analytics page — all wrapped in a polished dark/light themed UI.
- **拉取时间**：2026-07-23 22:56:51

---

# 📄 Resume Builder — AI-Powered Resume Creation Platform

A full-featured, production-grade resume builder built with React, TypeScript, and Redux Toolkit. It comes with an AI writing assistant, live resume preview, 4 customizable templates, PDF export, Firebase-backed authentication, a personal dashboard, and a resume analytics page — all wrapped in a polished dark/light themed UI.

---

## 📌 Overview

Resume Builder is a complete web application that walks users through creating a professional resume from scratch. After signing up, users land on a personal dashboard where they can manage their resumes, track views and downloads, and jump into the builder. The builder itself is a two-panel layout — a section editor on the left and a live preview on the right — with a top bar that shows the resume's ATS score in real time, lets users switch templates, toggle the AI assistant, save progress, and export to PDF. Everything is persisted to `localStorage`, so data survives page reloads without a backend.

---

## ✨ Features

### 🔐 Authentication
- **Email & Password Sign Up / Sign In** — Full registration and login flow with inline field validation (name ≥ 2 chars, valid email format, password ≥ 8 characters).
- **Password Strength Indicator** — Real-time strength meter on signup that scores the password across 4 criteria (length, uppercase, numbers, special characters) and shows Weak / Fair / Good / Strong labels with color-coded progress.
- **Google OAuth** — One-click sign in via Google account.
- **GitHub OAuth** — One-click sign in via GitHub account.
- **Forgot Password Flow** — Dedicated "forgot" mode on the auth page; checks if the email exists and simulates sending a reset link.
- **Resend Email Verification** — Option to resend the verification email if not received.
- **Protected Routes** — `ProtectedRoute` component wraps all authenticated pages. Unauthenticated users are redirected automatically.
- **Session Persistence** — Auth session is saved to `localStorage` and restored on every page load via a `restoreSession` Redux thunk, so users stay logged in across refreshes.
- **Logout Confirmation Modal** — A slide-in modal with an `AlertTriangle` icon asks users to confirm before logging out.

### 🏠 Dashboard
- **4 Stat Cards** — Shows Total Resumes, Average ATS Score, Total Views, and Downloads at the top of the dashboard.
- **Resume Cards** — Each saved resume is displayed as a card with its title, template name, ATS score, last-edited time, status (active / draft), and view/download counts.
- **Per-Card Actions** — Each card has an options menu with Edit, Duplicate, and Delete actions.
- **Quick Actions Panel** — 4 shortcut tiles: Create Resume (links to builder), Upload Resume, AI Optimize, and Job Match.
- **Sidebar Navigation** — 5-item sidebar: Dashboard, My Resumes, Templates, Analytics, Settings. Collapses to a hamburger on mobile.
- **Theme Toggle** — Sun/Moon button in the dashboard header toggles between light and dark mode.

### 🛠️ Resume Builder
- **Editable Resume Title** — A title input at the top of the builder (max 40 characters) lets users name their resume directly.
- **6 Resume Sections** — The sidebar lists all editable sections with Lucide icons: Personal Info, Experience, Education, Skills, Projects, and Certifications. Clicking any section opens its editor.
- **Live Preview Panel** — The right side of the builder renders the full resume in real time as the user types, switching between Edit and Preview tabs.
- **ATS Score Badge** — Displayed in the top bar with color coding: green for ≥ 85, amber for ≥ 65, red below 65.
- **Last Saved Timestamp** — The top bar shows when the resume was last saved.
- **Save Button** — Persists the current resume state to `localStorage`.
- **Reset Button** — Clears all resume data and resets the builder to its default state.
- **PDF Export** — The export flow clones the live preview HTML, wraps it in a self-contained A4 HTML document, loads it in a hidden iframe, and triggers the browser's print dialog. Users save it as PDF from there. A loading toast appears during preparation and a success toast guides the user through the print dialog.

### 🤖 AI Panel
- **Section-Specific AI Prompts** — Each of the 6 sections has a custom prompt template that sends the user's actual resume data to an AI model and returns targeted improvements:
  - **Personal** — Rewrites the professional summary to be ATS-friendly and impactful (≤ 3 sentences).
  - **Experience** — Improves job achievement bullets with quantified results; returns a JSON array of improved strings.
  - **Skills** — Suggests 5–8 additional in-demand skills based on the user's existing skill list.
  - **Education** — Returns 3 expert tips for improving the education section.
  - **Projects** — Rewrites a project description to be impact-focused (1–2 sentences).
  - **Certificates** — Suggests 5 highly valued certifications for software engineers.
- **Regenerate** — Re-runs the same AI prompt to get a fresh suggestion.
- **Copy to Clipboard** — Copies the AI-generated suggestion text with a single click; shows a checkmark confirmation.
- **ATS Score Breakdown** — Each section shows a mini ATS score card with 4 sub-scores: Keywords, Formatting, Completeness, and Impact.
- **Static Writing Tips** — Below the AI output, each section always shows 5 hand-written best-practice tips (e.g., "Quantify results — '40% faster'", "Start bullets with strong verbs").

### 🎨 Template Switcher
- **4 Templates** — Modern (violet `#7c3aed`), Classic (blue `#2563eb`), Minimal (cyan `#06b6d4`), and Creative (pink `#ec4899`).
- **Animated Modal** — Opens as a blur-backdrop overlay with scale-in animation (Framer Motion).
- **Mini Preview Cards** — Each template card shows a small visual preview with accent color and skeleton lines representing the resume layout.
- **Active Template Indicator** — The currently selected template shows a filled checkmark badge on its card.

### 📊 Analytics Page
- **Period Selector** — Toggle between 7-day, 30-day, and 90-day views.
- **4 Summary Stats** — Total Views, Downloads, ATS Score, and Active Resumes.
- **Weekly Bar Chart** — Custom bar chart showing daily views and downloads (Mon–Sun) with dynamic height scaling.
- **Per-Resume Stats Table** — Each resume is listed with its view count, download count, ATS score, and a trend indicator (up / down / flat) with percentage change.

### ⚙️ Profile Settings
- **4 Settings Tabs** — Profile (name, email, phone, location, website), Account (password change with show/hide toggle), Notifications (alerts preferences), and Billing (subscription info).
- **Theme Toggle** — Light/dark mode switch inside settings.
- **Delete Account** — Confirmation modal before account deletion.
- **Save Changes** — Saves profile updates with a loading state on the button.

### 🎨 UI & UX
- **Dark / Light Theme** — Theme is toggled globally via Redux (`themeSlice`) and synced to `document.documentElement` as a `dark` class. Persisted across sessions.
- **Custom Scrollbars** — A 4px-wide scrollbar with transparent track and subtle thumb, styled differently for dark and light modes.
- **Lazy Loading** — All 7 pages are loaded with React's `lazy()` + `Suspense`, keeping the initial bundle small.
- **Animated Page Loader** — A branded loading screen (📄 icon + 3 bouncing violet dots) shows during lazy page loads.
- **Toast Notifications** — `react-hot-toast` is used throughout for save confirmations, export status, auth errors, and more. Toasts appear at the top-center with a 4-second duration and rounded corners.
- **Framer Motion Animations** — Used across the template switcher modal, logout modal, dashboard cards, and topbar elements for smooth transitions.
- **Fully Responsive** — Layout adapts across desktop, tablet, and mobile using Tailwind CSS utility classes and breakpoints.
- **404 Page** — A dedicated `NotFoundPage` component handles unmatched routes.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| React 19 + TypeScript | Core framework with full type safety |
| Vite | Build tool and dev server |
| Redux Toolkit | Global state — auth, resume data, theme |
| React Router DOM v7 | Client-side routing with protected routes |
| Tailwind CSS v4 | Utility-first styling |
| Framer Motion | Animations — modals, transitions, loaders |
| Radix UI | Accessible headless UI primitives (Avatar, Dialog, Tabs, Switch, Select, etc.) |
| Lucide React | Icon library |
| React Hot Toast | In-app toast notifications |
| Firebase (config) | Auth infrastructure (Google/GitHub OAuth config) |
| localStorage | Resume data, auth session, and theme persistence |
| html2pdf.js | Referenced for PDF; active export uses iframe + print dialog |

---

## 📁 Project Structure

```
Resume_Builder/
├── src/
│   ├── components/
│   │   ├── builder/
│   │   │   ├── AIPanel.tsx          # AI writing assistant with section prompts, ATS scores, static tips
│   │   │   ├── BuilderSidebar.tsx   # Section navigation sidebar for the builder
│   │   │   ├── BuilderTopbar.tsx    # Title input, ATS badge, save/export/AI/template/reset buttons
│   │   │   ├── LivePreview.tsx      # Real-time resume renderer (largest file — 46KB)
│   │   │   ├── SectionEditors.tsx   # Form editors for all 6 resume sections
│   │   │   └── TemplateSwitcher.tsx # Animated modal with 4 template preview cards
│   │   ├── layout/
│   │   │   ├── Navbar.tsx           # Top navigation bar
│   │   │   └── Footer.tsx           # Site footer
│   │   ├── Home/
│   │   │   ├── HeroSection.tsx      # Landing hero
│   │   │   ├── FeaturesSection.tsx  # 6 feature highlights
│   │   │   ├── HowItWorksSection.tsx
│   │   │   ├── PricingSection.tsx   # Pricing tiers
│   │   │   ├── ReviewsSection.tsx   # User testimonials
│   │   │   ├── WhyChooseSection.tsx
│   │   │   └── CTASection.tsx
│   │   └── ProtectedRoute.tsx       # Auth guard — redirects unauthenticated users
│   ├── pages/
│   │   ├── HomePage.tsx             # Landing page
│   │   ├── AuthPage.tsx             # Sign in / Sign up / Forgot password
│   │   ├── DashboardPage.tsx        # Resume management hub
│   │   ├── ResumeBuilderPage.tsx    # Main builder with AI panel and live preview
│   │   ├── TemplatesPage.tsx        # Template browser
│   │   ├── ProfileSettingsPage.tsx  # 4-tab settings page
│   │   ├── AnalyticsPage.tsx        # Resume performance analytics
│   │   └── NotFoundPage.tsx         # 404 fallback
│   ├── store/
│   │   ├── slices/
│   │   │   ├── authSlice.ts         # Auth state — login, register, Google/GitHub OAuth, session restore
│   │   │   ├── resumeSlice.ts       # Resume data state
│   │   │   └── themeSlice.ts        # Dark/light theme toggle
│   │   ├── index.ts                 # Redux store setup
│   │   └── hooks.ts                 # Typed useAppDispatch / useAppSelector
│   ├── hooks/
│   │   ├── useAuthListener.ts       # Auth state listener
│   │   └── usePDFExport.ts          # PDF export via iframe + browser print dialog
│   ├── types/
│   │   ├── index.ts                 # Core types — User, ResumeData, Experience, Education, etc.
│   │   └── resume.types.ts          # Builder-specific resume types
│   ├── data/
│   │   └── resumeBuilder.data.ts    # Static data — templates, sections, features, stats
│   ├── lib/
│   │   ├── constants.ts             # Nav links, templates, skill levels, skill categories
│   │   └── utils.ts                 # Utility helpers
│   ├── config/
│   │   └── firebase.ts              # Firebase project config
│   ├── App.tsx                      # Root — Provider, BrowserRouter, Routes, Toaster, ThemeSync
│   └── main.tsx                     # Entry point
├── index.html
├── package.json
├── vite.config.ts
├── tsconfig.json
└── README.md
```

---

## 🚀 Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/tripathipawan/Resume_Builder.git
cd Resume_Builder
```

**2. Install dependencies**
```bash
npm install
```

**3. Set up Firebase (for Google/GitHub OAuth)**

Create a `.env` file in the root and add your Firebase project credentials:
```env
VITE_FIREBASE_API_KEY=your_api_key
VITE_FIREBASE_AUTH_DOMAIN=your_auth_domain
VITE_FIREBASE_PROJECT_ID=your_project_id
```

**4. Start the dev server**
```bash
npm run dev
```

**5. Build for production**
```bash
npm run build
```

---

## 🧭 How to Use

1. Visit the app and click **Sign Up** to create an account (or sign in with Google/GitHub).
2. From the **Dashboard**, click **Create Resume** to open the builder.
3. Fill in your details across the **6 sections** in the left panel — watch the live preview update on the right.
4. Click the **✨ AI button** in the top bar to get section-specific AI suggestions for any section you're editing.
5. Switch between **4 templates** using the Palette icon and pick the style that fits best.
6. Check your **ATS Score** badge in the top bar — aim for green (≥ 85).
7. Hit **Save** to persist your resume, then **Download** to export it as a PDF.
8. Head to **Analytics** from the sidebar to track your resume's performance over time.

---

## 🌱 What I Learned

- Building a multi-page React application with protected routing using React Router DOM and Redux auth state
- Managing complex global state across auth, resume data, and theme with Redux Toolkit slices
- Implementing a full authentication flow (email/password, OAuth, session restore) with localStorage as the persistence layer
- Designing a real-time live preview component that re-renders on every form change without performance degradation
- Integrating an AI panel that constructs context-aware prompts from live resume data and handles JSON + plain text responses
- Implementing PDF export using an iframe + browser print dialog without any server-side rendering
- Applying Framer Motion for animated modals, loaders, and micro-interactions across the UI
- Building a multi-tab settings page and a data visualization analytics page from scratch using Tailwind and Recharts

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -m 'Add: your feature description'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Pawan Tripathi**
- GitHub: [@tripathipawan](https://github.com/tripathipawan)

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
