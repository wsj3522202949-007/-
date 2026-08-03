---
id: tool-01580
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: sql-ai-prompt-generator
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/iloveitaly/sql-ai-prompt-generator
created: 2026-07-18
updated: 2026-07-18
no: 1580
category: 二、网文 / 长篇 AI 写作系统 库
repo: iloveitaly/sql-ai-prompt-generator
stars: 10
url: https://github.com/iloveitaly/sql-ai-prompt-generator
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# iloveitaly/sql-ai-prompt-generator

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/iloveitaly/sql-ai-prompt-generator
- **Stars**：10
- **语言**：Python
- **License**：MIT
- **Topics**：chatgpt, database, llms, postgres, prompt, sql, sqlite
- **GitHub 描述**：Utility to generate ChatGPT prompts for SQL writing, offering table structure snapshots and sample row data from Postgres and sqlite databases.
- **本地描述**：Utility to generate ChatGPT prompts for SQL writing, offering table structure snapshots and sample row data from Postgres and sqlite databases.
- **拉取时间**：2026-07-23 23:25:09

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# ChatGPT Prompt for SQL Writing

Generate a prompt for writing SQL queries with LLMs like ChatGPT. Drop your database URL and table name into the script and it will generate a prompt for you to copy and paste into your favorite LLM.

## What this does

- Snapshot of Table Structure: Understand the columns, types, and organization of your table at a glance.
- Sample Rows: Includes INSERT statements to describe the data in your table.
- Extracts Table and Field Comments: If you have comments on your tables or columns, they will be included in the prompt.

## Usage

Install the package:

```shell
pip install llm-sql-prompt
```

Here's how to use it:

```shell
Usage: llm-sql-prompt [OPTIONS] DATABASE_URL [TABLE_NAME]

Options:
  --help  Show this message and exit.
```

Generate a prompt from a postgres database:

```shell
llm-sql-prompt postgresql://postgres:postgres@localhost:5555/database_name table_name | pbcopy
llm-sql-prompt $DATABASE_URL
```

From a local sqlite database:

```shell
llm-sql-prompt "$HOME/Library/Application Support/BeeperTexts/index.db" --all
```

### Tunneling to a remote port

If you find yourself wanting to tunnel into a remote box and work with a production database, here's some helpful commands so you don't need to remember the weird SSH tunneling syntax:

```shell
function find_random_open_port() {
  local start_port=${1:-1024}
  local max_attempts=100
  local attempt=0
  local port=$start_port

  while (( attempt < max_attempts )); do
    if ! nc -z localhost $port 2>/dev/null; then
      echo $port
      return
    fi
    port=$((port + 1))
    attempt=$((attempt + 1))
  done

  echo "No open port found after $max_attempts attempts, starting from $start_port." > /dev/stderr
  return 1
}


function ssh-tunnel() {
  if [ $# -lt 2 ]; then
    echo "Usage: ssh-tunnel remote_host remote_port [local_port]"
    echo "This function sets up SSH port forwarding."
    return 1
  fi

  local remote_host=$1
  local remote_port=$2
  local local_port=${3:-$(find-random-open-port $remote_port)}

  if [[ -z $local_port ]]; then
    echo "Failed to find an open local port."
    return 1
  fi

  echo "Forwarding local port $local_port to remote port $remote_port on $remote_host..."
  set -x
  ssh $remote_host -L ${local_port}:localhost:${remote_port}
}
```

## TODO

Super basic script, needs a lot of work

- [x] pg support
- [x] one entrypoint
- [x] use DB comments on columns + tables
- [x] multiple tables
- [ ] prompt tweaking
- [ ] understand prompt size limits and sample records until one fits
