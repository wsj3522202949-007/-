---
id: tool-00336
type: tool
area: 库
status: active
tags: [校对, Python, 协议未明, 本地优先, 英文文档, 改稿润色, 本地写作]
title: PortoWrite
summary: 错别字/语法/风格校对
source: https://github.com/william10025/portowrite
created: 2026-07-18
updated: 2026-07-18
no: 336
category: 二、网文 / 长篇 AI 写作系统 库
repo: William10025/PortoWrite
stars: 0
url: https://github.com/william10025/portowrite
tier: "C"
use_case: "错别字/语法/风格校对"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# William10025/PortoWrite

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/william10025/portowrite
- **Stars**：0
- **语言**：Python
- **License**：NOASSERTION
- **Topics**：—
- **GitHub 描述**： PortoWrite is a distraction-free novel writing app for Windows, built with Python and PySide6. Features a WYSIWYG editor with named paragraph styles, chapter sidebar, EPUB/DOCX/Markdown export, spell check, find & replace, autosave with crash recovery, and Kindle/Kobo/Apple Books export profiles.
- **本地描述**：PortoWrite is a distraction-free novel writing app for Windows, built with Python and PySide6. Features a WYSIWYG editor with named paragraph styles, chapter sidebar, EPUB/DOCX/Markdown export, spell check, find & replace, autosave with crash recovery, and Kindle/Kobo/Apple Books export profiles.
- **拉取时间**：2026-07-23 22:48:53

---

# PortoWrite

A professional WYSIWYG ebook editor for Windows designed to streamline the novel writing and publishing workflow. Create, edit, and export books to EPUB, Markdown, and DOCX formats with sophisticated styling, metadata management, and Kindle preview.

