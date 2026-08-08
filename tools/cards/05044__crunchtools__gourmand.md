---
id: tool-05044
type: tool
area: 库
status: active
tags: [Dockerfile, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: gourmand
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/crunchtools/gourmand
created: 2026-07-18
updated: 2026-07-18
no: 5044
category: 一、去 AI 味 / Humanizer 库
repo: crunchtools/gourmand
stars: 0
url: https://github.com/crunchtools/gourmand
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 76c7304b77cf3906
  - methods/改稿润色指令库.md
---

# crunchtools/gourmand

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/crunchtools/gourmand
- **Stars**：0
- **语言**：Dockerfile
- **License**：NOASSERTION
- **Topics**：—
- **GitHub 描述**：Pre-built container image for gourmand AI-slop detector
- **本地描述**：Pre-built container image for gourmand AI-slop detector
- **拉取时间**：2026-07-25 18:04:02

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# gourmand container

Pre-built container image for [gourmand](https://codeberg.org/mattdm/gourmand), an AI-slop detector for codebases. Saves ~5 minutes of Rust compilation per CI run.

## Pull

```bash
podman pull quay.io/crunchtools/gourmand
```

## Usage

### Local

```bash
podman run --rm -v .:/workspace:Z quay.io/crunchtools/gourmand --full /workspace
```

### GitLab CI

```yaml
gourmand:
  stage: test
  image: quay.io/crunchtools/gourmand
  script:
    - gourmand --full .
```

### GitHub Actions

```yaml
- name: Run gourmand
  run: |
    docker run --rm -v ${{ github.workspace }}:/workspace quay.io/crunchtools/gourmand --full /workspace
```

## License

Container build infrastructure is AGPL-3.0-or-later. Gourmand itself is licensed under its upstream terms.
