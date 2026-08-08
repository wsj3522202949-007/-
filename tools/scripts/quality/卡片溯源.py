#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
卡片溯源.py —— 工具卡三层架构（原始/蒸馏/可信）与溯源元数据
================================================================

背景
----
tools/cards/ 现有 3572 张工具卡，frontmatter 缺溯源元数据：
  source_kind（原始层/蒸馏层/可信层）、spdx（许可证）、
  fetched_at（抓取日期）、content_hash（内容哈希）。
"世界级检索评估"不能凭感觉相信卡片内容——必须先锁定卡片来源与内容版本。

三层定义
--------
  raw       原始层：从 GitHub 等直接抓取的仓库卡片（有 source/repo，未深度加工）
  distilled 蒸馏层：经过人工/LLM 提炼（use_case/pitfalls 等深度字段非空）
  trusted   可信层：HTTP 已验证可达 + SPDX 许可证明确 + 内容哈希锁定

用法
----
  python 卡片溯源.py --scan          # 扫描并生成溯源报告（只读）
  python 卡片溯源.py --backfill      # 为缺失字段批量补默认值（写 frontmatter）
  python 卡片溯源.py --report PATH   # 指定报告输出路径（默认 tools/reports/卡片溯源.md）
"""

import os
import re
import sys
import json
import hashlib
import argparse
from datetime import datetime

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass

_FIELDS = ("source_kind", "spdx", "fetched_at", "content_hash")


def find_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "tools", "cards")):
            return d
        d = os.path.dirname(d)
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def parse_fm(text):
    if not text.startswith("---"):
        return None, 0
    lines = text.split("\n")
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, 0
    fm = {}
    for line in lines[1:end]:
        m = re.match(r'^([A-Za-z_][\w-]*):\s*(.*)$', line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"')
    return fm, end


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()[:16]  # 短哈希，足够锁定内容版本


def infer_source_kind(fm):
    """推断三层归属（启发式，backfill 时写入）。"""
    use_case = (fm.get("use_case") or "").strip()
    pitfalls = (fm.get("pitfalls") or "").strip()
    has_deep = len(use_case) > 20 or (pitfalls and pitfalls not in ("[]", ""))
    has_source = bool(fm.get("source") or fm.get("repo"))
    if has_deep and has_source:
        return "distilled"
    if has_source:
        return "raw"
    return "raw"  # 无 source 也按 raw 兜底（源头缺失需人工补）


def scan_cards(root):
    """扫描全部卡片，返回 (cards, stats)。"""
    card_dir = os.path.join(root, "tools", "cards")
    cards = []
    for fname in sorted(os.listdir(card_dir)):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(card_dir, fname)
        try:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
        except OSError:
            continue
        fm, _ = parse_fm(text)
        if fm is None:
            cards.append({"file": fname, "no_frontmatter": True})
            continue
        c = {
            "file": fname,
            "id": fm.get("id", "?"),
            "title": (fm.get("title") or fname)[:40],
            "content_hash": sha256_file(path),
            "has_source": bool(fm.get("source") or fm.get("repo")),
            "source_kind": fm.get("source_kind", ""),
            "spdx": fm.get("spdx", ""),
            "fetched_at": fm.get("fetched_at", ""),
            "inferred_kind": infer_source_kind(fm),
        }
        cards.append(c)
    return cards


def report_markdown(root, cards, gen_time):
    total = len(cards)
    with_kind = sum(1 for c in cards if c.get("source_kind"))
    with_spdx = sum(1 for c in cards if c.get("spdx"))
    with_fetched = sum(1 for c in cards if c.get("fetched_at"))
    with_hash = sum(1 for c in cards if c.get("content_hash"))
    no_fm = sum(1 for c in cards if c.get("no_frontmatter"))

    lines = [
        f"# 工具卡溯源报告（{gen_time}）",
        "",
        f"> 卡片总数：{total} 张 ｜ 已含 source_kind：{with_kind} ｜ "
        f"已含 SPDX：{with_spdx} ｜ 已含 fetched_at：{with_fetched} ｜ "
        f"已含 content_hash：{with_hash} ｜ 无 frontmatter：{no_fm}",
        "",
        "## 三层分布（含推断）",
        "",
        "| 层 | 数量 | 说明 |",
        "|---|---|---|",
    ]
    by_kind = {}
    for c in cards:
        if c.get("no_frontmatter"):
            continue
        k = c.get("source_kind") or c.get("inferred_kind") or "raw"
        by_kind[k] = by_kind.get(k, 0) + 1
    for k in ("raw", "distilled", "trusted"):
        lines.append(f"| {k} | {by_kind.get(k, 0)} | 见脚本头部定义 |")
    lines.append("")
    lines.append("## 缺失溯源字段清单（需 backfill 或人工补）")
    lines.append("")
    lines.append("| 文件 | 缺 source_kind | 缺 SPDX | 缺 fetched_at | 缺 content_hash |")
    lines.append("|---|---|---|---|---|")
    shown = 0
    for c in cards:
        if c.get("no_frontmatter"):
            lines.append(f"| {c['file']} | 无 frontmatter | - | - | - |")
            shown += 1
            continue
        missing = [k for k in ("source_kind", "spdx", "fetched_at", "content_hash")
                   if not c.get(k)]
        if missing:
            lines.append(f"| {c['file'][:50]} | "
                         f"{'❌' if 'source_kind' in missing else '✅'} | "
                         f"{'❌' if 'spdx' in missing else '✅'} | "
                         f"{'❌' if 'fetched_at' in missing else '✅'} | "
                         f"{'❌' if 'content_hash' in missing else '✅'} |")
            shown += 1
            if shown >= 60:
                lines.append(f"| …（其余 {sum(1 for c in cards if [k for k in _FIELDS if not c.get(k)]) - 60} 行略） |")
                break
    if shown == 0:
        lines.append("| （无缺失） | | | | |")
    lines.append("")
    lines.append("> 由 卡片溯源.py 生成 · backfill 前不修改任何卡片")
    return "\n".join(lines)


def backfill(root, cards):
    """为缺失字段批量补默认值（写 frontmatter）。"""
    card_dir = os.path.join(root, "tools", "cards")
    today = datetime.now().strftime("%Y-%m-%d")
    updated = 0
    for c in cards:
        if c.get("no_frontmatter"):
            continue
        path = os.path.join(card_dir, c["file"])
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        fm, fm_end = parse_fm(text)
        if fm is None:
            continue
        changed = False
        additions = []
        # 更新已有字段或收集新字段
        for key, val in (
            ("source_kind", c["inferred_kind"]),
            ("spdx", "unknown"),           # SPDX 需人工确认，先标 unknown
            ("fetched_at", c.get("fetched_at") or fm.get("created") or today),
            ("content_hash", c["content_hash"]),
        ):
            if fm.get(key):
                continue
            additions.append((key, val))
            changed = True
        if not changed:
            continue
        # 插到 frontmatter 末尾（--- 之前）
        lines = text.split("\n")
        insert_at = fm_end - 1
        new_lines = lines[:insert_at] + \
            [f"{k}: {v}" for k, v in additions] + lines[insert_at:]
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines))
        updated += 1
    return updated


def main():
    ap = argparse.ArgumentParser(description="工具卡三层溯源扫描器")
    ap.add_argument("--root", default=None)
    ap.add_argument("--scan", action="store_true", help="生成溯源报告（只读）")
    ap.add_argument("--backfill", action="store_true", help="批量补默认溯源字段")
    ap.add_argument("--report", default=None, help="报告输出路径")
    args = ap.parse_args()

    root = os.path.abspath(args.root) if args.root else find_root()
    cards = scan_cards(root)
    gen_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if args.backfill:
        n = backfill(root, cards)
        print(f"已 backfill {n} 张卡片的溯源字段（source_kind/spdx/fetched_at/content_hash）")
        print(f"提示：SPDX 统一标为 unknown，需按仓库实际许可证人工确认。")
        # backfill 后重扫
        cards = scan_cards(root)

    report_path = args.report or os.path.join(root, "tools", "reports", "卡片溯源.md")
    md = report_markdown(root, cards, gen_time)
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"溯源报告: {report_path}")
    print(f"  总数 {len(cards)} | 缺 source_kind: "
          f"{sum(1 for c in cards if not c.get('source_kind') and not c.get('no_frontmatter'))} | "
          f"缺 SPDX: {sum(1 for c in cards if not c.get('spdx') and not c.get('no_frontmatter'))} | "
          f"缺 fetched_at: {sum(1 for c in cards if not c.get('fetched_at') and not c.get('no_frontmatter'))} | "
          f"缺 content_hash: {sum(1 for c in cards if not c.get('content_hash') and not c.get('no_frontmatter'))}")


if __name__ == "__main__":
    main()
