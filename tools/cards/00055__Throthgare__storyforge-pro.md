---
id: tool-00055
type: tool
area: 库
status: active
tags: [Rust, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: storyforge-pro
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/throthgare/storyforge-pro
created: 2026-07-18
updated: 2026-07-18
no: 55
category: 二、网文 / 长篇 AI 写作系统 库
repo: Throthgare/storyforge-pro
stars: 0
url: https://github.com/throthgare/storyforge-pro
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# Throthgare/storyforge-pro

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/throthgare/storyforge-pro
- **Stars**：0
- **语言**：Rust
- **License**：None
- **Topics**：—
- **GitHub 描述**：StoryForge Pro is a comprehensive, multi-platform story writing application that combines visual planning with powerful writing tools. This Rust edition provides a modern, memory-safe implementation built with EGUI framework, offering exceptional performance and cross-platform compatibility.
- **本地描述**：StoryForge Pro is a comprehensive, multi-platform story writing application that combines visual planning with powerful writing tools. This Rust edition provides a modern, memory-safe implementation built with EGUI framework, offering exceptional performance and cross-platform compatibility.
- **拉取时间**：2026-07-23 22:40:28

---

# StoryForge Pro - Rust Edition

## Overview

StoryForge Pro is a comprehensive, multi-platform story writing application that combines visual planning with powerful writing tools. This Rust edition provides a modern, memory-safe implementation built with EGUI framework, offering exceptional performance and cross-platform compatibility.

## Features

### Core Functionality
- **Visual Planning**: Advanced node system with 6 node types (Plot Points, Characters, Locations, Themes, Conflicts, Resolutions)
- **Rich Text Editor**: Full-featured writing environment with formatting, HTML/Markdown conversion
- **Research Management**: Complete organization system for characters, locations, items, concepts, and notes
- **Version Control**: Snapshots and auto-save with restore capabilities
- **Export Capabilities**: Multiple professional export formats (Markdown, HTML, CSV, PDF, DOCX)

### Advanced Features
- **Spell Checking**: Real-time spell checking with suggestions and user dictionary
- **Writing Modes**: Typewriter mode, Distraction-free mode, Hemingway mode for complex sentence analysis
- **Find & Replace**: Advanced search with regex support and search history
- **Templates**: Story templates including Three-Act Structure, Hero's Journey, Save the Cat
- **Layout Algorithms**: Tree, Circular, Grid, Spiral, and Force-Directed positioning
- **Connection Styles**: Straight, curved, dashed, dotted, and animated connections

### UI/UX
- **Modern Interface**: Clean, intuitive interface with customizable themes
- **Touch Optimization**: Full support for touch and tablet devices
- **Keyboard Shortcuts**: Comprehensive shortcut system with customization
- **Responsive Design**: Adapts to different screen sizes and devices
- **Accessibility**: High contrast themes, keyboard navigation, screen reader support

## Installation

### Prerequisites
- Rust 1.70 or later
- Cargo package manager

### Build from Source

```bash
# Clone the repository
git clone https://github.com/storyforge/storyforge.git
cd storyforge/rust

# Build the project
cargo build --release

# Run the application
cargo run --release
```

### Development Build

```bash
# Build with debug symbols
cargo build

# Run tests
cargo test

# Run with logging
RUST_LOG=debug cargo run
```

## Project Structure

```
storyforge_rust/
├── src/
│   ├── main.rs                 # Application entry point
│   ├── app.rs                  # Main application struct
│   ├── project.rs              # Project management
│   ├── chapter.rs              # Chapter and node definitions
│   ├── rich_text.rs            # Rich text editing
│   ├── spellcheck.rs           # Spell checking system
│   ├── daily_stats.rs          # Writing statistics
│   ├── snapshot.rs             # Version history
│   ├── presentation.rs         # Presentation mode
│   ├── research.rs             # Research management
│   ├── undo_redo.rs            # Undo/redo system
│   ├── templates.rs            # Story templates
│   ├── layouts.rs              # Layout algorithms
│   ├── connections.rs          # Node connections
│   ├── comments.rs             # Comment system
│   ├── writing_modes.rs        # Writing modes
│   ├── find_replace.rs         # Find and replace
│   ├── autosave.rs             # Auto-save system
│   ├── toolbar.rs              # UI toolbar
│   ├── sidebar.rs              # Chapter sidebar
│   ├── settings.rs             # Application settings
│   ├── keyboard_shortcuts.rs   # Keyboard shortcuts
│   ├── touch_optimizations.rs  # Touch support
│   ├── theme.rs                # Theme system
│   ├── status_bar.rs           # Status bar
│   ├── main_menu.rs            # Main menu
│   ├── about_dialog.rs         # About dialog
│   └── tests.rs                # Test suite
├── Cargo.toml                  # Project dependencies
└── README.md                   # This file
```

## Usage

### Creating a New Project

1. Launch StoryForge Pro
2. Click "New Project" in the toolbar or File menu
3. Enter project title and settings
4. Choose a template or start from scratch

### Writing Workflow

1. **Plot View**: Plan your story using visual nodes
2. **Writing View**: Write chapters with rich text editor
3. **Research View**: Organize characters, locations, and notes
4. Switch between views using the sidebar or keyboard shortcuts

### Using Templates

1. Go to File > New from Template
2. Select a template (Three-Act Structure, Hero's Journey, etc.)
3. Customize the template for your story
4. Save as your project

### Exporting

1. Go to File > Export
2. Choose export format (Markdown, HTML, PDF, etc.)
3. Configure export options
4. Save the exported file

## Configuration

### Application Settings

Access settings via Tools > Preferences or keyboard shortcut Ctrl+,

**General Settings:**
- Auto-save interval
- Backup creation
- File paths

**Editor Settings:**
- Font size and family
- Line and paragraph spacing
- Word wrap and line numbers

**Writing Modes:**
- Typewriter scrolling
- Distraction-free mode
- Hemingway mode threshold

**Spell Checking:**
- Enable/disable spell check
- Language selection
- Auto-correction

**Appearance:**
- Theme selection (Light, Dark, High Contrast, Sepia)
- Custom colors
- UI scale

### Keyboard Shortcuts

Press `Ctrl+?` to view all keyboard shortcuts. Common shortcuts include:

- `Ctrl+N`: New Project
- `Ctrl+O`: Open Project
- `Ctrl+S`: Save Project
- `Ctrl+Z`: Undo
- `Ctrl+Y`: Redo
- `Ctrl+F`: Find
- `Ctrl+H`: Replace
- `Ctrl+B`: Bold
- `Ctrl+I`: Italic

## Development

### Running Tests

```bash
# Run all tests
cargo test

# Run specific test module
cargo test test_project_creation

# Run with output
cargo test -- --nocapture

# Run tests in parallel
cargo test -- --test-threads=4
```

### Building Documentation

```bash
# Generate documentation
cargo doc --open

# Generate documentation for dependencies
cargo doc --open --document-private-items
```

### Code Style

This project follows Rust naming conventions:
- Functions and variables: `snake_case`
- Types and structs: `PascalCase`
- Constants: `SCREAMING_SNAKE_CASE`

### Adding New Features

1. Create a new module in `src/`
2. Add module declaration in `main.rs`
3. Implement the feature with proper error handling
4. Add tests in `tests.rs`
5. Update documentation
6. Submit a pull request

## Performance

The Rust edition is optimized for:
- **Memory Safety**: Rust's ownership system prevents memory leaks and data races
- **Speed**: Efficient algorithms and data structures
- **Scalability**: Handles large projects with 300+ nodes
- **Responsiveness**: Lazy loading and on-demand rendering

## Cross-Platform Support

StoryForge Pro Rust edition supports:
- **Windows**: Windows 10 and later
- **macOS**: macOS 10.15 (Catalina) and later
- **Linux**: Most major distributions

## Contributing

We welcome contributions! Please see our contributing guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Authors and Contributors

**The Aetherial Team**
- Contact: realmselection@gmail.com

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- EGUI framework for the excellent GUI toolkit
- The Rust community for helpful libraries and tools
- All contributors who have helped improve StoryForge Pro

## Roadmap

### Planned Features
- [ ] Cloud synchronization
- [ ] Collaborative editing
- [ ] Mobile apps (iOS, Android)
- [ ] AI-powered writing assistance
- [ ] Advanced analytics and insights
- [ ] Plugin system for extensions

### Version 3.1
- Enhanced touch gestures
- Improved accessibility features
- Performance optimizations
- Bug fixes and stability improvements

## Support

For support, please contact:
- Email: realmselection@gmail.com
- GitHub Issues: https://github.com/storyforge/storyforge/issues
- Documentation: https://docs.storyforge.pro

## Changelog

### Version 3.0.0 (Rust Edition)
- Complete rewrite in Rust
- Modern EGUI-based interface
- Enhanced performance and memory safety
- Comprehensive testing suite
- Touch and tablet optimizations
- Advanced theme system
- Full keyboard shortcut customization

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

Made with ❤️ by The Aetherial Team
