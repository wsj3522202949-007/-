---
id: tool-00321
type: tool
area: 库
status: active
tags: [提示词, 协议宽松, 需API密钥, 英文文档, 多Agent]
title: advanced-prompt-engineering
summary: 提示词/写作工作流
source: https://github.com/querulantenkind/advanced-prompt-engineering
created: 2026-07-18
updated: 2026-07-18
no: 321
category: 二、网文 / 长篇 AI 写作系统 库
repo: Querulantenkind/advanced-prompt-engineering
stars: 0
url: https://github.com/querulantenkind/advanced-prompt-engineering
tier: "C"
use_case: "提示词/写作工作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 5a10831e223000a5
  - methods/最强写作方法论_全球最强综合版.md
---

# Querulantenkind/advanced-prompt-engineering

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/querulantenkind/advanced-prompt-engineering
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：An organized repository of advanced prompt engineering strategies for AI text generation, writing, and coding use-cases
- **本地描述**：An organized repository of advanced prompt engineering strategies for AI text generation, writing, and coding use-cases
- **拉取时间**：2026-07-23 22:48:26

---

# Advanced Prompt Engineering Collection

A systematically organized repository of prompt engineering strategies, templates, and best practices for AI text generation, creative writing, coding, analysis, and persona simulation.

## Overview

Advanced Prompt Engineering Collection is an evidence-based resource for optimizing interactions with large language models. This repository treats prompt engineering as both art and science, providing documented techniques, benchmark results, and practical templates.

Target audiences: AI writers and content creators, software developers and engineers, researchers and data analysts, creative professionals, educators and instructional designers.

## Repository Structure

### Fundamentals (`/fundamentals/`)
- prompt-anatomy.md - Prompt component analysis and structure
- core-techniques.md - Proven strategies and methodologies
- common-pitfalls.md - Anti-patterns and mistakes to avoid
- testing-methodology.md - Evaluation frameworks and metrics
- glossary.md - Technical terminology and definitions

### Prompt Archetypes (`/prompt-archetypes/`)
- role-assignment.md - Assigning personas and expertise to models
- few-shot-examples.md - Learning from input-output examples
- system-prompts.md - System-level instructions and configuration
- chain-of-thought.md - Step-by-step reasoning techniques
- tree-of-thought.md - Branching reasoning paths and exploration
- iterative-refinement.md - Progressive improvement strategies
- context-windowing.md - Managing token limits and context

### Use Cases (`/use-cases/`)

Creative Writing:
- fiction-generation.md - Generating consistent, compelling fiction
- poetry-and-verse.md - Poetic forms and techniques
- character-development.md - Creating believable characters
- worldbuilding.md - Constructing fictional worlds

Coding:
- code-generation.md - Generating functional, clean code
- debugging-assistance.md - Identifying and fixing bugs
- architecture-design.md - System design and architecture
- test-generation.md - Creating test cases and suites
- documentation.md - Writing clear technical documentation

Analysis:
- data-analysis.md - Analyzing datasets and patterns
- research-synthesis.md - Synthesizing research findings
- market-intelligence.md - Market analysis and insights
- trend-identification.md - Identifying patterns and trends

Professional:
- business-writing.md - Business documents and communications
- email-composition.md - Effective email writing
- presentations.md - Presentation content and structure
- proposals.md - Writing compelling proposals

Education:
- tutoring-prompts.md - Educational assistance and tutoring
- assessment-creation.md - Creating assessments and questions
- explanation-techniques.md - Explaining complex concepts
- scaffolding-strategies.md - Progressive learning support

Persona Simulation:
- expert-roles.md - Simulating domain experts
- character-simulation.md - Consistent character behavior
- perspective-taking.md - Alternative viewpoints and perspectives
- historical-figures.md - Historical persona simulation

