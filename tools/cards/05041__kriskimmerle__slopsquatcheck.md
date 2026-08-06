---
id: tool-05041
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 去AI味, 本地写作]
title: slopsquatcheck
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/kriskimmerle/slopsquatcheck
created: 2026-07-18
updated: 2026-07-18
no: 5041
category: 一、去 AI 味 / Humanizer 库
repo: kriskimmerle/slopsquatcheck
stars: 0
url: https://github.com/kriskimmerle/slopsquatcheck
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# kriskimmerle/slopsquatcheck

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/kriskimmerle/slopsquatcheck
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：ai, ai-security-toolkit, llm, python, security, static-analysis
- **GitHub 描述**：AI Hallucination Squatting Detector for Python Dependencies - detects packages LLMs commonly 'invent'
- **本地描述**：AI Hallucination Squatting Detector for Python Dependencies - detects packages LLMs commonly 'invent'
- **拉取时间**：2026-07-25 18:03:56

---

# slopsquatcheck

**AI Hallucination Squatting Detector for Python Dependencies**

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Detect suspicious packages in your `requirements.txt` or `pyproject.toml` that may be:

- 🎭 **AI hallucination squat targets** — packages that LLMs commonly "invent"
- 📛 **Typosquatting** popular packages
- 🆕 **Suspiciously new** packages targeting known names
- ⚠️ **Low reputation** packages (no downloads, no author, no repo)

## The Problem

When developers use AI coding assistants (ChatGPT, Claude, Copilot, etc.), the AI sometimes "hallucinates" package names that don't exist. Attackers have learned to exploit this:

