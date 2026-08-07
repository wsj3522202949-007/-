# -*- coding: utf-8 -*-
"""
chapter_selfcheck.py — 网文单章自检工具（世界级知识库配套）

对齐《最强去AI味铁律.md》黑名单 + 《章法与钩子学.md》五类强钩子。

字数口径（2026-08-05 修正，重要）
--------------------------------
旧实现用 `len(read_text(path))` 直接量**整份文件**，把三样非正文内容算进了字数：

  1. YAML frontmatter（约 250–300 字符）
  2. 文末 `**【章节数据】**` / `**【章末钩子】**` 等创作元信息块
  3. CRLF 换行按 2 字符计（一篇 440 行的稿子平白多出 440）

结果第011章被判「严重超标 4679>4000」，实际正文只有 3417。
更糟的是**钩子判定也被污染**：`【章节数据】` 里的「下章预告：」命中了
禁用空钩子黑名单词「下章」，于是一个强钩子章节被误判成空钩子。

现口径：**正文去除空白字符后的字符数（含标点）**，即
  整份文件 → 去 frontmatter → 去元信息块 → 去所有空白
达标区间由 chapter_policy 配置控制（默认 2600–3400；宽松 ≤4000）。同时附报纯中文字数供参照。

AI 味与钩子扫描同样只在正文上进行，不再被 frontmatter / 元信息块干扰。

指标：
  1. 字数（正文字符，含标点、不含空白）达标区间由 chapter_policy 控制（默认 2600–3400；宽松 ≤4000）。
  2. AI 味：按类别扫描黑名单词/句式，给出 轻度/中度/重度 判定。
  3. 章末钩子：扫描末段是否命中五类强钩子之一，并标记禁用空钩子。

用法：
  python chapter_selfcheck.py 正文/第001章.md
  python chapter_selfcheck.py 正文/            # 扫描目录下全部 *.md
  python chapter_selfcheck.py 正文/第001章.md --json report.json
  python chapter_selfcheck.py 正文/ --raw      # 附带旧口径（整份文件）字符数，便于对账
"""

import os
import sys
import re
import json
import argparse

# 统一篇幅政策（单一来源）：字数标准全部来自 chapter_policy，
# 禁止在此硬编码 2600/3400/4000，以免与 创作闭环助手.py 口径分裂。
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)
from chapter_policy import load_policy, char_verdict

# 终端编码安全：Windows GBK 控制台遇 emoji 会抛 UnicodeEncodeError，
# 重新配置为 UTF-8（errors=replace）保证不崩溃，无需 PYTHONUTF8=1。
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass

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

# 字数口径：标准统一来自 chapter_policy（见文件顶部 import）。
# 不再在此硬编码 2600/3400/4000，避免与 创作闭环助手.py 口径分裂。


# frontmatter：文件开头的 --- ... --- 块
FRONTMATTER_RE = re.compile(r'^---\r?\n.*?\r?\n---\r?\n', re.DOTALL)
# 创作元信息块：**【章节数据】** 之后全部内容属于写作笔记，不是正文。
# 这些块里常含「下章预告」「伏笔」「本章」等词，会同时污染字数、AI味、钩子三项判定。
META_BLOCK_RE = re.compile(
    r'\*\*【\s*(?:章节数据|数据|自检|创作笔记|写作笔记|备注)\s*】\*\*.*$',
    re.DOTALL)
# 行内小标记：**【章末钩子】** 只是排版提示，删标记但保留其后正文
INLINE_MARK_RE = re.compile(r'\*\*【\s*(?:章末钩子|正文|开篇)\s*】\*\*\r?\n?')


def read_text(path):
    """按字节读再解码。原样保留换行，交由 extract_body 归一。"""
    with open(path, "rb") as f:
        return f.read().decode("utf-8", errors="replace")


def extract_body(raw):
    """从整份文件中抽出**正文**。

    依次剥离：frontmatter → 文末元信息块 → 行内排版标记，
    并把 CRLF 归一为 LF（否则每行凭空多算 1 个字符）。
    字数、AI 味、钩子三项判定全部基于本函数的输出。
    """
    s = raw.replace("\r\n", "\n").replace("\r", "\n")
    s = FRONTMATTER_RE.sub("", s)
    s = META_BLOCK_RE.sub("", s)
    s = INLINE_MARK_RE.sub("", s)
    return s.strip()


