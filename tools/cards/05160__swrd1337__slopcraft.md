---
id: tool-05160
type: tool
area: 库
status: active
tags: [PowerShell, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: slopcraft
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/swrd1337/slopcraft
created: 2026-07-18
updated: 2026-07-18
no: 5160
category: 一、去 AI 味 / Humanizer 库
repo: swrd1337/slopcraft
stars: 1
url: https://github.com/swrd1337/slopcraft
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls: []
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# swrd1337/slopcraft

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/swrd1337/slopcraft
- **Stars**：1
- **语言**：PowerShell
- **License**：MIT
- **Topics**：agents, ai, claude, copilot, deepseek, gemini, performance, skills, slop, zed
- **GitHub 描述**：Stop your AI from writing slop.
- **本地描述**：Stop your AI from writing slop.
- **拉取时间**：2026-07-25 18:08:20

---

# 🚫 slopcraft

**Stop your AI from writing slop.**

Cross-tool performance optimization skill for AI-assisted development. Enforces research-first coding, code quality gates, security hardening, TDD workflow, and context-efficient practices — regardless of which AI coding assistant you use.

Works with **Zed Agent**, **GitHub Copilot**, **Claude Code**, **Cursor**, **Codex**, **DeepSeek**, and **Gemini**.

---

## What's Inside

```
slopcraft/
├── SKILL.md                        # Main skill definition (entry point)
├── rules/
│   ├── coding-style.md             # Immutability, KISS/DRY/YAGNI, naming, file organization
│   ├── performance.md              # Big-O, caching, async, memory, budgets, profiling
│   ├── security.md                 # Input validation, secrets, OWASP, dependency audit
│   └── testing.md                  # TDD cycle, AAA pattern, coverage targets, mocking
├── workflows/
│   ├── research-first.md           # Search-before-code decision framework
│   └── review.md                   # Structured 5-phase code review process
└── checklists/
    ├── pre-commit.md               # Quick/security/quality/test/documentation gates
    └── production-readiness.md     # 9-section deployment readiness + risk matrix
```

---

## The 10 Commandments

1. **Never mutate** — Create new objects, never modify in place
2. **Never hardcode secrets** — Use env vars or secret managers
3. **Never skip validation** — Validate all inputs at system boundaries
4. **Never guess at performance** — Profile first, optimize second
5. **Never ship without tests** — Minimum 80% coverage, TDD preferred
6. **Never reinvent the wheel** — Search for existing solutions first
7. **Never swallow errors** — Handle explicitly, log context, fail gracefully
8. **Never nest deeply** — Prefer early returns, max 3–4 levels
9. **Never write large files** — 200–400 lines typical, 800 absolute max
10. **Never commit known vulnerabilities** — Run security checks before every commit

---

## Installation

### Zed Agent (Global Skill)

Installs as a global Zed skill available across all your projects.

#### macOS / Linux

```bash
git clone https://github.com/YOUR_USERNAME/slopcraft.git /tmp/slopcraft \
  && mkdir -p ~/.agents/skills \
  && cp -R /tmp/slopcraft ~/.agents/skills/slopcraft \
  && rm -rf /tmp/slopcraft
```

Or if you've already cloned the repo:

```bash
./install.sh
```

#### Windows (PowerShell)

```powershell
git clone https://github.com/YOUR_USERNAME/slopcraft.git "$env:TEMP\slopcraft"; `
  New-Item -ItemType Directory -Force -Path "$HOME\.agents\skills" | Out-Null; `
  Copy-Item -Recurse "$env:TEMP\slopcraft" "$HOME\.agents\skills\slopcraft"; `
  Remove-Item -Recurse -Force "$env:TEMP\slopcraft"
```

Or if you've already cloned the repo:

```powershell
.\install.ps1
```

After installation, Zed Agent will automatically detect the skill. No restart needed for new conversations.

---

### GitHub Copilot (VS Code)

Copy the main skill file into your repository's Copilot instructions:

```bash
mkdir -p .github
cp ~/.agents/skills/slopcraft/SKILL.md .github/copilot-instructions.md
```

Or append to an existing instructions file. The rules, workflows, and checklists
work as attachable context in Copilot Chat prompts.

---

### Claude Code / Cursor / Codex

These tools support skill directories natively:

```bash
# Global install (Claude Code)
mkdir -p ~/.claude/skills
cp -R ~/.agents/skills/slopcraft ~/.claude/skills/slopcraft

# Project-local install (any tool)
mkdir -p .agents/skills
cp -R ~/.agents/skills/slopcraft .agents/skills/slopcraft
```

---

### DeepSeek / Gemini / Other LLMs

For tools without a native skill system, paste the content of `SKILL.md` (or specific rule/checklist files) as system instructions or project context.

---

## Uninstall

#### macOS / Linux

```bash
rm -rf ~/.agents/skills/slopcraft
```

#### Windows (PowerShell)

```powershell
Remove-Item -Recurse -Force "$HOME\.agents\skills\slopcraft"
```

---

## Usage

Once installed, slopcraft activates automatically when relevant. You can also invoke it explicitly:

- *"Use slopcraft principles for this feature"*
- *"Run the pre-commit checklist"*
- *"Review this code following the review workflow"*
- *"Check production readiness"*

The skill enforces:
- **Research-first** approach before any new code
- **TDD workflow** (Red → Green → Refactor)
- **Security hardening** at every boundary
- **Performance measurement** over guesswork
- **Quality gates** before commits and deploys

---

## Inspired By

Distills the core principles from [ECC](https://github.com/affaan-m/ecc) into a lightweight, portable format that works across all major AI coding tools — no plugins, hooks, or runtime infrastructure required.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## License

MIT
