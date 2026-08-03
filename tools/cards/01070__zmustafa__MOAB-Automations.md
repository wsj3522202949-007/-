---
id: tool-01070
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: MOAB-Automations
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/zmustafa/moab-automations
created: 2026-07-18
updated: 2026-07-18
no: 1070
category: 二、网文 / 长篇 AI 写作系统 库
repo: zmustafa/MOAB-Automations
stars: 0
url: https://github.com/zmustafa/moab-automations
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# zmustafa/MOAB-Automations

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/zmustafa/moab-automations
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：ai, ai-agents, ai-skills
- **GitHub 描述**：MOAB is a VS Code Copilot skill that turns any website you log into — internal portal, SaaS dashboard, shopping site, anything — into a fully autonomous AI agent, without writing a single line of code.
- **本地描述**：MOAB is a VS Code Copilot skill that turns any website you log into — internal portal, SaaS dashboard, shopping site, anything — into a fully autonomous AI agent, without writing a single line of code.
- **拉取时间**：2026-07-23 23:10:11

---

# Mother Of All Browser (MOAB) Automations

> One skill → unlimited autonomous AI agents, on demand.

**MOAB** is a VS Code Copilot **skill** that turns any website you log into — internal portal, SaaS dashboard, shopping site, anything — into a fully **autonomous AI agent**, without writing a single line of code.

You give it a URL. It does autonomous reconnaissance on the site, figures out what features exist, asks you which ones you'd like automated, and then **builds you a brand-new AI agent dedicated to that site** — wired up to exactly those features, registered in VS Code, ready to take goals in plain English and act on them on your behalf. The agent uses your existing browser session, so single sign-on (SSO) "just works."

Once built, the agent runs autonomously: you describe what you want ("export my orders", "watch this wishlist", "renew my library holds"), it plans the steps, drives the browser, captures the results, and reports back. Add new capabilities any time by just asking — it re-mines the live page and wires up the new tool for itself.

**The bigger idea:** MOAB is a *meta-agent* — an AI that builds other AIs. One skill, installed once, lets you spin up a personal autonomous agent for every site you regularly use.

---

## What makes it different

Most browser automations are hand-coded for a single website. MOAB flips that around:

- **AI reconnaissance is the product.** The skill (and every agent it generates) inspects the live page, discovers nav items, buttons, tables, search boxes, and routes, and proposes them back to you as automatable features.
- **No code required.** Your only input is a URL and a few multiple-choice answers.
- **Works on any site you log into.** Internal portals, dashboards, SaaS tools — anything you can reach in a browser.
- **Works with whatever SSO your site uses.** Microsoft Entra ID, Google, Okta, Auth0, ADFS, Ping, plain OAuth2 — if you can sign in once in the visible browser, the agent caches it.
- **Fast after the first login.** The first run opens a real browser so you authenticate; every subsequent run is silent and headless, reusing cached cookies (default 60 minutes, configurable).
- **Cross-platform.** Runs on Windows, macOS, and Linux — the generated agent resolves browser profile paths and process commands for your OS automatically.
- **Safe by default.** Captured page content is auto-scrubbed for secrets (JWTs, GitHub PATs, AWS keys, bearer tokens, credit cards, long hex blobs) with an audit log. Per-host rate-limiting and automatic retries on transient failures are built in.
- **Auto-extending.** Want a new feature on an existing agent later? Just ask. The agent has wildcard access to its own MCP server, so adding tools doesn't require editing config.
- **One skill, many agents.** Each agent is dedicated to one site, but you can build as many as you want.

---

## The flow

Start to finish with one prompt + a URL. Nothing else to type — only multiple-choice answers.