![Version](https://img.shields.io/badge/version-0.3.0--beta-blue)
![License](https://img.shields.io/badge/license-Proprietary-red)
![Platform](https://img.shields.io/badge/platform-Windows%2010%2B-blue)

> **Beta Release** — All features are available to all users during the beta. See [TIERS.md](TIERS.md) for the Free / Pro-Donation / Commercial licensing model.

## Features

### Core Writing
- **WYSIWYG Editor** — What you see is what you get. Style text as you write with 6 built-in styles plus custom style support
- **Multi-Format Export** — Save as EPUB (for e-readers), Markdown (for Git/blogging), or DOCX (for Word)
- **Chapter Organization** — Organize your novel into chapters with automatic numbering and hierarchy
- **Style System** — ChapterHeader, SubHeader, Body, BlockQuote, and more. Create custom styles with full control over font, size, color, alignment, spacing

### Kindle & Publishing
- **Kindle-Safe CSS** — Bookerly font fallback, justified text, hyphens, relative em units for perfect e-reader rendering
- **Scene Breaks** — Insert ⚬ ⚬ ⚬ visual breaks (Ctrl+Shift+Enter); exports as `<hr class="SceneBreak">`
- **Drop Caps** — Right-click any Body paragraph to toggle a decorative first-letter drop cap
- **Auto-Indent** — First paragraph after a heading or scene break has no indent automatically
- **Find & Replace** — Global search across all chapters with regex, case-sensitive, and whole-word support (Ctrl+F / Ctrl+H)

### Quality & Publishing
- **EPUB Validation** — Automatic EPUBCheck validation on export with detailed error/warning reporting
- **Metadata Management** — ISBN, publisher, series information, keywords, contributors with Dublin Core OPF mapping
- **Table of Contents** — Auto-generate from chapter titles and headings, manually edit for publication
- **Spell Checker** — Real-time spell checking with user dictionary support

### Professional Preview
- **Kindle Device Simulation** — Preview your novel in Kindle Paperwhite, Sepia, Night, and other themes
- **Live Preview** — See changes in real-time as you write (Ctrl+P to toggle)
- **Reader Experience** — Exactly how your book appears on Kindle devices

### Project Management
- **Save & Backup** — Automatic versioned backups with configurable retention
- **Project Organization** — All project files, drafts, and exports in one folder
- **Settings Persistence** — Your preferences saved across sessions

## Quick Start

### Installation

#### Option 1: Download Executable (Easiest)
1. Download `PortoWrite-v0.3.0-beta-windows.zip` from [Releases](https://github.com/yourusername/portowrite/releases)
2. Extract the ZIP file
3. Run `PortoWrite.exe`
4. ✨ Start writing!

**System Requirements:**
- Windows 10 or later
- 2 GB RAM (4+ recommended)
- 500 MB free disk space

#### Option 2: Run from Source
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/portowrite.git
   cd portowrite
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

### First Project

1. **Create Project** — Click "New Project" and name your novel
2. **Add Chapters** — Use "Add Chapter" to create structure
3. **Write Content** — Click chapters to edit, use styles panel to format
4. **Export** — File → Export as EPUB/Markdown/DOCX

## Usage Guide

### Writing & Styling
- **Apply Style** — Select text and choose style from Style Panel
- **Custom Styles** — Right-click Style Panel → Create Custom Style
- **Paragraph Formatting** — Use alignment and spacing controls
- **Font Selection** — Styles support Georgia, Arial, Times New Roman, etc.

### Managing Your Book
- **Chapter Titles** — Appear as ChapterHeader style, used for TOC
- **Headings** — SubHeader and Heading3-6 styles appear in TOC
- **Metadata** — Project → Edit Metadata to add ISBN, publisher, keywords, contributors
- **Table of Contents** — Project → Edit TOC to customize which entries appear

### Quality Checks
- **Spell Check** — Underlined misspelled words; right-click for suggestions
- **EPUB Validation** — Export automatically validates; review errors/warnings
- **Preview** — Ctrl+P to see Kindle rendering; check formatting on actual device theme

### Projects & Backups
- **Automatic Backups** — Every save creates a backup (Settings → Configure)
- **Restore Backup** — File → Restore Backup to recover previous versions
- **Project Files** — All located in `%USERPROFILE%/Documents/PortoWrite Projects/`

## Architecture

```
portowrite/
├── document.py          # Core document model (chapters, blocks, metadata)
├── styles.py            # Style definitions and registry
├── toc.py              # Table of contents generation
├── epub_io.py          # EPUB export with validation
├── md_io.py            # Markdown export
├── docx_io.py          # Word document export
├── epub_validator.py   # EPUB validation
├── project.py          # Project save/load with backups
├── spell.py            # Spell checker integration
└── ui/
    ├── main_window.py       # Main application window
    ├── editor_widget.py     # WYSIWYG text editor
    ├── chapter_sidebar.py   # Chapter navigation
    ├── style_panel.py       # Style selection/management
    ├── toolbar.py           # Formatting toolbar
    ├── kindle_preview.py    # Device preview widget
    └── dialogs.py          # Metadata, TOC, validation dialogs
```

## Development

### Setting Up Dev Environment

```bash
# Clone and setup
git clone https://github.com/yourusername/portowrite.git
cd portowrite
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-build.txt  # For building exe

# Run tests
python porto_write/self_test.py

# Run application
python main.py

# Build executable
pyinstaller portowrite.spec
```

### Project Status

Current version: **0.1.0 (Alpha)** | Next: **0.2.0 (Phase 1+2)**

**v0.1.0 — Completed Features:**
- ✅ WYSIWYG editor with style system
- ✅ EPUB, Markdown, DOCX export
- ✅ EPUB validation
- ✅ Metadata management with Dublin Core mapping
- ✅ Table of Contents with heading extraction
- ✅ Kindle preview simulation (3 themes)
- ✅ Spell checker
- ✅ Project backup system

**v0.2.0 — In Progress (Phase 1+2 UX Improvements):**
- 🔄 Display Font Override — render display fonts without changing Kindle export
- 🔄 Heading1/Heading2 Styles — new built-in styles (aliases for chapter/subheader)
- 🔄 Right-Click Context Menus — edit/duplicate/delete styles from style panel
- 🔄 Per-Paragraph Formatting — adjust spacing for selected paragraphs via right-click
- 🔄 Cursor Position Restore — remember last edit position per project
- 🔄 Status Bar Enhancements — word count with commas, last modified time, session timer
- 🔄 Active Typing Timer — track writing time with 5-minute idle detection
- 🔄 Font Toggle — View menu to switch between display and Kindle fonts
- 🔄 Emergency Backup Toggle — forced backup on close even if user declines save

**v0.3.0 — Planned (Phase 3 Kindle-Native Features):**
- 📋 Scene Breaks UI — visual break markers with auto-conversion to `<hr>`
- 📋 Drop Caps — per-paragraph decorative first-letter enlargement
- 📋 Kindle-Safe CSS — optimized export with relative units and `@media amzn-kf8`
- 📋 Auto-Indent Logic — zero indent after headings and scene breaks (automatic)
- 📋 Hyphens Support — enable soft-hyphenation in EPUB export
- 📋 Platform Optimization — Kobo and Apple Books export profiles

**v0.4+ — Future (Phase 4 Advanced Features):**
- 📋 Footnotes/Endnotes — linked footnotes with auto-numbering and backlinks
- 📋 Hyperlinks — create internal (TOC) and external URL links with UI
- 📋 Find & Replace — global search across all chapters with regex support
- 📋 Track Changes — change tracking and review mode

See [EPICS.md](EPICS.md) for detailed feature breakdown and [agent.md](agent.md) for development guidelines.

## Testing

Run self-tests:
```bash
python main.py --self-test
```

Or directly:
```bash
python porto_write/self_test.py
```

Current test status: **11/11 core tests passing**

## Building for Distribution

See [BUILD_EXE.md](BUILD_EXE.md) for detailed build instructions.

Quick build:
```bash
pip install -r requirements-build.txt
pyinstaller portowrite.spec
# Executable in dist/PortoWrite.exe
```

Distribution strategy in [DISTRIBUTION.md](DISTRIBUTION.md)

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl+N | New Project |
| Ctrl+O | Open Project |
| Ctrl+S | Save Project |
| Ctrl+E | Export |
| Ctrl+P | Toggle Preview |
| Ctrl+, | Settings |
| F7 | Spell Check |

## File Formats

### EPUB
- Standard ebook format
- Works on Kindle, Kobo, Apple Books, Google Play Books
- Includes validated OPF metadata, NCX navigation, proper styling

### Markdown
- Plain text with Markdown formatting
- Great for version control (Git friendly)
- Can be converted to other formats with Pandoc

### DOCX
- Microsoft Word format
- Easy to share with editors
- Maintains styles and formatting

## System Requirements

**Minimum:**
- Windows 10 (build 14393 or later)
- Python 3.10+ (if running from source)
- 2 GB RAM
- 500 MB disk space

**Recommended:**
- Windows 11
- Python 3.11+
- 4+ GB RAM
- SSD with 1+ GB space
- 1920x1080 resolution or higher

## Troubleshooting

### Application won't start
- Ensure Windows is up to date (Windows Update)
- Reinstall Visual C++ Redistributables from Microsoft
- Check antivirus isn't blocking execution

### "Module not found" errors (if running from source)
```bash
pip install -r requirements.txt
```

### EPUB validation errors
- Check all chapter titles are filled
- Ensure no empty chapters
- See EPUB validation dialog for specific errors

### Spell checker not working
- Check dictionary files are accessible
- Try reinstalling: `pip install spylls --force-reinstall`
- Check file permissions in PortoWrite data folder

## Support

### Getting Help
- **Docs:** [README.md](README.md) and [BUILD_EXE.md](BUILD_EXE.md)
- **Issues:** [GitHub Issues](https://github.com/yourusername/portowrite/issues)
- **Email:** support@portowrite.com (if applicable)

### Reporting Bugs
1. Check existing issues first
2. Include PortoWrite version (Help → About)
3. Steps to reproduce
4. Expected vs actual behavior
5. Attach problematic project file (if possible)

### Feature Requests
- [GitHub Discussions](https://github.com/yourusername/portowrite/discussions)
- Describe use case and why it's important
- Examples of other tools with similar features welcome

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

See [agent.md](agent.md) for development guidelines.

## License

PortoWrite is released under the MIT License. See [LICENSE](LICENSE) for details.

You are free to:
- ✅ Use for any purpose (personal, commercial)
- ✅ Modify and extend
- ✅ Distribute (with attribution)

## Credits

Built with:
- [PySide6](https://wiki.qt.io/Qt_for_Python) — Qt6 Python bindings
- [ebooklib](https://github.com/aerkalov/ebooklib) — EPUB handling
- [mistune](https://mistune.lepture.com/) — Markdown parsing
- [python-docx](https://python-docx.readthedocs.io/) — DOCX generation
- [spylls](https://github.com/Kijewski/spylls) — Spell checking

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and release notes.

## Project Vision

PortoWrite aims to be the best choice for indie authors:
- **Simple** — Easy to learn, no steep learning curve
- **Powerful** — All the features you need for professional publishing
- **Reliable** — Stable, well-tested, automatic backups
- **Free & Open** — No subscription, transparent development

We believe authors should focus on writing, not fighting their tools.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

**Latest Release:** [v0.1.0](https://github.com/yourusername/portowrite/releases/tag/v0.1.0)

**Get Started:** [Download Now](https://github.com/yourusername/portowrite/releases) or [Run from Source](https://github.com/yourusername/portowrite#installation)
