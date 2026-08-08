---
id: tool-00078
type: tool
area: 库
status: active
tags: [Claude插件, 协议宽松, 本地优先, 英文文档, 本地写作]
title: ai-ux-skills
summary: Claude Code 插件式写作流
source: https://github.com/slb2248/ai-ux-skills
created: 2026-07-18
updated: 2026-07-18
no: 78
category: 二、网文 / 长篇 AI 写作系统 库
repo: slb2248/ai-ux-skills
stars: 3
url: https://github.com/slb2248/ai-ux-skills
tier: "B"
use_case: "Claude Code 插件式写作流"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 8b365a243bd42ad4
  - methods/最强写作方法论_全球最强综合版.md
---

# slb2248/ai-ux-skills

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/slb2248/ai-ux-skills
- **Stars**：3
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI agent UX skills. Accessibility, UX writing, design critique, and data visualization—install once, your AI uses them automatically. Works with Cursor, Claude Code, VS Code Copilot, and Codex.
- **本地描述**：AI agent UX skills. Accessibility, UX writing, design critique, and data visualization—install once, your AI uses them automatically. Works with Cursor, Claude Code, VS Code Copilot, and Codex.
- **拉取时间**：2026-07-23 22:41:08

---

# AI/UX Skills

> AI coding skills for designers. Accessibility, UX writing, design critique, and data visualization—install once, your AI uses them automatically. Works with Cursor, Claude Code, VS Code Copilot, and Codex.

Curated AI coding skills for UX and product designers. Install once, and your AI activates them automatically when relevant.

## Available Skills

| Skill | Description | Best For |
|-------|-------------|----------|
| [Accessibility Expert](https://github.com/slb2248/ai-ux-skills/tree/main/skills/accessibility-expert/) | Build inclusive interfaces with WCAG compliance, screen reader support, and keyboard navigation | UX, UI, Product, Frontend |
| [UX Writing](https://github.com/slb2248/ai-ux-skills/tree/main/skills/ux-writing/) | Write effective microcopy: button labels, error messages, empty states, onboarding, and tooltips | UX Writers, Content, Product |
| [Design Critique](https://github.com/slb2248/ai-ux-skills/tree/main/skills/design-critique/) | Structured framework for giving and receiving design feedback | Product, UX, UI, Visual |
| [Data Visualization](https://github.com/slb2248/ai-ux-skills/tree/main/skills/d3-visualization/) | Design effective data visualizations: charts, graphs, dashboards, and infographics | Visual, Data, Product |
| [Design Workshop Facilitation](https://github.com/slb2248/ai-ux-skills/tree/main/skills/design-workshop-facilitation/) | Facilitate effective design workshops for problem-solving, ideation, customer journey mapping, design sprints, and team alignment | Product, UX, Design Leads |
| [AI Native Product Designer](https://github.com/slb2248/ai-ux-skills/tree/main/skills/ai-native-product-designer/) | LLM-first workflow, AI code prototyping, Figma as polish, self-serve research, outcome ownership; rubrics for leveling and AI readiness | Product, UX, UI, Design Systems, Research, Frontend |

## Installation

### Cursor

```bash
# Project-level (recommended)
mkdir -p .cursor/skills
cp -r skills/* .cursor/skills/

# Or global
cp -r skills/* ~/.cursor/skills/
```

[Official Cursor Skills Docs →](https://cursor.com/docs/context/skills)

### Claude Code

```bash
# User-level
cp -r skills/* ~/.claude/skills/

# Or project-level
mkdir -p .claude/skills
cp -r skills/* .claude/skills/
```

[Official Claude Code Skills Docs →](https://code.claude.com/docs/en/skills)

### VS Code (GitHub Copilot)

> ⚠️ Preview feature: Enable `chat.useAgentSkills` in settings first

```bash
# Project-level
mkdir -p .github/skills
cp -r skills/* .github/skills/

# Or global
cp -r skills/* ~/.copilot/skills/
```

[Official VS Code Agent Skills Docs →](https://code.visualstudio.com/docs/copilot/customization/agent-skills)

### OpenAI Codex

```bash
# User-level
cp -r skills/* ~/.codex/skills/

# Or project-level
mkdir -p .codex/skills
cp -r skills/* .codex/skills/
```

Use `$` to mention skills, or `/skills` to browse.

[Official OpenAI Codex Skills Docs →](https://developers.openai.com/codex/skills/)

### Quick Use (Any AI)

Copy the content from any `SKILL.md` file and paste it into your AI chat:

```
Here's a skill I want you to follow:

[paste SKILL.md content]

Now help me [your task]
```

## What are Skills?

Skills are `SKILL.md` files that teach AI coding agents specialized abilities. Unlike prompts (which you use once), skills are persistent—install them once, and your AI automatically activates them when relevant to your task.

## Contributing

Have a skill to share? Open a PR! Skills should be:

- **Focused**: One clear purpose
- **Actionable**: Specific guidance, not just concepts
- **Designer-friendly**: Relevant to UX, product, or visual design work

## License

MIT

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

Built by [AI/UX Playground](https://aidesignpatterns.com)
