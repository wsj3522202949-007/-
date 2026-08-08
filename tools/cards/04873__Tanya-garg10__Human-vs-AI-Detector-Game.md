---
id: tool-04873
type: tool
area: 库
status: active
tags: [HTML, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: Human-vs-AI-Detector-Game
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/tanya-garg10/human-vs-ai-detector-game
created: 2026-07-18
updated: 2026-07-18
no: 4873
category: 一、去 AI 味 / Humanizer 库
repo: Tanya-garg10/Human-vs-AI-Detector-Game
stars: 0
url: https://github.com/tanya-garg10/human-vs-ai-detector-game
tier: "C"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
  - "⚠️ 仓库疑似停更/归档，bug 不会修、依赖可能过期"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 17169460a68993bf
  - methods/改稿润色指令库.md
---

# Tanya-garg10/Human-vs-AI-Detector-Game

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/tanya-garg10/human-vs-ai-detector-game
- **Stars**：0
- **语言**：HTML
- **License**：None
- **Topics**：—
- **GitHub 描述**：An interactive Human vs AI Detector Game built with HTML, CSS, and JavaScript. Guess whether images, text, code, or artwork were created by a human or AI, receive instant explanations, track your score, and compete on a local leaderboard.
- **本地描述**：An interactive Human vs AI Detector Game built with HTML, CSS, and JavaScript. Guess whether images, text, code, or artwork were created by a human or AI, receive instant explanations, track your score, and compete on a local leaderboard.
- **拉取时间**：2026-07-25 17:57:39

---

# 🤖 vs 👤 Human vs AI Detector Game

An interactive browser-based game that challenges you to distinguish between human-created and AI-generated content — across text, code, poetry, emails, and artwork.

![Game Preview](https://img.shields.io/badge/Play-In%20Browser-00c896?style=for-the-badge&logo=html5)
![No Dependencies](https://img.shields.io/badge/Dependencies-None-a855f7?style=for-the-badge)
![Responsive](https://img.shields.io/badge/Responsive-Mobile%20%26%20Desktop-60a5fa?style=for-the-badge)

## 🎮 How to Play

1. Open `human-vs-ai-detector.html` in any modern browser — no server or install needed
2. Each round presents a piece of content: a text passage, code snippet, poem, email, or artwork
3. Decide: was it made by a **Human** 👤 or an **AI** 🤖?
4. Get instant feedback with a detailed explanation and clue tags
5. Complete all 10 rounds and see your final grade on the leaderboard

## ✨ Features

### 🧩 Content Types
| Type | Description |
|------|-------------|
| 📝 Text Passages | Blog posts, personal essays, opinion pieces, corporate writing |
| 💻 Code Snippets | Real dev code vs. AI-generated over-commented examples |
| 📜 Poetry | Free-form human verse vs. perfect-rhyme AI poems |
| 📧 Emails & Messages | Casual human threads vs. hollow professional AI emails |
| 🎨 Artwork Descriptions | SVG-generated visuals with human or AI artist statements |

### ⚡ Gameplay Mechanics
- **15-second timer** per round — answer faster for more points
- **Streak multiplier** — chain correct answers for bonus points up to +100
- **Instant feedback** — explanation + clue tags reveal the tells after every guess
- **Auto time-out** — running out of time counts as a wrong answer
- **20-question pool** — randomly selects 10 per game for replayability

### 🏆 Scoring System
| Component | Points |
|-----------|--------|
| Correct answer | 100 base |
| Time bonus | Up to +90 (6 pts/sec remaining) |
| Streak bonus | Up to +100 (20 pts × streak, max 5) |
| Wrong answer | 0 |

### 📊 Grades
| Score | Grade | Title |
|-------|-------|----related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| 10/10 | 🥇 S | Perfect! |
| 8–9/10 | 🥈 A | Expert Detector |
| 6–7/10 | 🥉 B | Sharp Eye |
| 4–5/10 | 📊 C | Getting There |
| 0–3/10 | 🤖 D | AI Won This Round |

### 💾 Leaderboard
- Scores saved locally via **localStorage** — persists across sessions
- Top 20 entries ranked by score
- Shows name, correct answers, and date

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/Tanya-garg10/Human-vs-AI-Detector-Game.git

# Open in browser — that's it!
cd Human-vs-AI-Detector-Game
open human-vs-ai-detector.html   # macOS
start human-vs-ai-detector.html  # Windows
xdg-open human-vs-ai-detector.html  # Linux
```

Or simply **download the file** and double-click it.

## 🛠 Tech Stack

- **HTML5** — semantic structure
- **CSS3** — custom properties, gradients, animations, responsive grid
- **Vanilla JavaScript** — zero dependencies, zero frameworks
- **SVG** — procedurally generated artwork visuals
- **localStorage** — client-side leaderboard persistence

## 📁 Project Structure

```
Human-vs-AI-Detector-Game/
└── human-vs-ai-detector.html   # Entire game — self-contained single file
```

## 🧠 What the Game Teaches

The game highlights real patterns that distinguish AI content from human content:

- **AI text** tends to use abstract nouns, balanced "on one hand / on the other hand" structures, and opening phrases like *"Certainly!"* or *"It is important to note"*
- **AI code** is over-commented, uses verbose variable names like `inputString` or `calculateFactorial`, and includes JSDoc for trivial functions
- **AI poetry** defaults to AABB rhyme schemes and motivational platitudes with no surprising imagery
- **Human writing** includes specific details, self-deprecating humour, imperfection, and emotional precision
- **Human code** has `// TODO: fix this later lol` comments, short variable names, and informal error strings like `'rip'`

<div align="center">Made with ❤️ — Can you beat the AI?</div>
