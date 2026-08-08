---
id: tool-07491
type: tool
area: 库
status: active
tags: [Python, 本地优先, 英文文档, 本地写作]
title: noveldown
summary: 上述两类主题的补充源，按子主题二次筛选
source: https://github.com/potatoeggy/noveldown
created: 2026-07-18
updated: 2026-07-18
no: 7491
category: 画龙补充 / 扩容入库 — 补充源
repo: potatoeggy/noveldown
stars: 9
url: https://github.com/potatoeggy/noveldown
tier: "B"
use_case: "上述两类主题的补充源，按子主题二次筛选"
pitfalls: []
related:
source_kind: raw
spdx: unknown
fetched_at: 2026-07-18
content_hash: 51165a1a4cb1f340
  - methods/QUICK_START.md
---

# potatoeggy/noveldown

- **分类**：画龙补充 / 扩容入库 — 补充源
- **链接**：https://github.com/potatoeggy/noveldown
- **Stars**：9
- **语言**：Python
- **License**：LGPL-3.0
- **Topics**：converter, downloader, ebook, python, webnovel
- **GitHub 描述**：Webnovel to EPUB downloader
- **本地描述**：noveldown
- **拉取时间**：2026-07-25 19:23:31

related:
  - methods/QUICK_START.md
---

# Noveldown

![Supported Python versions](https://img.shields.io/pypi/pyversions/noveldown)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Download from PyPI](https://img.shields.io/pypi/v/noveldown)](https://pypi.org/project/noveldown)
[![Download from the AUR](https://img.shields.io/aur/version/noveldown-git)](https://aur.archlinux.org/packages/noveldown-git)
[![Latest release](https://img.shields.io/github/v/release/potatoeggy/noveldown?display_name=tag)](https://github.com/potatoeggy/noveldown/releases/latest)
[![License](https://img.shields.io/github/license/potatoeggy/noveldown)](/LICENSE)

Webnovel downloader and converter to EPUB (with metadata!) as a Python library and command line application.

## Supported stories

To request a new story, please file a [new issue](https://github.com/potatoeggy/noveldown/issues/new).

- [The Wandering Inn](https://wanderinginn.com) - pirate aba
- [A Practical Guide to Evil](https://practicalguidetoevil.wordpress.com) - ErraticErrata
- [Pale](https://palewebserial.wordpress.com/) - Wildbow
- [Claw](https://https://clawwebserial.blog/) - Wildbow

## Installation

Install the package from PyPI:

```
pip3 install noveldown
```

Arch Linux users may also install the package from the [AUR](https://aur.archlinux.org/packages/noveldown-git.git):

```
git clone https://aur.archlinux.org/noveldown-git.git
makepkg -si
```

Or, to build from source:

Noveldown depends on [poetry](https://github.com/python-poetry/poetry) for building.

```
git clone https://github.com/potatoeggy/noveldown.git
poetry install
poetry build
pip3 install dist/noveldown*.whl
```

## Usage

To download the novel as an EPUB:

```
noveldown <ID>

# for example:
noveldown WanderingInn
```

IDs can be found through `noveldown --supported-ids`

Append the `--start` and `--end` options to limit the number of chapters downloaded.

Run `noveldown --help` for more info.

## Library Usage

```python
import noveldown

noveldown.download("WanderingInn", "./")
```
