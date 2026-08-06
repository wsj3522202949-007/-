---
id: tool-00025
type: tool
area: 库
status: active
tags: [多Agent, 协议宽松, 需API密钥, 英文文档]
title: ai-writing-studio
summary: 多 Agent 协作自动产文
source: https://github.com/maxjeffwell/ai-writing-studio
created: 2026-07-18
updated: 2026-07-18
no: 25
category: 二、网文 / 长篇 AI 写作系统 库
repo: maxjeffwell/ai-writing-studio
stars: 1
url: https://github.com/maxjeffwell/ai-writing-studio
tier: "B"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# maxjeffwell/ai-writing-studio

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/maxjeffwell/ai-writing-studio
- **Stars**：1
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI-powered writing platform for fiction authors. Multi-agent system helps maintain consistency across complex storylines with persistent memory, database branching for alternate   timelines, and specialized agents for continuity, characters, timeline, and story editing.
- **本地描述**：AI-powered writing platform for fiction authors. Multi-agent system helps maintain consistency across complex storylines with persistent memory, database branching for alternate   timelines, and specialized agents for continuity, characters, timeline, and story editing.
- **拉取时间**：2026-07-23 22:39:35

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI Writing Studio - World Builder for Authors

A collaborative AI-powered writing platform that helps fiction writers maintain consistency across complex storylines, characters, and world-building with persistent memory.

## Core Concept

Multiple specialized AI agents work together to help authors:
- Track character traits, relationships, and development arcs
- Maintain timeline consistency across complex narratives
- Catch continuity errors and plot holes
- Explore alternate story paths using database branches
- Build rich, consistent fictional worlds

## Key Features

### Branch-per-Story-Arc
- **Main branch** = canonical storyline
- **Feature branches** = "what-if" alternate timelines
- Test major plot changes (character deaths, alternate endings) without commitment
- Merge accepted changes back to canon

### AI Agent Roles

1. **Continuity Agent**: Catches contradictions in character details, locations, events
2. **Character Agent**: Tracks personality traits, speech patterns, relationships, arcs
3. **Timeline Agent**: Ensures events happen in logical chronological order
4. **Research Agent**: Fetches real-world facts for historical/sci-fi accuracy
5. **Editor Agent**: Suggests improvements for plot holes, pacing, character development

### Structured Story Database

- **Characters**: traits, backstories, relationships, dialogue history
- **Locations**: descriptions, who visited, what happened there
- **Plot Threads**: open/closed, foreshadowing, payoffs
- **Objects**: Chekhov's guns, magical items, important props
- **Timeline**: all events in chronological order with references
- **Scenes/Chapters**: actual story content linked to all entities

## Why Neon?

- **Branching**: Perfect for alternate timelines and story experimentation
- **Serverless**: Scale-to-zero for cost efficiency (writers work sporadically)
- **Multi-tenant**: Each author gets isolated data (via branches or separate projects)
- **Postgres**: Proven relational model for complex story relationships

## Tech Stack (Proposed)

- **Database**: Neon (Postgres with branching)
- **ORM**: Drizzle (type-safe, migrations)
- **Auth**: Neon Auth + Stack Auth
- **Backend**: Next.js App Router (API routes + server actions)
- **Frontend**: React + TypeScript
- **AI**: Claude API (Anthropic)
- **Vector Search**: pgvector for semantic search across story content
- **Deployment**: Vercel

## Monetization Strategy

- **Free Tier**: 1 story, 50k words, basic agents
- **Author Plan**: Unlimited stories, all agents, export features
- **Studio Plan**: Team collaboration, IP management, publishing integrations

## Target Users

- Fiction writers (novels, screenplays, game narratives)
- Dungeon Masters / RPG world builders
- Writing teams working on shared universes
- Anyone building complex fictional worlds

## Competitive Advantages

1. **Persistent Memory**: Unlike ChatGPT, the database remembers everything forever
2. **Structured Data**: Relational model beats unstructured notes/wikis
3. **Branch-based Exploration**: Unique capability for testing story directions
4. **Multi-Agent System**: Specialized agents for different aspects of writing
5. **Collaborative**: Teams can work on shared story universes

## Next Steps

See [ROADMAP.md](https://github.com/maxjeffwell/ai-writing-studio/blob/main/ROADMAP.md) for development phases and [SCHEMA.md](https://github.com/maxjeffwell/ai-writing-studio/blob/main/SCHEMA.md) for database design.
