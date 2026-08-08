---
id: tool-04194
type: tool
area: 库
status: active
tags: [多Agent, Python, 协议宽松, 需API密钥, 英文文档]
title: ai-test-generator
summary: 多 Agent 协作自动产文
source: https://github.com/vazidmansuri005/ai-test-generator
created: 2026-07-18
updated: 2026-07-18
no: 4194
category: 十、其他 AI 写作 / 文本工具 库
repo: vazidmansuri005/ai-test-generator
stars: 2
url: https://github.com/vazidmansuri005/ai-test-generator
tier: "B"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 01f64762ae479c19
  - methods/QUICK_START.md
---

# vazidmansuri005/ai-test-generator

- **分类**：十、其他 AI 写作 / 文本工具 库
- **链接**：https://github.com/vazidmansuri005/ai-test-generator
- **Stars**：2
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：AI-powered test case generator — from user stories to executable pytest/playwright tests, powered by Claude
- **本地描述**：AI-powered test case generator — from user stories to executable pytest/playwright tests, powered by Claude
- **拉取时间**：2026-07-24 00:04:35

---

# AI Test Generator — Agentic QA

An autonomous QA system powered by Claude with two features no other open-source tool has: **Failure Memory** (the agent learns from corrections and gets smarter over time) and **PR Impact Analysis** (predicts which tests break from a git diff, semantically).

```
┌──────────────────────────────────────────────────────────────────────┐
│                        AGENTIC QA PIPELINE                          │
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────┐  ┌────────┐  │
│  │ Layer 1  │─▶│ Layer 2  │─▶│ Layer 3  │  │ Memory │  │ Impact │  │
│  │ Generate │  │ Diagnose │  │ Report   │  │   🧠   │  │   🎯   │  │
│  │          │  │          │  │          │  │        │  │        │  │
│  │ Story →  │  │ 3 Hypo-  │  │ Pipeline │  │ Learns │  │ PR Diff│  │
│  │ Tests →  │  │ theses + │  │ + GitHub │  │ from   │  │ → Test │  │
│  │ Code     │  │ Evidence │  │ Issues   │  │ you    │  │ Risk   │  │
│  └──────────┘  └──────────┘  └──────────┘  └────────┘  └────────┘  │
└──────────────────────────────────────────────────────────────────────┘
```

## What Makes This Different

| Feature | Other Tools | This Tool |
|---------|------------|-----------|
| Test generation | Generate from code (Qodo) or NL (Shortest) | Generate structured test cases + executable code from user stories |
| Failure analysis | Group by similarity (ReportPortal) | Differential diagnosis — 3 hypotheses with evidence for/against |
| Learning | Stateless — every run starts from zero | **Failure Memory** — corrections improve future diagnoses |
| Impact prediction | File-level mapping (OpenClover) or proprietary (Microsoft) | **Semantic PR impact** — understands what changed, not just which file |
| Classification confidence | Binary pass/fail | Confidence scoring (high/medium/low) + severity ranking (P0-P3) |

## Quick Start

```bash
git clone https://github.com/vazidmansuri005/ai-test-generator.git
cd ai-test-generator
pip install -e ".[dev]"
export ANTHROPIC_API_KEY=sk-ant-xxxxx
```

## Layer 1 — Test Generation

```bash
# Generate test cases from a user story
ai-test-gen generate "User login with email and password"

# Generate executable pytest code
ai-test-gen code test_suite.json --framework pytest --output test_login.py

# Both in one shot
ai-test-gen one-shot "Shopping cart checkout" --framework playwright -d ./tests
```

Generates 8-12 test cases covering happy path, edge cases, negative, boundary, security, and accessibility — with executable pytest or Playwright code.

## Layer 2 — Failure Diagnosis

```bash
# Diagnose from pytest JSON report
ai-test-gen diagnose report.json

# Diagnose from JUnit XML (any framework)
ai-test-gen diagnose results.xml --format junit-xml --output triage.md
```

For each failure, evaluates three hypotheses:

| Hypothesis | Meaning |
|------------|------related:
  - methods/QUICK_START.md
---|
| `test_issue` | Broken locator, flaky wait, wrong assertion |
| `infra_issue` | Timeout, DNS failure, container crash |
| `product_bug` | Actual defect in the application |

Each gets evidence **for** and **against**. When evidence is split → classifies as `unknown` (better than guessing wrong).

## Layer 3 — Full Pipeline

