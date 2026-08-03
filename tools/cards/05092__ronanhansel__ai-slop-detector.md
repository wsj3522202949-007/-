---
id: tool-05092
type: tool
area: 库
status: active
tags: [Claude插件, Jupyter Notebook, 协议未明, 本地优先, 英文文档, 本地写作]
title: ai-slop-detector
summary: Claude Code 插件式写作流
source: https://github.com/ronanhansel/ai-slop-detector
created: 2026-07-18
updated: 2026-07-18
no: 5092
category: 一、去 AI 味 / Humanizer 库
repo: ronanhansel/ai-slop-detector
stars: 0
url: https://github.com/ronanhansel/ai-slop-detector
tier: "C"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# ronanhansel/ai-slop-detector

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/ronanhansel/ai-slop-detector
- **Stars**：0
- **语言**：Jupyter Notebook
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：ronanhansel/ai-slop-detector
- **拉取时间**：2026-07-25 18:05:48

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# ai-slop-detector

To set up the Python environment:

```bash
CONDA_PLUGINS_AUTO_ACCEPT_TOS=yes conda create -n slop python=3.10 -y
conda activate slop
pip install -r requirements.txt
```

To install latex-related packages (linux)

```bash
sudo apt update
sudo apt install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra cm-super dvipng fonts-liberation
```

## Download existing external evaluations

```bash
hf download ronanhansel/data-ai-slop-detector \
    --local-dir . \
    --repo-type dataset
```

## Using SOTA detector

Step 1: Select one user, filter all posts from that user with: at least 40 characters, no label.
Step 2: Select at most 20 random posts, perform SOTA detection sequentially.
Step 2.1: Fill in `ai_confidence` as a separate column.
Step 2.2: 10 posts are detected as human/ai, label all the remaining posts from the same user as human/ai.
Step 3: Select next user and perform from Step 1 to 2 again until no post left.
