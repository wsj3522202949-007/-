---
id: tool-03147
type: tool
area: 库
status: active
tags: [RAG, 提示词, Python, 协议宽松, 本地优先, 英文文档, 人物设定, 本地写作]
title: Self-Learning-Library
summary: 长篇设定/人物一致性（RAG 记忆）
source: https://github.com/llk-ll/self-learning-library
created: 2026-07-18
updated: 2026-07-18
no: 3147
category: 六、多 Agent 小说生产 / 叙事引擎 库
repo: LLK-LL/Self-Learning-Library
stars: 7
url: https://github.com/llk-ll/self-learning-library
tier: "B"
use_case: "长篇设定/人物一致性（RAG 记忆）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
---

# LLK-LL/Self-Learning-Library

- **分类**：六、多 Agent 小说生产 / 叙事引擎 库
- **链接**：https://github.com/llk-ll/self-learning-library
- **Stars**：7
- **语言**：Python
- **License**：MIT
- **Topics**：ai-agent, ai-memory, automation, codex, knowledge-base, local-first, markdown, obsidian, python, rag, research, self-learning, workflow, writing
- **GitHub 描述**：Local-first self-learning knowledge-base harness for AI agents. Retrieve rules, avoid regressions, and promote repeated lessons into stable reusable knowledge.
- **本地描述**：Local-first self-learning knowledge-base harness for AI agents. Retrieve rules, avoid regressions, and promote repeated lessons into stable reusable knowledge.
- **拉取时间**：2026-07-23 23:50:56

---

# Self-Learning Library

Self-Learning Library is a local-first self-learning knowledge-base harness for Codex-style AI work. It turns repeated corrections, writing rules, workflow lessons, and project memories into a layered vault that an AI assistant can retrieve before a task and improve after a task.

> Instead of asking your AI to remember everything, make it retrieve the right rule, avoid past regressions, and promote repeated lessons into stable knowledge.

Current release: **v0.3.0**. This version keeps the local RAG flow usable in a fresh clone and makes the setup-to-usage path explicit: clone the harness, query the included knowledge base, copy the harness into your own project, and let repeated lessons become reusable rules.

The included vault is exported from a real manuscript-assistance workflow, but the mechanism is domain-independent. You can reuse the same structure for coding habits, research notes, product work, lab workflows, prompt engineering, legal drafting, personal SOPs, or any knowledge process that should improve over time.

## What It Does

Self-Learning Library gives an AI assistant a small local operating loop:

```text
Retrieve relevant memory -> Apply rules -> Check no-regression -> Record lesson -> Promote stable rules
```

It combines:

- a layered Obsidian-compatible Markdown vault;
- lightweight local retrieval with `tools/kb_rag.py`, including a built-in fallback retriever for fresh clones;
- graph-style iteration and rule promotion with `tools/paper_iteration.py`;
- a root harness workflow in `PROJECT_HARNESS_WORKFLOW.md`;
- Codex-facing instructions in `AGENTS.md`;
- a PowerShell entrypoint for full iteration;
- copyable setup steps for adapting the same knowledge-base loop to another workspace.

## Why This Exists

LLM chats often:

- forget project-specific constraints;
- repeat mistakes that were already corrected;
- mix old preferences with newer ones;
- over-load context with irrelevant history;
- produce rules that are not grounded in concrete evidence;
- fail to distinguish stable rules from limited or conflicting rules.

This harness makes the useful parts of past work explicit, searchable, and promotable.

## Before and After

| Without the harness | With Self-Learning Library |
| --- | --- |
| The assistant repeats solved mistakes. | High-priority corrections become no-regression guards. |
| Old chat context is hard to reuse. | Reusable lessons become file-backed memories and rules. |
| Every task loads too much background. | Lightweight RAG retrieves only a few relevant notes. |
| Rules are mixed with evidence and opinions. | The vault separates evidence, reasoning, stable rules, limited rules, and conflicts. |
| Knowledge improves only inside one conversation. | Repeated lessons can be promoted into long-term rules. |

## Knowledge Layers

| Layer | Path | Purpose |
| --- | --- | related:
  - methods/网文写作最强SOP.md
--- |
| Index | `00_Index.md` | Entry point for the vault |
| Change log | `10_Project_Change_Log/` | Concrete changes made during real work |
| Memories | `20_Paper_Memories/` | Reusable lessons, user preferences, corrections, and baselines |
| Intermediate rules | `30_Writing_Rules/` | Rules extracted from memory but not always final |
| Workflow governance | `35_Workflow_Governance/` | Rules about how the harness itself should behave |
| Final rules | `40_Final_Generalized_Rules/` | Stable rules that are safe to reuse |
| Supervision | `45_Supervision/` | High-priority corrections and no-regression constraints |
| Conflicts | `50_Conflicts/` | Contradictions that need human judgment |
| Limited rules | `60_Limited_Rules/` | Useful rules that are scoped or not yet general |
| Iterative thinking | `70_Iterative_Thinking/` | Generated reports, graph summaries, and latest conclusions |

