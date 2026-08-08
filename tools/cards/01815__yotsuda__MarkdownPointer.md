---
id: tool-01815
type: tool
area: 库
status: active
tags: [校对, C#, 协议宽松, 本地优先, 英文文档, 改稿润色, 本地写作]
title: MarkdownPointer
summary: 错别字/语法/风格校对
source: https://github.com/yotsuda/markdownpointer
created: 2026-07-18
updated: 2026-07-18
no: 1815
category: 二、网文 / 长篇 AI 写作系统 库
repo: yotsuda/MarkdownPointer
stars: 1
url: https://github.com/yotsuda/markdownpointer
tier: "B"
use_case: "错别字/语法/风格校对"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: d5fc55cb7b560db2
  - methods/最强写作方法论_全球最强综合版.md
---

# yotsuda/MarkdownPointer

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/yotsuda/markdownpointer
- **Stars**：1
- **语言**：C#
- **License**：MIT
- **Topics**：ai, ai-agent, claude, copilot, developer-tools, markdown, markdown-viewer, mcp, vscode
- **GitHub 描述**：Vibe writing for Markdown. Point at anything, tell AI to fix it.  MarkdownPointer renders your Markdown and lets you click any element - headings, code blocks, table cells, Mermaid diagram nodes, KaTeX math - to copy a filepath:line reference. Paste it into your AI prompt, and the AI knows exactly where to look.
- **本地描述**：Vibe writing for Markdown. Point at anything, tell AI to fix it.  MarkdownPointer renders your Markdown and lets you click any element - headings, code blocks, table cells, Mermaid diagram nodes, KaTeX math - to copy a filepath:line reference. Paste it into your AI prompt, and the AI knows exactly where to look.
- **拉取时间**：2026-07-23 23:31:58

---

# MarkdownPointer

**Vibe writing for Markdown.** Point at anything, tell AI to fix it.

MarkdownPointer renders your Markdown and lets you click any element - headings, code blocks, table cells, Mermaid diagram nodes, KaTeX math - to copy a `filepath:line` reference. Paste it into your AI prompt, and the AI knows exactly where to look.

<div align="center">
  <img width="640" alt="social-image" src="https://github.com/user-attachments/assets/cdae3548-1e23-4639-9b38-3e03c5c2a337" />
</div>

**To change a node's color:**

<p align="center">
  <img width="40%" valign="middle" alt="Image" src="https://github.com/user-attachments/assets/af06577f-4f7c-40cd-b76e-e3426fd36699" />
  &nbsp;&nbsp;&nbsp;
  <img width="8%" valign="middle" alt="Image" src="https://github.com/user-attachments/assets/16b7d1ab-3799-421a-8d21-9ecdbc1ae66c" />
  &nbsp;&nbsp;&nbsp;
  <img width="40%" valign="middle" alt="Image" src="https://github.com/user-attachments/assets/daea5945-af62-47f7-8f02-a0206611d8e7" />
</p>

**Click the node, paste the reference into your prompt, and ask the AI — done.**

```
Color this node orange [c:\docs\architecture.md:6] mermaid node: mdp.exe
```

**More prompt examples:**
- Verify this section for technical accuracy [ref]
- Swap these two sections [ref] [ref]
- Delete this [ref]
- Simplify this paragraph [ref]
- Add a code example after this section [ref]
- Fix the grammar here [ref]
- Translate this section to Japanese [ref]

## Features

| Feature | Description |
|---------|-------------|
| Point & Prompt | Click any rendered element to copy `filepath:line` to clipboard |
| Mermaid Diagrams | Flowchart, Sequence, Class, State, ER, Gantt, Pie, Git graph, Mindmap |
| KaTeX Math | Inline `$...$` and block `$$...$$` |
| SVG | Embedded font support |
| Recent Files | Quick access with pin support |
| Tab Dock/Undock | Drag tabs between windows or detach to a new window |
| Always on Top | Pin the window above other apps for reference |
| Live Reload | Auto-refresh on file changes |
| Export | `.pptx` (built-in Open XML), `.docx` (via Pandoc). Mermaid/SVG rendered as images |
| MCP Server | Let AI open, navigate, export documents, and generate/import PPTX |

## Install
In a [PowerShell 7](https://learn.microsoft.com/powershell/scripting/install/install-powershell-on-windows) console:
```powershell
Install-Module MarkdownPointer
```

## Quick Start

```powershell
mdp .\README.md    # Open a file
mdp .\docs\*.md    # Open multiple files
mdp                # Just launch the viewer
```

## MCP Server Setup

Connect MarkdownPointer to Claude so your AI can open and navigate documents directly.

Run these in PowerShell 7:

```powershell
Register-MdpToClaudeCode       # Claude Code
Register-MdpToClaudeDesktop    # Claude Desktop
```

> **Other MCP clients:** Add the output of `Get-MarkdownPointerMCPPath -Escape` as the command in your MCP client's configuration file.

> **Troubleshooting:** If the MCP client fails to connect to the server, [.NET 10 Desktop Runtime](https://dotnet.microsoft.com/download/dotnet/10.0) may not be installed. .NET 10 is not included with Windows — install it and try again.

Then just ask Claude:

- "open README.md in mdp"
- "show the report in mdp and scroll to line 50"
- "export report.md to docx"
- "export slides.md to pptx"
- "import presentation.pptx to markdown"
- "show me slide 3 of slides.md"

### MCP Tools

| Tool | Description |
|------|-------------|
| `show_markdown` | Open files and scroll to a line |
| `get_status` | Get current window/tab state |
| `slide_control` | Navigate reveal.js slides |
| `get_slide_info` | Get slide shapes and content as text |
| `get_slide_image` | Get a slide as PNG image (requires PowerPoint) |
| `export_document` | Export to .pptx (built-in) or .docx (Pandoc) |
| `import_document` | Import .docx/.pptx to Markdown + extract images |
| `tag_asset` | Tag imported files and images in index.json |

## Keyboard Shortcuts

| Shortcut | Action |
|----------|-----related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---|
| `Ctrl+O` | Open file |
| `Ctrl+F` | Find in page |
| `Ctrl+G` | Go to line |
| `Ctrl+P` | Print |
| `Ctrl+W` / `Ctrl+F4` | Close tab |
| `Ctrl+Tab` / `Ctrl+Shift+Tab` | Switch tabs |
| `Mouse Wheel` | Scroll |
| `Ctrl+Mouse Wheel` | Zoom |
| `F5` | Reload |

## Requirements

- Windows 10/11
- [PowerShell 7.4+](https://learn.microsoft.com/powershell/scripting/install/install-powershell-on-windows)
- [.NET 10 Desktop Runtime](https://dotnet.microsoft.com/download/dotnet/10.0)

<details>
<summary>Build from Source</summary>

```powershell
git clone https://github.com/yotsuda/MarkdownPointer.git
cd MarkdownPointer
.\Build-Deploy.ps1
```

</details>

## License

MIT
