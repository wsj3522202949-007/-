---
id: tool-05215
type: tool
area: 库
status: active
tags: [TTS, TypeScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: ai-writing-detector
summary: 小说转语音/有声书
source: https://github.com/pertrai1/ai-writing-detector
created: 2026-07-18
updated: 2026-07-18
no: 5215
category: 一、去 AI 味 / Humanizer 库
repo: pertrai1/ai-writing-detector
stars: 1
url: https://github.com/pertrai1/ai-writing-detector
tier: "B"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# pertrai1/ai-writing-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/pertrai1/ai-writing-detector
- **Stars**：1
- **语言**：TypeScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：Analyses text and determines the likelihood it was written by an AI rather than a human
- **本地描述**：Analyses text and determines the likelihood it was written by an AI rather than a human
- **拉取时间**：2026-07-25 18:10:21

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Writing Detector

!`[CLI Screenshot](screenshot.png)`

`ai-writing-detector` is a TypeScript/Node.js CLI for analyzing prose with a
rule-based AI-writing heuristic. It looks for vocabulary, structural patterns,
vague claims, promotional language, and several statistical signals that are
commonly associated with AI-generated text.

The project is designed around explainable scoring rather than model inference.
Instead of sending text to an external service, it inspects the input locally
and builds a score from explicit detectors and linguistic analyzers.

## What It Detects

The repository currently includes:

- AI-associated vocabulary and phrase matching
- Structural patterns such as rule-of-three, negative parallelism, outline-style
  conclusions, and false ranges
- Vague attribution, superficial phrasing, and overgeneralization
- Promotional language, excessive emphasis, and elegant variation
- Statistical analysis including lexical diversity, sentence-length variation,
  passive voice, transition density, readability, punctuation, and rare-word
  usage
- Score normalization and classification into:
  - `Likely Human-Written`
  - `Possibly AI-Generated`
  - `Likely AI-Generated`

See `[ROADMAP.md](ROADMAP.md)` for implementation status and
`[REQUIREMENTS.md](REQUIREMENTS.md)` for the original challenge brief.

## How It Was Developed

This repository was built with a custom agent loop documented in
`[LOOP.md](LOOP.md)`.

!`[Agent Loop Diagram](agent-loop-diagram.png)`

The important part is that the loop is agent-driven, not a static shell script:

- An LLM agent running in OpenCode executes `/opsx-loop`
- The loop works phase-by-phase from `[ROADMAP.md](ROADMAP.md)`
- For each phase, the agent creates or updates openspec artifacts, writes tests,
  implements code, runs quality checks, updates docs, and archives the phase
- Progress is resumable, so re-running the loop continues from the next
  unchecked phase

Typical loop commands:

```bash
/opsx-loop
/opsx-loop 2
/opsx-loop 3-5
```

At a high level, each phase follows this pattern:

1. Read the next incomplete phase from the roadmap.
2. Create or reuse one openspec change for that phase.
3. Write specs, design notes, and tasks for the phase as a unit.
4. Add tests before implementation.
5. Implement the phase tasks and mark them complete.
6. Run checks, update docs, commit, and archive the change.

That loop is why the repo contains both implementation code and the supporting
spec artifacts under `openspec/`.

## Installation

```bash
npm install
```

## Development Commands

```bash
# Build
npm run build

# Test
npm test
npm run test:watch

# Lint and format
npm run lint
npm run lint:fix
npm run format

# Type checking
npm run typecheck
```

## CLI Usage

Build first:

```bash
npm run build
```

Then run the CLI against a file:

```bash
npm run start -- analyze samples/human-written/technology.txt
```


Or pass text on stdin:

```bash
cat samples/ai-generated/business.txt | npm run start -- analyze ignored.txt --stdin
```

Current command surface:

```bash
npm run start -- analyze <file>
npm run start -- analyze <file> --stdin
```

## What The CLI Does Today

The current CLI entrypoint validates input and prints basic text statistics for
the supplied text:

- character count
- word count

This behavior comes from `[src/cli.ts](src/cli.ts)` and
`[src/output/display.ts](src/output/display.ts)`.

The repository also contains the full scoring and report-generation pipeline in
`src/scoring/` and `src/report/`, including classification and formatted report
output. Those modules are implemented and tested, but they are not yet wired
into the default CLI command.

## Project Structure

```text
src/
├── analyzers/     # Statistical and linguistic analysis
├── detectors/     # Rule-based pattern detectors
├── input/         # File and stdin handling
├── output/        # Console display helpers
├── report/        # Report assembly and CLI formatting
├── scoring/       # Score aggregation, normalization, classification
└── utils/         # Tokenization and statistics helpers
```

## Limitations

- This tool analyzes natural-language writing, not source code authorship.
- It is heuristic-based, so results should be treated as signals, not proof.
- Short or heavily edited text can reduce accuracy.

## Samples

Sample inputs for manual testing are included in:

- `samples/ai-generated/`
- `samples/human-written/`
