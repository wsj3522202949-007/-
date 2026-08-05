---
id: tool-00643
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 需API密钥, 英文文档, 大纲规划, 多Agent, 灵感创意]
title: ghost
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/saiprasaddevare/ghost
created: 2026-07-18
updated: 2026-07-18
no: 643
category: 二、网文 / 长篇 AI 写作系统 库
repo: saiprasaddevare/ghost
stars: 0
url: https://github.com/saiprasaddevare/ghost
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# saiprasaddevare/ghost

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/saiprasaddevare/ghost
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：The first "Bring Your Own Model" (BYOM) SDLC Controller  A pure state machine that enforces software development process without writing code itself. Works with your existing AI tools (GitHub Copilot, Claude CLI, Gemini, Ollama).
- **本地描述**：The first "Bring Your Own Model" (BYOM) SDLC Controller  A pure state machine that enforces software development process without writing code itself. Works with your existing AI tools (GitHub Copilot, Claude CLI, Gemini, Ollama).
- **拉取时间**：2026-07-23 22:57:49

---

# SDLC Ghost Orchestrator 👻

**The first "Bring Your Own Model" (BYOM) SDLC Controller**

A pure state machine that enforces software development process without writing code itself. Works with your existing AI tools (GitHub Copilot, Claude CLI, Gemini, Ollama).

## 🎯 Key Features

- **Zero Hallucination Risk** - Orchestrator never writes code, only manages process
- **Zero Token Cost** - Pure Python logic, you pay for your own AI subscriptions
- **Process Enforcement** - Prevents skipping SDLC phases (Requirements → Architecture → Code)
- **Tool Agnostic** - Works with Claude CLI, GitHub Copilot, Ollama, and more

## 🚀 Quick Start

### Installation

```bash
pip install sdlc-ghost
```

Or install from source:

```bash
git clone https://github.com/sdlc-ghost/sdlc-ghost.git
cd sdlc-ghost
pip install -e .
```

### Prerequisites