1. **Invoke the skill** from Copilot Chat.
2. **Give it a URL** (e.g., `https://www.amazon.com/`).
3. The skill performs **initial reconnaissance** on the URL (detects SSO, SPA framework, hash routing, etc.), and warns you up front if the site sits behind bot-detection (Cloudflare, Akamai, hCaptcha, reCAPTCHA, …) that would break silent headless runs.
4. It asks a few **multiple-choice questions** (where to store data, app name, etc.).
5. It **logs you in visibly in front of you** — opens a real browser window so you can authenticate (sign-in, 2FA, whatever the site needs).
6. It performs **deeper reconnaissance** on the now-authenticated site (e.g., on Amazon it finds "Your Orders", "Your Lists / Wishlist", "Subscribe & Save", "Returns & Orders", "Recommendations", …).
7. It presents a **menu of automatable features** as multiple-choice. For example, if you pointed it at **amazon.com**, you might see:

   ```
   ✅ Export my entire order history to a CSV (date, item, price, seller, return window)
   ✅ Watch every item on my wishlist and alert me when one drops below a target price
   ✅ Auto-reorder Subscribe & Save staples I'm running low on, based on past cadence
   ⬜ Summarize last year's spending by category and surface my top 10 sellers
   ⬜ Find cheaper or higher-rated alternatives for items I buy repeatedly
   ⬜ Pull all pending returns and remind me which ones are about to expire
   ```

   Or, pointed at a city library site: *download my hold queue, renew everything that's renewable, and email me a reminder for what's due this week*. Or at a fitness tracker: *export every workout from the last year as JSON*. Or at a recipe site: *grab the ingredient list for tonight's planned meal and drop it into my grocery app*. You get the idea — whatever the site lets you click, the agent can do for you.

8. It **builds the AI agent for you**, wiring up exactly those features as invocable tools, and registers it in VS Code.
9. It **smoke-tests each new tool** with a sensible default input to confirm everything works end-to-end before handing back to you.

---

## What you get when MOAB finishes

Every agent MOAB builds comes pre-wired with the same standard toolkit, plus the feature-specific tools you picked from the menu:

| Tool | What it does |
|---|---|
| `launch` | Open the site (silent headless if cookies are fresh, visible-browser SSO otherwise) and capture the page. |
| `navigate` | Jump to any route within the site using the cached session. |
| `interact` | Run a sequence of fill / click / select / wait steps and capture the result. |
| `get_page_content` | Read previously-captured page content from disk — no browser needed. |
| `list_sessions` | Show what cached sessions exist and when they were captured. |

On top of that, each tool you picked in step 7 becomes its own named tool (e.g., `export_order_history`, `watch_wishlist_prices`, `reorder_subscribe_and_save`).

The generated layout in your workspace:

```
<app-name>-mcp-server/
  index.js              # MCP server exposing the tools above
  session-manager.js    # Playwright + Edge session handling
  package.json
.github/agents/
  <app-name>.agent.md   # VS Code agent definition
data/<app-name>/        # Cached session cookies and captured pages (gitignored)
```

You can invoke the new agent from the Copilot Chat agent dropdown, or programmatically via `runSubagent`.

---

## Once the agent is built

You can talk to your new Amazon agent like a personal shopper:

- *"Show me every order over $100 from the last 90 days and group them by category."*
- *"My wishlist item `B0XXXXXXXX` — ping me the moment it drops under $40."*
- *"Reorder the coffee beans I usually buy in March; pick the same size and seller."*
- *"Which of my open returns expire this week? Pre-fill the return labels for the ones I can still send back."*

Whatever the site lets you click, the agent can now do for you on demand.

---

## Why this matters

This wasn't built for one website. It works on any site, because AI reconnaissance is embedded into both the skill and every agent the skill generates. I’ve used it to spin up agents for everything from internal work portals to public sites — each one in minutes, not days.

**One skill → unlimited site-specific agents, on demand.**

---

## Requirements

- **VS Code** with GitHub Copilot Chat
- **Microsoft Edge** or **Chrome** installed (Playwright drives whichever you prefer)
- **Windows, macOS, or Linux**
- **Node.js** 18+ and **Playwright** — *you don't need to install these yourself; the agent will install them on first run if they're missing.*

---

## Set up VS Code from scratch (5 minutes)

Brand new to VS Code? Follow these steps in order:

