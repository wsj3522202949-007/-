---
id: tool-04588
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: skills-collection-2
summary: 本地优先、隐私可控的写作工作台
source: https://github.com/pinkpixel-dev/skills-collection-2
created: 2026-07-18
updated: 2026-07-18
no: 4588
category: 五、写作 IDE / 本地优先工作台 库
repo: pinkpixel-dev/skills-collection-2
stars: 1
url: https://github.com/pinkpixel-dev/skills-collection-2
tier: "B"
use_case: "本地优先、隐私可控的写作工作台"
pitfalls: []
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 5ca6a2bdc0d66a94
  - methods/QUICK_START.md
---

# pinkpixel-dev/skills-collection-2

- **分类**：五、写作 IDE / 本地优先工作台 库
- **链接**：https://github.com/pinkpixel-dev/skills-collection-2
- **Stars**：1
- **语言**：Python
- **License**：MIT
- **Topics**：agent-skills, agents, ai, automation, awesome-list, cloud, collection, context-engineering, design, development-tools, engineering, music, prompt-engineering, research, security, skill-library, skills, writing
- **GitHub 描述**：Part 2 of the AI and agent skills collection, with 650+ skill folders focused on reusable workflows, security playbooks, cloud implementation guides, scripts, references, and assets for builders and operators.
- **本地描述**：Part 2 of the AI and agent skills collection, with 650+ skill folders focused on reusable workflows, security playbooks, cloud implementation guides, scripts, references, and assets for builders and operators.
- **拉取时间**：2026-07-25 17:49:30

related:
  - methods/QUICK_START.md
---

# Skills Collection

A large collection of AI/agent skills, resources, references, scripts, and supporting assets.

This repo is organized for scale rather than a giant table of contents. Instead of listing every skill here, the repository keeps each skill in its own folder under [`SKILLS/`](https://github.com/pinkpixel-dev/skills-collection-2/blob/main//home/sizzlebop/PINKPIXEL/PROJECTS/CURRENT/skills-collection-2/SKILLS), where it can include its own instructions, references, scripts, and assets.

Related repos:

- This repo: `https://github.com/pinkpixel-dev/skills-collection-2`
- Companion repo: `https://github.com/pinkpixel-dev/skills-collection-1`

## What this repo contains

- `658` skill folders in [`SKILLS/`](https://github.com/pinkpixel-dev/skills-collection-2/blob/main//home/sizzlebop/PINKPIXEL/PROJECTS/CURRENT/skills-collection-2/SKILLS)
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

This repository is available under the MIT License. See [`LICENSE`](https://github.com/pinkpixel-dev/skills-collection-2/blob/main//home/sizzlebop/PINKPIXEL/PROJECTS/CURRENT/skills-collection-2/LICENSE).