The folder names still say `paper` because this repository was extracted from a writing project. The reusable part is the layered learning pattern.

## Thinking Flow

```mermaid
flowchart TD
    A["User asks a task"] --> B["Read AGENTS.md and PROJECT_HARNESS_WORKFLOW.md"]
    B --> C{"Does the task trigger the harness?"}
    C -- "No" --> D["Answer normally"]
    C -- "Yes" --> E["Run lightweight local RAG with tools/kb_rag.py"]
    E --> F["Retrieve relevant supervision, final rules, conflicts, limited rules, and intermediate rules"]
    F --> G["Build a short task checklist"]
    G --> H["Do the requested work or draft the proposed content"]
    H --> I["Run no-regression checks against high-priority corrections"]
    I --> J{"Need to write into a controlled file?"}
    J -- "Yes" --> K["Show proposed content in chat first and wait for confirmation"]
    J -- "No" --> L["Continue locally"]
    K --> M["After confirmation, write file changes"]
    L --> N["Collect reusable lessons into 10 -> 20 -> 30 when applicable"]
    M --> N
    N --> O{"User requested iteration or final generalization?"}
    O -- "No" --> P["Report result"]
    O -- "Yes" --> Q["Run run_paper_iteration.ps1"]
    Q --> R["Build evidence graph from vault notes and wikilinks"]
    R --> S["Promote stable rules, limited rules, and conflicts"]
    S --> T["Write latest reports to 70_Iterative_Thinking"]
```

## Quick Start: From Setup To First Retrieval

The fastest way to understand the project is to run retrieval against the included example vault, then copy the same harness into your own workspace.

### 1. Clone and verify the local harness

```powershell
git config --global core.longpaths true
git clone https://github.com/LLK-LL/Self-Learning-Library.git
cd Self-Learning-Library
```

On Windows, enable Git long paths before cloning and prefer a short local path such as `C:\dev\Self-Learning-Library`. The included Obsidian vault contains descriptive note filenames that can exceed the legacy Windows path limit when the repository is nested deeply.

Install Python 3.10 or newer. The included scripts use the Python standard library.

Check that the knowledge base can be searched:

```powershell
py tools\kb_rag.py --query "before writing into the document" --limit 3
```

Expected result: the command prints a small set of relevant notes from layers such as `45_Supervision`, `40_Final_Generalized_Rules`, `60_Limited_Rules`, or `30_Writing_Rules`. The point is not to load the whole vault; the point is to retrieve only the rules that matter for the current task.

### 2. Use the included vault before a task

Example task: you want an AI assistant to revise a paragraph, but you want it to remember previous writing rules first.

```powershell
py tools\kb_rag.py --query "revise introduction with mentor feedback" --limit 3
```

Then give the retrieved checklist to the assistant before the actual request:

```text
Use the retrieved rules as constraints. Revise this introduction paragraph, but first avoid any high-priority no-regression issues returned by the knowledge base.
```

For normal writing, coding, or research tasks, keep retrieval narrow with `--limit 3`. Do not load the entire vault unless you are doing a final review or full iteration.

### 3. Query workflow rules only for process questions

Use `--include-workflow` when the question is about how the harness should behave.

```powershell
py tools\kb_rag.py --query "how should the system apply rules before a task" --include-workflow
```

Example use:

```text
Search the workflow rules first. Should this correction become a one-time note, a reusable memory, or a stable rule?
```

### 4. Set up the harness in your own project

Create or choose a target workspace, then copy the harness files:

```powershell
$source = "C:\dev\Self-Learning-Library"
$target = "C:\dev\my-project"

New-Item -ItemType Directory -Path $target -Force | Out-Null
Copy-Item -LiteralPath "$source\AGENTS.md" -Destination $target -Force
Copy-Item -LiteralPath "$source\PROJECT_HARNESS_WORKFLOW.md" -Destination $target -Force
Copy-Item -LiteralPath "$source\run_paper_iteration.ps1" -Destination $target -Force
Copy-Item -LiteralPath "$source\tools" -Destination $target -Recurse -Force
Copy-Item -LiteralPath "$source\paper_writing_obsidian_vault" -Destination $target -Recurse -Force
```

Open the copied vault in Obsidian if you want a visual note interface:

```text
C:\dev\my-project\paper_writing_obsidian_vault
```

Then replace the example notes with your own domain knowledge over time. Keep the layer structure, because the retrieval and iteration scripts depend on it.

### 5. Use your project knowledge base during real work

From the target workspace:

```powershell
cd C:\dev\my-project
py tools\kb_rag.py --query "API error handling convention before editing client code" --limit 3
```

Example assistant instruction:

```text
Use the local harness. Retrieve the top 3 rules for API error handling, turn them into a checklist, then edit the client code without repeating prior regressions.
```