1. **Download and install VS Code** — [code.visualstudio.com/Download](https://code.visualstudio.com/Download). On first launch, VS Code will prompt you to sign in to GitHub Copilot — go ahead and sign in then; it saves you a step later.
2. **Install Microsoft Edge** (if you don't already have it) — [microsoft.com/edge](https://www.microsoft.com/edge). Chrome works too.
3. **Sign in with GitHub Copilot** *(skip this if you already signed in during the install prompt above).* Open VS Code, click the account icon in the bottom-left corner, choose *Sign in with GitHub*, and follow the prompts. If you don't have a Copilot subscription yet, start one here: [github.com/features/copilot](https://github.com/features/copilot).
4. **Create a new folder** anywhere on your computer (e.g., `C:\dev\my-agents` or `~/dev/my-agents`) and **open it in VS Code** (`File → Open Folder…`).
5. **Open the Copilot Chat window** — click the chat icon in the activity bar, or press `Ctrl+Alt+I` (Windows/Linux) / `Cmd+Ctrl+I` (Mac).
6. **Switch to Agent mode and turn on auto-approve ("YOLO" / bypass mode).** At the top of the chat panel, pick **Agent** from the mode dropdown, then open the chat settings (gear icon) and enable **Auto-approve tool calls** so the agent can install dependencies, edit files, and run commands without prompting for every step.

> **Heads-up:** Auto-approve lets the agent run terminal commands on your behalf. Only use it in a dedicated folder you trust, and review what the agent did before committing anything.

You're ready.

---

## Invoke the MOAB skill to build your first agent

With the skill installed (see [Installation](#installation)) and Copilot Chat open in **Agent** mode:

1. **Paste this prompt into Copilot Chat:**

   > *Use the MOAB skill to build me an agent for `https://www.amazon.com/`.*

   Swap the URL for any site you log into.

2. **Answer one question.** The skill confirms the URL, then disappears for a minute to do reconnaissance on its own (SSO detection, SPA framework, bot-detection markers, similar agents already in your workspace).

3. **Answer the batched follow-up questions.** App name, where to store data, browser channel, cookie lifetime, rate-limit, redact-secrets — all multiple-choice with sensible defaults pre-selected. Hit enter through anything you don't care about.

4. **Sign in when the browser pops up.** A real Edge/Chrome window opens on your screen — log in normally, do 2FA, accept any consent prompts. The skill waits up to 5 minutes, captures the cookies, and closes the window.

5. **Pick the features you want automated.** The skill mines the now-authenticated page (accessibility tree first, DOM second, vision as fallback) and presents a multi-select menu of 4–8 candidate features. Tick the ones you want, or type a freeform request for something it didn't detect.

6. **Watch the smoke tests run.** Each new tool is exercised once with a sensible default input. Failures are surfaced with an offer to retry or skip.

7. **Done.** You now have `<app>-mcp-server/` and `.github/agents/<app>.agent.md` in your workspace. Reload VS Code (`Developer: Reload Window`) so the new agent appears in the chat agent dropdown.

---

## Use your new agent

1. **Open Copilot Chat** and click the agent dropdown at the top of the chat panel. Your new agent (e.g., `amazon`) is in the list.
2. **Pick it.** Now every prompt in this chat goes to that agent and has access to its tools.
3. **Talk to it in plain English.** Try things like:

   - *"Export my last 90 days of orders to CSV and group them by category."*
   - *"What's on my wishlist that's dropped in price this month?"*
   - *"Reorder the coffee beans I usually get in March — same size, same seller."*

4. **First call opens a browser; subsequent calls are silent.** If the cached cookies are still fresh (default 60 min) the agent runs headless. Otherwise a visible Edge/Chrome window pops up so you can re-authenticate, then it caches the new session.

5. **Add more features later.** Stay in the agent and just ask: *"Add a tool that does X."* The skill re-mines the live page and wires up the new tool without you editing anything.

6. **Invoke from elsewhere.** You can also call the agent programmatically from another chat via `runSubagent` with the agent name.

---

## Installation

1. Drop the `moab-browser-automation/` folder into your workspace at `.github/skills/moab-browser-automation/`.
2. Reload VS Code (`Developer: Reload Window` from the command palette).
3. Open Copilot Chat and ask: *"Use the MOAB skill to build me an agent for amazon.com."* (or any other site you log into).

That's it. The skill takes over from there — including installing Node.js, Playwright, and the Edge browser driver on first run if they aren't already present.

---

## Security & responsible use

MOAB stores authentication material (cookies) on disk in a `data/` folder so it can skip re-login on subsequent runs. The generated `.gitignore` excludes this folder by default. Still — treat session files like passwords.

- Use this only for sites you are **authorized** to access.
- Respect each site's **terms of service** and rate limits. MOAB throttles requests per host by default (750 ms, configurable) and retries transient failures with exponential backoff.
- Captured page content (`*-content.txt` and feature outputs) is **auto-redacted** for common secret patterns — JWTs, GitHub PATs, AWS keys, generic API keys, bearer tokens, credit cards, long hex blobs — and an audit log at `data/<app>/redaction-log.jsonl` records what was scrubbed. You can opt out, but a `.RAW-SECRETS` marker file will be written next to the output as a visible warning.
- Don't commit captured page content if it contains personal or sensitive data.
- The full-path login closes any open Edge/Chrome windows (it needs the profile lock) — save your work first.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Feedback & contributions

Issues, ideas, and pull requests welcome. If you build an interesting agent with MOAB, I'd love to hear about it.
