---
id: tool-05345
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: sloppylint
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/rsionnach/sloppylint
created: 2026-07-18
updated: 2026-07-18
no: 5345
category: 一、去 AI 味 / Humanizer 库
repo: rsionnach/sloppylint
stars: 87
url: https://github.com/rsionnach/sloppylint
tier: "A"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# rsionnach/sloppylint

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/rsionnach/sloppylint
- **Stars**：87
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Python AI Slop Detector - Find over-engineering, hallucinations, and dead code in Python codebases
- **本地描述**：Python AI Slop Detector - Find over-engineering, hallucinations, and dead code in Python codebases
- **拉取时间**：2026-07-25 18:15:09

---

<!-- TODO: Add CLI demo GIF here -->

<div align="center">
  <h1>🐷 Sloppylint</h1>
  <p><strong>Detect AI-generated code anti-patterns in your Python codebase.</strong></p>
  <p><em>Catches AI-specific anti-patterns that traditional linters miss</em></p>
</div>

[![PyPI](https://img.shields.io/pypi/v/sloppylint?style=for-the-badge)](https://pypi.org/project/sloppylint/)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## ⚡ Quick Start

```bash
pip install sloppylint
sloppylint .

# Output:
# CRITICAL (2 issues)
# ============================================================
#   src/api.py:23  mutable_default_arg
#     Mutable default argument - use None instead
#     > def process(items=[]):
#
#   src/db.py:15  bare_except
#     Bare except catches everything including SystemExit
#     > except:
#
# SLOPPY INDEX
# ══════════════════════════════════════════════════
# Information Utility (Noise)    : 24 pts
# Information Quality (Lies)     : 105 pts
# Style / Taste (Soul)           : 31 pts
# Structural Issues              : 45 pts
# ──────────────────────────────────────────────────
# TOTAL SLOP SCORE               : 205 pts
#
# Verdict: SLOPPY
```

---

## 🤔 Why Sloppylint Exists

Traditional linters catch style and syntax issues. But AI-generated code introduces **new failure patterns** they weren't designed to detect:

- **Hallucinated imports** - packages and functions that don't exist
- **Cross-language leakage** - `.push()`, `.equals()`, `.length` in Python
- **Placeholder code** - `pass`, `TODO`, functions that do nothing
- **Confident wrongness** - code that looks right but fails at runtime

Sloppylint targets these AI-specific patterns that escape Pylint, Flake8, and code review.

---

## 🎯 What It Catches

### The Three Axes of AI Slop

| Axis | What It Detects | Examples |
|------|-----------------|----------|
| 📢 **Noise** | Debug artifacts, redundant comments | `print()`, `# increment x` above `x += 1` |
| 🤥 **Lies** | Hallucinations, placeholders | `def process(): pass`, mutable defaults |
| 💀 **Soul** | Over-engineering, bad style | God functions, deep nesting, hedging comments |
| 🏗️ **Structure** | Anti-patterns | Bare except, star imports, single-method classes |

---

## 📥 What You Put In

```bash
# Scan a directory
sloppylint src/

# Scan specific files
sloppylint app.py utils.py

# Only high severity issues
sloppylint --severity high

# CI mode - exit 1 if issues found
sloppylint --ci --max-score 50

# Export JSON report
sloppylint --output report.json
```

---

## 📤 What You Get Out

| Output | Description |
|--------|-------------|
| 🎯 **Issues by Severity** | Critical, High, Medium, Low |
| 📊 **Slop Score** | Points breakdown by axis |
| 📋 **Verdict** | CLEAN / ACCEPTABLE / SLOPPY / DISASTER |
| 📁 **JSON Report** | Machine-readable for CI/CD |

---

## 🔍 Pattern Examples

### Critical Severity

```python
# 🚨 mutable_default_arg - AI's favorite mistake
def process_items(items=[]):  # Bug: shared state between calls
    items.append(1)
    return items

# ✅ Fix: Use None and initialize inside
def process_items(items=None):
    if items is None:
        items = []
    items.append(1)
    return items
```

```python
# 🚨 bare_except - Catches SystemExit, KeyboardInterrupt
try:
    risky_operation()
except:  # Bug: swallows Ctrl+C!
    pass

# ✅ Fix: Catch specific exceptions
try:
    risky_operation()
except ValueError as e:
    logger.error(f"Invalid value: {e}")
```

### High Severity

```python
# 🚨 pass_placeholder - AI gave up
def validate_email(email):
    pass  # TODO: implement

# 🚨 hedging_comment - AI uncertainty
x = calculate()  # should work hopefully
```

---

## 💰 The Value

<div align="center">
  <h3>🔍 Catch AI mistakes before they hit production</h3>
</div>

### Why This Matters

| Problem | Impact | Sloppylint Catches |
|---------|--------|----------------|
| Mutable defaults | Shared state bugs | ✅ Critical alert |
| Bare except | Swallows Ctrl+C | ✅ Critical alert |
| Placeholder functions | Runtime failures | ✅ High alert |
| Hallucinated imports | ImportError in prod | ✅ High alert |
| Wrong language patterns | JS/Java/Ruby/Go/C#/PHP in Python | ✅ High alert |
| Unused imports | Code bloat | ✅ Medium alert |
| Dead code | Maintenance burden | ✅ Medium alert |
| Copy-paste code | Maintenance nightmare | ✅ Medium alert |

### Research Says

- **20% of AI package imports** reference non-existent libraries — *sloppylint catches these*
- **LLMs leak patterns** from other languages they were trained on — *sloppylint catches 100+ of these*
- **66% of developers** say AI code is "almost right" (the dangerous kind)

---

## 🛠️ CLI Commands

```bash
sloppylint .                    # 🔍 Scan current directory
sloppylint src/ tests/          # 📁 Scan multiple directories
sloppylint --severity high      # ⚡ Only critical/high issues
sloppylint --lenient            # 🎯 Same as --severity high
sloppylint --strict             # 🔬 Report everything
sloppylint --ci                 # 🚦 Exit 1 if any issues
sloppylint --max-score 50       # 📊 Exit 1 if score > 50
sloppylint --output report.json # 📋 Export JSON report
sloppylint --ignore "tests/*"   # 🚫 Exclude patterns
sloppylint --disable magic_number # ⏭️ Skip specific checks
sloppylint --version            # 📌 Show version
```

---

## ✅ Features

| Feature | Description | Status |
|---------|-------------|--------|
| 🌐 **Multi-Language Detection** | Catches patterns from JS, Java, Ruby, Go, C#, PHP | ✅ 100+ patterns |
| 🔍 **Hallucinated Imports** | Detect non-existent packages | ✅ Done |
| 📦 **Unused Imports** | AST-based detection | ✅ Done |
| 💀 **Dead Code** | Unused functions/classes | ✅ Done |
| 🔄 **Duplicate Detection** | Cross-file copy-paste | ✅ Done |
| 🎨 **Rich Output** | Colors and tables (optional) | ✅ Done |
| ⚙️ **Config Support** | pyproject.toml configuration | ✅ Done |

### Language Patterns Detected

LLMs are trained on code from many languages. When generating Python, they sometimes produce patterns from other languages:

| Language | Example Mistakes | Python Fix |
|----------|------------------|------------|
| **JavaScript** | `.push()`, `.length`, `.forEach()` | `.append()`, `len()`, `for` loop |
| **Java** | `.equals()`, `.toString()`, `.isEmpty()` | `==`, `str()`, `not obj` |
| **Ruby** | `.each`, `.nil?`, `.first`, `.last` | `for` loop, `is None`, `[0]`, `[-1]` |
| **Go** | `fmt.Println()`, `nil` | `print()`, `None` |
| **C#** | `.Length`, `.Count`, `.ToLower()` | `len()`, `len()`, `.lower()` |
| **PHP** | `strlen()`, `array_push()`, `explode()` | `len()`, `.append()`, `.split()` |

---

## 🚫 What Sloppylint Is Not

Sloppylint does **not** replace:
- Human code review
- Traditional linters (Pylint, Flake8, Ruff)
- Type checkers (mypy, pyright)
- Security scanners (Bandit, Semgrep)

It **complements** them by catching patterns these tools miss—patterns uniquely common in AI-generated code.

---

## 📦 Installation

```bash
# Install from PyPI
pip install sloppylint

# With colored output (recommended)
pip install sloppylint[rich]

# With all optional features
pip install sloppylint[all]

# Or install from source for development
git clone https://github.com/rsionnach/sloppylint.git
cd sloppylint
pip install -e ".[dev]"
```

---

## ⚙️ Configuration

Configure via `pyproject.toml`:

```toml
[tool.sloppy]
ignore = ["tests/*", "migrations/*"]
disable = ["magic_number", "debug_print"]
severity = "medium"
max-score = 100
ci = false
format = "detailed"  # or "compact" or "json"
```

---

## 🤝 Contributing

```bash
git clone https://github.com/rsionnach/sloppylint.git
cd sloppylint
pip install -e ".[dev]"
pytest tests/ -v  # 68 tests should pass
```

See [AGENTS.md](https://github.com/rsionnach/sloppylint/blob/main/AGENTS.md) for coding conventions and pattern implementation guide.

---

## 📄 License

MIT

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
see_also:
  - 05128__anasu1__text-humanizer.md
  - 05362__asavvin-pixel__unslop.md
  - 05251__DadaNanjesha__AI-content-detector-Humanizer.md
---

## 🙏 Acknowledgments

### Inspiration
- [KarpeSlop](https://github.com/CodeDeficient/KarpeSlop) - The original AI Slop Linter for TypeScript
- Andrej Karpathy's commentary on AI-generated code quality

### Research
- [Counterfeit Code](https://counterfeit-code.github.io/) - MIT research on "looks right but doesn't work" patterns
- [Package Hallucinations](https://arxiv.org/abs/2406.10279) - USENIX study on hallucinated dependencies
