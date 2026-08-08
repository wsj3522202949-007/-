---
id: tool-03148
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 人物设定, 本地写作]
title: ai-qa-pipeline
summary: 多角色 Agent 协作批量产文
source: https://github.com/masongarza7/ai-qa-pipeline
created: 2026-07-18
updated: 2026-07-18
no: 3148
category: 六、多 Agent 小说生产 / 叙事引擎 库
repo: MasonGarza7/ai-qa-pipeline
stars: 1
url: https://github.com/masongarza7/ai-qa-pipeline
tier: "B"
use_case: "多角色 Agent 协作批量产文"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 32065c08780c226b
  - methods/网文写作最强SOP.md
---

# MasonGarza7/ai-qa-pipeline

- **分类**：六、多 Agent 小说生产 / 叙事引擎 库
- **链接**：https://github.com/masongarza7/ai-qa-pipeline
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：Head Start: an AI-Driven Requirements-to-Test Artifact Generator serving as a schema-constrained LLM pipeline that converts structured user stories into validated test cases.
- **本地描述**：Head Start: an AI-Driven Requirements-to-Test Artifact Generator serving as a schema-constrained LLM pipeline that converts structured user stories into validated test cases.
- **拉取时间**：2026-07-23 23:50:58

---

# Mason Garza - Head Start: AI-QA Pipeline

I named this project "Head Start" as it provides QA engineers, like me, a head start when new product requirements arrive and test cases need to be created.  

