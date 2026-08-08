---
id: tool-07273
type: tool
area: 库
status: active
tags: [协议传染, 本地优先, 英文文档, 本地写作]
title: bulk-downloader
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/gochezkerrth/bulk-downloader
created: 2026-07-18
updated: 2026-07-18
no: 7273
category: 画龙补充 / 扩容入库 — 补充源
repo: gochezkerrth/bulk-downloader
stars: 1
url: https://github.com/gochezkerrth/bulk-downloader
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls:
  - "⚠️ 协议带传染性（GPL/AGPL），闭源或商用分发前需谨慎评估合规"
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 125fbfe8d82fae1f
  - methods/QUICK_START.md
---

# gochezkerrth/bulk-downloader

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/gochezkerrth/bulk-downloader
- **Stars**：1
- **语言**：None
- **License**：GPL-3.0
- **Topics**：—
- **GitHub 描述**：personal alternative to Calibre and fanfiction downloader; vibecoding with Claude
- **本地描述**：bulk-downloader
- **拉取时间**：2026-07-25 19:16:15

related:
  - methods/QUICK_START.md
---

# Fanfic Downloader

A powerful, open-source GUI application for downloading and organizing fanfiction from Archive of Our Own (AO3) and FanFiction.Net with support for multiple formats (HTML, PDF, EPUB, MOBI) and comprehensive metadata management.

## Features

- **Bulk Download Support**: Download from bookmarks, collections, author works, series, or batch URLs
- **Multiple Output Formats**: HTML, PDF, EPUB, and MOBI
- **Rich Metadata**: Captures all AO3 tags including title, author, fandoms, series, ratings, warnings, relationships, characters, and more
- **Smart Organization**: Automatically sorts downloads by fandom and author
- **Session Cookie Support**: Download private bookmarks and age-restricted content
- **Advanced Search/Filter**: Built-in GUI with AO3-style filtering capabilities
- **CAPTCHA Handling**: Intelligent handling of CAPTCHA challenges
- **Cross-Platform**: Separate versions for Windows and macOS

## Table of Contents

