---
id: tool-05314
type: tool
area: 库
status: active
tags: [多Agent, Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: multi-agent-technical-blogger-with-google-adk
summary: 多 Agent 协作自动产文
source: https://github.com/shawnspencerpsychicdetective/multi-agent-technical-blogger-with-google-adk
created: 2026-07-18
updated: 2026-07-18
no: 5314
category: 一、去 AI 味 / Humanizer 库
repo: shawnSpencerPsychicDetective/multi-agent-technical-blogger-with-google-adk
stars: 0
url: https://github.com/shawnspencerpsychicdetective/multi-agent-technical-blogger-with-google-adk
tier: "C"
use_case: "多 Agent 协作自动产文"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: a361a0d5c3ccc870
  - methods/改稿润色指令库.md
---

# shawnSpencerPsychicDetective/multi-agent-technical-blogger-with-google-adk

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/shawnspencerpsychicdetective/multi-agent-technical-blogger-with-google-adk
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：A lightweight multi-agent blogging system built with the Google Agent Development Kit (ADK). The application automatically generates high-quality technical blog posts by separating the workflow into planning, validation, writing, and quality assurance stages.
- **本地描述**：A lightweight multi-agent blogging system built with the Google Agent Development Kit (ADK). The application automatically generates high-quality technical blog posts by separating the workflow into planning, validation, writing, and quality assurance stages.
- **拉取时间**：2026-07-25 18:14:00

---

# Multi-Agent Technical Blogger (Google ADK)



A lightweight multi-agent blogging system built with the Google Agent Development Kit (ADK). The application automatically generates high-quality technical blog posts by separating the workflow into planning, validation, writing, and quality assurance stages.



## Features



### Automated Blog Planning



- Generates structured Markdown outlines.

- Creates clear introductions, sections, and conclusions.

- Can incorporate codebase-specific context when available.



### Outline Validation



- Verifies the generated outline contains:

  - Title

  - Introduction

  - 4–6 main sections

  - Conclusion

- Automatically retries generation if requirements are not met.



### Technical Blog Writing



- Expands approved outlines into complete articles.

- Targets software engineers and technical audiences.

- Focuses on practical insights and implementation details.

- Includes code snippets when appropriate.



### Article Validation



- Checks article completeness and structure.

- Ensures consistency with the approved outline.

- Retries generation when quality standards are not met.



### Multi-Agent Architecture



- Dedicated agents for planning and writing.

- Validation agents act as quality gates.

- Loop agents provide automatic retry mechanisms.



---



## Architecture



```text

User Topic

    │

    ▼

┌─────────────────────┐

│ RobustBlogPlanner   │

└─────────┬───────────┘

          │

          ▼

┌─────────────────────┐

│ BlogPlanner         │

│ Generate Outline    │

└─────────┬───────────┘

          │

          ▼

┌─────────────────────┐

│ OutlineValidator    │

└─────────┬───────────┘

          │

     Valid? ── No ──► Retry

          │

         Yes

          ▼

┌─────────────────────┐

│ RobustBlogWriter    │

└─────────┬───────────┘

          │

          ▼

┌─────────────────────┐

│ BlogWriter          │

│ Write Full Article  │

└─────────┬───────────┘

          │

          ▼

┌─────────────────────┐

│ PostValidator       │

└─────────┬───────────┘

          │

     Valid? ── No ──► Retry

          │

         Yes

          ▼

      Final Blog

```



---



## Agents



### BlogPlanner



Creates a structured Markdown outline containing:



- Title

- Introduction

- 4–6 main sections

- Section bullet points

- Conclusion



Output is stored in:



```python

blog_outline

```



---



### OutlineValidationChecker



Validates that the outline contains all required components.



Possible outputs:



```text

ok

```



or



```text

retry

<missing requirements>

```



---



### RobustBlogPlanner



A `LoopAgent` that repeatedly executes:



1. BlogPlanner

2. OutlineValidationChecker



until validation succeeds or the maximum iteration count is reached.



```python

max_iterations = 3

```



---



### BlogWriter



Converts the approved outline into a complete technical article.



Characteristics:



- Software-engineering focused

- Practical and implementation-oriented

- Explains both concepts and reasoning

- Uses Markdown formatting

- Includes concise code examples where useful



Output is stored in:



```python

blog_post

```



---



### BlogPostValidationChecker



Checks that the generated article:



- Contains an introduction

- Matches the outline structure

- Contains a conclusion

- Demonstrates technical clarity



---



### RobustBlogWriter



A `LoopAgent` that repeatedly executes:



1. BlogWriter

2. BlogPostValidationChecker



until validation succeeds.



```python

max_iterations = 3

```



---



### Blogger (Root Agent)



The root orchestration agent responsible for the entire workflow.



Process:



1. Generate an outline.

2. Validate the outline.

3. Write the article.

4. Validate the article.

5. Return:

   - Final blog post

   - 3 alternate titles

   - 2 tweet-length hooks



---



## Installation



### 1. Clone the Repository



```bash

git clone https://github.com/yourusername/multi-agent-blogger.git

cd multi-agent-blogger

```



### 2. Create a Virtual Environment



```bash

python -m venv .venv

```



Activate it:



**Windows**



```bash

.venv\Scripts\activate

```



**Linux / macOS**



```bash

source .venv/bin/activate

```



### 3. Install Dependencies



```bash

pip install -r requirements.txt

```



---



## Environment Variables



Create a `.env` file:



```env

MODEL=gemini-flash-latest

```



The application defaults to:



```env

MODEL=gemini-flash-latest

```



if no model is specified.



---



## Usage



Example topic:



```text

Building Production-Ready RAG Systems with LangGraph

```



Workflow:



```text

Topic

  ↓

Outline Generation

  ↓

Outline Validation

  ↓

Blog Writing

  ↓

Post Validation

  ↓

Final Article + Marketing Assets

```



---



## Example Output Structure



```markdown

# Building Production-Ready RAG Systems with LangGraph



Introduction...



## Retrieval Architecture



...



## State Management



...



## Evaluation Strategy



...



## Deployment Considerations



...



## Monitoring and Observability



...



Conclusion...

```



Additional generated assets:



```text

Alternate Titles:



1. ...

2. ...

3. ...



Hooks:



1. ...

2. ...

```



---



## Project Structure



```text

project/

│

├── .env

├── agent.py

├── README.md

```



---



## Why This Design?



Instead of relying on a single agent to generate a complete article, the system uses specialized agents with validation loops.



Benefits include:



- More reliable output structure

- Better article consistency

- Reduced hallucinations

- Automatic quality control

- Easier extensibility for future agents



Possible future enhancements:



- SEO optimization agent

- Fact-checking agent

- Citation generation

- Image generation agent

- Audience-specific rewriting

- Automatic publishing workflows



related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---



## License



MIT License

