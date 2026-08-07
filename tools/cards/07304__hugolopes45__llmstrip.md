---
id: tool-07304
type: tool
area: 库
status: active
tags: [Claude插件, Rust, 协议宽松, 需API密钥, 英文文档]
title: llmstrip
summary: Claude Code 插件式写作流
source: https://github.com/hugolopes45/llmstrip
created: 2026-07-18
updated: 2026-07-18
no: 7304
category: 画龙补充 / 扩容入库 — 补充源
repo: hugolopes45/llmstrip
stars: 11
url: https://github.com/hugolopes45/llmstrip
tier: "B"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/QUICK_START.md
---

# hugolopes45/llmstrip

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/hugolopes45/llmstrip
- **Stars**：11
- **语言**：Rust
- **License**：MIT
- **Topics**：ai-humanizer, ai-tools, ai-writing, anthropic, claude, claude-code, claude-code-skills, claude-skills, cli, cursor, developer-tools, git-hooks, humanize, linter, llm, opencode, productivity, rust, text-processing
- **GitHub 描述**：Strip LLM writing patterns from prose, code comments, and commits — CLI, Claude Code skill, Cursor rule, and LLM system prompt.
- **本地描述**：llmstrip
- **拉取时间**：2026-07-25 19:17:13

related:
  - methods/QUICK_START.md
---

# llmstrip

Strip AI patterns from text and code. Prompt + linter.

> 25× excess frequency of `delve` post-ChatGPT. 280+ excess words identified. 34 structural rules. Grounded in peer-reviewed data.

![demo](assets/demo.gif)

## Two ways to use it

**Interactive — the prompt (recommended)**

Paste the system prompt into any LLM, or use the Claude Code skill. The LLM rewrites your text using all 34 rules, including structural patterns that no regex can catch.

**Automation — the binary**

Run `llmstrip --report --fail` in CI or as a git hook. Same rules, deterministic, no network, no runtime.

## Install the prompt

**Claude Code skill:**

```bash
mkdir -p ~/.claude/skills/llmstrip
curl -sL https://raw.githubusercontent.com/HugoLopes45/llmstrip/main/prompts/claude-code.md \
  > ~/.claude/skills/llmstrip/SKILL.md
```

Or from the repo: `make install-skill`

Type `/llmstrip` in any Claude Code session to clean the current file.

**Other tools:**

```bash
make install-cursor    # Cursor — .cursor/rules/llmstrip.mdc
make install-copilot   # GitHub Copilot — .github/copilot-instructions.md
make install-windsurf  # Windsurf
make install-zed       # Zed
make install-all       # All of the above
```

Or copy `prompts/system-prompt.md` into any LLM's system prompt directly.

## Install the binary

```bash
curl -fsSL https://raw.githubusercontent.com/HugoLopes45/llmstrip/main/scripts/install.sh | sh
```

Or via Cargo:

```bash
cargo install --git https://github.com/HugoLopes45/llmstrip
```

## Use cases

### Filter every Claude response automatically

```bash
# .claude/settings.json — PostToolUse hook
{
  "hooks": {
    "PostToolUse": [{
      "matcher": ".*",
      "hooks": [{"type": "command", "command": "llmstrip"}]
    }]
  }
}
```

### Strip AI prose

```bash
echo "Let me delve into this robust and comprehensive approach." | llmstrip
# -> Let me dig into this solid and thorough approach.
```

### Clean AI-generated code comments

```bash
llmstrip --report --mode code service.py

# Mode: code  |  4 finding(s)
#
# HIGH (1)
#   line 2: LLM docstring boilerplate: 'this function serves as'
#
# MEDIUM (3)
#   line 1: Type-in-name: use 'user' instead of 'userDataObject'
```

### Catch AI commit messages before they land

```bash
# .git/hooks/commit-msg
#!/bin/sh
llmstrip --mode code --rules commits --report --fail --min-severity high "$1"
```

## CI gate

Block AI-written release notes in CI:

```bash
llmstrip --report --fail --min-severity high release-notes.md
```

## Rules

34 rules across two levels:

**Word-level (Rules 1-24):** significance inflation, banned vocabulary (delve, robust, leveraging, seamlessly...), copula avoidance, sycophantic openers, chatbot closers, filler phrases, excessive hedging.

**Structural (Rules 25-34):** compound clause addiction, mini-essay paragraphs, sentence-initial transition saturation, paired construction overuse, noun phrase bloat, self-congratulation framing, abstraction level monotony, missing contractions, forward projection cliche, resume verbs.

Full list: [`rules/`](https://github.com/hugolopes45/llmstrip/tree/main/rules/)

## Research

Rules are grounded in peer-reviewed corpus studies:

- **Kobak et al. (2025)** — 15M PubMed abstracts. `delve` appeared 25× more often post-ChatGPT. 280+ excess words. [arXiv:2406.07016](https://arxiv.org/abs/2406.07016)
- **Liang et al. (2024)** — 950K+ papers. `pivotal`, `intricate`, `realm` doubled post-2023. [arXiv:2404.01268](https://arxiv.org/abs/2404.01268)
- **Juzek & Ward (2025)** — RLHF causes it. Human raters prefer formal-sounding output. Models overfit. [arXiv:2412.11385](https://arxiv.org/abs/2412.11385)

## Contribute a pattern

See [CONTRIBUTING.md](https://github.com/hugolopes45/llmstrip/blob/main/CONTRIBUTING.md). Open an issue with the pattern, a before/after, and a corpus source if you have one. Label it `new-rule`.

## License

MIT.
