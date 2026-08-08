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

阻断语义（exit 1，与统一门禁 run_all.py 章节自检一致）：
  硬字数越界（严重不足/严重超标）· 重度AI味 · 禁用空钩子/末段无强钩子
  跨章重复段落 · 模板化句子（≥3 章重复）
"""

import os
import sys
import re
import json
import zlib
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
# 创作元信息块：**【<标题>】** 之后全部内容属于写作笔记，不是正文。
# 注意：实际文件用的标题是「数据预估」而非「章节数据」——旧正则在「数据」后
# 用 \s* 期望紧跟 】，遇到「预估」即失配，导致数据块被算进正文（字数虚高 +
# 钩子判定污染）。现把常见变体全部列入，防止再次出现格式漂移刷分。
META_BLOCK_RE = re.compile(
    r'\*\*【\s*(?:章节数据|数据预估|数据统计|数据|预估|统计|自检|'
    r'创作笔记|写作笔记|备注|复盘|记录|完读率|追读率)\s*】\*\*.*$',
    re.DOTALL)
# 行内小标记：**【章末钩子】** 只是排版提示，删标记但保留其后正文
INLINE_MARK_RE = re.compile(r'\*\*【\s*(?:章末钩子|正文|开篇)\s*】\*\*\r?\n?')
# 章末钩子区起点（钩子唯一性检查需要单独提取这段正文）
HOOK_ZONE_MARK_RE = re.compile(r'\*\*【\s*章末钩子\s*】\*\*\r?\n?')


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


def extract_hook_zone(raw):
    """提取**【章末钩子】**标记之后的正文钩子区（到元信息块或文末为止）。

    钩子唯一性检查需要这一区域：不能拿整章正文去比（会把叙事主体也算进去），
    也不能被尾部「数据预估」块污染（那里含「下一章/钩子强度」等模板词）。
    没有钩子标记时返回空串（由钩子判定/钩子唯一性自行处理）。
    """
    s = raw.replace("\r\n", "\n").replace("\r", "\n")
    s = FRONTMATTER_RE.sub("", s)
    m = HOOK_ZONE_MARK_RE.search(s)
    if not m:
        return ""
    zone = s[m.end():]
    mm = META_BLOCK_RE.search(zone)
    if mm:
        zone = zone[:mm.start()]
    # 去掉尾部纯分隔线（---）
    zone = re.sub(r'\n?-{3,}\s*$', '', zone)
    return zone.strip()


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
    if total >= 1:
        return "微量"
    return "干净"


def find_cross_chapter_duplicates(chapters_dir, threshold=0.80, min_para_len=30):
    """检测 chapters/ 目录下跨章重复段落。

    返回 list[dict]，每项包含 {file_a, file_b, para_a, para_b, similarity}。
    相似度 >= threshold 且段落长度 >= min_para_len 才视为问题。
    """
    import os as _os
    import difflib as _dl

    results = []
    files = sorted([
        f for f in _os.listdir(chapters_dir)
        if f.endswith('.md') and f.startswith('第') and f != 'README.md'
    ])
    if len(files) < 2:
        return results

    # 预加载所有章节的去 frontmatter 正文
    bodies = {}
    for fname in files:
        raw = read_text(_os.path.join(chapters_dir, fname))
        bodies[fname] = extract_body(raw)
    # 逐对比较
    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            f1, f2 = files[i], files[j]
            b1, b2 = bodies[f1], bodies[f2]
            paras1 = [p.strip() for p in b1.split('\n\n') if len(p.strip()) >= min_para_len]
            paras2 = [p.strip() for p in b2.split('\n\n') if len(p.strip()) >= min_para_len]
            for p1 in paras1:
                for p2 in paras2:
                    ratio = _dl.SequenceMatcher(None, p1, p2).ratio()
                    if ratio >= threshold:
                        results.append({
                            "file_a": f1,
                            "file_b": f2,
                            "para_a": p1[:120],
                            "para_b": p2[:120],
                            "similarity": round(ratio, 2),
                        })
    return results


def find_cross_chapter_template_sentences(chapters_dir, min_chapters=3, min_sent_len=5):
    """检测跨章「模板化句子」——同一句话出现在 >= min_chapters 章。

    模板化是 AI 写作的典型指纹：段落级检测（find_cross_chapter_duplicates）
    用 min_para_len 过滤了短句，而结尾模板恰恰由短句组成，因此会漏检。
    本函数按句号/问号/感叹号切分正文，统计跨章重复句子。

    返回 (template_sents, chapter_hits)：
      template_sents: list[dict] {sentence, chapters, count}
      chapter_hits:   dict[chapter] -> int（该章命中的模板句子数）
    """
    import os as _os
    import re as _re

    files = sorted([
        f for f in _os.listdir(chapters_dir)
        if f.endswith('.md') and f.startswith('第') and f != 'README.md'
    ])
    if len(files) < 2:
        return [], {}

    sent_owner = {}
    for fname in files:
        body = extract_body(read_text(_os.path.join(chapters_dir, fname)))
        # 切分句子（保留结尾标点），忽略纯空白
        sents = _re.split(r'(?<=[。！？…])', body)
        for s in sents:
            s = s.strip()
            # 过滤太短（<5 字符）与过长（>60，多为段落误拼）的"句子"
            if len(s) < min_sent_len or len(s) > 60:
                continue
            # 跳过明显的模板外围噪音（引号配对不完整时句内引号）
            sent_owner.setdefault(s, []).append(fname)

    template_sents = []
    for s, owners in sorted(sent_owner.items(), key=lambda x: -len(set(x[1]))):
        uniq = sorted(set(owners))
        if len(uniq) >= min_chapters:
            template_sents.append({
                "sentence": s,
                "chapters": uniq,
                "count": len(uniq),
            })

    chapter_hits = {}
    for t in template_sents:
        for ch in t["chapters"]:
            chapter_hits[ch] = chapter_hits.get(ch, 0) + 1
    return template_sents, chapter_hits


# ===========================================================================
# 反「指标刷分」检测（2026-08-08）
# ---------------------------------------------------------------------------
# 背景：旧门禁只查「≥30字段落、相似度≥0.80」的跨章重复，作者用短句/短段落
# 复制即可绕过——实测 81 个跨章完全重复段落（最短约 12 字）、"宿主，系统的
# 声音带着一丝意味深长，你确定吗？"在 6 章逐字重复，仍被判定「强钩子/达标」。
# 新增五道检测，全部基于 extract_body 后的纯正文：
#   1. 跨章精确重复段落（去空白 ≥12 字、≥2 章）
#   2. 跨章重复短语（句子级，去空白 ≥12 字、≥2 章；口头禅白名单可豁免）
#   3. MinHash 近似重复段落（字符 5-gram 签名，Jaccard ≥0.85）
#   4. SimHash 章节整体相似度（64-bit 指纹，汉明距离 ≤10 → WARN）
#   5. 章末钩子唯一性（各章【章末钩子】区域两两相似度 ≥0.80 → 钩子雷同）
# 白名单文件：项目目录下 chapter_oral_tic.txt，每行一条，# 开头为注释，
# 从章节目录向上查找（与 chapter_policy 的查找方式一致）。
# ===========================================================================

def _chapter_files(chapters_dir):
    """目录下按名排序的章节 .md 文件（排除 README）。"""
    return sorted([
        f for f in os.listdir(chapters_dir)
        if f.endswith('.md') and f.startswith('第') and f != 'README.md'
    ])


def _norm(s):
    """去空白归一（字数口径：正文去空白字符）。"""
    return re.sub(r'\s', '', s)


def _chapter_bodies(chapters_dir):
    """{fname: extract_body(...)} 全量预读，供多道检测共用。"""
    return {f: extract_body(read_text(os.path.join(chapters_dir, f)))
            for f in _chapter_files(chapters_dir)}


def find_exact_duplicate_paras(chapters_dir, min_len=12, whitelist=()):
    """跨章完全重复段落：去空白后 ≥min_len 字、出现在 ≥2 章。

    旧检测 find_cross_chapter_duplicates 用 min_para_len=30 + 相似度 0.80，
    短句复制（如 "宿主，系统的声音带着一丝意味深长，你确定吗？"）全部漏检，
    作者借此「凑字数 + 模板钩子」刷过门禁。本函数用精确匹配 + 低长度阈值堵住。

    whitelist：口头禅白名单——段落包含任一白名单项（如系统面板 UI）即豁免。
    """
    files = _chapter_files(chapters_dir)
    if len(files) < 2:
        return []
    owner = {}
    for fname in files:
        body = _chapter_bodies(chapters_dir).get(fname, "")
        for p in body.split("\n\n"):
            np = _norm(p)
            if len(np) >= min_len:
                owner.setdefault(np, set()).add(fname)
    dups = []
    for np, chs in owner.items():
        if len(chs) > 1:
            if any(w and w in np for w in whitelist):
                continue
            dups.append({"para": np[:120], "chapters": sorted(chs),
                         "count": len(chs)})
    dups.sort(key=lambda d: (-d["count"], -len(d["para"])))
    return dups


def find_repeated_phrases(chapters_dir, min_len=12, min_chapters=2, whitelist=()):
    """跨章重复短语：句子级（。！？… 切分）去空白 ≥min_len 字、≥min_chapters 章。

    whitelist 为口头禅白名单：短语**包含**任一白名单项即视为作者有意的口头禅，
    予以豁免（如 "叮"、"系统的声音带着一丝意味深长" 等系统文套路若属人物设定）。
    """
    files = _chapter_files(chapters_dir)
    if len(files) < 2:
        return []
    owner = {}
    for fname in files:
        body = _chapter_bodies(chapters_dir).get(fname, "")
        for s in re.split(r'(?<=[。！？…])', body):
            np = _norm(s)
            if len(np) >= min_len:
                owner.setdefault(np, set()).add(fname)
    out = []
    for np, chs in owner.items():
        if len(chs) < min_chapters:
            continue
        if any(w and w in np for w in whitelist):
            continue
        out.append({"phrase": np[:120], "chapters": sorted(chs), "count": len(chs)})
    out.sort(key=lambda d: (-d["count"], -len(d["phrase"])))
    return out


def find_duplicate_sequences(chapters_dir, window=3, min_total_len=20,
                             min_chapters=2, whitelist=()):
    """跨章段落序列重复：连续 window 段（空行分段）归一拼接后精确匹配。

    单段检测的盲区：模板结尾常由**若干短段组成**——"宿主…你确定吗？"/
    "确定。"/"那就明天见。"每段都不足 12 字，但整套序列在 6 章逐字复制。
    本函数按段落滑动窗口，把「整套结尾」作为一个整体指纹来比对。

    whitelist：序列拼接后包含任一白名单项（如系统面板 UI）即豁免。
    """
    files = _chapter_files(chapters_dir)
    if len(files) < 2:
        return []
    owner = {}
    for fname in files:
        body = _chapter_bodies(chapters_dir).get(fname, "")
        paras = [p for p in body.split("\n\n")]
        for i in range(0, max(1, len(paras) - window + 1)):
            seq = paras[i:i + window]
            np = _norm("".join(seq))
            if len(np) < min_total_len:
                continue
            owner.setdefault(np, set()).add(fname)
    out = []
    for np, chs in owner.items():
        if len(chs) < min_chapters:
            continue
        if any(w and w in np for w in whitelist):
            continue
        out.append({"sequence": np[:140], "chapters": sorted(chs),
                    "count": len(chs)})
    out.sort(key=lambda d: (-d["count"], -len(d["sequence"])))
    return out


# ---------------------------------------------------------------------------
# MinHash / SimHash 近似重复检测（无第三方依赖）
# ---------------------------------------------------------------------------
def _shingles(text, k=5):
    """字符 k-gram 集合（去空白后）。"""
    t = _norm(text)
    if len(t) <= k:
        return {t} if t else set()
    return {t[i:i + k] for i in range(len(t) - k + 1)}


def _crc(s):
    return zlib.crc32(s.encode("utf-8")) & 0xFFFFFFFF


def find_near_duplicate_paras(chapters_dir, min_len=12, threshold=0.68,
                              shingle_len=5, min_shared=3, whitelist=()):
    """近似重复段落：经改写/换词但仍高度雷同的段落（MinHash 思想的精确形态）。

    实现：字符 5-gram 倒排生成候选段对（共享 ≥min_shared 个 shingle），再按
    shingle 集合的 Jaccard 判定（不采样、不估计——短段上比 64 位 MinHash
    签名估计更稳）。跨章比对，同章内不查。

    jaccard ∈ [threshold, 1.0) 报近似重复；jaccard = 1.0 的完全重复段由
    find_exact_duplicate_paras 负责，此处不重复报告。

    实测校准（2026-08-08）：真实数据呈双峰分布——不相关段对 jaccard 均为
    0.0~0.05（29684 对无一介于 0.05~0.68），重复/改写段 ≥0.70；改 2 处短语
    的短段（65 字）jaccard≈0.70、长段（77 字）≈0.74。故阈值取 0.68 无误报空间。
    """
    files = _chapter_files(chapters_dir)
    paras = []
    for fname in files:
        for p in _chapter_bodies(chapters_dir).get(fname, "").split("\n\n"):
            np = _norm(p)
            if len(np) >= min_len:
                paras.append((fname, np))
    if len(paras) < 2:
        return []
    inv = {}
    for i, (_, np) in enumerate(paras):
        for s in _shingles(np, shingle_len):
            inv.setdefault(s, set()).add(i)
    cand = {}
    for s, ids in inv.items():
        ids = sorted(ids)
        for a in range(len(ids)):
            for b in range(a + 1, len(ids)):
                key = (ids[a], ids[b])
                cand[key] = cand.get(key, 0) + 1
    results = []
    for (i, j), shared in cand.items():
        if shared < min_shared:
            continue
        fa, pa = paras[i]
        fb, pb = paras[j]
        if fa == fb:
            continue
        # 白名单豁免：任一段包含系统面板 UI 等口头禅项即跳过
        if any(w and (w in pa or w in pb) for w in whitelist):
            continue
        # 长度悬殊的段落直接跳过（近似重复应篇幅相近）
        if abs(len(pa) - len(pb)) > max(15, 0.4 * min(len(pa), len(pb))):
            continue
        sh_a = _shingles(pa, shingle_len)
        sh_b = _shingles(pb, shingle_len)
        if not sh_a or not sh_b:
            continue
        jac = len(sh_a & sh_b) / len(sh_a | sh_b)
        if threshold <= jac < 1.0:
            results.append({
                "chapter_a": fa, "chapter_b": fb,
                "para_a": pa[:120], "para_b": pb[:120],
                "similarity": round(jac, 2),
            })
    seen, uniq = set(), []
    for r in sorted(results, key=lambda d: -d["similarity"]):
        k = (r["chapter_a"], r["chapter_b"], r["para_a"][:40])
        if k in seen:
            continue
        seen.add(k)
        uniq.append(r)
    return uniq


def _simhash(text, bits=64, shingle_len=5):
    """文本 64-bit 指纹（字符 k-gram 位加权）。"""
    sh = _shingles(text, shingle_len)
    if not sh:
        return 0
    v = [0] * bits
    for s in sh:
        h = _crc(s)
        for b in range(bits):
            v[b] += 1 if (h >> (b % 32)) & 1 else -1
    return sum(1 << b for b in range(bits) if v[b] > 0)


def _hamming(a, b):
    return bin(a ^ b).count("1")


def chapter_simhash_report(chapters_dir, max_hamming=10, shingle_len=5):
    """章节整体相似度：两章正文 simhash 汉明距离 ≤max_hamming 报 WARN。

    语义：不是抄袭判定，而是「这两章全文指纹过于接近」的风险提示——
    常见于大量复制-粘贴式写作。阈值经 13 章实测（同作者正常分布 30+）。
    """
    files = _chapter_files(chapters_dir)
    if len(files) < 2:
        return []
    sigs = {}
    for fname in files:
        sigs[fname] = _simhash(_chapter_bodies(chapters_dir).get(fname, ""),
                               shingle_len=shingle_len)
    out = []
    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            a, b = files[i], files[j]
            d = _hamming(sigs[a], sigs[b])
            if d <= max_hamming:
                out.append({"chapter_a": a, "chapter_b": b,
                            "hamming": d,
                            "similarity": round(1 - d / 64, 2)})
    out.sort(key=lambda x: -x["similarity"])
    return out


def check_hook_uniqueness(chapters_dir, threshold=0.80):
    """章末钩子唯一性：各章【章末钩子】区域两两相似度 ≥threshold → 钩子雷同。

    旧钩子判定只看末段是否命中强钩子关键词，作者把同一套钩子场景
    （如"明天见—失眠—看天花板—不会再错过"）复制到多章仍被判「强钩子」。
    本检查比较钩子区正文本身，堵住「关键词命中但内容雷同」的刷分。
    """
    files = _chapter_files(chapters_dir)
    zones = {}
    for fname in files:
        z = extract_hook_zone(read_text(os.path.join(chapters_dir, fname)))
        if len(_norm(z)) >= 15:
            zones[fname] = z
    if len(zones) < 2:
        return []
    import difflib
    out = []
    names = sorted(zones)
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = names[i], names[j]
            r = difflib.SequenceMatcher(None, zones[a], zones[b]).ratio()
            if r >= threshold:
                out.append({"chapter_a": a, "chapter_b": b,
                            "similarity": round(r, 2)})
    out.sort(key=lambda x: -x["similarity"])
    return out


# ---------------------------------------------------------------------------
# 口头禅白名单（项目可配置）
# ---------------------------------------------------------------------------
_ORAL_TIC_NAMES = ("chapter_oral_tic.txt", "oral_tic.txt")


def load_oral_tic_whitelist(start_dir=None):
    """从 start_dir（文件或目录）向上查找口头禅白名单文件。

    每行一条，# 开头为注释。找不到返回空元组（不豁免任何短语）。
    """
    base = os.path.abspath(start_dir) if start_dir else os.getcwd()
    if not os.path.isdir(base):
        base = os.path.dirname(base)
    cur = base
    for _ in range(10):
        for name in _ORAL_TIC_NAMES:
            cand = os.path.join(cur, name)
            if os.path.isfile(cand):
                items = []
                try:
                    with open(cand, "r", encoding="utf-8") as fh:
                        for line in fh:
                            line = line.strip()
                            if line and not line.startswith("#"):
                                items.append(line)
                except OSError:
                    return ()
                return tuple(items)
        parent = os.path.dirname(cur)
        if parent == cur:
            break
        cur = parent
    return ()


# ---------------------------------------------------------------------------
# 目录级质量扫描（统一入口：main 目录模式与 run_all 门禁共用，杜绝双轨）
# ---------------------------------------------------------------------------
def scan_chapter_dir(chapters_dir, label=None):
    """目录级章节质量扫描，返回 (errors, warns)。

    含：精确重复段落 / 重复短语 / MinHash 近似重复 / SimHash 章节相似 /
    钩子唯一性 / 跨章重复(0.8,30) / 模板化句子。label 用于错误消息中的路径显示。
    """
    errors, warns = [], []
    rel = label or os.path.basename(chapters_dir) or chapters_dir
    whitelist = load_oral_tic_whitelist(chapters_dir)

    # —— 跨章重复（四类粒度归并为一条 ERROR；细分清单见 生成清债清单.py）——
    dups = find_cross_chapter_duplicates(chapters_dir)
    exact = find_exact_duplicate_paras(chapters_dir, whitelist=whitelist)
    phrases = find_repeated_phrases(chapters_dir, whitelist=whitelist)
    seqs = find_duplicate_sequences(chapters_dir, whitelist=whitelist)
    rep_parts = []
    if exact:
        rep_parts.append(f"完全重复段落{len(exact)}")
    if phrases:
        rep_parts.append(f"重复短语{len(phrases)}")
    if seqs:
        rep_parts.append(f"序列重复{len(seqs)}")
    if dups:
        rep_parts.append(f"段落重复(≥30字/80%){len(dups)}")
    if rep_parts:
        examples = []
        for d in exact[:2]:
            examples.append(f"“{d['para']}”×{d['count']}章")
        for d in seqs[:2]:
            examples.append(f"“{d['sequence'][:30]}…”×{d['count']}章")
        if not examples and dups:
            d = dups[0]
            examples.append(f"“{d['para_a']}”↔“{d['para_b']}”")
        errors.append(
            f"跨章重复共 {'、'.join(rep_parts)}"
            + (f"（示例: {'；'.join(examples)}）" if examples else "")
            + f": {rel}/"
            + (" [口头禅白名单已豁免部分]" if whitelist else ""))

    near = find_near_duplicate_paras(chapters_dir, whitelist=whitelist)
    if near:
        top = "；".join(f"{d['chapter_a'][:10]}↔{d['chapter_b'][:10]}({d['similarity']})"
                        for d in near[:5])
        errors.append(f"近似重复段落(改写式,Jaccard≥0.68) {len(near)} 对（示例: {top}）: {rel}/")

    for s in chapter_simhash_report(chapters_dir):
        warns.append(
            f"章节整体指纹高度相近 {s['chapter_a'][:14]} ↔ {s['chapter_b'][:14]}"
            f" (sim {s['similarity']}): {rel}/")

    hk = check_hook_uniqueness(chapters_dir)
    if hk:
        top = "；".join(f"{h['chapter_a'][:10]}↔{h['chapter_b'][:10]}({h['similarity']})"
                        for h in hk[:5])
        errors.append(f"章末钩子雷同 {len(hk)} 对（示例: {top}）: {rel}/")

    tpl, _hits = find_cross_chapter_template_sentences(chapters_dir)
    if tpl:
        errors.append(f"模板化句子(≥3章重复) {len(tpl)} 个: {rel}/")

    return errors, warns


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

    # —— 目录级质量扫描（跨章重复 / 模板句 / 精确重复 / 短语 / 近似重复 /
    #    SimHash / 钩子唯一性，全部由 scan_chapter_dir 统一判定）——
    gate_errors, gate_warns = [], []
    for p in args.paths:
        if os.path.isdir(p):
            errs, wns = scan_chapter_dir(p)
            gate_errors += errs
            gate_warns += wns
            for w in wns:
                print(f"\nℹ️ 警告：{w}")
            for e in errs:
                print(f"\n⚠️ {e}")

            # —— 详细诊断打印（保留逐对信息，帮助定位）——
            dups = find_cross_chapter_duplicates(p)
            if dups:
                print("\n⚠️ 跨章重复段落详情：")
                print("-" * 72)
                for d in dups:
                    print(f"  [{d['file_a']}] ↔ [{d['file_b']}] 相似度 {d['similarity']:.0%}")
                    print(f"    A: {d['para_a']}...")
                    print(f"    B: {d['para_b']}...")
                    print()
                print("⚠️ 跨章重复属于严重质量问题，建议修改或删除重复段落")

            # —— 模板化句子检测（短句重复，AI 写作指纹）——
            tpl_sents, chapter_hits = find_cross_chapter_template_sentences(p)
            if tpl_sents:
                print(f"\n⚠️ 模板化句子检测：{len(tpl_sents)} 个句子在 ≥3 章重复出现")
                print("-" * 72)
                for t in tpl_sents[:20]:
                    print(f"  [{t['count']}章] {t['chapters'][:4]}{'...' if t['count']>4 else ''} | \"{t['sentence']}\"")
                print()
                worst = sorted(chapter_hits.items(), key=lambda x: -x[1])
                print("  受影响最重的章节：")
                for ch, n in worst[:6]:
                    print(f"    {ch[:16]}：{n} 个模板句")
                print("\n⚠️ 模板化结尾/台词属于严重质量问题（AI 复制指纹），必须逐章差异化重写")
            break  # 只检查第一个目录

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"\nJSON 报告已写入: {args.json}")

    # 硬性阻断（与统一门禁 run_all.py 的章节自检语义一致）：
    # 1) 硬字数区间越界（严重不足/严重超标）
    hard_block = [r for r in results
                  if "严重不足" in r["char_verdict"] or "严重超标" in r["char_verdict"]]
    # 2) 重度 AI 味
    heavy_ai = [r for r in results if r["ai_verdict"] == "重度"]
    # 3) 章末无强钩子 / 禁用空钩子
    bad_hook = [r for r in results
                if r["hook_verdict"] == "末段无强钩子(疑似空钩)"
                or r["hook_verdict"].startswith("禁用空钩子")]

    blocked = []
    if hard_block:
        blocked.append("硬性字数越界: " + ", ".join(r["file"] for r in hard_block))
    if heavy_ai:
        blocked.append("重度AI味: " + ", ".join(r["file"] for r in heavy_ai))
    if bad_hook:
        blocked.append("章末无强钩子/禁用空钩子: "
                       + ", ".join(r["file"] for r in bad_hook))
    if blocked:
        for msg in blocked:
            print(f"\n硬性阻断：{msg}", file=sys.stderr)
        sys.exit(1)

    # 目录级质量阻断（scan_chapter_dir 汇总）
    if gate_errors:
        print("\n硬性阻断：目录级章节质量检查未通过：", file=sys.stderr)
        for e in gate_errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