You need at least one AI tool installed:
- **Claude CLI**: `pip install claude-cli` or follow [Claude CLI docs](https://docs.anthropic.com/claude/docs/cli)
- **GitHub Copilot CLI**: `gh extension install github/gh-copilot`
- **Ollama**: Download from [ollama.ai](https://ollama.ai)

### Usage

**1. Start the backend server:**

```bash
sdlc-server
```

The server will start on `http://localhost:8000`

**2. Initialize a new project:**

```bash
mkdir my-project
cd my-project
sdlc init
```

You'll be prompted to select your AI model (e.g., `claude_cli`).

**3. Progress through SDLC phases:**

```bash
# Check current status
sdlc status

# Generate requirements
sdlc next
# This will open your AI tool with a requirements prompt
# Output is saved to requirements.md

# Approve requirements to move to architecture
sdlc approve requirements.md

# Generate architecture
sdlc next
# Output is saved to architecture.md

# Generate user stories
sdlc next
# Output is saved to tasks.json

# Generate code for a specific task
sdlc generate-code task-001
```

## 📋 SDLC Phases

The orchestrator enforces a 6-phase workflow:

| Phase | Name | Exit Condition |
|-------|------|----------------|
| **P0_INIT** | Project Setup | `.sdlc_config` created |
| **P1_REQ** | Requirements | `requirements.md` exists and approved |
| **P2_QA** | Question & Answer | All questions answered OR max iterations reached |
| **P3_ARCH** | Architecture | `architecture.md` exists AND all architecture questions answered |
| **P4_STORY** | User Stories | `tasks.json` generated |
| **P5_CODE** | Implementation | Code files created, tests pass |

### P2_QA: Question & Answer Phase

The Q&A phase enables iterative clarification of requirements before architecture design:

**Features:**
- AI analyzes requirements and generates clarifying questions
- Questions categorized by type (functional, non-functional, technical, business)
- Prioritized by importance (critical, high, medium, low)
- Human answers with optional AI suggestions
- Iterative loop (up to 3 iterations by default)
- Questions can be answered, skipped, or marked N/A

**Workflow:**
```
P1_REQ → P2_QA → (answer questions) → P2_QA → ... → P3_ARCH
          ↑___________________________|
```

**Commands:**
```bash
# List all questions
sdlc questions list

# Answer a question
sdlc questions answer q-001 --answer "Your answer here"

# Get AI suggestion for an answer
sdlc questions ai-suggest q-001

# Skip a question
sdlc questions skip q-002 --reason not_applicable

# Check Q&A status
sdlc questions status
```

### P3_ARCH: Architecture Q&A Phase

The architecture phase also supports iterative Q&A to clarify design decisions:

**Features:**
- AI analyzes architecture and generates clarifying questions
- Questions focus on: technology stack, scalability, security, integration, deployment
- Same Q&A commands work for both P2_QA and P3_ARCH phases
- Phase-aware filtering automatically shows relevant questions
- Separate iteration counter per phase

**Workflow:**
```
P2_QA → P3_ARCH → (answer arch questions) → P3_ARCH → ... → P4_STORY
                   ↑_______________________________|
```

**Commands:** (Same as P2_QA)
```bash
# List architecture questions (automatically filtered by current phase)
sdlc questions list

# Answer, skip, get AI suggestions - all work the same
sdlc questions answer q-arch-001 --answer "PostgreSQL"
sdlc questions status
```

## 🛠️ Commands

### `sdlc init`
Initialize a new SDLC project in the current directory.

### `sdlc status`
Show current phase, completed artifacts, and blockers.

### `sdlc next`
Execute the next phase action (generates prompts for your AI tool).

### `sdlc approve <artifact>`
Approve a requirements or architecture document to proceed.

### `sdlc generate-code <task_id>`
Generate code for a specific task from `tasks.json`.

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    CLI Client                           │
│  (Detects AI tools, executes prompts, saves outputs)    │
└────────────────────┬────────────────────────────────────┘
                     │ HTTP (REST API)
                     ▼
┌─────────────────────────────────────────────────────────┐
│              FastAPI Backend                            │
│         (State Machine Orchestrator)                    │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              LangGraph State Machine                    │
│ (P0_INIT → P1_REQ → P2_QA ⟲ → P3_ARCH → P4_STORY → P5_CODE) │
└─────────────────────────────────────────────────────────┘
```

**Key Principle:** The orchestrator is a "ghost" - it manages the process but delegates all intelligence to your local AI tools.

## 📖 Example: Q&A Workflow

Here's a complete example of the Q&A phase in action:

```bash
# 1. Generate and approve requirements
sdlc next  # Creates requirements.md
sdlc approve requirements.md

# 2. Enter Q&A phase (AI generates questions)
sdlc next
# Output: "Generated 5 questions in open_questions.json"

# 3. Review questions
sdlc questions list
# ┌──────┬──────────┬────────────────┬──────────────────────────┬────────┐
# │ ID   │ Priority │ Category       │ Question                 │ Status │
# ├──────┼──────────┼────────────────┼──────────────────────────┼────────┤
# │ q-001│ critical │ non_functional │ Expected response time?  │ open   │
# │ q-002│ high     │ technical      │ Authentication method?   │ open   │
# └──────┴──────────┴────────────────┴──────────────────────────┴────────┘

# 4. Get AI suggestion (optional)
sdlc questions ai-suggest q-001
# Shows AI-generated suggestion based on requirements

# 5. Answer questions
sdlc questions answer q-001 --answer "< 200ms for 95th percentile"
sdlc questions answer q-002 --answer "OAuth 2.0 with JWT tokens"

# 6. Check status
sdlc questions status
# Total: 5, Answered: 2, Open: 3

# 7. Skip irrelevant questions
sdlc questions skip q-003 --reason not_applicable

# 8. Continue answering until complete
# ... answer remaining questions ...

# 9. Proceed to architecture
sdlc next  # Transitions to P3_ARCH
```

## 🔒 Security & Privacy

- **Data Isolation**: Your code never leaves your local machine
- **State Signals Only**: Backend receives status updates, not file contents
- **Localhost Only**: Phase 1 binds to 127.0.0.1 (no network exposure)
- **Audit Trail**: All state transitions are logged for compliance

## 🧪 Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/sdlc-ghost/sdlc-ghost.git
cd sdlc-ghost

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install with dev dependencies
pip install -e ".[dev]"
```

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=backend --cov=client --cov-report=html

# Run specific test suite
pytest tests/backend/
pytest tests/client/
pytest tests/integration/
```

### Code Quality

```bash
# Format code
black .

# Lint
ruff check .

# Type checking
mypy backend/ client/
```

## 🐛 Troubleshooting

### "AI tool not found"
- Ensure your AI tool is installed and in your PATH
- Run `which claude` or `which gh` to verify
- Add custom tool paths in `.sdlc_config`:
  ```json
  {
    "custom_tool_paths": {
      "claude_cli": "/custom/path/to/claude"
    }
  }
  ```

### "Backend connection refused"
- Ensure the backend server is running: `sdlc-server`
- Check if port 8000 is available
- Verify `backend_url` in `.sdlc_config` is `http://localhost:8000`

### "State transition blocked"
- Run `sdlc status` to see current phase and blockers
- Ensure required artifacts exist (e.g., `requirements.md` for P1_REQ)
- Approve documents with `sdlc approve <artifact>`

## 📚 Documentation

- [Product Requirements Document](docs/01-prd/prd.md)
- [Implementation Plan](docs/02-architecture/implementation-plan.md)
- [User Stories](docs/06-user-stories/user-stories-v1.md)

## 🗺️ Roadmap

- **Phase 1 (Current)**: CLI tool with local AI integration
- **Phase 2**: VS Code extension with visual progress tracking
- **Phase 3**: Team dashboard for enterprise (SaaS)

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 💬 Support

- **Issues**: [GitHub Issues](https://github.com/sdlc-ghost/sdlc-ghost/issues)
- **Discussions**: [GitHub Discussions](https://github.com/sdlc-ghost/sdlc-ghost/discussions)

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

**Built with ❤️ by the SDLC Ghost Team**
