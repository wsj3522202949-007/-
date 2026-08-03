---
id: tool-00046
type: tool
area: 库
status: active
tags: [多Agent, Python, 协议未明, 需API密钥, 英文文档]
title: FictionAgent
summary: 多 Agent 协作自动产文
source: https://github.com/navyavelicheti10/fictionagent
created: 2026-07-18
updated: 2026-07-18
no: 46
category: 二、网文 / 长篇 AI 写作系统 库
repo: navyavelicheti10/FictionAgent
stars: 0
url: https://github.com/navyavelicheti10/fictionagent
tier: "C"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# navyavelicheti10/FictionAgent

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/navyavelicheti10/fictionagent
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：FictionAgent is a multi-agent AI system that turns simple prompts into structured stories. It builds narratives step by step-creating the world, characters, and plot, validating consistency, and generating a final story,resulting in more coherent and engaging storytelling than single-step generation.
- **本地描述**：FictionAgent is a multi-agent AI system that turns simple prompts into structured stories. It builds narratives step by step-creating the world, characters, and plot, validating consistency, and generating a final story,resulting in more coherent and engaging storytelling than single-step generation.
- **拉取时间**：2026-07-23 22:40:12

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# FictionAgent

A multi-agent AI system that collaboratively generates creative stories using LangGraph and OpenAI. Each agent specializes in a different aspect of storytelling: world-building, character creation, plot development, consistency checking, and narrative composition.

## Features

- **World Builder Agent** - Creates detailed fictional worlds with settings, rules, history, and environment
- **Character Agent** - Designs meaningful characters with personalities, goals, and relationships
- **Plot Agent** - Structures compelling 3-act story narratives
- **Consistency Agent** - Reviews and identifies logical inconsistencies and plot holes
- **Narrator Agent** - Composes the final polished story

## Prerequisites

- Python 3.12+
- Groq API key

## Installation

1. Clone the repository:
```bash
cd FictionAgent
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -e .
```

Or install from requirements directly:
```bash
pip install -r fiction_agent/requirements.txt
```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your Groq API key:
```bash
GROQ_API_KEY=your-groq-api-key-here
GROQ_MODEL=mixtral-8x7b-32768
```

## Usage

Run the interactive story generator:
```bash
python3 main.py
```

Enter your story idea when prompted:
```
Enter your story idea (or 'bye' to exit): girl in a magical world
```

The system will:
1. Build a magical world
2. Create characters suited to that world
3. Develop a compelling plot
4. Check for consistency issues
5. Generate the final story

Type `bye` to exit.

## Project Structure

```
FictionAgent/
├── main.py                          # Root entry point
├── pyproject.toml                   # Project configuration
├── README.md                        # This file
├── fiction_agent/
│   ├── main.py                      # Story generation entry point
│   ├── graph.py                     # LangGraph workflow definition
│   ├── state.py                     # Graph state schema
│   ├── config.py                    # LLM configuration
│   ├── requirements.txt             # Python dependencies
│   └── agents/
│       ├── world_agent.py           # World-building agent
│       ├── character_agent.py       # Character design agent
│       ├── plot_agent.py            # Plot structuring agent
│       ├── consistency_agent.py     # Logic verification agent
│       └── narrator_agent.py        # Story composition agent
```

## How It Works

The system uses LangGraph to orchestrate a sequence of AI agents:

```
User Input → World Agent → Character Agent → Plot Agent → Consistency Agent → Narrator Agent → Final Story
```

Each agent:
1. Takes the output of the previous agent
2. Processes it with OpenAI's language model
3. Adds its specialized contribution
4. Passes the enhanced state to the next agent

## Dependencies

- **langgraph** - Agent orchestration and graph execution
- **langchain** - LLM utilities and abstractions
- **langchain-groq** - Groq API integration
- **python-dotenv** - Environment variable management

## Configuration

The system is configured via environment variables:

- `GROQ_API_KEY` - Your Groq API key (required)
- `GROQ_MODEL` - Model to use (default: mixtral-8x7b-32768)

## Example

```bash
$ python3 main.py
Enter your story idea (or 'bye' to exit): A time traveler discovers they're the villain
```

The agents will generate a complete story based on your prompt, creating a world, characters, and plot that are logically consistent and narratively compelling.

## License

MIT
