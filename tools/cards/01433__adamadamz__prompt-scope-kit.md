---
id: tool-01433
type: tool
area: 库
status: active
tags: [协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: prompt-scope-kit
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/adamadamz/prompt-scope-kit
created: 2026-07-18
updated: 2026-07-18
no: 1433
category: 二、网文 / 长篇 AI 写作系统 库
repo: adamadamz/prompt-scope-kit
stars: 0
url: https://github.com/adamadamz/prompt-scope-kit
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# adamadamz/prompt-scope-kit

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/adamadamz/prompt-scope-kit
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Domain-scoped prompt writing skills for Codex and AI agents.
- **本地描述**：Domain-scoped prompt writing skills for Codex and AI agents.
- **拉取时间**：2026-07-23 23:20:53

---

# Prompt Scope Kit

> Domain-scoped prompt writing skills for Codex and AI agents.

`prompt-scope-kit` is an open-source prompt skill kit for writing concise, executable, domain-scoped prompts. It helps AI agents define business direction, technical scope, reuse rules, platform standards, loop stages, and acceptance gates before generating documents, product plans, designs, or code.

## Table of Contents

1. [What It Is](#1-what-it-is)
2. [Why It Exists](#2-why-it-exists)
3. [Core Principles](#3-core-principles)
4. [Current Skill](#4-current-skill)
5. [iOS / Apple Ecosystem Scope](#5-ios--apple-ecosystem-scope)
6. [Prompt Structure](#6-prompt-structure)
7. [Anchor Prompt Pattern](#7-anchor-prompt-pattern)
8. [Loop Rules](#8-loop-rules)
9. [Repository Structure](#9-repository-structure)
10. [Installation](#10-installation)
11. [Usage Examples](#11-usage-examples)
12. [Roadmap](#12-roadmap)
13. [License](#13-license)

## 1. What It Is

`prompt-scope-kit` turns vague AI requests into prompts with clear execution boundaries.

It is designed for:

| Use case | Output |
|---|---|
| Product research | Market reports, competitor maps, validation metrics |
| App Store growth | ASO, Apple Search Ads, onboarding, trial strategy |
| iOS development | Swift / SwiftUI implementation prompts with Apple constraints |
| Documentation | Markdown reports with title, table of contents, concise tables |
| Code tasks | Minimal implementation prompts that prefer reuse over custom code |
| Iterative workflows | Stage-based loops with clear gates and stop conditions |

## 2. Why It Exists

Most prompts fail because they lack scope. They ask an AI to "think broadly" when the task needs a narrow business direction, a platform boundary, and a clear validation signal.

This kit enforces four decisions before writing the final prompt:

| Decision | Purpose |
|---|---|
| Business direction | Prevents generic output |
| Platform scope | Keeps the prompt inside the right ecosystem |
| Reuse rule | Avoids rebuilding what existing components or packages already solve |
| Loop gate | Makes each iteration measurable |

## 3. Core Principles

| Principle | Rule |
|---|---|
| Be concise | Use short context and structured tables to save tokens |
| Define scope first | Every prompt should name domain, platform, user, goal, in-scope, and out-of-scope |
| Reuse before custom work | Use existing components, installed dependencies, native APIs, or mature packages before building custom code |
| Avoid overdesign | Do not add frameworks, modules, or abstractions unless the task requires them |
| Follow platform standards | Use Apple, Alibaba, App Store, or project standards when relevant |
| Validate by stage | Each loop stage should have an output and a gate |
| Use anchors for repeated scope | Define fixed scope once, then let later segment prompts inherit it |

## 4. Current Skill

The first skill in this kit is:

```text
prompt-writer-skill
```

It creates concise, executable, domain-scoped prompts for:

- Product research.
- Market analysis.
- iOS app development.
- App Store growth.
- Code implementation.
- Documents and reports.
- Iterative AI workflows.

Current local skill path:

```text
~/.codex/skills/prompt-writer-skill/SKILL.md
```

## 5. iOS / Apple Ecosystem Scope

The first supported business / technical scope is iOS and Apple ecosystem application development.

### 5.1 In Scope

| Area | Scope |
|---|---|
| Native iOS | Swift, SwiftUI, UIKit when needed, Xcode project work |
| Apple ecosystem | WidgetKit, App Intents, Shortcuts, Siri, Live Activities, Push Notifications, iCloud |
| Monetization | StoreKit, subscriptions, trials, paywall copy, restore purchase, entitlement states |
| Growth | App Store metadata, ASO, Custom Product Pages, Product Page Optimization, Apple Search Ads |
| Compliance | Apple Human Interface Guidelines, App Store Review Guidelines, privacy disclosures |
| Quality | Accessibility, localization, analytics events, performance, review-ready behavior |

### 5.2 Out of Scope Unless Requested

| Area | Boundary |
|---|---|
| Android | Do not include unless the user asks for cross-platform |
| Web app | Do not add dashboards or landing pages unless needed for validation |
| WeChat / mini programs / mini games | Keep separate; these will be added as future domain references |
| Backend platform buildout | Keep minimal unless the feature requires backend work |
| Social/community systems | Avoid unless the product hypothesis depends on it |
| Complex AI pipelines | Avoid unless they are the product core and review risk is addressed |

### 5.3 iOS Prompt Rules

```text
iOS / Apple constraints:
- Target native iOS and Apple ecosystem only.
- Follow Apple HIG, App Store Review Guidelines, StoreKit rules, and project conventions.
- Use SwiftUI/native Apple frameworks unless the existing project dictates otherwise.
- Reuse existing project code and installed dependencies before custom implementation.
- Keep implementation minimal and review-safe.
- Define permission, privacy, subscription, and restore-purchase behavior when relevant.
- Include validation steps: simulator/device, StoreKit test, UI check, analytics event, or App Store metadata review as appropriate.
```

## 6. Prompt Structure

Use this structure for generated prompts:

```text
You are [role only if useful].

Task:
[One-sentence job.]

Context:
- [Only decision-relevant background.]
- [Constraints.]

Anchor:
- Create new anchor: [anchor-name]
- Or inherit anchor: [anchor-name]

Business / technical scope:
- Domain:
- Target platform:
- User / buyer:
- Business goal:
- Required standards:
- Validation signal:

In scope:
- [...]

Out of scope:
- [...]

Rules:
- Keep output concise and token-efficient.
- Prefer tables when they reduce prose.
- Reuse existing project components, utilities, dependencies, native APIs, or mature open-source packages before custom development.
- Follow relevant standards: Apple HIG / App Store rules / StoreKit / Alibaba Java style / project conventions.
- Do not overdesign; choose the smallest solution that satisfies the goal.

Loop stages:
1. [Stage]: [goal] -> [output] -> [gate]
2. [Stage]: [goal] -> [output] -> [gate]

Output format:
- Markdown document with title and table of contents.
- Numbered sections matching the requested deliverables.
- Tables for comparisons, metrics, and decisions.
- Final verdict.

Acceptance criteria:
- [...]
- [...]
```

## 7. Anchor Prompt Pattern

For multi-step work, use one fixed anchor prompt and short segment prompts.

### 7.1 First Prompt: Anchor

```text
Anchor: ios-faithflow-growth

Fixed scope and direction:
- Domain: iOS subscription app growth
- Target platform: Native iOS, App Store, Apple Search Ads, StoreKit
- User / buyer: Young Christian iOS users
- Business goal: Validate trial and retention signal with small-budget ASA
- In scope: ASO, CPP, onboarding, paywall, subscription trust, validation metrics
- Out of scope: Android, WeChat, full backend, community platform, audio library
- Required standards: Apple HIG, App Store Review Guidelines, StoreKit rules
- Reuse rules: Prefer existing components, native Apple APIs, installed dependencies, and mature packages before custom work
- Loop / validation rules: Each segment must define output and gate

Use this anchor as fixed context for all follow-up segment prompts unless explicitly overridden.
```

### 7.2 Later Prompt: Segment

```text
Inherit anchor: ios-faithflow-growth.

Segment task:
Create the Apple Search Ads keyword testing prompt for the first validation loop.

Output:
Markdown with title, table of contents, keyword groups, CPP mapping, budget split, success gates, and stop conditions.
```

Chinese shorthand:

```text
沿用《ios-faithflow-growth》总提示词的固定范围和方向。本段只处理：Apple Search Ads 第一阶段关键词测试。
```

Create a new anchor only when the platform, business direction, user, standards, or validation logic changes.

## 8. Loop Rules

Use loop stages only when the task needs iteration. Keep loops explicit and gated.

### 8.1 Product Validation Loop

| Stage | Goal | Output | Gate |
|---|---|---|---|
| 1. Segment | Pick narrow user and scenario | User segment + use case | One clear paid pain |
| 2. Store demand | Map keywords and competitors | ASO / ASA keyword set | Search intent exists |
| 3. Onboarding | Convert intent to setup | Onboarding script | User reaches aha moment |
| 4. Paywall | Test willingness to pay | Offer + trial hypothesis | Install-to-trial target |
| 5. Retention | Prove habit | D1/D7 events | Retention threshold met |

### 8.2 iOS Development Loop

| Stage | Goal | Output | Gate |
|---|---|---|---|
| 1. Inspect | Read project patterns | Implementation notes | Reuse path chosen |
| 2. Implement | Smallest viable change | Code changes | Scope unchanged |
| 3. Verify | Run targeted checks | Test/manual evidence | No obvious regression |
| 4. Review | Check Apple/platform risk | Risk note | Review-safe behavior |
| 5. Report | Summarize outcome | Files + verification | User can continue |

## 9. Repository Structure

Recommended structure:

```text
prompt-scope-kit/
├── README.md
├── docs/
│   ├── self-test-report.md
│   └── top3-skill-breakdown.md
└── skills/
    └── prompt-writer-skill/
        ├── SKILL.md
        └── references/
            └── ios-apple-ecosystem.md
```

Future domains should be added as separate reference files, not mixed into the main skill.

```text
skills/[domain]-skill/SKILL.md
skills/[domain]-skill/references/[domain-scope].md
```

## 10. Installation

For Codex local usage, place the skill under:

```text
~/.codex/skills/prompt-writer-skill/
```

Expected installed layout:

```text
~/.codex/skills/prompt-writer-skill/
├── SKILL.md
└── references/
    └── ios-apple-ecosystem.md
```

After installation, Codex can trigger the skill when the user asks to write, refine, split, or standardize prompts.

## 11. Usage Examples

### 11.1 iOS Market Research Prompt

```text
Use prompt-writer-skill to create a concise market research prompt for an iOS subscription app.
The scope is App Store, Apple Search Ads, onboarding, trial validation, and first-stage paid signal.
Output should be Markdown with a title, table of contents, tables, and a clear go/no-go verdict.
```

### 11.2 iOS Development Prompt

```text
Use prompt-writer-skill to create an implementation prompt for a SwiftUI iOS app.
The prompt must require reading existing project patterns first, reusing existing components and packages, following Apple HIG and StoreKit rules, and running targeted verification.
```

### 11.3 Prompt Library Expansion

```text
Use prompt-writer-skill to add a new business scope for WeChat Mini Programs.
Keep it separate from iOS rules.
Define in-scope areas, out-of-scope areas, platform standards, reuse rules, loop stages, and acceptance gates.
```

### 11.4 Anchor + Segment Prompt

```text
Use prompt-writer-skill to create:
1. A fixed anchor prompt for the FaithFlow iOS / App Store growth direction.
2. Three segment prompts that inherit the anchor: ASO, onboarding, and paywall validation.

Each segment prompt should use one-line anchor inheritance instead of repeating the full fixed scope.
```

## 12. Roadmap

| Priority | Scope | Status |
|---|---|related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| P0 | `prompt-writer-skill` | Done |
| P0 | `ios-apple-skill` | Planned |
| P1 | `wechat-mini-program-skill` | Planned |
| P1 | `wechat-mini-game-skill` | Planned |
| P1 | `wechat-ecosystem-skill` | Planned |
| P2 | SaaS / web app scope | Planned |
| P2 | App Store growth prompt library | Planned |

## 13. License

This project is released under the:

```text
MIT
```