def count_chars(body):
    """正文字数口径：去除所有空白字符后的字符数（含标点）。"""
    return len(re.sub(r'\s', '', body))


def count_cjk(body):
    """纯中文字数（不含标点/数字/英文），供参照。"""
    return len(re.findall(r'[\u4e00-\u9fff]', body))


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


def check_chapter(path, include_raw=False, policy=None):
    policy = policy or load_policy(path)
    raw = read_text(path)
    body = extract_body(raw)          # 剥离 frontmatter / 元信息块 / 行内标记 + CRLF 归一
    n = count_chars(body)             # 正文去空白字符数（含标点）—— 字数判定唯一口径
    cjk = count_cjk(body)
    raw_len = len(raw)                # 仅 --raw 对账用

    # AI 味 / 钩子 一律在 body 上扫描，不再被 frontmatter、章节数据块污染
    per_cat, total, severe, wa, wa_per_1k = scan_ai(body)
    tail_hits, full_hits, banned = scan_hooks(body)
    ai_v = verdict_ai(per_cat, total, severe, wa_per_1k)

    # 字数判定（正文去空白口径，标准来自 chapter_policy）
    char_v = char_verdict(n, policy)

    # 钩子判定
    if banned:
        hook_v = "禁用空钩子(" + "/".join(banned) + ")"
    elif tail_hits:
        hook_v = "强钩子:" + "/".join(tail_hits.keys())
    elif full_hits:
        hook_v = "钩子在中段(" + "/".join(full_hits.keys()) + ")，末段偏弱"
    else:
        hook_v = "末段无强钩子(疑似空钩)"

    r = {
        "file": os.path.basename(path),
        "chars": n,
        "chars_cjk": cjk,
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
    if include_raw:
        r["raw_chars"] = raw_len
    return r


def print_report(results, show_raw=False, policy=None):
    p = policy or load_policy()
    print("=" * 72)
    print(f"网文单章自检报告  |  字数口径: 正文去空白字符(含标点)  "
          f"| 平台: {p['platform']}  |  政策: {p.get('policy_version', 'v1')}")
    print(f"   目标区间 {p['soft_min']}–{p['soft_max']} (警告,不阻断)  "
          f"硬性区间 {p['hard_min']}–{p['hard_max']} (阻断)")
    print("=" * 72)
    for r in results:
        print(f"\n📄 {r['file']}")
        print(f"   字数      : {r['char_verdict']}  (正文 {r['chars']} 字 / 纯中文 {r['chars_cjk']} 字)")
        if show_raw and "raw_chars" in r:
            print(f"              整份文件旧口径: {r['raw_chars']} 字符")
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
    ap.add_argument("--raw", action="store_true",
                    help="附带旧口径（整份文件字符数）便于对账")
    args = ap.parse_args()

    files = []
    for p in args.paths:
        if os.path.isdir(p):
            for fn in sorted(os.listdir(p)):
                if not fn.lower().endswith(".md"):
                    continue
                # 过滤非正文文件：chapters/README.md 是索引，不是章节正文
                if fn == "README.md":
                    continue
                files.append(os.path.join(p, fn))
        else:
            files.append(p)

    if not files:
        print("未找到 .md 文件", file=sys.stderr)
        sys.exit(1)

    # 统一篇幅政策：以首个路径为锚向上查找 chapter_policy 配置
    policy = load_policy(args.paths[0])
    results = [check_chapter(f, include_raw=args.raw, policy=policy) for f in files]
    print_report(results, show_raw=args.raw, policy=policy)

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"\nJSON 报告已写入: {args.json}")

    # 硬性区间阻断：发现 hard_short/hard_long 时返回非零退出码
    hard_block = [r for r in results
                  if "严重不足" in r["char_verdict"] or "严重超标" in r["char_verdict"]]
    if hard_block:
        names = ", ".join(r["file"] for r in hard_block)
        print(f"\n硬性阻断：以下章节未通过硬性字数校验：{names}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
