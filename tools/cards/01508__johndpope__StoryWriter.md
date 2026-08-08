---
id: tool-01508
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: StoryWriter
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/johndpope/storywriter
created: 2026-07-18
updated: 2026-07-18
no: 1508
category: 二、网文 / 长篇 AI 写作系统 库
repo: johndpope/StoryWriter
stars: 0
url: https://github.com/johndpope/storywriter
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 38bc2fc2c967d9e7
  - methods/最强写作方法论_全球最强综合版.md
---

# johndpope/StoryWriter

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/johndpope/storywriter
- **Stars**：0
- **语言**：None
- **License**：None
- **Topics**：—
- **GitHub 描述**：StoryWriter: A dynamic creative writing application leveraging Entity Framework Core and Blazor. Create and manage characters, locations, events, and plot points with robust relationships and narrative consistency. Ideal for writers to craft and visualize complex storylines.
- **本地描述**：StoryWriter: A dynamic creative writing application leveraging Entity Framework Core and Blazor. Create and manage characters, locations, events, and plot points with robust relationships and narrative consistency. Ideal for writers to craft and visualize complex storylines.
- **拉取时间**：2026-07-23 23:23:04

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# AI-Integrated Writing Application

## Overview

Welcome to the AI-Integrated Writing Application, a tool designed to enhance your writing experience by combining advanced AI capabilities with robust data management. This application supports various writing styles and document types, ensuring versatility and flexibility for all users.

## Features

1. **AI Autocompletion**:

   - **Intelligent Suggestions**: AI-powered autocompletions for faster writing.
   - **Customizable Suggestions**: Adjust the AI’s creativity level for tailored suggestions.
   - **Context-Aware Recommendations**: Suggestions adapt to the user’s writing style.

2. **Local Data Management**:

   - **Tagging System**: Organize elements with tags for easy retrieval. (In work)
   - **Description Support**: Add detailed descriptions to elements for better context.
   - **Search Functionality**: Quickly find elements using keywords or tags. (In Work)

3. **Text Generation**:
   - **AI-Generated Text**: Create new content with AI-generated text.
   - **Customizable Length**: Generate text of any length for various purposes.

## Planned Features

1. **Local Data Storage**

   - **Encryption**: Data is encrypted using AES-256 for protection.
   - **Password Protection**: Secure access with user-defined passwords.
   - **Secure Communication**: Data transmission is encrypted using TLS.

2. **Advanced AI Capabilities**

   - **Context-Aware Suggestions**: Provides intelligent suggestions for autocompletions and more, adapting to the user’s writing style.
   - **Tagging System**: Users can tag elements to enhance AI suggestions.
   - **Dynamic Context Updates**: AI suggestions stay relevant with updated tags and descriptions.

3. **User-Friendly Interface**
   - **Minimalist Design**: A clean, uncluttered interface to avoid distractions.
   - **Seamless Integration**: AI suggestions appear smoothly as you type.
   - **Creativity Control**: Adjust the AI’s suggestion creativity level.

## Technical Architecture

1. **Front-End**:

   - Built using Blazor

2. **Back-End**:

   - **AI Model**: Generates text based on user input using Ollama AI.
   - Interacts with the local database and the AI model.

3. **Database Integration**:
   - **Vector Database**: Stores embeddings for fast similarity searches. (In Work)
   - **Relational Database**: Stores detailed tags and descriptions. (In Work)

## Acknowledgments

We acknowledge the following libraries and frameworks that contributed to this application:

- **[Bootstrap](https://getbootstrap.com/)**: For creating a responsive front-end framework.
- **[FontAwesome](https://fontawesome.com/)**: For a comprehensive library of icons.
- **[Tabulator](http://tabulator.info/)**: For powerful and interactive table functionalities.
- **[Blazor](https://dotnet.microsoft.com/apps/aspnet/web-apps/blazor)**: For building interactive web UIs using C#.
- **[Ollama AI](https://ollama.com/)**: For providing advanced AI capabilities for text generation.
