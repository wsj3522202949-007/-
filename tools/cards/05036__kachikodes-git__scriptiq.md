---
id: tool-05036
type: tool
area: 库
status: active
tags: [去AI味, TTS, TypeScript, 协议未明, 需API密钥, 英文文档]
title: scriptiq
summary: 投稿前文本降 AI 痕、过检测
source: https://github.com/kachikodes-git/scriptiq
created: 2026-07-18
updated: 2026-07-18
no: 5036
category: 一、去 AI 味 / Humanizer 库
repo: kachikodes-git/scriptiq
stars: 0
url: https://github.com/kachikodes-git/scriptiq
tier: "C"
use_case: "投稿前文本降 AI 痕、过检测"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: e689cf321be1d5a0
  - methods/改稿润色指令库.md
---

# kachikodes-git/scriptiq

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/kachikodes-git/scriptiq
- **Stars**：0
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Ai text detector...
- **本地描述**：Ai text detector...
- **拉取时间**：2026-07-25 18:03:45

---

# ScriptIQ — AI Detector & Humanizer

Paste any text → see how **AI-detectable** it is (with per-sentence highlighting) → **humanize** it in one tap → verify the score drop. Mobile-first, premium "Deep Ocean" design with **light & dark themes** (follows your system by default), installable as a PWA.

Built with **Next.js 16** (App Router, Turbopack), **Tailwind CSS v4**, **Drizzle ORM + Neon Postgres**, **Auth.js v5**, **motion** and **sonner** — runs entirely on free tiers ($0/month).

## Features

- 🔎 **AI detection** through a resilient provider chain — **Sapling (primary)** → GPTZero (optional, paid API) → **ScriptIQ's built-in LLM analyzer (free, always available)**. Every provider feeds the same UI: score gauge, AI/Mixed/Human breakdown, confidence, and sentence-level highlighting of AI-flagged lines. If the Sapling dev key (30-day) expires, detection fails over automatically
- ✍️ **Humanizer** — a two-pass LLM pipeline: deep structural paraphrase (the research-proven detector attack), then a burstiness/voice pass with 4 tone modes (Standard, Formal, Casual, Academic). Runs on Groq `openai/gpt-oss-120b` → Gemini `gemini-flash-latest` with per-model failover; override via `GROQ_MODEL` / `GEMINI_MODEL` env vars
- ✅ **"Verify new score"** — re-detects the humanized output on demand and animates the before → after drop (kept user-triggered to conserve free detector quota)
- 📱 **Guest history per device** (private httpOnly cookie) + hashed-IP analytics; **registering migrates the device's history into the account** for multi-device sync
- 🔐 **Auth**: email + password (bcrypt) and optional Google OAuth; JWT sessions carrying the role
- 👑 **Admin dashboard**: live stats + 14-day activity, user & guest inspection with full history drill-down, and **branding controls** (app name, theme colors with live preview, hero/footer copy, daily rate limits) that restyle the whole app instantly
- 🛡️ **Resilience**: provider abstraction, detector→LLM fallback (clearly labeled "estimated"), graceful keyless/DB-less degradation, typed `{ error, code }` API contract, emoji-prefixed logs

## Quick start

```bash
npm install
cp .env.example .env         # then fill it in (see below)
npm run db:migrate           # creates tables on your Neon database
npm run db:seed              # inserts default settings + creates your admin account
npm run dev                  # → http://localhost:9999 — sign in with ADMIN_EMAIL / ADMIN_PASS
```

### Environment variables (all free)

| Variable | Where to get it |
|---|---|
| `DATABASE_URL` | [neon.com](https://neon.com) → New project → **Connect** → copy the pooled connection string |
| `AUTH_SECRET` | run `npx auth secret` (or any long random string) |
| `ADMIN_EMAIL` + `ADMIN_PASS` | `npm run db:seed` creates the **admin account** from these (8+ char password). Rotate it later in **Admin → Profile** |
| `GROQ_API_KEY` | [console.groq.com](https://console.groq.com) (free) — powers the humanizer **and** the built-in detection analyzer |
| `GEMINI_API_KEY` | [aistudio.google.com](https://aistudio.google.com) (free) — automatic fallback for both |
| `IP_SALT` | any random string (salts the hashed IPs stored with history) |
| `SAPLING_API_KEY` | [sapling.ai](https://sapling.ai) → API Settings → Keys — **primary detector**. Dev keys expire after 30 days; the built-in analyzer takes over automatically |
| `GPTZERO_API_KEY` | *optional* — GPTZero's API needs a paid Professional plan; slots in after Sapling if you ever add it |
| `GOOGLE_CLIENT_ID` / `GOOGLE_CLIENT_SECRET` | *optional* — enables "Continue with Google" when both are set |

The app still runs with missing keys: AI endpoints return a clear "provider not configured" error, and the UI/DB features degrade gracefully — handy while you're collecting keys.

## Deploying to Vercel

1. Push this repo to GitHub and import it in [vercel.com](https://vercel.com).
2. Add every variable from `.env.local` in **Project → Settings → Environment Variables**.
3. Run the migration against your Neon DB once (locally): `npm run db:migrate && npm run db:seed`.
4. Deploy. For Google OAuth, add `https://<your-domain>/api/auth/callback/google` as an authorized redirect URI in Google Cloud.

> **Demo-day tip:** Neon's free tier scales to zero after ~5 idle minutes — open the app once before presenting so the first request is warm.

## Database scripts

| Script | Purpose |
|---|related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| `npm run db:generate` | Generate SQL migrations from the Drizzle schema |
| `npm run db:migrate` | Apply migrations to `DATABASE_URL` |
| `npm run db:push` | Push schema directly (prototyping) |
| `npm run db:seed` | Insert default settings + seed the admin account (idempotent) |
| `npm run db:studio` | Browse the database in Drizzle Studio |

## Architecture notes

- **`src/lib/ai/`** — provider layer. `detector.ts` (Sapling → GPTZero → built-in LLM analyst chain with logged failover **and a circuit breaker**: a failing provider — e.g. an expired Sapling key — is skipped for 6 h on auth errors / 60 s on transient errors, so users never feel the failover), `llm.ts` (Groq→Gemini chain), `humanizer.ts` (mode-conditioned rewrite prompts in `prompts.ts`). Swappable behind `DetectionResult`/`HumanizeResult` contracts; analyzer results are flagged `estimated` and labeled in the UI.
- **Guest identity** — `siq_anon` httpOnly cookie per device (no history leakage between people on shared WiFi); `sha256(ip + IP_SALT)` stored per row for admin analytics only. `POST /api/history/claim` migrates device rows to the account after sign-in (fired automatically by `AutoClaim`).
- **Theming** — admin-saved colors/texts live in the `settings` table; the root layout injects them as CSS variables consumed by Tailwind v4 `@theme` tokens, so saving in the admin panel rebrands every page.
- **Rate limiting** — daily counts derived from the `history` table (guest vs. user limits, admin-editable), no extra infrastructure.
- **Auth guard** — `src/proxy.ts` (Next 16 middleware successor) redirects non-admins away from `/admin`; the admin layout and server actions re-verify the role server-side.

## Roadmap (future work)

Email verification & password reset · plagiarism checking · file upload (docx/pdf) · export history · light theme · i18n.
