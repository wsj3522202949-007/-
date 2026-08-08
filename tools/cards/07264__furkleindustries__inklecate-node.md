---
id: tool-07264
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 本地写作]
title: inklecate-node
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/furkleindustries/inklecate-node
created: 2026-07-18
updated: 2026-07-18
no: 7264
category: 画龙补充 / 扩容入库 — 补充源
repo: furkleindustries/inklecate-node
stars: 6
url: https://github.com/furkleindustries/inklecate-node
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 9dadd12a7e5d37e1
  - methods/QUICK_START.md
---

# furkleindustries/inklecate-node

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/furkleindustries/inklecate-node
- **Stars**：6
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：A tiny wrapper around the desktop executables for ink's command-line Ink language compiler.
- **本地描述**：inklecate-node
- **拉取时间**：2026-07-25 19:15:59

related:
  - methods/QUICK_START.md
---

# inklecate

Install with `npm i -D inklecate`.

This package is a thin wrapper around [Inkle](https://inkle.com)'s [inklecate](https://github.com/inkle/ink/blob/master/inklecate/) tool for compiling and playing [Ink](https://github.com/inkle/ink) stories. It will not compile for client-side execution in a browser.

The inklecate binaries were written solely by Inkle and this package is released under the same license as Ink. That license is MIT at the time of this writing, but if it changes, the license of this package should be considered to follow it.

## How to use

The `inklecate` package can be used either as the `inklecate` export of the module and as a command-line app.

CLI options:

```
  inklecate <options> ...<ink file(s)>

  -o, --outputFile <outputFile>: Output file name.
  -c: Count all visits to knots, stitches and weave points, not just those referenced by TURNS_SINCE and read counts.
  --verbose: Verbose mode - print compilation timings.
  --DEBUG: Enable debug logging for inklecate-node.
```

The arguments for the module's `inklecate` function:

```js
function inklecate(args: {
  countAllVisits?: boolean;
  outputFilepath?: string;
  inputFilepath?: string;
}): Promise<InklecateReturn>;
```

The single positional argument is the input filepath.

If the output filepath argument is not provided, the file will be generated in a cache location and output as plain text JSON (in CLI mode) or a plain JavaScript object (as a node module).

## Other notes

* How do I use this with Webpack?
  Try [inklecate-loader](https://github.com/furkleindustries/inklecate-loader)