### Model-Specific Guides (`/model-guides/`)
- gpt-series.md - OpenAI GPT-4, GPT-4 Turbo, GPT-3.5 optimization
- claude-series.md - Anthropic Claude models optimization
- llama-models.md - Meta Llama models optimization
- gemini-series.md - Google Gemini models optimization
- mistral-models.md - Mistral AI models optimization
- local-models.md - Self-hosted and on-device models
- comparison-matrix.md - Side-by-side feature and performance comparison

### Advanced Techniques (`/advanced-techniques/`)
- prompt-chaining.md - Connecting multiple prompts in workflows
- multi-turn-conversations.md - Managing conversation state and context
- temperature-exploration.md - Controlling creativity versus consistency
- token-optimization.md - Maximizing efficiency and reducing costs
- output-formatting.md - Structuring responses in desired formats
- guardrails-and-constraints.md - Safety, control, and boundaries
- jailbreak-mitigation.md - Security considerations and protections
- cost-optimization.md - Reducing API expenses and usage

### Templates (`/templates/`)
- basic-prompt-template.md - Simple, single-task prompt structure
- few-shot-template.md - Example-based learning template
- system-prompt-template.md - System instruction template
- complex-task-template.md - Multi-step objective template
- creative-writing-template.md - Fiction and narrative template
- code-generation-template.md - Programming task template
- analysis-template.md - Research and insights template

### Benchmarks (`/benchmarks/`)
- methodology.md - Testing and evaluation framework
- results-gpt4.md - GPT-4 model performance data
- results-claude.md - Claude model performance data
- results-llama.md - Llama model performance data
- comparison-tables.md - Side-by-side performance metrics
- performance-metrics.md - Measurement definitions and methodology

### Gallery (`/gallery/`)
- FEATURED-PROMPTS.md - Index of curated high-performing examples
- top-performing-prompts/ - Highest-rated prompts by category
- innovative-techniques/ - Novel approaches and experiments
- community-submissions/ - User-contributed examples

### Tools and Scripts (`/tools-and-scripts/`)
- prompt-tester.py - Test multiple prompts programmatically
- benchmark-runner.py - Run standardized benchmarks across models
- token-counter.py - Calculate token usage and costs
- response-analyzer.py - Analyze response quality and metrics
- prompt-validator.py - Check for common issues and problems
- cost-calculator.py - Estimate API costs for prompts
- batch-processor.sh - Process multiple prompts in batch

### Examples (`/examples/`)

Complete Projects:
- fiction-generator/ - Full fiction generation system
- code-assistant/ - Programming assistance implementation
- research-assistant/ - Research synthesis tool

Prompt Iterations:
- before-after-examples/ - Evolution of prompts through refinement
- refinement-process/ - Step-by-step improvement documentation

### Documentation (`/docs/`)
- QUICKSTART.md - Getting started guide
- FAQ.md - Frequently asked questions
- PHILOSOPHY.md - Prompt engineering principles and philosophy
- ETHICS.md - Responsible AI usage guidelines
- ROADMAP.md - Future development plans
- CHANGELOG.md - Project version history

## Prompt Anatomy

Every effective prompt contains five core components:

1. Context - Background information the model needs to understand the task
2. Task - Explicit statement of what you want the model to do, clear and actionable
3. Constraints - Limitations, requirements, boundaries (format, length, style, tone)
4. Format - Desired output structure (JSON, markdown, code, prose, etc.)
5. Examples - Few-shot demonstrations of input-output pairs (optional but powerful)

See fundamentals/prompt-anatomy.md for comprehensive analysis.

## Core Techniques

Role Assignment: Define expertise, perspective, and approach. Example: "You are an expert Python developer specializing in API design."

Few-Shot Learning: Provide input-output examples to guide model behavior. Example: "Input: [example] Output: [desired response]"

Chain-of-Thought: Request step-by-step reasoning. Example: "Let's think through this step by step: First, analyze the requirements..."

Iterative Refinement: Progressive improvement through multiple passes. Example: "Create a first draft, then review for clarity, then optimize for conciseness."

Context Windowing: Manage information within token limits through chunking, summarization, and reference systems.

Each technique includes theoretical foundation, implementation examples, performance benchmarks, use case recommendations, and common pitfalls.

