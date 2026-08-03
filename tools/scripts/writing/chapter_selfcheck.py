# -*- coding: utf-8 -*-
"""
chapter_selfcheck.py — 网文单章自检工具（世界级知识库配套）

对齐《最强去AI味铁律.md》黑名单 + 《章法与钩子学.md》五类强钩子。
指标：
  1. 字数（总字符，对齐 PowerShell `(Get-Content -Raw).Length` 口径，含标点换行）
     达标区间 2600–3400；宽松 2600–4000。
  2. AI 味：按类别扫描黑名单词/句式，给出 轻度/中度/重度 判定。
  3. 章末钩子：扫描末段是否命中五类强钩子之一，并标记禁用空钩子。

用法：
  python chapter_selfcheck.py 正文/第001章.md
  python chapter_selfcheck.py 正文/            # 扫描目录下全部 *.md
  python chapter_selfcheck.py 正文/第001章.md --json report.json
"""

import os
import sys
import re
import json
import argparse

# ---------------------------------------------------------------------------
# 1. AI 味黑名单（来源：最强去AI味铁律.md §二~§十，分门别类）
#    每类：短语列表。脚本统计命中次数并按类别汇总。
# ---------------------------------------------------------------------------
BLACKLIST = {
    "套话收束": ["值得注意的是", "毫无疑问", "诚然", "综上所述", "归根结底", "本质上",
               "让我来解释", "希望这有帮助", "毕竟", "想必"],
    "对比骨架": [],  # 由 REGEX_PATTERNS 中的"不是A而是B"句式检测，避免"不是"单独误判
    "表演性动宾": ["实现了", "推动了", "促进了", "彰显了", "体现了", "见证了", "标志着",
               "深深植根于", "不可磨灭的印记", "关键转折点"],
    "无源权威": ["研究表明", "数据显示", "行业专家认为", "有研究指出", "据说", "业内人士认为"],
    "空泛判断": ["意义重大", "核心价值在于", "真正理解了", "关键作用", "影响深远",
               "长远来看", "站在更高维度"],
    "虚假强调": ["真正的", "唯一的", "毫无疑问的", "至关重要的"],
    "工程词泄露": ["第X章", "上章", "前文", "后文", "伏笔", "细纲", "读者", "本章"],
    "网文最毒句": ["，带着", "声音不大", "语气毫无波澜", "平静无波", "眼中闪过一丝",
               "嘴角勾起一抹", "心中涌起一股", "心头一震", "这一刻终于明白",
               "命运", "棋局", "獠牙", "反击才刚刚开始", "他不知道的是",
               "她不知道的是", "殊不知", "冥冥之中", "仿佛预示着"],
    "高频词": ["不禁", "仿佛", "映入眼帘", "心中暗道", "沉声道", "嘴角微扬",
             "不由自主", "只见", "此时此刻"],
    "意义膨胀": ["意义深远", "前所未有", "可谓"],
    "万能结论": ["未来可期", "充满希望", "前途无量"],
    "论文体": ["不难看出", "由此可见", "事实上", "综上所述"],
    "书面语连词": ["于是乎", "与此同时", "从而", "因而"],
    "解释腔上帝视角": ["之所以", "这是因为", "这意味着", "正是因为", "多年以后",
                  "演得真好", "他就是这样", "她就是这样"],
    "升华式收尾": ["命运终于露出獠牙", "属于他的反击才刚刚开始", "终于明白了", "真谛"],
}

# 最高优先级句式：命中任一即判「重度 AI 味」（★★★★★ / 升华 / 上帝视角）
SEVERE_PHRASES = [
    "他不知道的是", "她不知道的是", "殊不知", "冥冥之中", "仿佛预示着",
    "命运终于露出獠牙", "属于他的反击才刚刚开始",
    "声音不大", "语气毫无波澜", "平静无波", "眼中闪过一丝", "嘴角勾起一抹",
    "心中涌起一股", "心头一震",
]