1. LLM recommends `huggingface-cli` (which doesn't exist)
2. Attacker registers `huggingface-cli` on PyPI with malware
3. Developer runs `pip install huggingface-cli`
4. Malware executes on developer's machine

This is called **"Slopsquatting"** or **"AI Hallucination Squatting"** — and it's a growing supply chain attack vector.

## Installation

```bash
pip install slopsquatcheck
```

Or run directly (zero dependencies):

```bash
curl -O https://raw.githubusercontent.com/kriskimmerle/slopsquatcheck/main/slopsquatcheck.py
python slopsquatcheck.py requirements.txt
```

## Quick Start

```bash
# Scan a requirements file
slopsquatcheck requirements.txt

# Scan pyproject.toml
slopsquatcheck pyproject.toml

# Check a single package
slopsquatcheck --package some-suspicious-lib

# CI mode: fail if high-risk packages found
slopsquatcheck requirements.txt --check --min-score 40
```

## Example Output

```
============================================================
slopsquatcheck - AI Hallucination Squat Detector
============================================================
Packages scanned: 5
Total findings: 3

Findings by severity:
  CRITICAL: 1
  HIGH: 1
  MEDIUM: 1

------------------------------------------------------------
📦 huggingface-cli (Risk: 60/100, Grade: F)

  🔴 [SS01] CRITICAL: Package is a known AI hallucination target
      reason: This package name is commonly 'invented' by LLMs and may be registered by attackers

  🟠 [SS03] HIGH: Package is very new (created 15 days ago)
      first_release: 2026-01-25T14:32:00+00:00
      age_days: 15
      threshold: 30

------------------------------------------------------------
📦 reqeusts (Risk: 20/100, Grade: C)

  🟠 [SS04] HIGH: Package name is suspiciously similar to 'requests'
      similar_to: requests
      levenshtein_distance: 2
      reason: May be typosquatting or hallucination squat

============================================================
Overall Risk Grade: F (max score: 60/100)

⚠️  HIGH RISK: Review flagged packages carefully before installing!
```

## Detection Rules

| Rule | Severity | Description |
|------|----------|-------------|
| SS01 | CRITICAL | Package is a known AI hallucination target |
| SS02 | CRITICAL | Package does not exist on PyPI |
| SS03 | HIGH | Package is very new (< 30 days old) |
| SS04 | HIGH | Package name is suspiciously similar to popular package |
| SS05 | MEDIUM | Package has missing or minimal description |
| SS06 | MEDIUM | Package has no author information |
| SS07 | LOW | Package has no homepage or repository URL |
| SS08 | HIGH/MEDIUM | Package has very low downloads |
| SS09 | MEDIUM | Package name matches common hallucination pattern |

## CLI Options

```
usage: slopsquatcheck [-h] [--package PACKAGE] [--format {text,json}]
                      [--check] [--min-score MIN_SCORE] [--no-stats]
                      [--version]
                      [file]

positional arguments:
  file                  requirements.txt or pyproject.toml to scan

options:
  -h, --help            show this help message and exit
  --package, -p PACKAGE Check a single package name
  --format, -f {text,json}
                        Output format
  --check               Exit with code 1 if high-risk packages found
  --min-score MIN_SCORE Minimum risk score to fail (with --check)
  --no-stats            Skip download statistics check (faster)
  --version, -V         show version and exit
```

## CI/CD Integration

### GitHub Actions

```yaml
- name: Check for hallucination squat packages
  run: |
    pip install slopsquatcheck
    slopsquatcheck requirements.txt --check --min-score 40
```

### Pre-commit Hook

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: slopsquatcheck
        name: Check for hallucination squat packages
        entry: slopsquatcheck
        language: python
        files: ^requirements.*\.txt$|^pyproject\.toml$
        args: [--check]
```

## API Usage

```python
from slopsquatcheck import check_package, fetch_pypi_info

# Check a single package
findings = check_package("some-suspicious-package")
for finding in findings:
    print(f"{finding.rule}: {finding.message}")

# Fetch package info
info = fetch_pypi_info("requests")
print(f"First released: {info.first_release_date}")
```

## Known Hallucination Targets

The tool includes a database of package names that LLMs commonly hallucinate:

- `huggingface-cli` — documented case with 30K downloads
- `*-helper`, `*-utils`, `*-connector` patterns
- AI-related: `gpt-helper`, `llm-utils`, `chatgpt-helper`, etc.
- Generic: `api-connector`, `db-connector`, `auth-helper`, etc.

## How It Works

1. **Parse dependencies** from requirements.txt or pyproject.toml
2. **Query PyPI API** for each package's metadata
3. **Check for red flags:**
   - Package doesn't exist (hallucination confirmed)
   - Package is in known hallucination list
   - Package name is similar to popular packages (typosquatting)
   - Package is very new (registered recently)
   - Package has no author, description, or repository
   - Package has very low download counts
4. **Calculate risk score** and report findings

## Comparison with Other Tools

| Tool | CVE Detection | Malicious Code Scan | Hallucination Detection | Package Age Check |
|------|---------------|---------------------|------------------------|-------------------|
| pip-audit | ✅ | ❌ | ❌ | ❌ |
| GuardDog | ❌ | ✅ | ❌ | ❌ |
| safety | ✅ | ❌ | ❌ | ❌ |
| **slopsquatcheck** | ❌ | ❌ | ✅ | ✅ |

Use slopsquatcheck **alongside** these tools for comprehensive supply chain security.

## Contributing

1. Fork the repository
2. Add new hallucination targets to `KNOWN_HALLUCINATIONS`
3. Add new popular packages to `POPULAR_PACKAGES`
4. Submit a pull request

## References

- [AI Hallucination Squatting: The New Frontier of Supply Chain Attacks](https://instatunnel.my/blog/ai-hallucination-squatting-the-new-frontier-of-supply-chain-attacks)
- [Bar Lanyado's huggingface-cli Research](https://www.lasso.security/blog/ai-package-hallucination)
- [Vulcan Cyber's LLM Package Hallucination Study](https://vulcan.io/blog/ai-hallucinations-package-risk/)

## License

MIT License — see [LICENSE](https://github.com/kriskimmerle/slopsquatcheck/blob/main/LICENSE) for details.