## Model-Specific Optimization

| Model | Strengths | Optimization Strategies |
|-------|-----------|------------------------|
| GPT-4 | Complex reasoning, multi-step tasks, code generation | Explicit instructions, clear examples, structured output requests |
| Claude | Nuanced analysis, ethical reasoning, long documents | Detailed context, conversational framing, step-by-step breakdowns |
| Llama | Open-source, customizable, local deployment | Clear task definition, concise prompts, format specification |
| Gemini | Multimodal, search integration, long context | Rich context, iterative refinement, information synthesis |

See model-guides/comparison-matrix.md for comprehensive comparison.

## Benchmark Methodology

Performance metrics measured:
- Effectiveness Score (0-100): Task completion, accuracy, relevance
- Response Quality: Coherence, clarity, depth, creativity
- Token Efficiency: Output quality per token used
- Cost per Request: API pricing consideration
- Latency: Response time and throughput

Results updated regularly in benchmarks/ directory.

## Testing Framework

Systematic prompt evaluation tools:

prompt-tester.py: Load prompt variants, execute against test cases, collect responses, calculate metrics, generate comparison reports.

benchmark-runner.py: Define benchmark suite, run across multiple models, aggregate results, produce analysis.

response-analyzer.py: Parse model outputs, apply quality metrics, identify patterns, suggest improvements.

See tools-and-scripts/ for implementation details.

## Quick Navigation

| Objective | Recommended Path |
|-----------|-----------------|
| Learn fundamentals | fundamentals/core-techniques.md |
| Improve creative writing | use-cases/creative-writing/ |
| Optimize code generation | use-cases/coding/ |
| Model-specific optimization | model-guides/ |
| See working examples | gallery/FEATURED-PROMPTS.md |
| Test prompts systematically | tools-and-scripts/ |
| Understand performance | benchmarks/ |

## Methodology

Three-step approach:
1. Baseline - Start with basic template, get initial output
2. Iterate - Test variations, apply techniques, refine based on results
3. Benchmark - Measure results, compare metrics, document findings

## Philosophy

Prompt engineering bridges human intent and AI capability. Effective prompts require clear thinking about the task, understanding of model capabilities and limitations, iterative refinement based on results, and awareness of ethical implications.

This repository treats prompt engineering as a learnable skill with documented best practices, measurable results, and room for creative experimentation.

## Contributing

Contributions welcome: new prompts and techniques, benchmark results for additional models, gallery submissions of effective prompts, improvements to documentation, bug reports and corrections, testing tools and utilities, use case examples and case studies.

Requirements: document methodology, include performance metrics, provide reproducible examples, test across multiple models when applicable.

See CONTRIBUTING.md for detailed guidelines.

## Resources

Official Documentation:
- OpenAI Prompt Engineering: https://platform.openai.com/docs/guides/prompt-engineering
- Anthropic Claude Guide: https://docs.anthropic.com/
- Google AI Studio: https://ai.google.dev/

Community Resources:
- Prompt Engineering Institute: https://www.promptengineering.org/
- Learn Prompting: https://learnprompting.org/
- Papers with Code: https://paperswithcode.com/

Academic Research:
- Arxiv.org (cs.CL, cs.AI): https://arxiv.org/
- ACL Anthology: https://aclanthology.org/

## Project Information

- License: CC0 1.0 Universal (Public Domain)
- Version: 1.0.0
- Last Updated: 2025-11-19
- Maintainer: @Querulantenkind
- Languages: English (contributions in other languages welcome)
- Requirements: None (documentation only)
- Tools: Python 3.8+ (for testing scripts)
- Repository: https://github.com/Querulantenkind/advanced-prompt-engineering

## Citation
```
@misc{advanced-prompt-engineering-2025,
  author = {Querulantenkind},
  title = {Advanced Prompt Engineering Collection},
  year = {2025},
  url = {https://github.com/Querulantenkind/advanced-prompt-engineering}
}
```

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

Engineer with precision. Create with intention.