# 需上下文的句式（正则检测，避免单独字误判）
REGEX_PATTERNS = {
    "对比骨架(不是A而是B)": r"不是.{0,25}而是",
    "对比骨架(与其不如)": r"与其.{0,25}不如",
    "命运棋局/獠牙": r"命运.{0,12}(棋局|獠牙)",
}

# 弱化副词：频率型（每千字 >3 视为 AI 签名）
WEAK_ADV = ["微微", "淡淡", "缓缓", "轻轻"]

# ---------------------------------------------------------------------------
# 2. 五类强钩子关键词（来源：章法与钩子学.md §3.1）
# ---------------------------------------------------------------------------
HOOK_KEYWORDS = {
    "信息炸弹": ["没想到", "竟然", "原来", "真相", "秘密", "居然", "竟是", "揭穿",
              "根本不是", "其实就是", "谁也想不到", "系统", "任务生成", "解锁",
              "奖励", "叮", "提示"],
    "危机降临": ["危机", "危险逼近", "逼近", "倒计时", "迫在眉睫", "即将到来",
              "威胁", "悬于", "断供", "崩盘", "围剿", "只剩", "最后期限", "麻烦", "拦路"],
    "决策时刻": ["抓起", "冲出", "转身就", "深吸一口气", "汇报方案", "他决定",
              "她决定", "选择了", "一把抓起", "分工", "计划", "准备", "明天起",
              "下一步", "说干就干", "明儿"],
    "打脸预示": ["反派", "对手", "狂笑", "领奖", "蔑视", "不屑", "令牌",
              "嘴角一扯", "冷笑", "所有人以为", "种子", "拦不住", "长出来", "拱破"],
    "身份暴露": ["摘下", "面具", "真实身份", "暴露", "揭开", "露出", "原来他是",
              "竟是", "摘掉"],
}

# 章末禁用空钩子（来源：章法与钩子学.md §3.4 / §5.1）
BANNED_TAIL = ["下回分解", "且看下回", "欲知", "下章", "且听下回", "未完待续"]

# 字数口径
CHAR_MIN = 2600
CHAR_MAX = 3400
CHAR_LOOSE_MAX = 4000


def read_text(path):
    """按字节读再解码，保留 \\r\\n，对齐 PowerShell Get-Content -Raw .Length。"""
    with open(path, "rb") as f:
        return f.read().decode("utf-8", errors="replace")


def scan_ai(raw):
    """返回 (per_cat: dict, total: int, severe_hits: list)。"""
    per_cat = {}
    total = 0
    for cat, phrases in BLACKLIST.items():
        c = 0
        for p in phrases:
            c += raw.count(p)
        if c:
            per_cat[cat] = c
            total += c
    # 上下文句式检测（正则）
    for label, pat in REGEX_PATTERNS.items():
        m = len(re.findall(pat, raw))
        if m:
            per_cat[label] = m
            total += m
    severe = [p for p in SEVERE_PHRASES if p in raw]
    # 弱化副词频率
    wa = sum(raw.count(w) for w in WEAK_ADV)
    wa_per_1k = wa * 1000 / max(len(raw), 1)
    return per_cat, total, severe, wa, wa_per_1k


