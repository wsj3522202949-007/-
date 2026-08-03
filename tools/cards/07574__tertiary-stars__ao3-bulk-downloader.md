---
id: tool-07574
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: ao3-bulk-downloader
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/tertiary-stars/ao3-bulk-downloader
created: 2026-07-18
updated: 2026-07-18
no: 7574
category: 画龙补充 / 扩容入库 — 补充源
repo: tertiary-stars/ao3-bulk-downloader
stars: 1
url: https://github.com/tertiary-stars/ao3-bulk-downloader
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/QUICK_START.md
---

# tertiary-stars/ao3-bulk-downloader

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/tertiary-stars/ao3-bulk-downloader
- **Stars**：1
- **语言**：Python
- **License**：None
- **Topics**：—
- **GitHub 描述**：—
- **本地描述**：ao3-bulk-downloader
- **拉取时间**：2026-07-25 19:26:04

related:
  - methods/QUICK_START.md
---

# AO3 Bulk Downloader 

A tool to download multiple works from Archive of Our Own (AO3) and scheduler.

## Features

- Bulk download works from AO3 using one or multiple links
- Save works in multiple formats (HTML, EPUB, PDF, MOBI)
- Schedule future posts and chapter updates (upcoming)
- Manage multiple works and their posting schedules through a simple interface (upcoming)

## Installation

1. Ensure you have Python 3.8 or higher installed
2. Clone this repository:
```bash
git clone https://github.com/tertiary-stars/ao3-downloader-scheduler
cd ao3-downloader-scheduler
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Set up

Edit the `config.json` file in the root directory to include your AO3 username and password:
```json
{
    "download_format": "EPUB",
    "download_path": "./downloads",
    "credentials": {"AO3_USERNAME":"username", 
                    "AO3_PASSWORD":"password"
    }
}
```
Download format takes all formats AO3 allows, it is not case sensitive. 

## Authentication

To use the bulk downloader or scheduler, you'll need to log in to your AO3 account:

1. Ensure you edited config.json file with your credentials
2. Run the authentication setup:
```bash
python auth_setup.py
```
This is to ensure restricted works can be downloaded, too.

## Downloading Works

To download works, you can either:

1. Use the command line:
```bash
python ao3_downloader.py --url "https://archiveofourown.org/works/..."
```

2. Use multiple URLs:
```bash
python ao3_downloader.py --urls urls.txt
```
Where `urls.txt` contains one AO3 URL per line.

## Disclaimers
- Your AO3 credentials are stored securely using environment variables. We have absolutely **no** access to them.
- Downloaded works are saved locally only. 
- The tool respects AO3's Terms of Service and rate limits.


## Troubleshooting

Common issues and solutions:

1. **Download fails**
   - Check your internet connection
   - Verify the URL is accessible
   - Ensure you're logged in for restricted works


## License

This project is licensed under MIT license. 

## Acknowledgments

- Built using the AO3 API guidelines
- Inspired by the AO3 community's needs

## Support

- Create an issue on GitHub for bug reports.
- DM me on discord (tertiary.stars) or twt (binary_starz) or email me (xunswriting@gmail.com)! 
