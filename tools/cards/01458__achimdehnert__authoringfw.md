---
id: tool-01458
type: tool
area: 库
status: active
tags: [提示词, Python, 协议宽松, 本地优先, 英文文档, 多Agent, 本地写作]
title: authoringfw
summary: 提示词/写作工作流
source: https://github.com/achimdehnert/authoringfw
created: 2026-07-18
updated: 2026-07-18
no: 1458
category: 二、网文 / 长篇 AI 写作系统 库
repo: achimdehnert/authoringfw
stars: 0
url: https://github.com/achimdehnert/authoringfw
tier: "C"
use_case: "提示词/写作工作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 0a0ec57d046f725f
  - methods/最强写作方法论_全球最强综合版.md
---

# achimdehnert/authoringfw

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/achimdehnert/authoringfw
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Authoring Framework — domain schemas for AI-assisted creative writing applications
- **本地描述**：Authoring Framework — domain schemas for AI-assisted creative writing applications
- **拉取时间**：2026-07-23 23:21:35

---

# iil-authoringfw — Authoring Framework

Domain schemas for AI-assisted creative writing applications.

[![PyPI](https://img.shields.io/pypi/v/iil-authoringfw)](https://pypi.org/project/iil-authoringfw/)
[![Python](https://img.shields.io/pypi/pyversions/iil-authoringfw)](https://pypi.org/project/iil-authoringfw/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation

```bash
pip install iil-authoringfw
# With aifw LLM integration:
pip install "iil-authoringfw[aifw]"
# All optional dependencies:
pip install "iil-authoringfw[all]"
```

## Extras / Optional Dependencies

| Extra | Dependencies | Purpose |
|---|---|related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| `aifw` | iil-aifw>=0.11.4 | LLM completion integration (quality_level/priority routing needs >=0.11.2) |
| `yaml` | pyyaml>=6.0 | YAML template loading |
| `promptfw` | iil-promptfw>=0.5.5 | Prompt template rendering |
| `all` | all above | Full feature set |

## Quick Start

```python
from authoringfw import StyleProfile, CharacterProfile, WorldContext, get_format

# Style constraints for prompt injection
style = StyleProfile(tone="melancholic", pov="third_limited", tense="past")
constraints = style.to_constraints()

# Character context
alice = CharacterProfile(
    name="Alice",
    role="protagonist",
    personality_traits=["brave", "curious"],
    arc="From fear to courage",
)
print(alice.to_context_string())

# World context
world = WorldContext(
    title="The Shattered Realms",
    genre="fantasy",
    world_rules=["Magic costs life force", "Dragons are extinct"],
)
print(world.to_context_string())

# Format profiles (novel, essay, series, scientific)
roman = get_format("roman")
print(roman.style_constraints)
```

## Schemas

- **`StyleProfile`** — tone, POV, tense, vocabulary, sentence rhythm
- **`CharacterProfile`** — name, role, traits, backstory, arc, relationships
- **`WorldContext`** — title, genre, setting, world rules, locations, lore
- **`VersionMetadata`** — immutable content snapshot with hash, semver, LLM metadata
- **`PhaseSnapshot`** — project state at a workflow phase boundary

## Format Profiles

Built-in formats: `roman` (alias `novel`), `essay`, `serie`, `scientific`,
`nonfiction`, `academic`, `screenplay`, `short_story`, `blog_post`, `podcast_script`.
The registry (`authoringfw.formats.base.FORMAT_REGISTRY`) is the source of truth.

```python
from authoringfw.formats.base import get_format, WorkflowPhase

novel = get_format("roman")
outline_steps = novel.steps_for_phase(WorkflowPhase.OUTLINE)
```

## Adapter Interfaces

Protocol-based adapters — no inheritance required:

```python
from authoringfw.adapters.interfaces import IStyleAdapter

class MyStyleAdapter:
    async def get_profile(self, style_id): ...
    async def analyze_text(self, text): ...
    def generate_style_constraints(self, profile): ...
    async def score_conformity(self, text, profile): ...

adapter = MyStyleAdapter()
assert isinstance(adapter, IStyleAdapter)  # True via @runtime_checkable
```

## Changelog

See [CHANGELOG.md](https://github.com/achimdehnert/authoringfw/blob/main/CHANGELOG.md).