After the task, record only lessons that are reusable. A concrete correction can go into `10_Project_Change_Log/`; a reusable takeaway can go into `20_Paper_Memories/`; a candidate rule can go into `30_Writing_Rules/`.

Example memory note:

```markdown
# API timeout retry rule

## Reusable Lesson

When a request can be retried safely, use bounded exponential backoff and log the final failure with request context, not raw credentials.

## Evidence

Derived from the 2026-07-08 API timeout fix.
```

### 6. Promote stable knowledge with a full iteration

Run a full iteration when you explicitly want screening, final generalization, or a complete rule refresh:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\run_paper_iteration.ps1
```

The latest reports appear in:

```text
paper_writing_obsidian_vault/70_Iterative_Thinking/
```

Use full iteration after several tasks have produced enough evidence. Stable, broadly reusable rules belong in `40_Final_Generalized_Rules/`; scoped rules belong in `60_Limited_Rules/`; contradictions belong in `50_Conflicts/`.

Optional environment variables for custom local integrations:

```powershell
$env:TOTAL_MEMORY_SRC = "C:\path\to\total-agent-memory\src"
$env:TAM_MEMORY_DB = "C:\path\to\memory.db"
$env:SCI_MEMORY_SKILL = "C:\path\to\SCI-memory\SKILL.md"
$env:SELF_LEARNING_LIBRARY_PYTHON = "C:\path\to\python.exe"
```

## Chat Commands

Use these with a Codex-style assistant in this repository:

```text
Use the local harness and revise this paragraph.
```

```text
Search the self-learning knowledge base first, then answer.
```

```text
Use lightweight RAG with limit 3 before revising this content.
```

```text
Record this correction as a reusable rule.
```

```text
Run a self-iteration and tell me what rules became stable, limited, or conflicting.
```

```text
Before writing into the document, show me the proposed replacement text in chat.
```

## Examples

- [Build a domain-specific vault](examples/domain-vault-adaptation.md)
- [Use lightweight retrieval before a task](examples/lightweight-rag.md)
- [Run a full rule iteration](examples/full-iteration.md)
- [No-regression guard pattern](examples/no-regression-guard.md)

## Repository Layout

```text
.
├── AGENTS.md
├── PROJECT_HARNESS_WORKFLOW.md
├── run_paper_iteration.ps1
├── tools/
│   ├── kb_rag.py
│   └── paper_iteration.py
└── paper_writing_obsidian_vault/
    ├── 00_Index.md
    ├── 10_Project_Change_Log/
    ├── 20_Paper_Memories/
    ├── 30_Writing_Rules/
    ├── 35_Workflow_Governance/
    ├── 40_Final_Generalized_Rules/
    ├── 45_Supervision/
    ├── 50_Conflicts/
    ├── 60_Limited_Rules/
    └── 70_Iterative_Thinking/
```

## Adapt It To Your Own Domain

To use this outside paper writing, replace or rewrite notes under:

- `10_Project_Change_Log/`: concrete task history;
- `20_Paper_Memories/`: reusable memories;
- `30_Writing_Rules/`: intermediate rules;
- `40_Final_Generalized_Rules/`: stable rules;
- `45_Supervision/`: high-priority corrections.

You can keep the current vault name or rename it and update constants in:

- `tools/kb_rag.py`
- `tools/paper_iteration.py`
- `PROJECT_HARNESS_WORKFLOW.md`

## Safety Notes

- Do not upload private documents, unpublished manuscripts, credentials, raw chat logs, or personal data unless you intend them to be public.
- Keep workflow rules separate from content rules.
- Treat final generalized rules as stable only when supported by evidence notes.
- Keep unresolved contradictions in `50_Conflicts/` instead of forcing a false rule.
- Review the included vault before using it as a public template.

See [Security and publishing](docs/security-and-publishing.md).

## Project Status

Self-Learning Library is an extracted working prototype. The current scripts are intentionally simple and local-first. They use Markdown files, JSON reports, wikilinks, and Python standard-library parsing instead of a server or database.

See the latest published release metadata on the [GitHub Releases page](https://github.com/LLK-LL/Self-Learning-Library/releases).

## Roadmap

- Add a clean demo vault with synthetic examples.
- Add macOS/Linux convenience scripts.
- Add tests for retrieval ranking and rule promotion.
- Add templates for coding, research, product, and lab-work domains.
- Add a short demo GIF or screenshot walkthrough.

## Contributing

Contributions are welcome when they keep the project local-first, inspectable, and evidence-grounded. Good contributions include new domain templates, safer publishing guidance, retrieval improvements, tests, and clear workflow examples.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## One-Sentence Summary

**Self-Learning Library is a local self-learning knowledge-base harness that helps AI assistants retrieve relevant rules, avoid repeated mistakes, and promote repeated lessons into stable reusable knowledge.**
