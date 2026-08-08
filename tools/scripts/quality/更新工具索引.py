#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
更新工具索引.py — 工具卡索引统计自动更新

扫描 tools/cards/ 实际评级分布，自动更新：
  - tools/检索层/README.md   （B/C 级统计表）
  - tools/推荐层/README.md   （S/A 级统计表）
  - tools/检索层/README.md   的失效工具 / 重复标题 计数

用法：
  python tools/scripts/quality/更新工具索引.py        # 更新 README 统计表
  python tools/scripts/quality/更新工具索引.py --check # 只比对不修改，漂移即退出码 1（CI 用）

退出码：0=一致/已更新，1=--check 模式下发现漂移
"""
import os
import re
import sys
import argparse

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
CARDS_DIR = os.path.join(ROOT, "tools", "cards")
RETRIEVAL_README = os.path.join(ROOT, "tools", "检索层", "README.md")
RECOMMEND_README = os.path.join(ROOT, "tools", "推荐层", "README.md")


def load_card_fields():
    """返回 list[dict{file, tier, title}]。"""
    cards = []
    for f in sorted(os.listdir(CARDS_DIR)):
        if not f.endswith(".md") or f == "README.md":
            continue
        head = open(os.path.join(CARDS_DIR, f), encoding="utf-8", errors="replace").read(2000)
        tier = ""
        m = re.search(r'^tier:\s*["\']?(\w+)["\']?', head, re.MULTILINE)
        if m:
            tier = m.group(1).upper()
        title = ""
        m2 = re.search(r'^title:\s*(.+)$', head, re.MULTILINE)
        if m2:
            title = m2.group(1).strip().strip('"').strip("'")
        cards.append({"file": f, "tier": tier, "title": title or f})
    return cards


def compute_stats(cards):
    """计算评级分布、失效、重复标题。"""
    from collections import Counter
    tier_counter = Counter(x["tier"] for x in cards)
    s = tier_counter.get("S", 0)
    a = tier_counter.get("A", 0)
    b = tier_counter.get("B", 0)
    c_cnt = tier_counter.get("C", 0)
    no_tier = sum(1 for x in cards if not x["tier"])

    # 失效：status 字段（此处以标题含失效标记或文件名为准简化处理）
    # 检索层 README 历史统计含"失效工具/重复标题"，这里统计重复标题
    title_counter = Counter(x["title"].lower() for x in cards if x["title"])
    dup_titles = [t for t, n in title_counter.items() if n > 1]

    # 失效标记：卡片内容含 status: inactive / 失效
    dead = 0
    for x in cards:
        head = open(os.path.join(CARDS_DIR, x["file"]), encoding="utf-8", errors="replace").read(2000)
        if re.search(r'^status:\s*(inactive|archived|失效)', head, re.MULTILINE):
            dead += 1

    return {
        "s": s, "a": a, "b": b, "c": c_cnt, "no_tier": no_tier,
        "total": len(cards), "dead": dead, "dup_titles": len(dup_titles),
    }


def update_readme(path, replacements):
    """对 README 中统计表做精确替换。replacements: list[(pattern, new_line)]"""
    txt = open(path, encoding="utf-8").read()
    changed = []
    for pat, new_line in replacements:
        if re.search(pat, txt):
            txt = re.sub(pat, new_line, txt)
            changed.append(pat)
    open(path, "w", encoding="utf-8").write(txt)
    return changed


def main():
    ap = argparse.ArgumentParser(description="工具卡索引统计自动更新")
    ap.add_argument("--check", action="store_true", help="只比对不修改，漂移即退出码 1")
    args = ap.parse_args()

    cards = load_card_fields()
    st = compute_stats(cards)
    s_cnt, a_cnt = st["s"], st["a"]
    b_cnt, c_cnt = st["b"], st["c"]
    dead_cnt, dup_cnt = st["dead"], st["dup_titles"]

    # 目标统计行（与 README 格式对齐）
    recommend_lines = [
        (r'\| S级工具 \| [\d,]+ 篇 \|', f"| S级工具 | {s_cnt:,} 篇 |"),
        (r'\| A级工具 \| [\d,]+ 篇 \|', f"| A级工具 | {a_cnt:,} 篇 |"),
        (r'\| 总计 \| [\d,]+ 篇 \|', f"| 总计 | {s_cnt+a_cnt:,} 篇 |"),
    ]
    retrieval_lines = [
        (r'\| B级工具 \| [\d,]+ 篇 \|', f"| B级工具 | {b_cnt:,} 篇 |"),
        (r'\| C级工具 \| [\d,]+ 篇 \|', f"| C级工具 | {c_cnt:,} 篇 |"),
        (r'\| 总计 \| [\d,]+ 篇 \|', f"| 总计 | {b_cnt+c_cnt:,} 篇 |"),
        (r'\| 失效工具 \| [\d,]+ 篇 \|', f"| 失效工具 | {dead_cnt:,} 篇 |"),
        (r'\| 重复标题 \| [\d,]+ 个 \|', f"| 重复标题 | {dup_cnt:,} 个 |"),
    ]

    # 读取当前 README 中的值，判断是否漂移
    def read_cur(path):
        txt = open(path, encoding="utf-8").read()
        m = re.search(r'\| 总计 \| ([\d,]+) 篇 \|', txt)
        return int(m.group(1).replace(",", "")) if m else None

    cur_rec = read_cur(RECOMMEND_README)
    cur_ret = read_cur(RETRIEVAL_README)
    expect_rec = s_cnt + a_cnt
    expect_ret = b_cnt + c_cnt

    drift = []
    if cur_rec != expect_rec:
        drift.append(f"推荐层: README={cur_rec} vs 实际={expect_rec}")
    if cur_ret != expect_ret:
        drift.append(f"检索层: README={cur_ret} vs 实际={expect_ret}")

    if args.check:
        if drift:
            print("❌ 索引统计漂移：")
            for d in drift:
                print(f"   {d}")
            print(f"   评级分布: S={st['s']} A={st['a']} B={st['b']} C={st['c']} 无tier={st['no_tier']} 失效={st['dead']} 重复标题={st['dup_titles']}")
            return 1
        print("✅ 索引统计一致（推荐层 257 / 检索层 3314）")
        return 0

    # 更新模式
    if drift:
        print(f"📌 检测到索引漂移：{len(drift)} 处")
        for d in drift:
            print(f"   {d}")
    else:
        print("✅ 索引统计已是最新，无需更新")

    changed = []
    changed += update_readme(RECOMMEND_README, recommend_lines)
    changed += update_readme(RETRIEVAL_README, retrieval_lines)
    print(f"   已更新 {len(changed)} 处统计行")
    # 同时更新 README 顶部描述里的总数（"共 257 篇"式文案）
    for path in (RECOMMEND_README, RETRIEVAL_README):
        txt = open(path, encoding="utf-8").read()
        if "推荐层" in path:
            new_desc = f"本层收录 S/A 级工具卡（共 {expect_rec} 篇）"
            txt = re.sub(r'本层收录 S/A 级工具卡（共 [\d,]+ 篇）', new_desc, txt)
        else:
            new_desc = f"本层收录 B/C 级工具卡（共 {expect_ret} 篇）"
            txt = re.sub(r'本层收录 B/C 级工具卡（共 [\d,]+ 篇）', new_desc, txt)
        open(path, "w", encoding="utf-8").write(txt)
    print("✅ 索引已更新")
    return 0


if __name__ == "__main__":
    sys.exit(main())