This project is an AI-assisted Quality Assurance pipeline that converts user stories into structured QA artifacts including test cases, acceptance criteria classification, lint validation, metrics, and an interactive HTML report. Example stories are provided that test the [Internet Herokuapp](https://the-internet.herokuapp.com/) website which I have used in my other projects. 

The system uses local LLMs via Ollama to generate deterministic, schema-validated QA artifacts and can be run by both CLI and a Web UI. 


## Overview

The AI-QA Pipeline demonstrates how large language models can assist in test design and QA analysis workflows.

Given a user story (Markdown text), the pipeline automatically:

1. Extracts acceptance criteria
2. Classifies acceptance criteria
3. Generates test cases
4. Validates artifact quality (lint checks)
5. Computes QA metrics
6. Produces a structured HTML report

The system is designed to be:

- deterministic
- schema-validated
- locally runnable
- reproducible

It supports three modes of execution:

- CLI
- Python web server
- Standalone Windows executable (recommended)


## Tech Stack
Language:
- Python

AI / LLM:
- Ollama 
- Llama 3.1

Backend:
- FastAPI
- Uvicorn

Frontend:
- HTML
- CSS
- JavaScript

Validation:
- JSON Schema
- Pydantic

Packaging:
- PyInstaller


## Why use a system like this instead of ChatGPT or Claude?

Large language models like ChatGPT or Claude can certainly generate test cases when given product requirements and/or acceptance criteria. However, this project demonstrates how AI can be integrated into a structured, reproducible QA workflow rather than used in ad-hoc prompting.

This pipeline provides several advantages over manually prompting an AI assistant.

### Deterministic Workflow

Traditional AI prompting is conversational and non-deterministic. This pipeline enforces a structured flow:

1. Acceptance criteria extraction
2. AC classification
3. Test case generation
4. Artifact validation
5. Metrics calculation
6. Report generation

This ensures the same pipeline logic runs every time.

---

### Schema Validation

Generated artifacts are validated against a JSON schema.  
This prevents erroneous outputs and enforces structure such as:

- test case format
- acceptance criteria mappings
- metadata consistency

Generic AI chat tools provide no structural guarantees.

---

### Automated QA Quality Checks

The pipeline includes a lint stage that checks artifacts for issues such as:

- missing test coverage
- inconsistent formatting
- structural validation failures

This adds a layer of QA governance to AI-generated content.

---

### Metrics and Insights

Instead of just producing text output, the pipeline calculates metrics including:

- test case coverage
- artifact completeness
- estimated time savings compared to manual QA

These metrics help teams understand the impact of AI-assisted test generation.

---

### Reproducibility

Runs are stored in structured directories: `outputs/runs/<run-id>`  
Each run contains:
- generated artifacts
- metrics
- HTML report
- original story input
- pipeline status

This allows the user to review, compare, and audit pipeline runs.

---

### Local AI Execution

The system uses **Ollama** to run models locally.

Benefits include:

- reducing reliance on external hosted AI services
- no external API costs
- full control over model selection
- offline capability
- privacy for proprietary requirements

---

### Integrated QA Tooling

Instead of manually copying prompts into a chat window, this system provides:

- CLI interface
- Web UI
- structured reporting
- pipeline orchestration

This moves AI usage from prompt experimentation to repeatable tooling.

related:
  - methods/网文写作最强SOP.md
---

## Summary

Traditional prompting is useful for experimentation, but this project demonstrates how AI can be integrated into a structured QA automation workflow that provides validation, metrics, reproducibility, and tooling around the model.


# Getting Started

## 1. Clone the Repository
```bash
git clone https://github.com/MasonGarza7/ai-qa-pipeline.git
cd ai-qa-pipeline
```

## 2. Install Dependencies
Once inside the project, run:
```bash
pip install -r requirements.txt
```

## 3. Install Ollama
1. Download Ollama from the [Official Website](https://ollama.com/)
2. Open a PowerShell terminal and start the server by running: 
```bash
ollama serve
```
3. Pull the model I used in this project (though the system should allow any installed Ollama model) by running: 
```bash
ollama pull llama3.1:8b
```

# Running the Pipeline
The pipeline can be run in three different ways.  

**IMPORTANT**: Ollama must be running for successful artifact generation:
1. Open a dedicated PowerShell instance to start the Ollama server and run:
```bash
ollama serve
```

2. When you want to kill the Ollama server, run: 
```bash
taskkill /IM "ollama.exe" /F
```

3. Use the following commands to verify if Ollama is running: 
```bash
netstat -ano | findstr 11434
tasklist | findstr /I ollama
Get-Service | findstr /I ollama
schtasks /Query | findstr /I ollama
```

## Recommended: Standalone Executable (WebUI)
1. Download the compiled executable from GitHub Releases.
2. Run the **AI-QA-Pipeline.exe** (this will start the FastAPI server and open the Web UI in your browser) 
3. From there you can:
    - paste or upload a story
    - select an installed Ollama model
    - enable Lint, Strict Lint, or Expanded modes
    - run the pipeline
    - view generated reports


## Running the Web UI via Python
1. Start the server manually by running: 
```bash
python -m agent.webapp
```
2. Then open [http://127.0.0.1:8000](http://127.0.0.1:8000)


## Running the Pipeline via CLI
#### Baseline run: (one test case per acceptance criteria)
```bash
python -m agent.cli --story examples/checkboxes_story.md
```
#### Specify model and prompt version:
```bash
python -m agent.cli --story examples/checkboxes_story.md --model llama3.1:8b --prompt-version v1
```
#### Lint mode: (reports errors and warnings but does not fail the run)
```bash
python -m agent.cli --story examples/checkboxes_story.md --lint
```
#### Strict Lint mode: (fails if there are lint warnings)
```bash
python -m agent.cli --story examples/checkboxes_story.md --lint --lint-strict
```
#### Deterministic Expanded mode: (allows for multiple test cases per acceptance criteria)
```bash
python -m agent.cli --story examples/login_story.md --expanded 
```

## File Structure 
```bash
AI-QA-Pipeline/
│
├── agent/                                     # Core AI QA pipeline implementation
│   ├── static/                                # Frontend assets for the Web UI
│   │   ├── app.js                             # Client-side logic (pipeline polling, UI updates, model loading)
│   │   └── styles.css                         # UI styling
│   │
│   ├── templates/                             # Jinja HTML templates rendered by FastAPI
│   │   ├── index.html                         # Main Web UI interface
│   │   └── run.html                           # Report viewer page
│   │
│   ├── __init__.py                            # Package initializer
│   ├── ac_classifier.py                       # Classifies extracted acceptance criteria
│   ├── ac_tc_generator.py                     # Generates test cases from ACs
│   ├── cli.py                                 # Command-line interface entrypoint
│   ├── generator.py                           # Main pipeline orchestration logic
│   ├── linter.py                              # Artifact lint validation and quality checks
│   ├── metrics.py                             # QA metrics calculation
│   ├── ollama_client.py                       # Handles communication with the Ollama API
│   ├── post_process.py                        # Deterministic artifact formatting and cleanup
│   ├── reporting.py                           # HTML report generation
│   └── webapp.py                              # FastAPI web server powering the Web UI
│
├── build/                                     # Temporary build artifacts created by PyInstaller
│
├── examples/                                  # Example user stories for testing the pipeline
│   ├── checkboxes_story.md
│   ├── dropdown_story.md
│   └── login_story.md
│
├── outputs/                                   # Generated pipeline outputs
│   └── runs/                                  # Individual pipeline runs
│       └── <run-id>/                          # Unique run directory
│           ├── artifacts.json                 # Generated QA artifacts
│           ├── metrics_*.json                 # Computed QA metrics
│           ├── report.html                    # Generated HTML report
│           ├── status.json                    # Pipeline status tracking
│           └── story.md                       # Original user story used for the run
│
├── prompts/                                   # Prompt templates used for LLM generation
│   └── v1.txt
│
├── schemas/                                   # JSON schemas used for artifact validation
│   └── test_artifacts.schema.json
│
├── .gitignore                                 # Files and directories excluded from version control
├── AI-QA-Pipeline.exe                         # Standalone Windows executable
├── AI-QA-Pipeline.spec                        # PyInstaller build configuration
├── launcher.py                                # Executable launcher entrypoint
├── requirements.txt                           # Python dependencies
└── README.md                                  # Project documentation
```


## Output Artifacts
Each run generates:
- artifacts.json
- metrics_*.json
- report.html
- status.json

These files are stored in:
`outputs/runs/<run-id>`

## Metrics
The pipeline computes several QA metrics including:
- acceptance criteria coverage
- generated test case count
- artifact completeness
- estimated manual effort savings

The metric `time_saved_pct` represents the estimated percentage of manual QA effort saved by using the pipeline instead of writing test cases manually.

## Example Output
Each pipeline run produces an interactive HTML report summarizing:
- extracted acceptance criteria
- generated test cases
- lint results
- QA metrics
- execution metadata

## Future Improvements
- automated GitHub Actions build for the executable
- test and accept a wider range of product requirements and acceptance criteria styles and formats


## Final Thoughts
I had a lot of fun on this project!

It went way beyond what I thought it was going to become. I had "Deploy AI Model for Test Case Generation" on my whiteboard for weeks but I didn't exactly know what I wanted to do. I had no experience with local LLMs at the time. But the more I researched, the clearer the direction became. 

I did not experience any major blockers throughout this project. Minor blockers include: 
- I wanted the progress popup to display the live status of the pipeline, whether it be AC classification, artifact generation, computing metrics, etc. However, this would require a significant change to my generator script to allow for those hooks to be used. 
- Expanded mode took the longest to implement. Allowing the model to determine which acceptance criteria required multiple test cases was a challenge. And still, it's not as good as could be. But, that's why this project is a "Head Start". It doesn't replace QA; it gives them a head start on writing up new test cases when given new requirements. 

In conclusion, I am very proud of this project and hope to try it out in my next role! 

Thank you for reading,  
Mason Garza
