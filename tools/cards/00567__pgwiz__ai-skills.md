---
id: tool-00567
type: tool
area: 库
status: active
tags: [Claude插件, PowerShell, 协议未明, 本地优先, 英文文档, 本地写作]
title: ai-skills
summary: Claude Code 插件式写作流
source: https://github.com/pgwiz/ai-skills
created: 2026-07-18
updated: 2026-07-18
no: 567
category: 二、网文 / 长篇 AI 写作系统 库
repo: pgwiz/ai-skills
stars: 0
url: https://github.com/pgwiz/ai-skills
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: bf08dd8b6a9d9b7f
  - methods/最强写作方法论_全球最强综合版.md
---

# pgwiz/ai-skills

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/pgwiz/ai-skills
- **Stars**：0
- **语言**：PowerShell
- **License**：None
- **Topics**：—
- **GitHub 描述**：Agent memory + session control skills for GitHub Copilot and Claude Code. Persistent project memory, safe file-writing rules, cross-platform install.
- **本地描述**：Agent memory + session control skills for GitHub Copilot and Claude Code. Persistent project memory, safe file-writing rules, cross-platform install.
- **拉取时间**：2026-07-23 22:55:35

---

# ai-skills

Agent memory and session control skills for GitHub Copilot, Claude Code,
and any agent runtime that supports the Agent Skills open standard.

## Skills

### agent-memory
Gives your agent persistent project memory, safe file-writing rules,
and cross-session context. Works across all projects without re-explaining
your stack, conventions, or codebase every session.

## Install

### Using GitHub CLI (recommended)

Follow these steps to install or upgrade the GitHub CLI (`gh`), authenticate, and install the skill.

Windows (winget)

```powershell
# Install
winget install --id GitHub.cli
# Upgrade
winget upgrade --id GitHub.cli
```

Linux (Debian/Ubuntu - apt)

```bash
# Ensure curl is present
type -p curl >/dev/null || (sudo apt update && sudo apt install curl -y)
# Add GitHub CLI package repo and key
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update && sudo apt install gh -y
```

Authenticate with GitHub:

```bash
gh auth login
```

Finally, install the skill:

```bash
gh skills install pgwiz/ai-skills agent-memory
```

Or see [install/INSTALL.md](https://github.com/pgwiz/ai-skills/blob/main/install/INSTALL.md) for curl/PowerShell/manual options.

## Compatibility

| Runtime | Supported |
|---------|--------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| GitHub Copilot (VS Code) | ✓ |
| Claude Code | ✓ |
| GitHub Copilot CLI | ✓ |
| Any .agents/skills runtime | ✓ |
| Windows / macOS / Linux | ✓ |

## Author
pgwiz — https://github.com/pgwiz
