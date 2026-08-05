---
id: tool-05154
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 需API密钥, 英文文档, 去AI味]
title: slop-detector
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/the-swarm-corporation/slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5154
category: 一、去 AI 味 / Humanizer 库
repo: The-Swarm-Corporation/slop-detector
stars: 5
url: https://github.com/the-swarm-corporation/slop-detector
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# The-Swarm-Corporation/slop-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/the-swarm-corporation/slop-detector
- **Stars**：5
- **语言**：Python
- **License**：Apache-2.0
- **Topics**：agents, ai, claude, code, code-agent, coding-agent, ml, opencode
- **GitHub 描述**：Slop Detector is an agent-powered GitHub Actions workflow that acts as an automated code quality gate on every push. It catches low-effort, careless, or AI-generated code collectively known as "slop" before it reaches your main branch, production environment, or your teammates' code review queue.
- **本地描述**：Slop Detector is an agent-powered GitHub Actions workflow that acts as an automated code quality gate on every push. It catches low-effort, careless, or AI-generated code collectively known as "slop" before it reaches your main branch, production environment, or your teammates' code review queue.
- **拉取时间**：2026-07-25 18:08:07

---

# Slop Detector

<p align="left">
  <a href="https://github.com/The-Swarm-Corporation/slop-detector/stargazers"><img src="https://img.shields.io/github/stars/The-Swarm-Corporation/slop-detector?style=for-the-badge&logo=starship&logoColor=white&color=f5a623&labelColor=1a1a2e" alt="Stars"/></a>
  <a href="https://discord.gg/EamjgSaEQf"><img src="https://img.shields.io/badge/Discord-Join%20Community-5865F2?style=for-the-badge&logo=discord&logoColor=white&labelColor=1a1a2e" alt="Discord"/></a>
  <a href="https://twitter.com/swarms_corp"><img src="https://img.shields.io/badge/Twitter-%40swarms__corp-000000?style=for-the-badge&logo=x&logoColor=white&labelColor=1a1a2e" alt="Twitter"/></a>
  <a href="https://swarms.ai"><img src="https://img.shields.io/badge/Website-swarms.ai-6C63FF?style=for-the-badge&logo=firefox-browser&logoColor=white&labelColor=1a1a2e" alt="Website"/></a>
</p>

!`[slop detector](logo.png)`

**AI-powered code quality enforcement for GitHub — identify slop, block it from reaching production, and get actionable feedback on every commit.**

> **Full documentation:** `[DOCS.md](./DOCS.md)` — covers architecture, local testing, threshold tuning, troubleshooting, security considerations, and complete configuration reference.

---

## Overview

Slop Detector is an AI-powered GitHub Actions workflow that acts as an automated code quality gate on every push. It catches low-effort, careless, or AI-generated code collectively known as "slop" — before it reaches your main branch, production environment, or your teammates' code review queue.

