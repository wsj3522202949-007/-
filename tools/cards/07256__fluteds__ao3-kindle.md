---
id: tool-07256
type: tool
area: 库
status: active
tags: [Python, 协议未明, 本地优先, 英文文档, 本地写作]
title: ao3-kindle
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/fluteds/ao3-kindle
created: 2026-07-18
updated: 2026-07-18
no: 7256
category: 画龙补充 / 扩容入库 — 补充源
repo: fluteds/ao3-kindle
stars: 0
url: https://github.com/fluteds/ao3-kindle
tier: "C"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 0 stars，未经社区验证，试用前先小范围测试"
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 3a95344f0c91a2b7
  - methods/QUICK_START.md
---

# fluteds/ao3-kindle

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/fluteds/ao3-kindle
- **Stars**：0
- **语言**：Python
- **License**：None
- **Topics**：ao3, kindle, send-to-kindle
- **GitHub 描述**：Download fanfiction works from Archive of Our Own (AO3) and send them directly to your Amazon Kindle device via email
- **本地描述**：ao3-kindle
- **拉取时间**：2026-07-25 19:15:44

related:
  - methods/QUICK_START.md
---

# AO3 to Kindle

This script allows you to download fanfiction works from Archive of Our Own (AO3) and send them directly to your Amazon Kindle device via email.

## Features

- Download AO3 works in EPUB format.
- Send downloaded works to Kindle via email.
- Easy configuration for SMTP settings and Kindle email address.
- Uses file hashes to determine if a fic has been updated.

## Installation

1. Clone the repository
2. Install required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Configure the script:

    Run the following command to generate the configuration file:

    ```bash
    python main.py --configure
    ```

    Follow the prompts to enter your Kindle email address and SMTP server settings.

2. Run the script:

    To process a single AO3 URL:

    ```bash
    python main.py https://archiveofourown.org/works/12345678
    ```

    To process a list of URLs from a file:

    ```bash
    python main.py urls.txt
    ```

    The file `urls.txt` should contain one AO3 URL per line.

## Configuration

The script will create a configuration file at `~/.config/ao3-kindle/conf` (on Unix-based systems) or `C:\Users\<YourUsername>\AppData\Roaming\ao3-kindle\conf` (on Windows) where your SMTP server and Kindle email settings will be saved.

## Notes

- Ensure that your Kindle email address is added to your Amazon account's approved email list.
- Make sure that your SMTP server settings are correct, and that you use an app-specific password if your email provider requires it.
