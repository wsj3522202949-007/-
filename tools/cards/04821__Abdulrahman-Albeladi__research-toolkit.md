---
id: tool-04821
type: tool
area: 库
status: active
tags: [文风迁移, Python, 协议未明, 本地优先, 英文文档, 改稿润色, 本地写作]
title: research-toolkit
summary: 风格微调/文风迁移
source: https://github.com/abdulrahman-albeladi/research-toolkit
created: 2026-07-18
updated: 2026-07-18
no: 4821
category: 一、去 AI 味 / Humanizer 库
repo: Abdulrahman-Albeladi/research-toolkit
stars: 0
url: https://github.com/abdulrahman-albeladi/research-toolkit
tier: "C"
use_case: "风格微调/文风迁移"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
  - "⚠️ 仓库疑似停更/归档，bug 不会修、依赖可能过期"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# Abdulrahman-Albeladi/research-toolkit

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/abdulrahman-albeladi/research-toolkit
- **Stars**：0
- **语言**：Python
- **License**：NOASSERTION
- **Topics**：data-analysis, natural-language-processing, python, reproducible-research, research, statistics
- **GitHub 描述**：Reusable Python and notebook workflows for multilingual research-data preparation, statistical analysis, and AI-text detector evaluation.
- **本地描述**：Reusable Python and notebook workflows for multilingual research-data preparation, statistical analysis, and AI-text detector evaluation.
- **拉取时间**：2026-07-25 17:55:36

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI in Saudi Higher Education: Reproducible Research Code

This monorepository contains cleaned, journal-ready Python code supporting a coordinated three-paper research project on artificial intelligence in Saudi higher education.

The original work was distributed across Google Colab notebooks. The public repository version removes notebook outputs, repeated cells, machine-specific Google Drive path discovery, embedded credentials, one-off recovery fragments, and exploratory code that did not contribute to the reported analyses. The retained workflows are organized as ordinary `.py` modules and command-line scripts.

## Repository structure

```text
.
├── paper1_survey/                 # AI-use survey, psychometrics, ordinal models, open responses
├── paper2_assignment_corpus/      # Authentic assignment corpus, detectors, conflict and adjusted analyses
├── paper3_detector_benchmark/     # Controlled Arabic/English/code detector benchmark
├── docs/                          # Cross-paper security, data, and audit notes
└── scripts/check_repository_for_secrets.py
```

Each paper directory is self-contained and has its own README, dependency metadata, scripts, tests, and data-layout documentation.

## Papers

### Paper 1

**Artificial Intelligence Use Among Undergraduates in Selected Saudi Universities: Adoption, Attitudes, and Perceived Academic Effects**

Code covers survey mapping and quality checks, university-weighted descriptive analysis, reliability and one-factor validation, ordinal-logit models, robustness diagnostics, and supervised multi-label coding of open responses.

### Paper 2

**AI-Writing Signals in Saudi University Assignments: A Detector-Based Analysis**

Code covers assignment-file preprocessing, detector-output collection and normalization, language-specific calibration weights, descriptive and nonparametric comparisons, robust adjusted models, detector-disagreement analysis, and optional OpenAI-assisted textual-feature coding.

### Paper 3

**A Multilingual Benchmark of Commercial AI Detection Tools for Arabic, English, and Code Assignments in Saudi Higher Education**

Code covers benchmark-corpus preparation, matched AI generation/humanization workflows, detector collection, performance metrics, Cochran's Q and McNemar tests, methodological weights, and conflict analysis.

## Installation

Python 3.10 or newer is recommended. Install only the paper you need:

```bash
pip install -e "paper1_survey[dev,qualitative]"
pip install -e "paper2_assignment_corpus[dev,api,ocr]"
pip install -e "paper3_detector_benchmark[generation,dev]"
```

Run the paper-specific unit tests:

```bash
(cd paper1_survey && PYTHONPATH=src pytest -q --import-mode=importlib tests)
(cd paper2_assignment_corpus && PYTHONPATH=src pytest -q --import-mode=importlib tests)
(cd paper3_detector_benchmark && PYTHONPATH=src pytest -q --import-mode=importlib tests)
```

## Data are not included

The survey data, authentic student assignments, controlled benchmark files, and commercial detector outputs are not included in this code archive. They require separate controlled or public-repository deposition consistent with ethics, copyright, and privacy requirements. Each paper directory contains a data-layout guide and manifest templates.

## Security notice

The supplied research notebooks contained hard-coded service credentials. All credential values have been removed. Before publishing this repository, rotate or revoke every key/password that ever appeared in the original notebooks. Store replacement credentials only in environment variables or a local untracked `.env` file.

Run the repository scanner before each public push:

```bash
python scripts/check_repository_for_secrets.py .
```

## Reproducibility boundaries

Commercial detector services, humanization services, and hosted generative-AI models are proprietary systems that may change over time. Re-running API collection may not reproduce archived scores exactly. The statistical analysis stages are deterministic when run on the archived input datasets used for the manuscripts.

## License

No open-source license is imposed in this package because ownership and institutional requirements should be confirmed by all authors. Add an approved license before public release if desired.
