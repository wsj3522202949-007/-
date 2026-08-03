---
id: tool-00030
type: tool
area: 库
status: active
tags: [TTS, Claude插件, 协议未明, 本地优先, 英文文档, 本地写作]
title: copywriting
summary: 小说转语音/有声书
source: https://github.com/growthquest/copywriting
created: 2026-07-18
updated: 2026-07-18
no: 30
category: 二、网文 / 长篇 AI 写作系统 库
repo: growthquest/copywriting
stars: 1
url: https://github.com/growthquest/copywriting
tier: "B"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# growthquest/copywriting

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/growthquest/copywriting
- **Stars**：1
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：Claude Code skill for writing high-converting marketing copy across any format: ad copy, page copy, video scripts, graphic text, and voiceovers. Includes 13 proven frameworks (PAS, AIDA, BAB, Hook-Story-Offer, etc.) and principles from Schwartz, Sugarman, Hopkins, Halbert, Cialdini, and Ogilvy.
- **本地描述**：Claude Code skill for writing high-converting marketing copy across any format: ad copy, page copy, video scripts, graphic text, and voiceovers. Includes 13 proven frameworks (PAS, AIDA, BAB, Hook-Story-Offer, etc.) and principles from Schwartz, Sugarman, Hopkins, Halbert, Cialdini, and Ogilvy.
- **拉取时间**：2026-07-23 22:39:44

---

# Copywriting Skill for Claude Code

A Claude Code skill that writes high-converting marketing copy across any format. Built on proven direct response frameworks and principles from the masters (Schwartz, Sugarman, Hopkins, Halbert, Cialdini, Ogilvy).

## What It Does

Give it a brief and it writes conversion-focused copy for:

- **Ad Copy** (Meta, Google, LinkedIn, TikTok) with primary text, headlines, and descriptions
- **Page Copy** (homepage, landing page, pricing, feature, about) with full section structure
- **Video Scripts** (talking head, UGC, product demo, VSL) in two-column visual/spoken format
- **Graphic/Static Image Copy** (headlines, sublines, CTAs optimized for mobile readability)
- **Voiceover Scripts** with pause/emphasis markers and timing

## Key Features

- **13 copywriting frameworks** with auto-selection based on awareness stage, length, and format (PAS, AIDA, BAB, Hook-Story-Offer, PPPP, PASTOR, ACCA, SLAP, FAB, Star-Chain-Hook, UGC Direct Response, Hook-Body-CTA, Harmon Brothers)
- **Awareness stage mapping** using Eugene Schwartz's 5 stages to match messaging to where the customer is in their buying journey
- **Masters-layer principles** from Schwartz, Sugarman, Hopkins, Halbert, Cialdini, and Ogilvy applied contextually
- **Creative DNA integration** - automatically pulls strategic ingredients (personas, pain points, hooks, angles) from a client research workbook if one exists
- **Sound Human auto-trigger** - spoken formats (scripts, voiceovers) automatically get a natural voice pass

## How to Install

### Option 1: Copy into your project

```bash
# From your project root
mkdir -p .claude/skills/copywriting/references
curl -o .claude/skills/copywriting/SKILL.md https://raw.githubusercontent.com/growthquest/copywriting/main/SKILL.md
curl -o .claude/skills/copywriting/references/frameworks.md https://raw.githubusercontent.com/growthquest/copywriting/main/references/frameworks.md
```

### Option 2: Clone and copy

```bash
git clone https://github.com/growthquest/copywriting.git
cp -r copywriting/SKILL.md .claude/skills/copywriting/
cp -r copywriting/references .claude/skills/copywriting/
```

## How to Use

Once installed, Claude Code will automatically detect when to use the skill based on your request. You can also invoke it directly:

```
/copywriting
```

### Example Prompts

**Ad copy:**
> "Write Meta ad copy for our SaaS product targeting small business owners who are problem-aware. Use PAS framework."

**Landing page:**
> "Write homepage copy for a fitness app. Target audience is busy professionals who want to work out at home."

**Video script:**
> "Write a 30-second UGC script for our skincare product. Target: women 25-35, solution-aware."

**Graphic copy:**
> "Write headline and CTA text for a static Meta ad promoting our free trial."

**Voiceover:**
> "Write a 60-second voiceover script for a product demo video."

## File Structure

```
.claude/skills/copywriting/
  SKILL.md              # Main skill definition
  references/
    frameworks.md       # 13 framework structures with timing, examples, and principle pairings
```

## Framework Selection Guide

| Framework | Best For | Awareness Stage | Length |
|-----------|----------|----------------|-----related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| PAS | Pain-driven ads and scripts | Problem Aware | Short-Medium |
| AIDA | Structured persuasion sequences | Solution Aware | Medium-Long |
| BAB | Quick transformation messaging | Problem Aware | Short-Medium |
| Hook-Story-Offer | Story-driven ads and scripts | All stages | Medium-Long |
| SLAP | Ultra-short graphic/ad copy | Most Aware | Ultra-Short |
| FAB | Feature-to-benefit connections | Product Aware | Short |
| UGC Direct Response | Authentic testimonial scripts | Problem-Solution Aware | Medium |
| Harmon Brothers | Comedy-driven explainer videos | Unaware-Problem Aware | Long |

See `references/frameworks.md` for the full list with structures and examples.

## Related Skills

This skill works well alongside:
- **[ad-creative](https://github.com/growthquest/ad-creative)** - Platform specs, bulk generation, performance iteration
- **[meta-ads-research](https://github.com/growthquest/meta-ads-research)** - Deep client research that feeds into copywriting via Creative DNA
- **[organic-client-research](https://github.com/growthquest/organic-client-research)** - Organic strategy research

## License

MIT
