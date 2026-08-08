---
id: tool-05182
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: OriginAI
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/realchrissean/originai
created: 2026-07-18
updated: 2026-07-18
no: 5182
category: 一、去 AI 味 / Humanizer 库
repo: RealChrisSean/OriginAI
stars: 1
url: https://github.com/realchrissean/originai
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 51873a8a549dfea7
  - methods/改稿润色指令库.md
---

# RealChrisSean/OriginAI

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/realchrissean/originai
- **Stars**：1
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：AI Content Detector. Check if text was written by a human or AI.
- **本地描述**：AI Content Detector. Check if text was written by a human or AI.
- **拉取时间**：2026-07-25 18:09:08

---

# OriginAI - Chrome Extension

AI content detection extension that analyzes text to determine if it was written by AI or human. Features popup analysis, right-click context menu, and floating popup on text selection.

## Features

- **Instant Detection** - Highlight text, get a score
- **Floating Popup** - Select text on any webpage, click "Check AI"
- **Context Menu** - Right-click selected text to analyze
- **Popup Interface** - Paste text directly into the extension

## Installation

1. Clone this repo
2. Go to `chrome://extensions`
3. Enable "Developer mode"
4. Click "Load unpacked"
5. Select this folder

## How It Works

The extension sends text to a detection API that runs multiple ML models:
- OpenAI's text classifier
- ChatGPT detector
- Fakespot model
- Ensemble scoring

Results come back with a "human score" (0-100%) and confidence level.

## Usage

Three ways to use it:

1. **Floating popup** - Select text on any page, a small popup appears. Click "Check AI".
2. **Right-click** - Select text, right-click, choose "Check with AI Detector"
3. **Extension popup** - Click the extension icon, paste text, hit detect

## Files

```
├── manifest.json    # Extension config
├── content.js       # Injected into pages, handles floating popup
├── content.css      # Styles for floating popup
├── popup.html       # Extension popup UI
├── popup.js         # Extension popup logic
├── background.js    # Service worker for context menu
└── icons/           # Extension icons
```

## API

The extension hits `app.parallellives.ai/api/detect` for detection. This is a hosted API - you don't need to run anything locally.

## Free vs Pro

- **Free** - Basic ML detection, daily limit
- **Pro** - Higher accuracy models, humanization tips, plagiarism check, no limits

Pro requires a subscription at parallellives.ai.

---

## Technical Details

### Architecture

The extension is a standard Chrome Manifest V3 extension. Content script injects into all pages and listens for text selection. When detected, it shows a floating popup anchored near the selection.

### Backend Stack

The detection API runs on Vercel (Next.js). Nothing fancy - just API routes that call ML models and return scores.

For tracking and analytics, the backend uses **TiDB** (MySQL-compatible distributed database). Here's how it's set up:

**Why TiDB:**
- MySQL compatibility means standard queries, no learning curve
- Serverless tier is free and handles the scale I need
- Distributed by default, so I don't worry about scaling later

**What's stored:**
- `detector_usage` - Every detection gets logged (text hash, score, site URL, timestamp)
- `detector_cache` - Results cached for 24 hours to avoid re-running ML models on same text
- `detector_feedback` - When users click "accurate" or "wrong", it gets stored here

**Schema example:**
```sql
CREATE TABLE detector_usage (
  id VARCHAR(36) PRIMARY KEY,
  user_id VARCHAR(36),
  text_hash VARCHAR(64) NOT NULL,
  word_count INT NOT NULL,
  score INT NOT NULL,
  confidence VARCHAR(20) NOT NULL,
  provider VARCHAR(50) NOT NULL,
  site_url VARCHAR(500),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE detector_cache (
  text_hash VARCHAR(64) PRIMARY KEY,
  result JSON NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  expires_at TIMESTAMP NOT NULL
);

CREATE TABLE detector_feedback (
  id VARCHAR(36) PRIMARY KEY,
  user_id VARCHAR(36),
  text_hash VARCHAR(64) NOT NULL,
  feedback_type ENUM('false_positive', 'false_negative', 'accurate') NOT NULL,
  original_score INT NOT NULL,
  comment TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

The feedback loop is the interesting part. When enough users report a false positive on similar text patterns, I can use that data to tune the detection. Not doing anything fancy with it yet, but the data's there.

Connection is straightforward - TiDB Cloud gives you a MySQL connection string, and I use `mysql2` in Node:

```javascript
import mysql from "mysql2/promise";

const pool = mysql.createPool({
  host: process.env.TIDB_HOST,
  port: 4000,
  user: process.env.TIDB_USER,
  password: process.env.TIDB_PASSWORD,
  database: process.env.TIDB_DATABASE,
  ssl: { ca: fs.readFileSync("/etc/ssl/cert.pem") }
});
```

That's it. No ORM, no abstraction layers. Just SQL.

related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---

## License

MIT
