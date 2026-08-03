---
id: tool-07596
type: tool
area: 库
status: active
tags: [Claude插件, Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: claude-banana-story-agent
summary: Claude Code 插件式写作流
source: https://github.com/vtrivedy/claude-banana-story-agent
created: 2026-07-18
updated: 2026-07-18
no: 7596
category: 画龙补充 / 扩容入库 — 补充源
repo: vtrivedy/claude-banana-story-agent
stars: 27
url: https://github.com/vtrivedy/claude-banana-story-agent
tier: "B"
use_case: "Claude Code 插件式写作流"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# vtrivedy/claude-banana-story-agent

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/vtrivedy/claude-banana-story-agent
- **Stars**：27
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：🍌 Autonomous story agent creating illustrated storybooks with Claude Code SDK
- **本地描述**：claude-banana-story-agent
- **拉取时间**：2026-07-25 19:26:45

---

# Claude's Bananas Story Agent 🍌

An autonomous story agent that turns any idea into illustrated stories. Real multi-image consistency.


https://github.com/user-attachments/assets/2a6761a2-9535-48e7-b854-d0a6b2246d30


## What It Actually Does

- Feed it any topic → get a complete illustrated story
- The agent figures out characters, scenes, and style on its own  
- Every character looks the same across all pages (using Nano-Banana's multi-ref magic)
- Watch the agent think, plan, and call tools in real-time
- Outputs ready-to-read PDF + all the source files
- **Beautiful web interface** for creating and viewing stories

## How It Works

Topic → Claude SDK agent reads custom prompt → orchestrates MCP tools → Nano-Banana generates images → local files + PDF

The agent handles everything. You watch it work (or just wait for your story).

## Two Ways to Use

### 🖥️ Beautiful Web Interface (Recommended for Demos)
```bash
# Terminal 1: Start the gorgeous frontend
cd frontend
python app_simple.py
# Opens browser at http://localhost:8080

# Click "Create My Storybook", enter your idea, and watch the magic happen!
# Stories appear in the gallery with page-flip animation
```

### ⚡ Pure Terminal (Fastest)
```bash
# Just run directly
python create_story.py "detective cat solves art heist"
```

## Quick Start

```bash
# Get uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone and setup
git clone <repo>
cd cc-sdk-storybook
uv venv && source .venv/bin/activate
uv pip install -r requirements.txt

# Add your FAL key
cp .env.example .env
# Edit .env - add FAL_KEY from https://fal.ai

# Copy MCP config (no editing needed)
cp .mcp.json.template .mcp.json

# Make a story
python create_story.py "detective cat solves art heist"
```

## Try These

**Simple:**
```bash
python create_story.py "robot discovers emotions"
```

**Multiple characters with style:**
```bash
python create_story.py "fox and owl solve mysteries in watercolor style"
python create_story.py "three pirates find treasure, digital art, vibrant colors"
```

**Specify length:**
```bash
python create_story.py "space adventure, 10 pages"
python create_story.py "dragon learns to fly, 5 page short story"
```

**Go wild:**
```bash
python create_story.py "philosophical zombies debate existence in a coffee shop, noir style, 7 pages"
```

**See everything:**
```bash
python create_story.py --debug "your story"  # Watch the agent think and work
python create_story.py --verbose "your story"  # See tool calls as they happen
```

## You Get

**Web Interface:**
- 🎨 Ghibli-inspired design with floating animations
- 📚 Beautiful gallery showing all your stories
- 📖 Interactive page-flip book viewer
- 🖱️ One-click story creation with preset examples
- 📱 Responsive design works on all devices

**File Output:**
```
stories/your-story/
├── story_data.json    # The whole story
├── storybook.pdf      # Ready to read
└── images/            # All the art
```

## Frontend Features

- **Preset Story Ideas**: Quick-start buttons with examples like "robot discovers emotions" 
- **Real-time Progress**: Watch terminal output while enjoying the beautiful interface
- **Story Gallery**: Browse all your created stories with cover images
- **Page-flip Animation**: Smooth, realistic book reading experience
- **Keyboard Navigation**: Use arrow keys to flip pages
- **Demo Perfect**: Ideal for presentations and showcases

## Requirements

- Python 3.11+
- FAL API key from https://fal.ai
- That's literally it

## Perfect for Demos

The web interface is designed for impressive demonstrations:
1. Start the frontend (`python app_simple.py`)
2. Keep the terminal visible to show the agent working
3. Use preset buttons for quick story generation
4. Stories automatically appear in the beautiful gallery
5. Wow your audience with the page-flip viewer

related:
  - methods/QUICK_START.md
---
Built with Claude Code SDK + Nano-Banana. The agent does the work, you get the story.