1. [Installation](#installation)
2. [Session Cookies Explained](#session-cookies-explained)
3. [Quick Start](#quick-start)
4. [Usage Guide](#usage-guide)
5. [Troubleshooting](#troubleshooting)
6. [Development](#development)
7. [License](#license)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning the repository)

### Windows Installation

#### Using PowerShell

1. **Clone the repository:**
```powershell
git clone https://github.com/yourusername/fanfic-downloader.git
cd fanfic-downloader
```

2. **Create a virtual environment:**
```powershell
python -m venv venv
.\venv\Scripts\Activate
```

3. **Install dependencies:**
```powershell
pip install -r requirements-windows.txt
```

4. **Run the application:**
```powershell
python fanfic_downloader/main.py
```

#### Using Anaconda Prompt

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/fanfic-downloader.git
cd fanfic-downloader
```

2. **Create a conda environment:**
```bash
conda create -n fanfic-downloader python=3.9
conda activate fanfic-downloader
```

3. **Install dependencies:**
```bash
pip install -r requirements-windows.txt
```

4. **Run the application:**
```bash
python fanfic_downloader/main.py
```

### macOS Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/fanfic-downloader.git
cd fanfic-downloader
```

2. **Create a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements-mac.txt
```

4. **Run the application:**
```bash
python fanfic_downloader/main.py
```

## Session Cookies Explained

### What is a Session Cookie?

A session cookie is a small piece of data that websites use to remember you're logged in. Think of it as a temporary ID card that proves to the website that you've already entered your username and password. This allows the fanfic downloader to access your private bookmarks and age-restricted content just as if you were browsing the site yourself.

### Why Do I Need It?

- **Access Private Bookmarks**: Download works you've bookmarked privately
- **Age-Restricted Content**: Access mature/explicit content if you're logged in
- **Avoid Rate Limits**: Logged-in users often have more generous download limits
- **Personal Collections**: Access your personal collections and reading history

### How to Get Your Session Cookie

#### For Chrome/Edge:

1. **Log into AO3** with your account
2. **Press F12** to open Developer Tools (or right-click → Inspect)
3. **Click the "Application" tab** (might be under >> if not visible)
4. **In the left sidebar**, expand "Cookies" and click on "archiveofourown.org"
5. **Find the cookie named "_otwarchive_session"**
6. **Copy the entire value** (it's a long string of random characters)

#### For Firefox:

1. **Log into AO3** with your account
2. **Press F12** to open Developer Tools
3. **Click the "Storage" tab**
4. **Expand "Cookies" and click on "https://archiveofourown.org"**
5. **Find "_otwarchive_session"**
6. **Copy the value**

#### For Safari:

1. **Enable Developer Menu**: Safari → Preferences → Advanced → Show Develop menu
2. **Log into AO3**
3. **Develop → Show Web Inspector**
4. **Storage tab → Cookies → archiveofourown.org**
5. **Find and copy "_otwarchive_session" value**

### Security Notes

- **Keep it private**: Your session cookie is like a password - don't share it
- **Temporary**: Session cookies expire (usually after a few hours/days)
- **Refresh when needed**: If downloads stop working, get a fresh cookie
- **Safe usage**: This app stores cookies locally and never transmits them anywhere

## Quick Start

1. **Launch the application**
2. **Paste your session cookie** in the Settings section
3. **Choose download method** (Bookmarks, Series, Batch URLs, etc.)
4. **Select output format** (HTML, PDF, EPUB, or MOBI)
5. **Click "Start Download"**

Downloads are automatically organized by fandom and author in timestamped folders.

## Usage Guide

### Download Methods

#### 1. Author Bookmarks
Download all public and private bookmarks from an author's profile.
- Enter the author's AO3 profile URL
- Option to include only recent bookmarks (past 6 months)
- Automatically captures bookmark notes and tags

#### 2. Collections
Download entire collections or multiple collections at once.
- Paste collection URLs (one per line)
- Supports both public and private collections (with session cookie)
- Maintains collection metadata

#### 3. Single Download
Quick download of individual works.
- Paste the work URL
- Ideal for testing or one-off downloads

#### 4. Batch Download
Download multiple works at once.
- Paste URLs one per line or load from a text file
- Progress tracking for each work
- Continues even if individual downloads fail

#### 5. Author Works
Download all works by a specific author.
- Enter author's AO3 URL
- Options to filter by completion status, word count, or date

#### 6. Series
Download complete series in reading order.
- Paste series URL
- Maintains series metadata and ordering

### File Organization

Files are saved using the following structure:
```
FANFICTION/
├── EFDownloader_20240107/
│   ├── Harry Potter/
│   │   ├── AuthorName/
│   │   │   ├── AuthorName_SeriesName_StoryTitle_15chapters.epub
│   │   │   └── AuthorName_SeriesName_StoryTitle_15chapters_metadata.json
│   └── Marvel/
│       └── DifferentAuthor/
│           ├── DifferentAuthor_AnotherStory_8chapters.pdf
│           └── DifferentAuthor_AnotherStory_8chapters_metadata.json
└── Backups/
    └── backup_20240107_120000/
```

### Metadata Structure

Each download includes a comprehensive metadata JSON file:
```json
{
  "title": "Story Title",
  "author": "AuthorName",
  "fandoms": ["Harry Potter - J. K. Rowling"],
  "series": "Series Name",
  "series_part": 2,
  "chapters": {
    "current": 15,
    "total": 15
  },
  "last_updated": "2024-01-07",
  "rating": "Mature",
  "warnings": ["Creator Chose Not To Use Archive Warnings"],
  "categories": ["F/M", "Gen"],
  "relationships": ["Hermione Granger/Draco Malfoy"],
  "characters": ["Hermione Granger", "Draco Malfoy"],
  "freeform_tags": ["Slow Burn", "Enemies to Lovers"],
  "language": "English",
  "stats": {
    "words": 125000,
    "comments": 450,
    "kudos": 2500,
    "bookmarks": 350,
    "hits": 45000
  },
  "summary": "Work summary here...",
  "notes": {
    "beginning": "Author's beginning notes",
    "end": "Author's end notes"
  }
}
```

### Search and Filter

The built-in search supports:
- **Text search**: Title, author, summary
- **Tag filters**: Rating, warnings, relationships, characters
- **Metadata filters**: Word count, chapter count, completion status
- **Date filters**: Updated within, published date range
- **Sort options**: Title, author, date, word count, kudos

## Troubleshooting

### CAPTCHA Challenges

AO3 occasionally presents CAPTCHA challenges to prevent automated access. Here's how to handle them:

#### Automatic Detection
The app detects CAPTCHA challenges and will:
1. **Pause downloads** immediately
2. **Show a notification** with instructions
3. **Open a browser window** to the CAPTCHA page

#### Manual Resolution
1. **Complete the CAPTCHA** in the opened browser
2. **Stay logged in** to maintain your session
3. **Click "Continue Downloads"** in the app
4. The app will resume using your refreshed session

#### Prevention Tips
- **Space out downloads**: Add delays between downloads (configurable in settings)
- **Vary your pattern**: Don't download hundreds of works in sequence
- **Use during off-peak hours**: Less likely to trigger protection
- **Maintain activity**: Occasionally browse AO3 normally between bulk downloads

### Common Issues

#### "Session Cookie Invalid"
- **Cause**: Cookie expired or copied incorrectly
- **Solution**: Get a fresh cookie following the guide above

#### "Cannot Convert to MOBI"
- **Cause**: MOBI conversion requires additional tools
- **Solution**: Install KindleGen or use the built-in EPUB format

#### "Access Denied" Errors
- **Cause**: Work may be restricted or deleted
- **Solution**: Verify you can access the work while logged in

#### "Connection Timeout"
- **Cause**: Network issues or AO3 server problems
- **Solution**: Check your internet, try again later, or increase timeout in settings

#### Download Speed Issues
- **Cause**: Rate limiting or server load
- **Solution**: Enable download delays in settings (recommended: 2-5 seconds)

### Debug Mode

Enable debug mode for detailed logging:
1. Settings → Advanced → Enable Debug Mode
2. Logs are saved to `fanfic_downloader_debug.log`
3. Include logs when reporting issues

## Development

### Project Structure
```
fanfic-downloader/
├── fanfic_downloader/          # Main package
│   ├── __init__.py
│   ├── main.py                 # GUI application entry
│   ├── core/                   # Core functionality
│   │   ├── __init__.py
│   │   ├── downloader.py       # Download logic
│   │   ├── parser.py           # HTML parsing
│   │   ├── metadata.py         # Metadata handling
│   │   └── converter.py        # Format conversion
│   ├── gui/                    # GUI components
│   │   ├── __init__.py
│   │   ├── main_window.py
│   │   ├── settings.py
│   │   └── search.py
│   └── utils/                  # Utilities
│       ├── __init__.py
│       ├── session.py          # Session management
│       ├── captcha.py          # CAPTCHA handling
│       └── organization.py     # File organization
├── tests/                      # Unit tests
├── docs/                       # Documentation
├── requirements-windows.txt
├── requirements-mac.txt
├── setup.py
├── LICENSE
└── README.md
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Building Executables

#### Windows (.exe)
```powershell
python build_script.py
```

#### macOS (.app)
```bash
python build_mac.py
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](https://github.com/gochezkerrth/bulk-downloader/blob/main/LICENSE) file for details.

This means you are free to:
- Use the software for any purpose
- Change the software to suit your needs
- Share the software with your friends and neighbors
- Share the changes you make

Under the following conditions:
- If you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.
- You must license derivatives under GPL v3.0
- You must document changes made to the code

## Acknowledgments

- AO3 for providing an excellent fanfiction platform
- The fanfiction community for inspiration and feedback
- Contributors and testers who help improve this tool

## Disclaimer

This tool is for personal use only. Please respect authors' wishes and AO3's Terms of Service. Do not use this tool to:
- Redistribute downloaded works without permission
- Circumvent author-requested download restrictions
- Violate copyright or intellectual property rights
- Create archives that compete with AO3

Always support authors by leaving kudos and comments on works you enjoy!

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/gochezkerrth/bulk-downloader)
[![GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge)](https://www.gnu.org/licenses/gpl-3.0)
