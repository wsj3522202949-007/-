#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
shared_wordcount.py — 统一字数统计模块

本模块定义项目唯二字数统计口径，供所有脚本（自检、STATUS、README）共用。

口径（2026-08-05 定稿）
-----------------------
**正文去空白字符后的字符数（含标点）**，即：
  整份文件 → 去 frontmatter → 去元信息块 → 去所有空白字符（含换行、空格、全角空格）

达标区间：2600-3400（严格）/ 2600-4000（宽松）

使用方法
--------
    from shared_wordcount import extract_body, count_chars, count_file, ProjectCounter

    # 单文件
    body = extract_body(read_text("第011章.md"))
    n = count_chars(body)                     # 正文字数
    cjk = count_cjk(body)                     # 纯中文字数（供参照）

    # 单文件快捷
    result = count_file("第011章.md")          # 返回 dict

    # 批量统计整个项目
    counter = ProjectCounter("projects/（已删除项目）")
    counter.scan_all()
    print(counter.report())                   # 生成 Markdown 片段
"""
from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Optional

import sys
# Windows GBK 终端安全：避免 emoji/中文输出 UnicodeEncodeError
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass


# ---------------------------------------------------------------------------
# 1. 正文提取规则（与 chapter_selfcheck.py 保持一致）
# ---------------------------------------------------------------------------

# frontmatter：文件开头的 --- ... --- 块
FRONTMATTER_RE = re.compile(r'^---\r?\n.*?\r?\n---\r?\n', re.DOTALL)
# 创作元信息块：**【<标题>】** 之后全部内容属于写作笔记，不是正文。
# 注意：同 chapter_selfcheck.py —— 旧正则只匹配「数据」后紧跟 】，漏掉「数据预估」格式。
META_BLOCK_RE = re.compile(
    r'\*\*【\s*(?:章节数据|数据预估|数据统计|数据|预估|统计|自检|'
    r'创作笔记|写作笔记|备注|复盘|记录|完读率|追读率)\s*】\*\*.*$',
    re.DOTALL)
# 行内小标记：**【章末钩子】** 等排版标记，删标记但保留其后正文
INLINE_MARK_RE = re.compile(r'\*\*【\s*(?:章末钩子|正文|开篇)\s*】\*\*\r?\n?')


def read_text(path: str | Path) -> str:
    """按字节读再解码 UTF-8。"""
    with open(path, "rb") as f:
        return f.read().decode("utf-8", errors="replace")


def extract_body(raw: str) -> str:
    """从整份文件中抽出**正文**。

    依次剥离：frontmatter → 文末元信息块 → 行内排版标记，
    并把 CRLF 归一为 LF（否则每行凭空多算 1 个字符）。
    """
    s = raw.replace("\r\n", "\n").replace("\r", "\n")
    s = FRONTMATTER_RE.sub("", s)
    s = META_BLOCK_RE.sub("", s)
    s = INLINE_MARK_RE.sub("", s)
    return s.strip()


def extract_frontmatter(raw: str) -> dict[str, str]:
    """提取 YAML frontmatter 为简易字典（纯文本，非完整 YAML 解析）。"""
    m = re.match(r'^---\r?\n(.*?)\r?\n---', raw, re.DOTALL)
    if not m:
        return {}
    result: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            result[key.strip()] = val.strip().strip('"').strip("'")
    return result


# ---------------------------------------------------------------------------
# 2. 字数统计函数
# ---------------------------------------------------------------------------


def count_chars(body: str) -> int:
    """正文字数口径：去除所有空白字符后的字符数（含标点）。"""
    return len(re.sub(r'\s', '', body))


def count_cjk(body: str) -> int:
    """纯中文字数（不含标点/数字/英文），供参照。"""
    return len(re.findall(r'[\u4e00-\u9fff]', body))


def count_file(path: str | Path) -> dict:
    """统计单文件，返回含多口径的字典。

    返回字段:
        file          : 文件名
        body_chars    : 正文去空白字符数（主口径）
        body_cjk      : 纯中文字数
        frontmatter_wc: frontmatter 中 word_count 字段值（若存在）
        raw_bytes     : 整份文件字节数
        raw_chars     : 整份文件字符数（含 frontmatter / 空白）
    """
    raw = read_text(path)
    body = extract_body(raw)
    fm = extract_frontmatter(raw)
    fm_wc = int(fm["word_count"]) if "word_count" in fm else None
    return {
        "file": os.path.basename(path),
        "body_chars": count_chars(body),
        "body_cjk": count_cjk(body),
        "frontmatter_wc": fm_wc,
        "raw_bytes": os.path.getsize(path),
        "raw_chars": len(raw),
    }


# ---------------------------------------------------------------------------
# 3. 项目批量统计
# ---------------------------------------------------------------------------


class ProjectCounter:
    """对整个项目目录做统一字数统计。

    用法:
        counter = ProjectCounter("projects/（已删除项目）")
        counter.scan_all()
        print(counter.summary_text())   # 单行摘要
        print(counter.report())         # 完整 Markdown 报告
    """

    def __init__(self, project_dir: str | Path):
        self.project_dir = Path(project_dir)
        self.chapters_dir = self.project_dir / "chapters"
        self.results: list[dict] = []
        self._total_chars = 0
        self._total_cjk = 0
        self._total_fm_wc = 0
        self._fm_wc_count = 0

    def scan_all(self) -> list[dict]:
        """扫描 chapters/ 下所有 .md 文件并统计。"""
        self.results = []
        self._total_chars = 0
        self._total_cjk = 0
        self._total_fm_wc = 0
        self._fm_wc_count = 0

        if not self.chapters_dir.exists():
            return self.results

        for f in sorted(self.chapters_dir.iterdir()):
            if not f.name.lower().endswith(".md"):
                continue
            # 跳过非章节文件（如 README.md）
            if not re.match(r'第\d+章-', f.name):
                continue
            r = count_file(f)
            self.results.append(r)
            self._total_chars += r["body_chars"]
            self._total_cjk += r["body_cjk"]
            if r["frontmatter_wc"] is not None:
                self._total_fm_wc += r["frontmatter_wc"]
                self._fm_wc_count += 1

        return self.results

    @property
    def total_chars(self) -> int:
        return self._total_chars

    @property
    def total_cjk(self) -> int:
        return self._total_cjk

    @property
    def avg_chars(self) -> float:
        if not self.results:
            return 0.0
        return self._total_chars / len(self.results)

    @property
    def avg_fm_wc(self) -> Optional[float]:
        if self._fm_wc_count == 0:
            return None
        return self._total_fm_wc / self._fm_wc_count

    def summary_text(self) -> str:
        """返回单行摘要，如 '11 章 / 25,929 字 / 均 2,357 字'"""
        n = len(self.results)
        return f"{n} 章 / {self._total_chars:,} 字 / 均 {self.avg_chars:,.0f} 字"

    def report(self) -> str:
        """返回 Markdown 报告片段，可直接嵌入 STATUS.md。"""
        lines = [
            "| 指标 | 数值 | 备注 |",
            "|---|---|---|",
            f"| 总章节数 | {len(self.results)} 章 | — |",
            f"| 正文总字数 | {self._total_chars:,} 字 | 去空白字符口径，均 {self.avg_chars:,.0f} 字/章 |",
            f"| 纯中文字数 | {self._total_cjk:,} 字 | 不含标点/数字，供参照 |",
        ]

        if self._fm_wc_count > 0:
            diff = self._total_chars - self._total_fm_wc
            if diff != 0:
                lines.append(
                    f"| ⚠️ frontmatter 合计 | {self._total_fm_wc:,} 字 | "
                    f"与正文口径差 {diff:+,} 字，frontmatter 数据可能过期 |"
                )
            else:
                lines.append(
                    f"| frontmatter 合计 | {self._total_fm_wc:,} 字 | 与正文口径一致 ✅ |"
                )

        lines.append("")
        lines.append("> 统计口径：正文去空白字符(含标点)，由 `shared_wordcount.py` 统一计算。")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# 4. CLI 入口
# ---------------------------------------------------------------------------


def main():
    import argparse

    ap = argparse.ArgumentParser(description="统一字数统计工具")
    ap.add_argument("paths", nargs="*", default=None,
                    help="章节 .md 文件路径，或项目目录路径（默认扫描当前项目）")
    ap.add_argument("--json", action="store_true", help="输出 JSON 格式")
    ap.add_argument("--detail", action="store_true", help="列出每章明细")
    args = ap.parse_args()

    # 默认路径：脚本在 tools/scripts/writing/，项目在 ROOT/projects/（已删除项目）
    script_dir = os.path.dirname(os.path.abspath(__file__))       # .../writing/
    scripts_dir = os.path.dirname(script_dir)                     # .../scripts/
    tools_dir = os.path.dirname(scripts_dir)                      # .../tools/
    root_dir = os.path.dirname(tools_dir)                         # 知识库根目录
    default_project = os.path.join(root_dir, "projects", "（已删除项目）")
    paths = args.paths or [default_project]

    for p in paths:
        p_abs = os.path.abspath(p)
        if os.path.isdir(p_abs) and "chapters" in os.listdir(p_abs):
            # 项目目录模式
            counter = ProjectCounter(p_abs)
            counter.scan_all()
            if args.json:
                import json
                print(json.dumps(counter.results, ensure_ascii=False, indent=2))
            else:
                print(f"📊 项目: {os.path.basename(p_abs)}")
                print(f"   总章数: {len(counter.results)}")
                print(f"   正文总字数: {counter.total_chars:,}")
                print(f"   纯中文字数: {counter.total_cjk:,}")
                print(f"   平均每章: {counter.avg_chars:,.0f} 字")
                if args.detail:
                    print()
                    print("   明细:")
                    for r in counter.results:
                        fm_tag = f" (fm: {r['frontmatter_wc']})" if r["frontmatter_wc"] else ""
                        print(f"     {r['file']}: {r['body_chars']:,} 字{fm_tag}")
        else:
            # 单文件模式
            r = count_file(p_abs)
            if args.json:
                import json
                print(json.dumps(r, ensure_ascii=False, indent=2))
            else:
                print(f"📄 {r['file']}")
                print(f"   正文去空白: {r['body_chars']} 字")
                print(f"   纯中文:     {r['body_cjk']} 字")
                if r["frontmatter_wc"] is not None:
                    tag = "✅" if r["frontmatter_wc"] == r["body_chars"] else "⚠️"
                    print(f"   frontmatter: {r['frontmatter_wc']} 字 {tag}")
                print(f"   文件字节:    {r['raw_bytes']}")
                print(f"   文件字符:    {r['raw_chars']}")


if __name__ == "__main__":
    main()