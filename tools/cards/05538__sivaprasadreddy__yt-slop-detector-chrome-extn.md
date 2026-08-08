---
id: tool-05538
type: tool
area: 库
status: active
tags: [JavaScript, 协议未明, 本地优先, 英文文档, 去AI味, 本地写作]
title: yt-slop-detector-chrome-extn
summary: 投稿前给正文降 AI 检测痕迹、改自然语气
source: https://github.com/sivaprasadreddy/yt-slop-detector-chrome-extn
created: 2026-07-18
updated: 2026-07-18
no: 5538
category: 一、去 AI 味 / Humanizer 库
repo: sivaprasadreddy/yt-slop-detector-chrome-extn
stars: 4
url: https://github.com/sivaprasadreddy/yt-slop-detector-chrome-extn
tier: "B"
use_case: "投稿前给正文降 AI 检测痕迹、改自然语气"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/最强去AI味铁律.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: f5b6d9b796aeee77
  - methods/改稿润色指令库.md
---

# sivaprasadreddy/yt-slop-detector-chrome-extn

- **分类**：一、去 AI 味 / Humanizer 库
- **链接**：https://github.com/sivaprasadreddy/yt-slop-detector-chrome-extn
- **Stars**：4
- **语言**：JavaScript
- **License**：None
- **Topics**：—
- **GitHub 描述**：YouTube AI Slop Detector Chrome Extension
- **本地描述**：YouTube AI Slop Detector Chrome Extension
- **拉取时间**：2026-07-25 18:22:24

---

# YT Slop Detector

A Chrome extension that automatically detects AI-related videos on YouTube and marks them in-place so you can clean up your feed without losing the original context.

Matching videos keep their original title, but get an **AI Slop:** prefix, the matched keyword inside the title is highlighted, and the thumbnail is covered with a custom warning image.

![yt-ai-slop-detector-screenshot.png](https://github.com/sivaprasadreddy/yt-slop-detector-chrome-extn/blob/main/yt-ai-slop-detector-screenshot.png)

---

## Installation

This extension is not on the Chrome Web Store. Install it directly from the source folder.

**Step 1 — Open Chrome Extensions**

Navigate to `chrome://extensions` in your browser.

**Step 2 — Enable Developer Mode**

Toggle **Developer mode** on using the switch in the top-right corner of the page.

**Step 3 — Load the extension**

Click **Load unpacked**, then select the `yt-slop-detector-chrome-extn` folder.

The extension icon will appear in your Chrome toolbar. Pin it for easy access via the puzzle-piece menu.

---

## How it works

Once installed, the extension runs automatically on supported YouTube pages.

- **Home feed** — matching video cards are marked as the page loads and as you scroll.
- **Search results** — matching results are marked inline.
- **Watch page sidebar** — recommended videos are marked too.
- **Navigation** — YouTube is a single-page app; the extension re-runs every time you navigate to a new page.

A video is considered slop if its title contains any word from the keyword list (case-insensitive). Matching videos get two changes applied:

1. The title becomes `AI Slop: <original title>`, with the matched keyword segment highlighted.
2. The thumbnail is covered by `images/potential-ai-slop.png`.

If more than one keyword matches, the extension highlights the earliest match in the title. If two matches start at the same position, it prefers the longer keyword.

The original title and thumbnail are never permanently altered. Reloading the page, disabling the extension, or removing the matching keyword restores the original YouTube UI.

---

## Managing keywords

Click the extension icon in the toolbar to open the settings popup.

### Add a keyword

Type a word or phrase into the input field and press **Enter** or click **Add**. The keyword takes effect on the current YouTube page immediately.

### Remove a keyword

Click the **×** button on any keyword chip to remove it. The videos that matched only that keyword will be restored on the page.

### Reset to defaults

Click **Reset defaults** to restore the built-in keyword list.

### Default keyword list

| Keyword | Keyword | Keyword |
|---|---|---|
| AI | Agent | Agents |
| Claude | OpenAI | ChatGPT |
| LLM | GPT | GPT-4 |
| GPT-5 | Gemini | Copilot |
| Grok | Perplexity | Cursor |
| Windsurf | Vibe coding | Vibe code |
| Dead | | |

Keywords are saved to Chrome sync storage and persist across browser sessions. If you are signed into Chrome, they can sync across your devices.

---

## File structure

```
yt-slop-detector-chrome-extn/
├── manifest.json          # Chrome extension manifest (v3)
├── content.js             # Detects matching videos and updates titles/thumbnails
├── content.css            # Styles for the thumbnail overlay and title highlight
├── popup.html             # Settings UI shown when clicking the toolbar icon
├── popup.js               # Keyword management logic
├── popup.css              # Settings UI styles
├── generate-icons.html    # Helper page to regenerate PNG icons (open in browser)
└── images/
    ├── potential-ai-slop.png # Warning image shown over matched thumbnails
    ├── slop-thumbnail.svg # Legacy thumbnail asset
    ├── icon16.png         # Extension toolbar icon
    ├── icon48.png
    └── icon128.png
```

---

## Regenerating icons

If you want to customise the toolbar icon, open `generate-icons.html` in any browser and click **Generate & Download Icons**. Three PNG files will download (`icon16.png`, `icon48.png`, `icon128.png`). Move them into the `images/` folder, then go to `chrome://extensions` and click the reload button on the extension card.

---

## Troubleshooting

**Videos are not being marked**

- Make sure the extension is enabled on `chrome://extensions`.
- Check that the keyword list in the popup is not empty.
- If you changed `manifest.json`, click the extension's **Reload** button in `chrome://extensions` before testing again.
- Some YouTube layouts (e.g. Shorts shelf, Mix playlists) use different DOM structures and may not be detected.

**The custom thumbnail does not appear**

- Reload the extension in `chrome://extensions`. The thumbnail image is exposed through `web_accessible_resources`, so manifest changes require an extension reload.
- Refresh the YouTube tab after reloading the extension.

**A video was marked but should not have been**

Open the popup and remove the keyword that caused the false match. Changes apply instantly.

**Keywords were lost after a browser update**

Keywords are stored in Chrome sync storage. If storage was cleared, use **Reset defaults** in the popup to restore the built-in list.

---

## Privacy

The extension requires only two permissions plus web-accessible access to its bundled thumbnail assets:

| Permission | Why |
|---|related:
  - methods/最强去AI味铁律.md
  - methods/改稿润色指令库.md
---|
| `storage` | Saves and loads your keyword list via Chrome's sync storage |
| Host access to `youtube.com` | Allows the content script to read and modify the YouTube page |

No data is sent to any server. No browsing history is collected. All matching and DOM updates happen locally in your browser.
