---
id: tool-07489
type: tool
area: 库
status: active
tags: [Ren'Py, 协议未明, 本地优先, 英文文档, 本地写作]
title: rvre
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/picobyte/rvre
created: 2026-07-18
updated: 2026-07-18
no: 7489
category: 画龙补充 / 扩容入库 — 补充源
repo: picobyte/rvre
stars: 3
url: https://github.com/picobyte/rvre
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 541222c7492bfa0a
  - methods/QUICK_START.md
---

# picobyte/rvre

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/picobyte/rvre
- **Stars**：3
- **语言**：Ren'Py
- **License**：None
- **Topics**：—
- **GitHub 描述**：Ren'Py Visual Runtime Editor
- **本地描述**：rvre
- **拉取时间**：2026-07-25 19:23:28

related:
  - methods/QUICK_START.md
---

## Ren'Py Visual Runtime Editor

This repository is intended to be added as a submodule to a git project, a minimal installation of the Ren'Py visual runtime editor.

To include the editor in a renpy project make your project a git repository (if you haven't already):

```bash
git init

# add python and Ren'py files to your repository. You may want to add any other files that you might change for your project.
find game -type f -name "*.*py" -exec git add {} \+

git commit -m 'Initial commit for my visual novel'
```

In windows you can run these commands after installation of  https://gitforwindows.org/ which provides a commandline which should enable you to run this (at least the find command is Linux and Mac(?) command line only). 

```bash
# add the RVRE as a submodule 
git submodule add https://github.com/picobyte/RVRE game/RVRE

#install
bash game/RVRE/scripts_and_fixes/install.sh
```
For Windows there's `scripts_and_fixes\install.bat` which should do the same.

An example visual novel with RVRE included is https://github.com/picobyte/EditButton. The readme there discusses some of the features of the editor.
