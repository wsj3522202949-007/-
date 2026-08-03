---
id: tool-05491
type: tool
area: 库
status: active
tags: [JavaScript, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: slopspec
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/sangmorg1-debug/slopspec
created: 2026-07-18
updated: 2026-07-18
no: 5491
category: 一、去 AI 味 / Humanizer 库
repo: sangmorg1-debug/slopspec
stars: 0
url: https://github.com/sangmorg1-debug/slopspec
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# sangmorg1-debug/slopspec

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/sangmorg1-debug/slopspec
- **Stars**：0
- **语言**：JavaScript
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Static detector for AI-agent-generated slop tests -- tautological assertions and SUT-mocking, across Python and JS/TS
- **本地描述**：Static detector for AI-agent-generated slop tests -- tautological assertions and SUT-mocking, across Python and JS/TS
- **拉取时间**：2026-07-25 18:20:41

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# slopspec

Static detector for AI-agent-generated "slop tests" — tests that pass but
don't verify real behavior.

## Why

A 2026 peer-reviewed study ([arXiv 2602.00409](https://arxiv.org/abs/2602.00409))
mined 1.2M commits across 2,168 JS/TS/Python repos and found coding agents
add mocks in 36% of test-touching commits versus 26% for humans. `slopspec`
statically flags two specific, well-evidenced patterns: tautological
assertions (`assert True`, `expect(x).toBe(x)`) and mocking the exact
module/function a test claims to cover, rather than a genuine collaborator.

Fast enough to run on every agent turn — pure static analysis, no test
execution, no mutation testing (that's a different, complementary tool).

## Install

Not on PyPI yet — install from source:

```bash
pip install git+https://github.com/sangmorg1-debug/slopspec.git
```

## Usage

```bash
slopspec path/to/test_file.py path/to/other.test.ts
slopspec src/ --format json
slopspec src/ --watch
```

## What it does not do

- No mutation testing — use Stryker/mutmut/PIT for "did this test actually
  catch a bug"; `slopspec` is a fast, diagnostic complement, not a
  replacement.
- No "function under test never invoked" check, no near-duplicate-test
  detection — real patterns, deferred to a later version.
- No auto-fix — report only.
- JS/TS checks require `node` on `PATH` (no `npm install` needed — the
  analyzer ships pre-bundled). If `node` isn't found, Python checks still
  run and the gap is reported explicitly.

MIT License.
