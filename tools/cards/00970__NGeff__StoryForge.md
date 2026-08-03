---
id: tool-00970
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: StoryForge
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/ngeff/storyforge
created: 2026-07-18
updated: 2026-07-18
no: 970
category: 二、网文 / 长篇 AI 写作系统 库
repo: NGeff/StoryForge
stars: 1
url: https://github.com/ngeff/storyforge
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# NGeff/StoryForge

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/ngeff/storyforge
- **Stars**：1
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：StoryForge is an AI‑driven user story generator that turns wireframes/screenshots into structured product stories — complete with acceptance criteria and dependencies — while keeping data private in the browser.
- **本地描述**：StoryForge is an AI‑driven user story generator that turns wireframes/screenshots into structured product stories — complete with acceptance criteria and dependencies — while keeping data private in the browser.
- **拉取时间**：2026-07-23 23:07:20

---

<p align="center">
  <img src="assets/logo.svg" alt="StoryForge Logo" width="120" height="120">
</p>

<h1 align="center">StoryForge</h1>

<p align="center">
  <strong>Interactive Narrative Engine</strong><br>
  Create immersive branching stories with themes, characters, and achievements
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#demo">Demo</a> •
  <a href="#installation">Installation</a> •
  <a href="#configuration">Configuration</a> •
  <a href="#creating-stories">Creating Stories</a> •
  <a href="#api">API</a> •
  <a href="#contributing">Contributing</a>
</p>

---

## Features

- **Branching Narrative System** — Create stories with multiple paths and endings
- **Customizable Characters** — Define classes, attributes, and unique abilities
- **Visual Themes** — Three included themes (Fantasy, Dark, Celestial) + custom theme support
- **Achievement System** — Unlock achievements based on player choices
- **Effects & Consequences** — Each choice can modify attributes and unlock paths
- **Journey History** — View all decisions made during the adventure
- **Local Persistence** — Progress automatically saved in browser
- **Fully Responsive** — Optimized experience for desktop and mobile devices
- **Zero Dependencies** — Vanilla JavaScript, no external frameworks
- **Accessibility** — Keyboard navigation and screen reader support

## Demo

