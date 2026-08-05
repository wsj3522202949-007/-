---
id: tool-00673
type: tool
area: 库
status: active
tags: [协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: ai-ready-issues
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/wolffcatskyy/ai-ready-issues
created: 2026-07-18
updated: 2026-07-18
no: 673
category: 二、网文 / 长篇 AI 写作系统 库
repo: wolffcatskyy/ai-ready-issues
stars: 0
url: https://github.com/wolffcatskyy/ai-ready-issues
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# wolffcatskyy/ai-ready-issues

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/wolffcatskyy/ai-ready-issues
- **Stars**：0
- **语言**：None
- **License**：MIT
- **Topics**：ai, ai-assisted, contributing, developer-tools, github-issues, open-source, templates
- **GitHub 描述**：A standard for writing open source issues that AI assistants can help solve — templates, guides, and workflow for AI-ready contributions
- **本地描述**：A standard for writing open source issues that AI assistants can help solve — templates, guides, and workflow for AI-ready contributions
- **拉取时间**：2026-07-23 22:58:39

---

# AI-Ready Issues

---
**Note:** This project was developed with and is supported exclusively by AI. There is no human support — issues and PRs are triaged and responded to by AI agents. If AI-assisted software isn't for you, no hard feelings — but you might want to reconsider, since so is most of the software you already use.

---

A standard for writing open source issues that AI assistants can help solve.

Most people want to contribute to projects they use but don't know where to start. The codebase is unfamiliar, the setup is complex, and who has time to learn a whole project just to fix one thing?

AI-Ready Issues solve this by giving contributors everything they need — context, requirements, expected behavior — formatted so they can paste it into Claude, ChatGPT, or any AI assistant and get working code back.

## Philosophy

The question isn't "should we use AI in open source?"

The question is: **how do we structure participation so AI becomes a force multiplier for contribution, not a substitute for it?**

Most people want to contribute to projects they use but don't know where to start. The codebase is unfamiliar, the setup is complex, and who has time to learn a whole project just to fix one thing?

But what if maintainers gave you everything you needed — context, requirements, expected behavior — formatted so you could paste it directly into Claude/ChatGPT and get working code back?

That's the idea behind AI-Ready Issues: a standard that lets anyone contribute their AI subscription to a project.

**Here's how it works:**

1. Contributors find an AI-Ready issue
2. Copy the issue into their AI assistant
3. Review and test the output — understand every line
4. Submit it back to GitHub as a pull request
5. Note that AI was used so maintainers know what to scrutinize

The bottleneck in open source has never been talent. It's context. A skilled developer can fix most bugs in most projects, but they'd need hours just to understand the codebase enough to attempt it. AI-Ready Issues eliminate that barrier.

AI assistants are good at taking structured context and producing working code. Humans are good at reviewing, testing, and understanding intent. This standard combines both strengths — crowdsourced open source, powered by distributed AI compute.

The contributor still needs to:
- Understand what the code does
- Test it in their environment
- Take responsibility for what they submit
- Disclose that AI was used

The AI just gets them past the blank-page problem.

I've applied this to my own [crowdsec-blocklist-import](https://github.com/wolffcatskyy/crowdsec-blocklist-import). If you'd like to participate or see it in action, check it out.

## The Standard

An AI-Ready issue includes:

1. **Context** — what the project does, relevant files, architecture
2. **Current behavior** — what happens now (with code references)
3. **Expected behavior** — what should happen
4. **Implementation guide** — file paths, function names, code snippets showing where to make changes
5. **Acceptance criteria** — specific, testable requirements (checkboxes)
6. **Constraints** — what not to break
7. **AI Prompt** — a copy-paste-ready block that feeds the AI everything it needs

## The Workflow

```
Maintainer writes AI-ready issue
        |
        v
Contributor copies it into Claude/ChatGPT/Copilot
        |
        v
Contributor reviews output, tests it, learns from it
        |
        v
Contributor submits PR with AI disclosure
        |
        v
Maintainer reviews and merges
```

## The Hard Part: Right-Sizing Issues

The AI-ready format has a cost. Writing a good issue takes 10-20 minutes of structured thinking — context, implementation guide, acceptance criteria, AI prompt. That investment only pays off when the issue is the right size.

**Too small** — If you can fix it faster than you can describe it, just fix it. A two-line change doesn't need a structured template. The overhead of writing the issue exceeds the value of crowdsourcing the fix.

**Too large** — If the change touches 10 files across 3 subsystems, no amount of context will make it AI-friendly. The model loses coherence, the contributor can't meaningfully review the output, and the PR becomes un-reviewable.

**The sweet spot** — A single, well-bounded change that requires real codebase knowledge to implement but not to understand. Adding a new endpoint behind a clear interface. Fixing a bug where you know the root cause but the fix touches code a newcomer wouldn't find. Implementing a feature where the design is settled but the contributor needs to know where things live.

The maintainer's judgment is what makes this work. You know your codebase — you know which changes are self-contained enough for someone to pick up cold. That curation is the standard's real value.

See the [Maintainer Guide](guide/MAINTAINER_GUIDE.md) for detailed guidance on when to use (and not use) this standard.

## What This Is

- Lowering the barrier to open source participation
- AI handles boilerplate, humans handle thinking
- Turning "I wish this had feature X" into "I'll just add it"
- Distributed development using distributed compute

## What This Isn't

- Dumping untested AI garbage
- Submitting code you don't understand
- Replacing real developers
- Writing issues for things you could fix faster yourself

## Quick Start

### For Maintainers

1. Copy the [issue templates](.github/ISSUE_TEMPLATE/) into your repo
2. Adapt the [CONTRIBUTING.md template](templates/CONTRIBUTING.md) for your project
3. Write issues using the AI-Ready format
4. Label them `ai-ready` so contributors can find them

### For Contributors

1. Find an issue labeled `ai-ready`
2. Copy the issue body + the project's AI context block (from CONTRIBUTING.md)
3. Paste into your AI assistant
4. Review every line of output — understand it before submitting
5. Test locally
6. Submit a PR with AI disclosure

## Templates Included

| File | Purpose |
|------|---------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| [templates/CONTRIBUTING.md](templates/CONTRIBUTING.md) | Drop-in CONTRIBUTING.md with AI contribution guidelines |
| [.github/ISSUE_TEMPLATE/ai-ready-bug.md](.github/ISSUE_TEMPLATE/ai-ready-bug.md) | Bug report formatted for AI consumption |
| [.github/ISSUE_TEMPLATE/ai-ready-feature.md](.github/ISSUE_TEMPLATE/ai-ready-feature.md) | Feature request formatted for AI consumption |
| [templates/PR_TEMPLATE.md](templates/PR_TEMPLATE.md) | Pull request template with AI disclosure section |
| [guide/MAINTAINER_GUIDE.md](guide/MAINTAINER_GUIDE.md) | How to write effective AI-ready issues |
| [guide/CONTRIBUTOR_GUIDE.md](guide/CONTRIBUTOR_GUIDE.md) | How to use AI responsibly for contributions |

## Projects Using This Standard

- [crowdsec-blocklist-import](https://github.com/wolffcatskyy/crowdsec-blocklist-import) — Import 120k+ IPs from 36 threat feeds into CrowdSec
- [crowdsec-unifi-bouncer](https://github.com/wolffcatskyy/crowdsec-unifi-bouncer) — Native CrowdSec bouncer for UniFi OS
- [crowdsec-unifi-parser](https://github.com/wolffcatskyy/crowdsec-unifi-parser) — CrowdSec-parseable firewall logs from UniFi
- [emby-playback-guardian](https://github.com/wolffcatskyy/emby-playback-guardian) — Playback protection for Emby/Jellyfin
- [homeops-mcp](https://github.com/wolffcatskyy/homeops-mcp) — Home infrastructure MCP server

*Using this standard? Open a PR to add your project here.*

## Background

Inspired by [Fedora's 2025 policy on AI-assisted contributions](https://communityblog.fedoraproject.org/council-policy-proposal-policy-on-ai-assisted-contributions/) which established that AI-assisted contributions are welcome when contributors take responsibility for the output.

This standard takes that a step further: instead of just *allowing* AI contributions, we actively *optimize* for them by structuring issues so AI tools can be maximally effective.

## Contributing

This standard itself is open for contributions. If you have ideas for improving the templates, workflow, or documentation, open an issue or PR.

## License

MIT — use these templates in any project, commercial or open source.
