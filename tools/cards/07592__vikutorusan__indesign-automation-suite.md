---
id: tool-07592
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 本地写作]
title: indesign-automation-suite
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/vikutorusan/indesign-automation-suite
created: 2026-07-18
updated: 2026-07-18
no: 7592
category: 画龙补充 / 扩容入库 — 补充源
repo: vikutorusan/indesign-automation-suite
stars: 0
url: https://github.com/vikutorusan/indesign-automation-suite
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# vikutorusan/indesign-automation-suite

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/vikutorusan/indesign-automation-suite
- **Stars**：0
- **语言**：None
- **License**：NOASSERTION
- **Topics**：—
- **GitHub 描述**：Professional editorial automation scripts for Adobe InDesign
- **本地描述**：indesign-automation-suite
- **拉取时间**：2026-07-25 19:26:38

related:
  - methods/QUICK_START.md
---

# InDesign Automation Suite

A collection of 21 automation scripts for Adobe InDesign, focusing on bilingual publishing and editorial workflows.

## Overview

This suite automates common InDesign tasks that are typically time-consuming when done manually. The scripts are organized into six categories based on functionality.

## Categories

### Bilingual (3 scripts)
- `create_bilingual_book_complete.jsx` - Creates bilingual books with facing pages and linked text frames
- `fix_bilingual_text_flow.jsx` - Fixes text overflow issues between languages
- `bilingual_precision_layout.jsx` - Precise positioning version with coordinate logging

### Footnotes (3 scripts)
- `migrate_footnotes_between_docs.jsx` - Transfers footnotes between documents
- `convert_brackets_to_footnotes.jsx` - Converts [1], [2] style references to actual footnotes
- `apply_footnote_marker_styles.jsx` - Applies styles only to footnote markers in main text

### Pages (2 scripts)
- `apply_master_by_content.jsx` - Applies master pages based on page content
- `apply_master_by_chapter.jsx` - Specialized version for chapter pages

### Text Processing (5 scripts)
- `auto_apply_entry_style.jsx` - Automatically applies "Entry" style after titles
- `prevent_orphan_subtitles.jsx` - Prevents orphaned subtitles using keepWithNext
- `clean_empty_paragraphs.jsx` - Removes empty paragraphs around titles
- `adjust_title_spacing.jsx` - Adjusts title spacing automatically
- `adjust_title_spacing_v2.jsx` - Alternative version with different settings

### Import-Conversion (3 scripts)
- `import_markdown_auto.jsx` - Imports Markdown files using Pandoc
- `convert_heading1_to_chapter.jsx` - Converts Word heading styles to editorial styles
- `convert_normal_to_body.jsx` - Standardizes basic paragraph styles

### Utilities (5 scripts)
- `update_index_references.jsx` - Updates page numbers in index automatically
- `delete_frames_selective.jsx` - GUI for selective frame deletion
- `reset_frame_spacing.jsx` - Resets frame spacing to default values
- `format_chapters_gui.jsx` - Chapter formatting with native InDesign interface
- `debug_advanced.jsx` - Debugging and diagnostic tools

## Installation

1. Copy the scripts to your InDesign Scripts Panel folder
2. Access via Window > Utilities > Scripts
3. Run scripts as needed

## Compatibility

- InDesign CS6 through 2025
- Windows and macOS

## Usage Notes

- Scripts include error handling and user prompts
- Some scripts require specific document structure
- Test on sample documents before production use

## License

Scripts are available for commercial use under license. Contact for pricing and terms.