🎮 **[Play Online Demo](https://ngeff.github.io/storyforge)**

<p align="center">
  <img src="assets/screenshot-menu.png" alt="Main Menu" width="400">
  <img src="assets/screenshot-gameplay.png" alt="Gameplay" width="400">
</p>

## Installation

### Option 1: Direct Clone

```bash
git clone https://github.com/ngeff/storyforge.git
cd storyforge
```

Open `index.html` in your browser or use a local server:

```bash
# Python 3
python -m http.server 8000

# Node.js
npx serve
```

### Option 2: GitHub Pages

1. Fork this repository
2. Go to **Settings** → **Pages**
3. Select branch `main` and folder `/ (root)`
4. Access at `https://yourusername.github.io/storyforge`

## Project Structure

```
storyforge/
├── index.html              # Application entry point
├── css/
│   ├── main.css            # Core styles and layout
│   ├── themes.css          # Visual theme definitions
│   └── animations.css      # Keyframes and transitions
├── js/
│   ├── app.js              # Initialization and orchestration
│   ├── engine.js           # Narrative engine (core)
│   ├── ui.js               # DOM manipulation and rendering
│   ├── storage.js          # Persistence and save management
│   └── data/
│       └── stories.js      # Story and character data
├── assets/
│   ├── logo.svg            # Project logo
│   └── icons/              # Character SVG icons
└── README.md
```

## Configuration

### Global Settings

Edit `js/app.js` to modify default behaviors:

```javascript
const CONFIG = {
    defaultTheme: 'fantasy',      // Initial theme: fantasy | dark | celestial
    textSpeed: 30,                // Typing speed (ms per character)
    enableAnimations: true,       // Enable/disable animations
    enableSound: false,           // Reserved for future implementation
    autoSave: true,               // Automatically save progress
    saveSlots: 3                  // Number of available save slots
};
```

### Creating Custom Themes

Add new themes in `css/themes.css`:

```css
[data-theme="mytheme"] {
    --bg-primary: #1a1a2e;
    --bg-secondary: #16213e;
    --accent-start: #e94560;
    --accent-end: #ff6b6b;
    --text-primary: #eaeaea;
    --text-secondary: #a0a0a0;
    --card-bg: rgba(22, 33, 62, 0.9);
    --border-color: rgba(255, 255, 255, 0.1);
}
```

Register the theme in `js/data/stories.js`:

```javascript
export const THEMES = {
    // ... existing themes
    mytheme: {
        id: 'mytheme',
        name: 'My Theme',
        icon: '🎨'
    }
};
```

## Creating Stories

### Story Structure

Each story is defined as an object with connected nodes:

```javascript
export const STORIES = {
    my_story: {
        // Metadata
        meta: {
            title: 'Adventure Title',
            description: 'A brief description',
            author: 'Your Name',
            version: '1.0.0'
        },
        
        // Available characters
        characters: {
            warrior: {
                name: 'Warrior',
                description: 'Raw strength and courage',
                icon: 'sword',               // Icon identifier
                iconPath: '<path d="..."/>',  // SVG path (required)
                colorClass: 'color-amber',    // CSS color class
                stats: { strength: 8, agility: 5, magic: 2 }
            }
        },
        
        // Narrative nodes
        nodes: {
            start: {
                text: 'The narrative text appears here...',
                choices: [
                    { 
                        text: 'First choice',
                        next: 'next_node',
                        effect: { reputation: +5 },
                        condition: null  // Optional: display condition
                    },
                    {
                        text: 'Second choice',
                        next: 'another_node',
                        effect: { gold: -10 }
                    }
                ]
            },
            
            next_node: {
                text: 'Story continues...',
                choices: [/* ... */]
            },
            
            good_ending: {
                text: 'You won! Congratulations.',
                ending: true,
                title: 'The Victorious Hero',
                achievement: 'hero_ending'
            }
        },
        
        // Unlockable achievements
        achievements: {
            hero_ending: {
                name: 'Legendary Hero',
                description: 'Complete the story with the heroic ending',
                icon: '🏆'
            }
        }
    }
};
```

### Character Icons

Character icons are **required**. Each character must include:

- `iconPath`: SVG path data for the icon (required)
- `colorClass`: CSS class for icon color (required)

Example:
```javascript
warrior: {
    name: 'Warrior',
    iconPath: '<path fill="none" stroke="currentColor" stroke-width="1.5" d="M14.5 17.5L3 6V3h3l11.5 11.5..."/>',
    colorClass: 'color-amber',
    // ...
}
```

### Advanced Conditions

Display choices conditionally based on attributes:

```javascript
{
    text: 'Use ancient magic',
    next: 'secret_magic',
    condition: (state) => state.stats.magic >= 7,
    hiddenWhenLocked: false  // false = show disabled, true = hide
}
```

### Complex Effects

```javascript
{
    text: 'Sacrifice the amulet',
    next: 'sacrifice',
    effect: {
        inventory: { remove: 'sacred_amulet' },
        stats: { magic: +15, health: -20 },
        flags: { sacrificed_amulet: true },
        unlock: 'dark_path'
    }
}
```

## API

### StoryEngine

```javascript
import { StoryEngine } from './js/engine.js';

const engine = new StoryEngine(storyData);

// Start new game
engine.start(characterId);

// Make a choice
engine.choose(choiceIndex);

// Get current state
const state = engine.getState();

// Check if current node is an ending
const isEnding = engine.isEnding();

// Get choice history
const history = engine.getHistory();

// Save/Load
const saveData = engine.export();
engine.import(saveData);
```

### Events

```javascript
engine.on('nodeChange', (node) => { /* ... */ });
engine.on('choiceMade', (choice, effect) => { /* ... */ });
engine.on('ending', (endingData) => { /* ... */ });
engine.on('achievementUnlock', (achievement) => { /* ... */ });
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a branch for your feature (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

### Code Guidelines

- Use ES6+ features
- Keep functions small and focused
- Document public functions with JSDoc
- Test in multiple browsers before submitting

## License

This project is licensed under the [MIT License](LICENSE).

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

<p align="center">
  Built with ☕ by <a href="https://github.com/NGeff">NGeff</a>
</p>
