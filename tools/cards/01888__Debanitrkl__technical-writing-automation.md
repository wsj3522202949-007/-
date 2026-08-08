---
id: tool-01888
type: tool
area: 库
status: active
tags: [协议未明, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: technical-writing-automation
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/debanitrkl/technical-writing-automation
created: 2026-07-18
updated: 2026-07-18
no: 1888
category: 二、网文 / 长篇 AI 写作系统 库
repo: Debanitrkl/technical-writing-automation
stars: 0
url: https://github.com/debanitrkl/technical-writing-automation
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 0f6efd9166f2446d
  - methods/最强写作方法论_全球最强综合版.md
---

# Debanitrkl/technical-writing-automation

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/debanitrkl/technical-writing-automation
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Agent skills, workflows, and SEO content playbook for Parseable technical writing.
- **本地描述**：Agent skills, workflows, and SEO content playbook for Parseable technical writing.
- **拉取时间**：2026-07-23 23:34:01

---

# Technical Writing Automation

A plug-and-play toolkit of **agent skills** and **workflows** that you can
drop into any repo and use with
[Claude Code](https://claude.com/claude-code) or
[OpenAI Codex CLI](https://github.com/openai/codex) to plan, draft, and
review technical writing at the same quality bar we use at
[Parseable](https://www.parseable.com).

> **No coding required.** If you can copy a folder and paste it into another
> folder, you can use this.

---

## What you get

| Folder | What it is | Why you'd use it |
|---|---|---|
| `.agents/skills/` | 4 ready-to-use writing skills | Turn your AI coding assistant into a careful editor |
| `.claude/workflows/` | Step-by-step blog creation playbook | Never miss frontmatter, images, or SEO fields |

### The 4 skills

Each skill lives in `.agents/skills/<skill-name>/SKILL.md`. An AI assistant
reads the `SKILL.md` and applies its rules to your writing.

- **`review-writing`** — structured editorial review. Catches weak claims,
  unclear arguments, and missing evidence.
- **`seo-aeo-best-practices`** — modern SEO + Answer Engine Optimization
  (AEO). Makes content rankable *and* quotable by AI answer engines.
- **`stop-slop`** — strips the telltale "AI-sounding" filler: hedges,
  throat-clearing intros, "In today's fast-paced world…" openers.
- **`writing-clearly-and-concisely`** — Strunk & White-style concision pass.
  Cuts flab, strengthens verbs, tightens sentences.

---

## Who this is for

- **Founders, marketers, DevRel, solo writers** who want their AI assistant
  to stop writing like a bot.
- **Engineering teams** publishing technical content and tired of reviewing
  the same AI-generated clichés.
- **Anyone** who has Claude Code or Codex installed and a folder of writing
  to improve.

You do **not** need to know JavaScript, Python, or how to use git beyond
`git clone` (and we cover that below).

---

## Two ways to use this

### Option A — Fork the repo (recommended if you want updates)

1. Click **Fork** at the top-right of
   https://github.com/Debanitrkl/technical-writing-automation
2. Clone your fork to your computer:
   ```bash
   git clone https://github.com/<your-username>/technical-writing-automation.git
   cd technical-writing-automation
   ```
3. Open the folder in Claude Code or Codex and start working (see
   "Using the skills" below).

### Option B — Copy-paste into your existing repo (fastest)

1. Download this repo as a ZIP:
   https://github.com/Debanitrkl/technical-writing-automation/archive/refs/heads/main.zip
2. Unzip it.
3. Copy these two folders into the root of *your* project:
   - `.agents/` → gives you the skills
   - `.claude/` → gives you the workflow playbook
4. That's it. Your repo now has the skills. Commit them if you want them
   shared with teammates:
   ```bash
   git add .agents .claude
   git commit -m "Add technical writing skills"
   ```

> The leading dot (`.`) in `.agents` and `.claude` is intentional —
> these are "hidden" config folders that AI tools look for automatically.
> On macOS Finder, press `Cmd+Shift+.` to see hidden folders.

---

## Using the skills

### With Claude Code

1. **Install Claude Code** (one-time):
   https://claude.com/claude-code
2. **Open your project** in a terminal and run:
   ```bash
   claude
   ```
3. **Ask Claude to use a skill** in plain English. Examples:
   - `review this draft using the review-writing skill: drafts/my-post.md`
   - `run the stop-slop skill on the intro I just wrote`
   - `apply seo-aeo-best-practices to blog/launch.md`
   - `use writing-clearly-and-concisely on the README`
4. Claude will read the relevant `SKILL.md`, apply its rules, and either
   suggest edits or rewrite inline. You review, accept, or push back.

### With OpenAI Codex CLI

1. **Install Codex CLI** (one-time):
   https://github.com/openai/codex
2. **Run it** in your project folder:
   ```bash
   codex
   ```
3. **Ask Codex to read a skill and apply it.** Codex doesn't auto-load
   `.agents/skills/` the way Claude Code does, so point it at the file:
   ```
   Read .agents/skills/stop-slop/SKILL.md and apply it to drafts/post.md
   ```
   ```
   Follow .agents/skills/seo-aeo-best-practices/SKILL.md when writing
   the outline for my new post about log management.
   ```
4. Codex will follow the instructions inside the `SKILL.md` file and edit
   accordingly.

### With any other AI assistant (Cursor, Continue, Aider, ChatGPT web, etc.)

The skills are just markdown files. You can paste the contents of a
`SKILL.md` directly into any chat:

```
Here are the rules I want you to follow when reviewing my writing:

<paste the full contents of .agents/skills/review-writing/SKILL.md>

Now review this draft:

<paste your draft>
```

---

## The blog workflow

`.claude/workflows/create-blog-post.md` is a checklist for creating a blog
post — originally written for the Parseable website, but the structure
(frontmatter fields, author registry, image specs, local preview, commit)
maps to any Next.js/Hugo/Jekyll/Astro blog.

**How to use it:**

- Claude Code: `follow the create-blog-post workflow for a post titled "…"`
- Codex: `read .claude/workflows/create-blog-post.md and walk me through it`
- Manually: open the file and follow the steps.

Adapt the frontmatter fields and author list in the workflow to match your
own site.

---

## FAQ

**Do I need a paid Claude or OpenAI account?**
Yes — both Claude Code and Codex require API access (or a subscription).
See their setup pages linked above.

**Can I change the skills?**
Yes. They're plain markdown — open any `SKILL.md`, edit the rules, save.
The AI will pick up your edits next time you invoke the skill.

**Can I add new skills?**
Yes. Create `.agents/skills/<your-skill-name>/SKILL.md` and describe when
and how it should be applied. Both Claude Code and Codex can read it.

**Is this affiliated with Anthropic or OpenAI?**
No. This repo bundles independently-written skills that happen to work well
with their tools.

---

## License

Individual skills may carry their own `LICENSE` file (e.g. `stop-slop/`
bundles one). The rest of this repo is provided as-is for public use —
fork it, copy it, adapt it.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

## Questions / issues

Open an issue on this repo, or reach out via the Parseable team.