```bash
# End-to-end: generate → execute → diagnose → report
ai-test-gen pipeline "User login with email and password"

# With auto GitHub issue filing
ai-test-gen pipeline "Checkout flow" --auto-issue --github-repo myuser/myapp
```

## Failure Memory — The Agent Learns From You

**This is the feature no other OSS testing tool has.**

Every AI testing tool today is stateless. This one remembers. When you correct a misdiagnosis, the pattern is stored and used to improve future runs.

```bash
# The agent diagnoses a timeout as infra_issue
ai-test-gen diagnose report.json
> test_checkout::test_payment → 🔧 infra_issue (medium confidence)

# You know better — it's a stale CSS selector
ai-test-gen feedback "test_checkout::test_payment" \
    --correct-to test_issue \
    --reason "Stale CSS selector, not a network issue" \
    --error-pattern "TimeoutError: wait_for_selector"

# Next run — the agent remembers your correction
ai-test-gen diagnose report2.json
> test_cart::test_total → 🧪 test_issue (high confidence)
> Note: Similar to corrected pattern from test_checkout::test_payment

# Check what the agent has learned
ai-test-gen memory
```

The memory compounds over time. After 20-30 corrections, the agent becomes deeply tuned to YOUR codebase's specific failure patterns.

**How it works:**
- Corrections stored in `~/.ai-test-gen/memory/corrections.json`
- Pattern matching uses token overlap + substring matching (no embeddings needed)
- Matching corrections are injected into the diagnosis prompt as context
- Stats tracked: which classifications get corrected most often

## PR Impact Analysis — Predict Before You Break

**Microsoft and Google have this internally. Nobody has open-sourced it. Until now.**

```bash
# Predict impact of your last commit
ai-test-gen impact

# Predict impact of changes vs main branch
ai-test-gen impact --diff main

# Analyze a specific commit
ai-test-gen impact --diff abc123 --repo /path/to/project
```

Output:
```
🎯 PR Impact Analysis

3 tests at risk from 3 changed files

┌────────────────────────────────────────────────────────────────┐
│ Risk │ Test                │ Changed File     │ Reason          │
├──────┼─────────────────────┼──────────────────┼─────────────────┤
│ 🔴   │ test_checkout_flow  │ src/payment.py   │ Removed null    │
│ HIGH │                     │                  │ check on L47    │
│ 🟡   │ test_apply_discount │ src/pricing.py   │ Discount logic  │
│ MED  │                     │                  │ changed         │
│ 🟢   │ test_search         │ src/search.py    │ Only logging    │
│ LOW  │                     │                  │ changes         │
└──────┴─────────────────────┴──────────────────┴─────────────────┘

Recommendation: Run test_payment.py first, then test_cart.py.
```

**What makes this semantic, not just file-level:**
- Understands that a change to an error path only affects error-scenario tests
- Knows that logging changes are low risk even if the file is heavily tested
- Provides the **causal chain**: "file X changed function Y which handles Z, test T asserts on Z"

## All CLI Commands

```
ai-test-gen generate   — Generate test cases from feature description
ai-test-gen code       — Generate test code from test suite JSON
ai-test-gen one-shot   — Generate cases + code in one command
ai-test-gen diagnose   — Diagnose failures with differential diagnosis
ai-test-gen pipeline   — Run the full agentic pipeline
ai-test-gen feedback   — Correct a diagnosis (agent learns)
ai-test-gen memory     — View stored corrections and learning stats
ai-test-gen impact     — Predict test impact from code changes
```

## Running Tests

```bash
pytest tests/ -v
```

47 tests covering all layers — generation, parsing, diagnosis, memory, impact, and reporting.

## Architecture

```
src/ai_test_generator/
├── generator.py          # Layer 1: Test generation from user stories
├── diagnoser.py          # Layer 2: Differential diagnosis engine
├── orchestrator.py       # Layer 3: Full pipeline orchestration
├── memory.py             # Failure Memory: persistent learning loop
├── impact.py             # PR Impact: semantic test risk prediction
├── models.py             # Pydantic models for all components
├── cli.py                # CLI interface (click + rich)
├── parsers/
│   ├── pytest_parser.py  # Parse pytest-json-report output
│   └── junit_parser.py   # Parse JUnit XML (universal)
└── reporters/
    ├── markdown_reporter.py  # Generate triage reports
    └── github_reporter.py    # File GitHub issues via gh CLI
```

## License

MIT
