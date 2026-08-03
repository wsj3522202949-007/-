---
id: tool-00772
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: skills-collection-1
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/pinkpixel-dev/skills-collection-1
created: 2026-07-18
updated: 2026-07-18
no: 772
category: 二、网文 / 长篇 AI 写作系统 库
repo: pinkpixel-dev/skills-collection-1
stars: 7
url: https://github.com/pinkpixel-dev/skills-collection-1
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# pinkpixel-dev/skills-collection-1

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/pinkpixel-dev/skills-collection-1
- **Stars**：7
- **语言**：Python
- **License**：MIT
- **Topics**：agent-skills, agents, ai, automation, awesome-list, cloud, collection, context-engineering, design, developer-tools, engineering, music, prompt-engineering, research, security, skill-library, skills, writing
- **GitHub 描述**：Part 1 of a large AI and agent skills collection featuring 900+ reusable skill folders, prompt workflows, references, scripts, and assets across engineering, cloud, security, research, writing, design, and automation.
- **本地描述**：Part 1 of a large AI and agent skills collection featuring 900+ reusable skill folders, prompt workflows, references, scripts, and assets across engineering, cloud, security, research, writing, design, and automation.
- **拉取时间**：2026-07-23 23:01:32

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Skills Collection

A large collection of AI/agent skills, resources, references, scripts, and supporting assets.

This repo is organized for scale rather than a giant table of contents. Instead of listing every skill here, the repository keeps each skill in its own folder under [`SKILLS/`](/home/sizzlebop/PINKPIXEL/PROJECTS/CURRENT/skills-collection-1/SKILLS), where it can include its own instructions, references, scripts, and assets.

Related repos:

- This repo: `https://github.com/pinkpixel-dev/skills-collection-1`
- Companion repo: `https://github.com/pinkpixel-dev/skills-collection-2`

## What this repo contains

- `969` skill folders in [`SKILLS/`](/home/sizzlebop/PINKPIXEL/PROJECTS/CURRENT/skills-collection-1/SKILLS)
- Skill definitions, typically in `SKILL.md`
- Optional supporting material such as `references/`, `scripts/`, `assets/`, examples, and license files
- A mix of engineering, security, research, writing, product, automation, frontend, growth, and domain-specific skills

## Repository structure

Typical layout:

```text
SKILLS/
  some-skill/
    SKILL.md
    references/
    scripts/
    assets/
```

Not every skill uses the same structure, but most follow some version of this pattern.

## Browse the collection

The fastest way to explore is by folder name or by searching inside skill files.

Examples:

```bash
find SKILLS -mindepth 1 -maxdepth 1 -type d | sort
rg --files SKILLS
rg -n "security|auth|frontend|react|agent" SKILLS
find SKILLS -name SKILL.md
```

## Notes

- This repository is intentionally broad and evolving.
- Some skills are minimal, while others include deeper reference material and helper scripts.
- Folder names are the best starting point for discovery.

## License

This repository is available under the MIT License. See [`LICENSE`](/home/sizzlebop/PINKPIXEL/PROJECTS/CURRENT/skills-collection-1/LICENSE).
