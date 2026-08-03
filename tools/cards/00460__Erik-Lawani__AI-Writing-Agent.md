---
id: tool-00460
type: tool
area: 库
status: active
tags: [多Agent, Jupyter Notebook, 协议未明, 本地优先, 英文文档, 本地写作]
title: AI-Writing-Agent
summary: 多 Agent 协作自动产文
source: https://github.com/erik-lawani/ai-writing-agent
created: 2026-07-18
updated: 2026-07-18
no: 460
category: 二、网文 / 长篇 AI 写作系统 库
repo: Erik-Lawani/AI-Writing-Agent
stars: 0
url: https://github.com/erik-lawani/ai-writing-agent
tier: "C"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Erik-Lawani/AI-Writing-Agent

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/erik-lawani/ai-writing-agent
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：This project is build using LangChain to automatically generates posts using user prompts
- **本地描述**：This project is build using LangChain to automatically generates posts using user prompts
- **拉取时间**：2026-07-23 22:52:29

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

A multi-agent writing system built with AutoGen that demonstrates collaborative AI agents working together to create structured content. This project showcases how specialized AI agents can be orchestrated to handle complex writing tasks through role-based collaboration.

## Features

- **Multi-Agent Architecture**: Two specialized agents working in tandem
  - **Planner Agent**: Creates structured outlines for blog posts and articles
  - **Writer Agent**: Transforms outlines into comprehensive written content
- **Intelligent Handoff System**: Agents seamlessly pass work between each other using handoff messages
- **Flexible Termination**: Smart termination conditions that stop the workflow when content is complete
- **Streaming Output**: Real-time display of agent interactions and content generation

## How It Works

1. **Planning Phase**: The Planner Agent receives a topic and creates a structured outline with key sections (Introduction, Background, Key Insights, Challenges, Conclusion)
2. **Handoff**: The planner signals completion and hands off to the writer with a handoff message
3. **Writing Phase**: The Writer Agent takes the outline and generates detailed content for each section
4. **Termination**: The system automatically stops when the writer completes the conclusion section

## Technical Implementation

- Built with **AutoGen** for multi-agent coordination
- Uses **OpenAI GPT-4o** for content generation
- Implements custom agent classes inheriting from `BaseChatAgent`
- Features intelligent termination conditions using `TextMentionTermination` and `HandoffTermination`
- Console-based UI for real-time interaction monitoring

## Usage

The system can be easily extended to handle different types of writing tasks by modifying the agent prompts and outline structures. Simply provide a topic and watch as the agents collaborate to create well-structured, comprehensive content.

## Example Output

For a topic like "The impact of AI on education", the system will:
1. Generate a structured outline covering all key aspects
2. Create detailed content for each section
3. Provide a complete, publication-ready article

This project demonstrates the power of multi-agent systems in content creation and serves as a foundation for building more complex collaborative AI workflows.