def scan_hooks(raw):
    """扫描全文 + 末段，返回 五类命中计数（末段）与 全文计数。"""
    tail = raw[-max(300, len(raw) // 6):]
    tail_hits = {}
    full_hits = {}
    for htype, kws in HOOK_KEYWORDS.items():
        t = sum(tail.count(k) for k in kws)
        f = sum(raw.count(k) for k in kws)
        if t:
            tail_hits[htype] = t
        if f:
            full_hits[htype] = f
    banned = [b for b in BANNED_TAIL if b in tail]
    return tail_hits, full_hits, banned


def verdict_ai(per_cat, total, severe, wa_per_1k):
    if severe or total >= 12 or wa_per_1k > 3:
        return "重度"
    if total >= 6 or wa_per_1k > 2:
        return "中度"
    if total >= 2:
        return "轻度"
    return "干净"


def check_chapter(path):
    raw = read_text(path)
    n = len(raw)
    per_cat, total, severe, wa, wa_per_1k = scan_ai(raw)
    tail_hits, full_hits, banned = scan_hooks(raw)
    ai_v = verdict_ai(per_cat, total, severe, wa_per_1k)

    # 字数判定
    if n < CHAR_MIN:
        char_v = f"不足({n}<{CHAR_MIN})"
    elif n > CHAR_MAX:
        char_v = f"超标({n}>{CHAR_MAX})" if n <= CHAR_LOOSE_MAX else f"严重超标({n}>{CHAR_LOOSE_MAX})"
    else:
        char_v = f"达标({n})"

    # 钩子判定
    if banned:
        hook_v = "禁用空钩子(" + "/".join(banned) + ")"
    elif tail_hits:
        hook_v = "强钩子:" + "/".join(tail_hits.keys())
    elif full_hits:
        hook_v = "钩子在中段(" + "/".join(full_hits.keys()) + ")，末段偏弱"
    else:
        hook_v = "末段无强钩子(疑似空钩)"

    return {
        "file": os.path.basename(path),
        "chars": n,
        "char_verdict": char_v,
        "ai_total": total,
        "ai_per_cat": per_cat,
        "ai_severe": severe,
        "ai_weak_adv_per_1k": round(wa_per_1k, 2),
        "ai_verdict": ai_v,
        "hook_tail": tail_hits,
        "hook_full": full_hits,
        "hook_verdict": hook_v,
    }


def print_report(results):
    print("=" * 72)
    print("网文单章自检报告  |  字数口径: 总字符(含标点换行) 达标 2600–3400")
    print("=" * 72)
    for r in results:
        print(f"\n📄 {r['file']}")
        print(f"   字数      : {r['char_verdict']}")
        print(f"   AI 味     : {r['ai_verdict']}  (总命中 {r['ai_total']} | 弱副词 {r['ai_weak_adv_per_1k']}/千字)")
        if r["ai_per_cat"]:
            cat_str = "  ".join(f"{k}×{v}" for k, v in r["ai_per_cat"].items())
            print(f"             分类: {cat_str}")
        if r["ai_severe"]:
            print(f"             重度信号: {'  '.join(r['ai_severe'])}")
        print(f"   章末钩子  : {r['hook_verdict']}")
        if r["hook_tail"]:
            print(f"             末段命中: {'  '.join(f'{k}×{v}' for k, v in r['hook_tail'].items())}")
    print("\n" + "=" * 72)
    # 汇总
    n_files = len(results)
    ok_char = sum(1 for r in results if "达标" in r["char_verdict"])
    clean_ai = sum(1 for r in results if r["ai_verdict"] == "干净")
    good_hook = sum(1 for r in results if "强钩子" in r["hook_verdict"])
    print(f"汇总: {n_files} 篇 | 字数达标 {ok_char} | AI味干净 {clean_ai} | 末段强钩子 {good_hook}")
    print("=" * 72)


def main():
    ap = argparse.ArgumentParser(description="网文单章自检工具")
    ap.add_argument("paths", nargs="+", help="章节 .md 文件，或含 .md 的目录")
    ap.add_argument("--json", help="把报告写入指定 JSON 文件", default=None)
    args = ap.parse_args()

    files = []
    for p in args.paths:
        if os.path.isdir(p):
            for fn in sorted(os.listdir(p)):
                if fn.lower().endswith(".md"):
                    files.append(os.path.join(p, fn))
        else:
            files.append(p)

    if not files:
        print("未找到 .md 文件", file=sys.stderr)
        sys.exit(1)

    results = [check_chapter(f) for f in files]
    print_report(results)

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"\nJSON 报告已写入: {args.json}")


if __name__ == "__main__":
    main()
