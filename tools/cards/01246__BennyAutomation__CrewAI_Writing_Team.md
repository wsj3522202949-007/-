---
id: tool-01246
type: tool
area: 库
status: active
tags: [多Agent, 校对, Python, 协议未明, 需API密钥, 英文文档, 改稿润色]
title: CrewAI_Writing_Team
summary: 多 Agent 协作自动产文
source: https://github.com/bennyautomation/crewai_writing_team
created: 2026-07-18
updated: 2026-07-18
no: 1246
category: 二、网文 / 长篇 AI 写作系统 库
repo: BennyAutomation/CrewAI_Writing_Team
stars: 0
url: https://github.com/bennyautomation/crewai_writing_team
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

# BennyAutomation/CrewAI_Writing_Team

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/bennyautomation/crewai_writing_team
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A team of AI agents that will create a short story based off a sentence prompt.
- **本地描述**：A team of AI agents that will create a short story based off a sentence prompt.
- **拉取时间**：2026-07-23 23:15:25

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Writerideamachine Crew

This is a team of AI agents I created using CrewAI. Given a simple prompt, agents will:
- Create a list of story points/characters
- From that list, create a basic story summary
- Check that story summary against well-known book and movie plots
- Confirm whether the story is unique or derivative
- Write a short story if given the go ahead from the previous agent
- Proofread it for typos and grammatical errors/improvements
- Save the story to a text file.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/writerideamachine/config/agents.yaml` to define your agents
- Modify `src/writerideamachine/config/tasks.yaml` to define your tasks
- Modify `src/writerideamachine/crew.py` to add your own logic, tools and specific args
- Modify `src/writerideamachine/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the WriterIdeaMachine Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The WriterIdeaMachine Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Writerideamachine Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