**Identify slop.** Every commit is analysed by a Gemini-powered [Swarms](https://github.com/kyegomez/swarms) agent trained to think like a principal engineer. It reads the diff, scores it from `0.0` (pristine) to `1.0` (catastrophic), and surfaces every specific violation — missing types, undocumented functions, placeholder logic, and AI-generated noise — with precise line references.

**Prevent slop from reaching production.** When a commit's score exceeds your configured threshold, Slop Detector automatically runs `git revert` and pushes the revert commit back to the branch — no human intervention required. The workflow step is also marked red in the GitHub UI, blocking any dependent CI steps or deployment pipelines.

**Get strategic feedback.** Every analysis produces a structured report: a numeric quality score, a one-sentence summary of what the diff does and how good it is, a ranked list of violations with severity levels, a set of positive notes on what the code gets right, and a single concrete recommendation for what the developer should fix. This lands directly in the GitHub Actions step summary, visible to every contributor.

Drop it into any repository in under two minutes. No infrastructure, no dashboards, no new tools to learn — just a workflow file and an API key.

---

## What is Slop?

Slop refers to code that is careless, unfinished, or generated without thought. The agent evaluates four categories of violations:

| Category | Examples |
|---|---|
| Missing types | Python functions with no parameter or return type hints; TypeScript variables typed as `any`; untyped callback parameters |
| Missing documentation | Public functions or classes with no docstring or JSDoc; complex logic blocks over 10 lines with no explanatory comments; new API surface with no parameter descriptions |
| Placeholder code | `TODO`, `FIXME`, `HACK`, `NOCOMMIT` comments; `pass` inside functions; `raise NotImplementedError`; placeholder variable names such as `foo`, `bar`, `tmp`; empty `except` or `catch` blocks; hardcoded sentinel strings such as `CHANGEME` |
| AI-generated slop patterns | Comments that restate the code; over-engineered solutions for trivial problems; inconsistent naming conventions within the same file; verbatim copy-paste blocks differing only by a variable name; generic meaningless names such as `handleData`, `doThing`, or `utils2`; dead code and unused imports |

The agent only examines **added lines** (lines prefixed with `+` in the diff, excluding `+++` header lines). Deleted lines are never penalised. The following are always scored `0.0` and skipped:

- Config and data files (JSON, YAML, TOML, `.env`, `.ini`)
- Lockfiles (`package-lock.json`, `yarn.lock`, `poetry.lock`, `go.sum`)
- Auto-generated files (`*.pb.go`, `*.pb.ts`, `_generated.*`, `schema.prisma`, migration files)
- Diffs consisting entirely of whitespace or formatting changes
- Diffs with fewer than 10 added lines of substantive code

---

## Rating Scale

| Range | Meaning |
|---|---|
| 0.00 – 0.20 | Excellent — fully typed, documented, and purposeful. Production-ready. |
| 0.20 – 0.40 | Good — a handful of missing annotations or brief comments. Solid overall. |
| 0.40 – 0.50 | Acceptable — noticeable gaps in types or docs; no critical red flags. |
| 0.50 – 0.70 | Poor — multiple violations. Real work needed before this can ship. |
| 0.70 – 0.90 | Bad — widespread slop patterns or large swaths of placeholder logic. |
| 0.90 – 1.00 | Catastrophic — this should never have been committed. |

The default threshold is `0.5`. Any commit rated above `0.5` is reverted automatically.

---

## Installation

### 1. Add the Gemini API key as a repository secret

Navigate to **Settings > Secrets and variables > Actions > New repository secret** and add:

```
Name:  GEMINI_API_KEY
Value: sk-...
```

### 2. Add the workflow file

Create `.github/workflows/slop-detector.yml` in your repository. The fastest approach is to copy the bundled example:

```bash
mkdir -p .github/workflows
curl -o .github/workflows/slop-detector.yml \
  https://raw.githubusercontent.com/The-Swarm-Corporation/slop-detector/main/example-workflow.yml
```

Alternatively, copy `[`example-workflow.yml`](./example-workflow.yml)` manually.

### 3. Update the `uses:` reference

Edit the workflow file and replace the placeholder reference with your fork or a pinned release tag:

```yaml
uses: The-Swarm-Corporation/slop-detector@main
```

The action requires `contents: write` permission on the workflow job so the bot can push revert commits.

---

## Usage

Minimal workflow configuration:

```yaml
name: Slop Detector

on:
  push:
    branches:
      - main

permissions:
  contents: write

jobs:
  slop-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 2

      - uses: The-Swarm-Corporation/slop-detector@main
        with:
          gemini_api_key: ${{ secrets.GEMINI_API_KEY }}
```

`fetch-depth: 2` is required so the action can compute `git diff HEAD~1 HEAD`. A depth of `1` (the default shallow clone) will cause the diff capture step to fall back to comparing against an empty tree.

### Inputs

| Input | Required | Default | Description |
|---|---|---|---|
| `gemini_api_key` | Yes | — | Gemini API key. Store as a repository secret and pass via `${{ secrets.GEMINI_API_KEY }}`. |
| `threshold` | No | `0.5` | Slop rating above which a commit is automatically reverted. Accepts any float between `0.0` and `1.0`. Set to `1.1` to disable automatic reverts while keeping reporting. |
| `model_name` | No | `gemini-2.0-flash` | Gemini model identifier. Use `gemini-2.0-flash` for lower cost and faster analysis at the expense of some accuracy. |
| `github_token` | No | `${{ github.token }}` | Token used to push the revert commit. The default `GITHUB_TOKEN` is sufficient for most repositories. |
| `fail_on_slop` | No | `true` | When `true`, the step exits with a non-zero code if slop is detected. Set to `false` to revert silently without marking the check red. |

### Outputs

| Output | Type | Description |
|---|---|---|
| `rating` | float string | Numeric slop score, e.g. `0.72`. |
| `verdict` | string | `PASS` or `FAIL`. |
| `summary` | string | One-sentence description of the diff and its overall quality. |
| `reverted` | boolean string | `true` if the commit was reverted, `false` otherwise. |

### Using Outputs in Downstream Steps

Assign an `id` to the action step to reference its outputs:

```yaml
- name: Run slop-detector
  id: slop
  uses: The-Swarm-Corporation/slop-detector@main
  with:
    gemini_api_key: ${{ secrets.GEMINI_API_KEY }}

- name: Post PR comment on failure
  if: steps.slop.outputs.verdict == 'FAIL'
  uses: actions/github-script@v7
  with:
    script: |
      github.rest.issues.createComment({
        issue_number: context.issue.number,
        owner: context.repo.owner,
        repo: context.repo.repo,
        body: `Slop detected (rating: ${{ steps.slop.outputs.rating }})\n${{ steps.slop.outputs.summary }}`
      })
```

### Threshold Tuning

```yaml
threshold: '0.3'   # Strict — revert anything below a good rating
threshold: '0.5'   # Default — revert poor or worse
threshold: '0.7'   # Lenient — only revert genuinely bad or catastrophic code
threshold: '1.1'   # Reporting only — never revert, only annotate
```

---

## Architecture

### Action Composite Steps

`action.yml` defines the action as a composite run, executing the following steps in sequence:

```
1. Set up Python 3.11
       |
       v
2. Restore pip cache (keyed on OS + action.yml hash)
       |
       v
3. Install dependencies (swarms>=7.9.0)
       |
       v
4. Capture git diff
       git diff HEAD~1 HEAD > /tmp/slop_diff.patch
       (falls back to empty-tree diff for the initial commit)
       |
       v
5. Run scripts/detect.py
       |
       v
6. Revert commit (conditional: only if should_revert == 'true')
       git revert --no-edit <sha>
       git commit --amend -m "revert: slop-detector reverted <sha>..."
       git push origin HEAD:<branch>
       |
       v
7. Propagate failure (conditional: only if fail_on_slop == 'true')
       exit 1
```

Steps 5 and 6 are decoupled: step 5 runs with `continue-on-error: true` and communicates its decision through `GITHUB_OUTPUT` rather than its exit code. Step 7 is what ultimately fails the workflow, ensuring the revert push in step 6 always completes first.

### Analysis Agent

`scripts/detect.py` constructs a single-turn Swarms `Agent` instance on each invocation:

```python
agent = Agent(
    agent_name="SlopDetector",
    system_prompt=SYSTEM_PROMPT,
    model_name=model_name,   # from MODEL_NAME env var
    max_loops=1,
    output_type="str",
)
```

The system prompt defines the agent as a principal engineer with explicit scoring criteria, severity levels for each violation category, context rules (what to ignore), and a strict JSON-only output contract. Setting `max_loops=1` ensures a single inference call with no autonomous tool use or re-prompting.

Before invoking the agent, the script applies two pre-flight checks:

- **Trivial diff detection** — diffs with zero added lines or whose only changed files match a hardcoded skip list (lockfiles, generated code) bypass the agent entirely and receive a synthetic `PASS` with `rating: 0.0`.
- **Diff truncation** — diffs exceeding 60,000 characters are truncated to keep the request within context limits. A note is appended to the task prompt informing the agent of the truncation.

### Scoring and Decision Logic

The agent returns a JSON object with the following contract:

```json
{
  "rating": 0.0,
  "verdict": "PASS",
  "summary": "...",
  "violations": [
    {
      "type": "missing_types | missing_docs | placeholder_code | slop_pattern",
      "severity": "critical | high | medium | low",
      "description": "...",
      "line": "..."
    }
  ],
  "positive_notes": ["..."],
  "recommendation": "..."
}
```

After receiving the response, `detect.py` strips any accidental markdown fences and parses the JSON with a regex fallback. The rating is then clamped to `[0.0, 1.0]` regardless of what the model returns. `verdict` is recomputed deterministically from `rating > threshold` so the action's pass/fail logic does not rely on the model's own verdict field.

### Automatic Revert Mechanism

When `should_revert` is `true`, the composite action:

1. Configures git identity as `slop-detector[bot]`.
2. Updates the remote URL to include the GitHub token for authentication.
3. Runs `git revert --no-edit <sha>` to generate the inverse commit.
4. Amends the commit message to include the slop rating, threshold, one-sentence summary, and original SHA.
5. Pushes the revert commit directly to the source branch.

The revert commit message follows this format:

```
revert: slop-detector reverted <sha[:7]>

Slop rating <rating> exceeded threshold <threshold>.
<summary>

Original commit: <sha>
Reverted by: slop-detector[bot]
```

### GitHub Step Summary

After every analysis, `detect.py` writes a Markdown table to `GITHUB_STEP_SUMMARY`, which renders as a formatted report on the workflow run's summary page. When a revert is triggered, the summary includes a blockquote warning indicating the automatic revert.

---

## Requirements

| Requirement | Details |
|---|---|
| GitHub Actions | Any runner with `ubuntu-latest` or Python 3.11+ available |
| Gemini API key | Required for Gemini model access |
| Repository permission | `contents: write` on the workflow job |
| Python | 3.11 (installed automatically by the action) |
| swarms | `>=7.9.0` (installed automatically by the action) |
| Checkout depth | `fetch-depth: 2` minimum to enable parent-commit diffing |

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## Further Reading

See `[DOCS.md](./DOCS.md)` for the complete documentation including architecture deep dive, local testing instructions, threshold tuning guide, troubleshooting, and security considerations.
