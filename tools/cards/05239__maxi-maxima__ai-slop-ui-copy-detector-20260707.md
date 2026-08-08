---
id: tool-05239
type: tool
area: 库
status: active
tags: [TTS, Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: ai-slop-ui-copy-detector-20260707
summary: 小说转语音/有声书
source: https://github.com/maxi-maxima/ai-slop-ui-copy-detector-20260707
created: 2026-07-18
updated: 2026-07-18
no: 5239
category: 一、去 AI 味 / Humanizer 库
repo: maxi-maxima/ai-slop-ui-copy-detector-20260707
stars: 0
url: https://github.com/maxi-maxima/ai-slop-ui-copy-detector-20260707
tier: "C"
use_case: "小说转语音/有声书"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/最强去AI味铁律.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: c6e1f8da9dafea5d
  - methods/改稿润色指令库.md
---

# maxi-maxima/ai-slop-ui-copy-detector-20260707

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/maxi-maxima/ai-slop-ui-copy-detector-20260707
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：maxi-maxima/ai-slop-ui-copy-detector-20260707
- **拉取时间**：2026-07-25 18:11:13

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

# AI Slop UI Copy Detector

AI-generated apps often ship with bland marketing and UI copy that makes products look interchangeable.

## Why now

Developer communities are explicitly reacting against AI slop in generated UI; copy linting is a small, shareable quality gate.

## Features

- Flags common generic AI-marketing phrases.
- Suggests replacing vague claims with specific outcomes.
- Can fail CI with `--max-findings`.

## Install / Run

No external dependencies. Python 3.11+ is enough.

```bash
python src/ai_slop_ui_copy_detector_20260707.py --help
python src/ai_slop_ui_copy_detector_20260707.py examples/input.txt
```

## Example

Input (`examples/input.txt`):

```text
Unlock your potential with our seamless experience.
Export invoices in CSV.
A cutting-edge all-in-one platform for teams.
```

Command:

```bash
python src/ai_slop_ui_copy_detector_20260707.py examples/input.txt
```

Output excerpt:

```text
line 1: seamless experience, unlock your potential -> [specific user outcome] with our [specific user outcome].
summary: 2 generic-copy findings
```

## Self check

```bash
python tests/self_check.py
```

## Roadmap

- Add JSON and SARIF output.
- Add GitHub Actions workflow examples.
- Add richer rules learned from real open-source repositories.
- Publish packaged binaries for common platforms.

## License

MIT
