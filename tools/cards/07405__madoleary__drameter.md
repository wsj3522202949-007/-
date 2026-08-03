---
id: tool-07405
type: tool
area: 库
status: active
tags: [Python, 协议宽松, 本地优先, 英文文档, 本地写作]
title: drameter
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/madoleary/drameter
created: 2026-07-18
updated: 2026-07-18
no: 7405
category: 画龙补充 / 扩容入库 — 补充源
repo: madoleary/drameter
stars: 0
url: https://github.com/madoleary/drameter
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
related:
  - methods/QUICK_START.md
---

# madoleary/drameter

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/madoleary/drameter
- **Stars**：0
- **语言**：Python
- **License**：MIT
- **Topics**：—
- **GitHub 描述**：Smart screenplay analysis tool for filmmakers
- **本地描述**：drameter
- **拉取时间**：2026-07-25 19:20:54

---

# 🎬 Drameter

**Smart screenplay analysis tool for filmmakers.**

Drameter analyzes the underlying structure, rhythm, and cinematic language of a screenplay, quantifying tone, pacing, and visual storytelling at the scene level.

It aims to define the metadata of film language, giving screenwriters, directors, editors, and assistant directors a breakdown of each scene’s tempo, complexity, and visual rhythm, thus helping them move beyond generic WPM estimates or the one-page-per-minute myth.

I built this because I tend to write action-heavy scripts, which complicates time and complexity anticipation. I also found other tools either:  
1) Annoying to use, or  
2) Geared toward content creators, not filmmakers (no shade).

---

## ✨ Features

- 🗂️ Scene-by-scene analysis from `INT.` / `EXT.` headings  
- 🗣️ Differentiates between dialogue and action blocks  
- ⏱️ Estimates time using customizable words-per-minute (WPM)  
- 🎭 Adds time for `(beat)` pauses in dialogue (beat-aware timing)  
- 🎞️ Detects montage sequences and visual pacing cues  
- 🧠 Labels scenes by **dialogue and action complexity** (`none`, `light`, `moderate`, `dense`) 
- 🧭 Flags transitions (`DISSOLVE TO`, `MATCH CUT`, `INTERCUT WITH`, etc.)  
- 🖼 Detects flashbacks, dream sequences, intercuts, fast cuts, and more  
- 📤 Exports full breakdown as CSV with structured fields  
- 🕒 Auto-names CSVs using script title + timestamp  
- 📁 Includes test runner and sample script

---

## 📦 Requirements

- Python 3.8+
- [`pdfplumber`](https://pypi.org/project/pdfplumber/)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python run_test.py path/to/your_script.pdf
```

Add `--export` to generate a CSV:

```bash
python run_test.py path/to/your_script.pdf --export
```

Optional flags:

```bash
--export-path        Custom CSV path (default: outputs/report_*.csv)
--wpm                Words per minute (default: 130)
--beat               Seconds per (beat) pause (default: 1.5)
```

---

## 🧪 Sample Output

```
Scene 1: INT. WAREHOUSE - NIGHT  
  Type: INT | Location: WAREHOUSE | Time: NIGHT  
  Dialogue: 12w | Action: 122w | Beat count: 1  
  Dialogue complexity: light | Action complexity: moderate  
  ⏱ Estimated time: 56.4s  
  🎞 Visual pacing: montage, fast-cut  
  🔀 Transitions: MATCH CUT  
  🗣 Dialogue pacing: overlapping, VO  

Scene 2: EXT. PARK - MORNING  
  Type: EXT | Location: PARK | Time: MORNING  
  Dialogue: 0w | Action: 87w | Beat count: 0  
  Dialogue complexity: none | Action complexity: moderate  
  ⏱ Estimated time: 39.8s  
  🎞 Visual pacing: intercut  
  🔀 Transitions:  
  🗣 Dialogue pacing:  

🎬 Total scenes analyzed: 2  
⏳ Estimated total runtime: 1m 36s  
```

---

## 📁 Project Structure

```
drameter/
├── drameter.py             # Core parser & scene analyzer
├── run_test.py             # CLI runner
├── requirements.txt
├── outputs/                # Exported CSVs
└── examples/
    └── sample_script.pdf   # Sample screenplay
```

---

## 🔍 CSV Field Highlights

- `scene_heading`, `scene_type`, `location`, `time_of_day`
- `dialogue_words`, `action_words`, `beat_count`
- `estimated_seconds`, `dialogue_complexity`, `action_complexity`
- `dialog_pacing_tags`, `visual_pacing_tags`
- `transitions` (e.g. ["MATCH CUT", "DISSOLVE TO"])

All pacing and cue fields are **structured lists** for easy filtering/sorting in future interfaces.

---

## 🎯 Who Is This For?

- **Screenwriters** evaluating structure and rhythm  
- **Directors** prepping a shoot or visual tone  
- **Assistant Directors** estimating day plans  
- **Editors** visualizing timing and pacing pre-edit  
- **Producers** approximating runtime vs. page count

---

## 💡 Why Drameter?

Storyboards don’t dictate the final frame. Beat sheets don’t define tone. Drameter doesn't replace a director. It gives creative teams a data-informed jumping-off point as to maximise preparation before production.

---

## 🚧 Roadmap

### For Filmmakers
- [x] Visual pacing tag detection (montage, intercut, flashback)
- [x] Hybrid scene detection (`montage + dialogue`)
- [x] Split dialogue and action complexity
- [x] Add dialog pacing tags (VO, OS, overlaps, interruptions)
- [ ] Scene duration tiers (short/med/long)

### Tooling
- [x] CLI with custom args
- [ ] Lightweight web GUI (PDF → breakdown)
- [ ] VS Code extension

### Format Support
- [ ] Fountain `.fountain` parser
- [ ] Final Draft `.fdx` parser

---

## 🪪 License

MIT

related:
  - methods/QUICK_START.md
---

## 👤 Author

**Madeline O'Leary**  
[github.com/madoleary](https://github.com/madoleary)
