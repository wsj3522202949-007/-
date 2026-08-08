---
id: tool-03871
type: tool
area: 库
status: active
tags: [Java, 协议未明, 需API密钥, 英文文档, 改稿润色]
title: OpenAI_Test_Case_Generator
summary: 错别字/语法/风格校对
source: https://github.com/qapournima/openai_test_case_generator
created: 2026-07-18
updated: 2026-07-18
no: 3871
category: 十三、语法 / 风格检查 / 校对 库
repo: QAPournima/OpenAI_Test_Case_Generator
stars: 1
url: https://github.com/qapournima/openai_test_case_generator
tier: "B"
use_case: "错别字/语法/风格校对"
pitfalls:
  - "🔑 需自备 LLM API Key（多为 OpenAI/Claude/Gemini），有 token 成本与网络门槛"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/改稿润色指令库.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: ddca8c9c705e47ca
  - methods/自检清单_升级版.md
---

# QAPournima/OpenAI_Test_Case_Generator

- **分类**：十三、语法 / 风格检查 / 校对 库
- **链接**：https://github.com/qapournima/openai_test_case_generator
- **Stars**：1
- **语言**：Java
- **License**：None
- **Topics**：—
- **GitHub 描述**：This project is a Java-based automation tool that integrates with Jira and OpenAI to generate Gherkin-style test cases based on user stories. The tool fetches user stories from Jira, uses OpenAI to generate test cases, and updates Jira with the generated test cases.
- **本地描述**：This project is a Java-based automation tool that integrates with Jira and OpenAI to generate Gherkin-style test cases based on user stories. The tool fetches user stories from Jira, uses OpenAI to generate test cases, and updates Jira with the generated test cases.
- **拉取时间**：2026-07-24 00:00:33

related:
  - methods/改稿润色指令库.md
  - methods/自检清单_升级版.md
---

# OpenAI Test Case Generator

## Overview

This project is a Java-based automation tool that integrates with Jira and OpenAI to generate Gherkin-style test cases based on user stories. The tool fetches user stories from Jira, uses OpenAI to generate test cases, and updates Jira with the generated test cases.

## Features

- Fetches user stories from Jira issues
- Uses OpenAI's API to generate Gherkin test cases
- Updates Jira with generated test cases
- Supports authentication via API keys

## Prerequisites

Ensure you have the following before running the project:

- Java 8 or later installed
- Apache HttpComponents library
- A Jira account with API access
- OpenAI API key

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/JiraOpenAITestCaseGenerator.git
   cd JiraOpenAITestCaseGenerator
   ```
2. Add required dependencies (if using Maven, include Apache HttpClient dependencies in `pom.xml`).

## Configuration

Update the following fields in the `JiraOpenAITestCaseGenerator.java` file:

```java
private static final String JIRA_DOMAIN = "https://yourjira.atlassian.net/";
private static final String JIRA_EMAIL = "your-email@example.com";
private static final String JIRA_API_TOKEN = "YOUR_JIRA_API_TOKEN";
private static final String OPENAI_API_KEY = "YOUR_OPENAI_API_KEY";
```

## Usage

1. Compile the Java file:
   ```sh
   javac -cp .:lib/* JiraOpenAITestCaseGenerator.java
   ```
2. Run the program:
   ```sh
   java -cp .:lib/* JiraOpenAITestCaseGenerator
   ```

## How It Works

1. The tool fetches the user story from a Jira issue using Jira API.
2. It sends the user story to OpenAI API to generate Gherkin test cases.
3. The generated test cases are added to Jira as a description update.

## Example Output

```
Raw Jira Response: { ... }
Generated Test Cases:
Scenario: User logs into the system
Given the user is on the login page
When the user enters valid credentials
Then the user is redirected to the dashboard
Updated Jira issue with test cases: JIRA-1
```

## Troubleshooting

- Ensure your Jira API token and OpenAI API key are correctly configured.
- If Jira API calls fail, check your Jira domain and issue key.
- If OpenAI responses are invalid, verify the API request format.

## Contributing

Feel free to submit issues or pull requests to improve the project.


