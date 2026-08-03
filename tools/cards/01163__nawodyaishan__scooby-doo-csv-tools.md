---
id: tool-01163
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: scooby-doo-csv-tools
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/nawodyaishan/scooby-doo-csv-tools
created: 2026-07-18
updated: 2026-07-18
no: 1163
category: 二、网文 / 长篇 AI 写作系统 库
repo: nawodyaishan/scooby-doo-csv-tools
stars: 0
url: https://github.com/nawodyaishan/scooby-doo-csv-tools
tier: "C"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# nawodyaishan/scooby-doo-csv-tools

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/nawodyaishan/scooby-doo-csv-tools
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：cli, csv, pandas, python, tkinter, tkinter-gui
- **GitHub 描述**：ScoobyDoo CSV Tool is a Python application that processes CSV files containing story plot information. This version of the project includes a Tkinter-based graphical user interface (GUI) for a more user-friendly experience.
- **本地描述**：ScoobyDoo CSV Tool is a Python application that processes CSV files containing story plot information. This version of the project includes a Tkinter-based graphical user interface (GUI) for a more user-friendly experience.
- **拉取时间**：2026-07-23 23:12:57

---

# ScoobyDoo CSV Tool with Tkinter GUI

ScoobyDoo CSV Tool is a Python application that processes CSV files containing story plot information. It provides the
following functionalities:

## Features

1. **Split long plots**: Splits long plots in a CSV file into multiple smaller plots, based on a given maximum token
   count.
2. **Remove specific characters**: This feature provides several options:
   - Remove non-breaking spaces (NBSP)
   - Remove custom character
   - Remove season and episode indicators
3. **Story plots data preparation to a JSON**: Extract a specified number of story plots from the CSV file and generate
   a `story_plots.json` file.
4. **Generate Text File**: Extract a specified number of story plots from the CSV file and generate a `story_plots.txt`
   file in a given format.
5. **Generate PDF File**: Extract a specified number of story plots from the CSV file and generate a `story_plots.pdf`
   file in a given format.
6. **Exit**: Exit the application.

This version of the project includes a Tkinter-based graphical user interface (GUI) for a more user-friendly experience.

## Installation

To install the required dependencies, simply run:

```bash
pip install -r requirements.txt
```

## Usage

To run the application, execute the following command:

```bash
python scoobydoo_csv_gui.py
```

The application will open in a new window with the main menu.

### Split long plots

1. Click on the 'Split long plots' button.
2. Select the input CSV file.
3. Select the output CSV file.
4. Enter the maximum tokens per plot chunk (default: 1000).
5. Click 'OK' and the plots will be split in the output CSV file.

### Remove specific characters

1. Click on the 'Remove specific characters' button.
2. Choose one of the following options:
   - Remove non-breaking spaces (NBSP)
   - Remove custom character
   - Remove season and episode indicators
3. Select the input CSV file.
4. Select the output CSV file.
5. If you chose 'Remove custom character', enter the custom character to remove.
6. Click 'OK' and the specified characters will be removed in the output CSV file.

### Story plots data preparation to a JSON

1. Click on the 'Story plots data preparation to a JSON' button.
2. Select the input CSV file.
3. Enter the number of JSON data objects to generate (default: all CSV data).
4. Click 'OK' and a `story_plots.json` file will be generated in the current directory.

### Exit

To exit the application, click on the 'Exit' button and confirm your choice.

Sure, here's how you can update the `README.md` file in your GitHub repository to include the new features.

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

