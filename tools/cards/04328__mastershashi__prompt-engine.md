---
id: tool-04328
type: tool
area: 库
status: active
tags: [互动叙事, Go, 协议宽松, 本地优先, 英文文档, 本地写作]
title: prompt-engine
summary: 互动叙事/聊天写故事
source: https://github.com/mastershashi/prompt-engine
created: 2026-07-18
updated: 2026-07-18
no: 4328
category: 四、长篇一致性 / RAG / 故事圣经 库
repo: mastershashi/prompt-engine
stars: 0
url: https://github.com/mastershashi/prompt-engine
tier: "C"
use_case: "互动叙事/聊天写故事"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/人物思维蒸馏法.md
  - methods/模板库.md
---

# mastershashi/prompt-engine

- **分类**：四、长篇一致性 / RAG / 故事圣经 库
- **链接**：https://github.com/mastershashi/prompt-engine
- **Stars**：0
- **语言**：Go
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Prompt Engine is a lightweight Go library for building efficient prompts for chatbots, AI agents, and LLM apps. It assembles system, user, and assistant messages, renders templates with variables, enforces token and character limits, summarizes older context if needed, and compiles prompts with low memory overhead.
- **本地描述**：Prompt Engine is a lightweight Go library for building efficient prompts for chatbots, AI agents, and LLM apps. It assembles system, user, and assistant messages, renders templates with variables, enforces token and character limits, summarizes older context if needed, and compiles prompts with low memory overhead.
- **拉取时间**：2026-07-25 17:42:17

related:
  - methods/人物思维蒸馏法.md
  - methods/模板库.md
---

# Prompt Engine

A production-oriented prompt compiler for Go that helps you assemble bounded, low-allocation prompts for chatbots, agents, and LLM-backed services.

## What this library currently provides

The package is built around a small but useful set of primitives:

- a bounded sliding window of role/content messages
- character and token budget enforcement
- optional summarization when a conversation grows past the configured budget
- pluggable token counting through a tokenizer interface
- prompt rendering with `{{var}}` and `{{messages}}` placeholders
- context-aware rendering for cancelable request flows
- provider execution hooks for sending compiled prompts to an external model
- pooled message blocks and reusable byte buffers to keep allocation pressure low

## Quick start

```go
package main

import (
    "fmt"

    pe "github.com/mastershashi/go-patterns/pkg/prompt-engine"
)

func main() {
    engine := pe.NewEngine(pe.Config{
        MaxChars:    64 * 1024,
        MaxMessages: 64,
        MaxTokens:   8192,
    })

    _ = engine.AddSystem("You are a helpful assistant")
    _ = engine.AddUser("Translate this to {{language}}: {{text}}")

    buf := make([]byte, 0, 1024)
    rendered := engine.CompileTemplate(buf, "{{messages}}", map[string]string{
        "language": "English",
        "text":     "hello world",
    })

    fmt.Println(string(rendered))
}
```

## Real-world use cases

This library is a good fit when you need a lightweight prompt assembly layer inside a larger AI application:

- chat assistants with long-running conversations
- agent runtimes that must keep context bounded while preserving recent turns
- RAG systems that combine retrieved documents with the latest chat history
- tool-using workflows where prompts are assembled repeatedly under tight latency budgets
- backend services that need predictable memory behavior and low GC churn

## Example: summarize older context before sending to a provider

```go
type wordTokenizer struct{}
func (wordTokenizer) CountTokens(text string) int { return len(strings.Fields(text)) }

type compactSummarizer struct{}
func (compactSummarizer) Summarize(messages []pe.Message) string {
    return "summary: earlier context retained"
}

engine := pe.NewEngine(pe.Config{
    MaxChars:    64 * 1024,
    MaxMessages: 16,
    MaxTokens:   96,
    Tokenizer:   wordTokenizer{},
    Summarizer:  compactSummarizer{},
})

_ = engine.AddSystem("You are a travel planner")
_ = engine.AddUser("Plan a weekend trip to Berlin")
_ = engine.AddAssistant("Focus on museums and food")

prompt := string(engine.CompileTemplate(nil, "{{messages}}", nil))
_ = prompt
```

## Limitations and non-goals

This package is intentionally focused on prompt assembly rather than being a full AI framework.

Current limitations include:

- it does not persist conversation state or provide durable memory
- it does not implement retries, streaming, or provider-specific request handling
- token counting is approximate unless a custom tokenizer is supplied
- summarization is a hook you provide; the package does not ship a learned summarizer
- it is best suited for the “prompt construction” layer, not full orchestration, tool routing, or agent planning

## Design highlights

- fixed-capacity ring window with no array-copy churn during eviction
- pooled message blocks to reduce GC pressure
- atomic character and token budget tracking
- reusable output buffers for hot-path rendering
- context-aware compile flow for cancelable execution
- provider hooks for integrating with external model execution backends

## Performance guidance

For the best results:

- reuse the same output byte slice across requests
- keep budgets aligned with your model and workload
- use larger budgets for long-running sessions and smaller budgets for latency-sensitive services
- treat this package as the prompt assembly layer, not as a complete agent framework
