#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
创作闭环助手
============

辅助完成创作闭环的7个步骤：
1. 找细纲
2. 写草稿
3. 正文自检
4. 去 AI 味处理
5. 移入正式章节
6. 更新项目进度
7. 追读/完读复盘

用法
----
    python tools/scripts/创作闭环助手.py --next-chapter          # 获取下一章细纲
    python tools/scripts/创作闭环助手.py --template <chapter>    # 生成创作模板
    python tools/scripts/创作闭环助手.py --self-check <file>     # 正文自检
    python tools/scripts/创作闭环助手.py --remove-ai <file>      # 去 AI 味处理
    python tools/scripts/创作闭环助手.py --move-chapter <num>    # 移入正式章节
    python tools/scripts/创作闭环助手.py --update-progress <num> # 更新项目进度
    python tools/scripts/创作闭环助手.py --review               # 追读/完读复盘
"""

import os
import re
import sys
import json
import shutil
import glob
from pathlib import Path
from datetime import datetime

# 脚本目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))

# 统一篇幅政策 + 字数口径（与 chapter_selfcheck / shared_wordcount 一致，禁止各自硬编码魔数）
WRITING_DIR = os.path.join(SCRIPT_DIR, "writing")
if WRITING_DIR not in sys.path:
    sys.path.insert(0, WRITING_DIR)
from chapter_policy import load_policy, char_status
from shared_wordcount import extract_body, count_chars

# Windows GBK 终端安全：避免 emoji/中文输出 UnicodeEncodeError
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass


# 项目目录
PROJECTS_DIR = os.path.join(ROOT_DIR, "projects")

# 当前项目
CURRENT_PROJECT = "（已删除项目）"


def get_project_dir():
    """获取当前项目目录"""
    return os.path.join(PROJECTS_DIR, CURRENT_PROJECT)


def get_current_progress():
    """获取当前进度——以 chapters/ 目录为唯一真源。

    直接扫描 chapters/ 下的 第NNN章-xxx.md 文件，取最大编号。
    不再依赖 STATUS.md 的正则（该正则长期与 STATUS 实际格式不匹配，
    导致返回 0 → --next-chapter 永远返回第1章）。
    """
    project_dir = get_project_dir()
    chapters_dir = os.path.join(project_dir, "chapters")
    if not os.path.isdir(chapters_dir):
        return 0

    max_chapter = 0
    for fname in os.listdir(chapters_dir):
        m = re.match(r'^第(\d{3})章-.+\.md$', fname)
        if m:
            max_chapter = max(max_chapter, int(m.group(1)))
    return max_chapter


def get_next_chapter_outline():
    """获取下一章细纲（兼容「第N章：标题」与「第A-B章：标题」区间写法）"""
    project_dir = get_project_dir()
    outline_file = os.path.join(project_dir, "outline-第一卷.md")
    
    if not os.path.exists(outline_file):
        return None
    
    current_chapter = get_current_progress()
    next_chapter = current_chapter + 1
    
    with open(outline_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
        # 匹配所有章节标题（单章或区间）
        headers = list(re.finditer(
            r'###\s*第(\d+)(?:-(\d+))?章[：:]\s*(.+?)\n', content))
        for h in headers:
            start = int(h.group(1))
            end = int(h.group(2)) if h.group(2) else start
            if start <= next_chapter <= end:
                body_start = h.end()
                nxt = re.search(r'\n###\s', content[body_start:])
                body_end = body_start + (nxt.start() if nxt else len(content) - body_start)
                block = content[h.start():body_end]
                return {
                    "chapter": next_chapter,
                    "title": h.group(3).strip(),
                    "content": block,
                    "is_range": end > start,
                }
    
    return None


def generate_chapter_template(chapter_num):
    """生成章节模板——带双守卫验证。

    守卫 1：chapter_num 必须等于下一章（chapters/ 最大编号 + 1），否则拒绝。
    守卫 2：目标文件不得已存在于 chapters/ 或 drafts/，否则拒绝。
    """
    project_dir = get_project_dir()
    policy = load_policy(project_dir)

    # —— 守卫 1：必须为下一章 ——
    current = get_current_progress()
    expected = current + 1
    if chapter_num != expected:
        print(f"错误：当前进度为第 {current} 章，下一章应为第 {expected} 章，"
              f"不能直接生成第 {chapter_num} 章")
        sys.exit(1)

    # —— 守卫 2：目标文件不得已存在 ——
    chapters_dir = os.path.join(project_dir, "chapters")
    drafts_dir = os.path.join(project_dir, "..", "drafts", "projects",
                               CURRENT_PROJECT)
    target_name = f"第{chapter_num:03d}章"
    for check_dir in [chapters_dir, drafts_dir]:
        if os.path.isdir(check_dir):
            for fname in os.listdir(check_dir):
                if fname.startswith(target_name):
                    print(f"错误：{target_name} 已存在于 {check_dir}，"
                          f"拒绝重复生成")
                    sys.exit(1)
    outline = get_next_chapter_outline()
    
    if not outline:
        print(f"错误：找不到第 {chapter_num} 章的细纲")
        return None
    
    # 提取标题
    title_match = re.search(r'第\d+章：(.+)', outline['content'])
    title = title_match.group(1) if title_match else f"第{chapter_num}章"
    
    # 提取核心任务（兼容「核心任务」与「目标」两种写法）
    task_match = re.search(r'(?:核心任务|目标)[：:]\s*(.+)', outline['content'])
    task = task_match.group(1) if task_match else ""
    
    # 提取爽点引擎
    climax_match = re.search(r'爽点引擎[：:]\s*(.+)', outline['content'])
    climax = climax_match.group(1) if climax_match else ""
    
    # 提取章末钩子
    hook_match = re.search(r'章末钩子[：:]\s*(.+)', outline['content'])
    hook = hook_match.group(1) if hook_match else ""
    
    template = f"""---
id: ch{chapter_num:03d}
type: chapter
area: 项目
status: draft
tags: [第{chapter_num}章, {title}]
title: 第{chapter_num}章：{title}
summary: {task}
word_count: 0
created: {datetime.now().strftime("%Y-%m-%d")}
updated: {datetime.now().strftime("%Y-%m-%d")}
chapter: {chapter_num}
volume: 1
---

# 第{chapter_num}章：{title}

{task}

---

## 场景设计

{outline['content']}

---

## 正文

（在此开始写正文）

---

## 自检清单

- [ ] 字数达标（软目标 {policy['soft_min']}-{policy['soft_max']}字，硬下限 ≥{policy['hard_min']}，硬上限 ≤{policy['hard_max']}）
- [ ] 章首有钩子
- [ ] 章末有钩子
- [ ] 爽点密度达标（每800字一个小高潮）
- [ ] 无 AI 味
- [ ] 人物性格一致
- [ ] 符合细纲

---
> 本文件由创作闭环助手生成
> 最后更新时间：{datetime.now().strftime("%Y-%m-%d")}
"""
    
    return template


def self_check(file_path):
    """正文自检——直接委托 chapter_selfcheck.check_chapter()，不维护第二套检测逻辑。

    此前本函数维护了自己的一套 AI 味词表（14 个），与 chapter_selfcheck.py
    的 6 类完整词表不一致，导致同一章节在本函数中通过、在完整自检中却命中。
    现统一委托单一权威来源。
    """
    from writing.chapter_selfcheck import check_chapter as _cs_check
    from writing.chapter_policy import char_status, load_policy as _cs_load_policy

    if not os.path.exists(file_path):
        print(f"错误：文件不存在 {file_path}")
        return False

    policy = _cs_load_policy(get_project_dir())
    result = _cs_check(file_path, policy=policy)
    issues = []

    # 字数检查（两级判级：硬阻断/软警告）
    word_count = result["chars"]
    cs = char_status(word_count, policy)
    plat = policy["platform"]
    verdict = {
        "hard_short": f"❌ 严重不足：{word_count}字 < 硬下限{policy['hard_min']}（{plat}，硬阻断）",
        "hard_long":  f"❌ 严重超标：{word_count}字 > 硬上限{policy['hard_max']}（{plat}，硬阻断）",
        "soft_short": f"⚠️ 字数偏短：{word_count}字 < 软下限{policy['soft_min']}（{plat}，警告不阻断）",
        "soft_long":  f"⚠️ 字数偏长：{word_count}字 > 软上限{policy['soft_max']}（{plat}，警告不阻断）",
        "ok":         f"✅ 字数达标：{word_count}字（{plat}标准 {policy['soft_min']}-{policy['soft_max']}）",
    }
    print(verdict.get(cs, verdict["ok"]))
    if cs in ("hard_short", "hard_long"):
        issues.append(verdict[cs])
    elif cs in ("soft_short", "soft_long"):
        issues.append(verdict[cs])

    # 章末钩子（由 chapter_selfcheck 判定）
    hook_v = result["hook_verdict"]
    if "强钩子" in hook_v:
        print(f"✅ 章末钩子存在")
    elif "禁用空钩子" in hook_v:
        issues.append(f"⚠️ {hook_v}")
        print(f"⚠️ {hook_v}")
    else:
        issues.append(f"⚠️ {hook_v}")
        print(f"⚠️ {hook_v}")

    # AI 味（由 chapter_selfcheck 判定）
    ai_v = result["ai_verdict"]
    ai_total = result["ai_total"]
    if ai_total > 0:
        # 严重级别分档：重度→硬阻断，微量/轻度/中度→警告但不可忽略
        prefix = "❌" if ai_v == "重度" else "⚠️"
        print(f"{prefix} AI 味：{ai_v}（命中 {ai_total} 处）")
        if result["ai_per_cat"]:
            for cat, n in sorted(result["ai_per_cat"].items()):
                print(f"   {cat} ×{n}")
        if result["ai_severe"]:
            for s in result["ai_severe"]:
                issues.append(f"❌ 重度信号(硬阻断)：{s}")
        # 非零 AI 味即为问题，不再静默放过
        issues.append(f"{'硬阻断' if ai_v == '重度' else '警告'}：AI味{ai_v}（{ai_total}处）")
    else:
        print(f"✅ AI 味：干净")
    
    has_hard = any("硬阻断" in iss for iss in issues)
    if issues:
        print("自检结果：发现问题")
        for issue in issues:
            print(f"  {issue}")
        return 2 if has_hard else 1
    else:
        print("自检结果：✅ 通过")
        return 0


def remove_ai(file_path):
    """去 AI 味处理——引用 chapter_selfcheck 的黑名单，不维护独立词表。

    替换规则来自 BLACKLIST 各大类，覆盖 14 类共 80+ 条禁用表达。
    删除类（替换为空）：套话收束、空泛判断、虚假强调、无源权威、工程词泄露
    改词类（保留语义）：表演性动宾、意义膨胀、论文体、书面语连词
    警告类（仅标记不自动改）：网文最毒句、高频词、解释腔、升华式收尾（需人工判断）
    """
    from writing.chapter_selfcheck import BLACKLIST as _BL

    if not os.path.exists(file_path):
        print(f"错误：文件不存在 {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 删除类：直接移除这些禁用表达
    delete_cats = ["套话收束", "空泛判断", "虚假强调", "无源权威", "工程词泄露"]
    # 替换类：有明确更自然的替代词
    replace_map = {
        "实现了": "做到了", "推动了": "推进了", "促进了": "帮助了",
        "彰显了": "显示了", "体现了": "表现了", "见证了": "看到了",
        "标志着": "意味着", "深深植根于": "扎根在", "不可磨灭的印记": "印记",
        "关键转折点": "转折点", "核心价值在于": "关键是", "意义深远": "影响很大",
        "前所未有": "从没见过的", "可谓": "可以说", "未来可期": "值得期待",
        "充满希望": "有希望", "前途无量": "很有前途",
        "不难看出": "看得出来", "由此可见": "看得出", "事实上": "其实",
        "于是乎": "于是", "与此同时": "同时", "从而": "就", "因而": "所以",
    }

    changes = []
    body = content

    # 删除类
    for cat in delete_cats:
        for phrase in _BL.get(cat, []):
            if phrase and phrase in body:
                body = body.replace(phrase, "")
                changes.append(f"删除[{cat}] {phrase}")

    # 替换类
    for old, new in replace_map.items():
        if old in body:
            body = body.replace(old, new)
            changes.append(f"替换 {old} → {new}")

    # 保存
    if changes:
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(body)
        print(f"已修复 {len(changes)} 处 AI 味表达：")
        for change in changes:
            print(f"  {change}")
    else:
        print("未发现明显的 AI 味表达")


def move_chapter(chapter_num):
    """移入正式章节：把草稿从 drafts/ 真正移动到 chapters/，并更新索引"""
    project_dir = get_project_dir()
    chapters_dir = os.path.join(project_dir, "chapters")
    os.makedirs(chapters_dir, exist_ok=True)

    # 草稿来源：vault/drafts/projects/<项目>/ 第NNN章*.md
    draft_base = os.path.join(ROOT_DIR, "drafts", "projects", CURRENT_PROJECT)
    candidates = sorted(glob.glob(os.path.join(draft_base, f"第{chapter_num:03d}章*.md")))
    # 排除作战卡等非正文草稿
    candidates = [c for c in candidates if "作战卡" not in os.path.basename(c)]

    if not candidates:
        print(f"错误：在 {draft_base} 找不到 第{chapter_num:03d}章 开头的草稿")
        return False

    draft_path = candidates[0]

    # ---- 硬性字数校验：hard_short / hard_long 时拒绝移动 ----
    with open(draft_path, 'r', encoding='utf-8') as f:
        draft_text = f.read()
    body = extract_body(draft_text)
    wc = count_chars(body)
    policy = load_policy(get_project_dir())
    cs = char_status(wc, policy)
    if cs == "hard_short":
        print(f"硬性阻断：正文字数 {wc} < 硬下限 {policy['hard_min']}，禁止移入正式章节")
        print(f"  请扩充内容至 ≥{policy['soft_min']} 字后重试")
        return False
    if cs == "hard_long":
        print(f"硬性阻断：正文字数 {wc} > 硬上限 {policy['hard_max']}，禁止移入正式章节")
        print(f"  请精简内容至 ≤{policy['soft_max']} 字后重试")
        return False
    if cs in ("soft_short", "soft_long"):
        print(f"软警告：{wc} 字（{'偏短' if cs == 'soft_short' else '偏长'}），允许移入但建议优化")
    else:
        print(f"字数校验通过：{wc} 字 ✅")
    # ---------------------------------------------------------

    # 从草稿 frontmatter 取标题，决定正式文件名
    title = None
    m = re.search(r'^title:\s*第\d+章[：:]\s*(.+)$', draft_text, re.MULTILINE)
    if m:
        title = m.group(1).strip()
    if not title:
        title = "未命名"
    safe = re.sub(r'[\\/:*?"<>|]', '', title)
    final_name = f"第{chapter_num:03d}章-{safe}.md"
    final_path = os.path.join(chapters_dir, final_name)

    shutil.move(draft_path, final_path)
    print(f"已移入正式章节：{final_path}")

    # 更新 chapters/README.md 索引（替换占位或追加到列表末尾）
    readme_file = os.path.join(chapters_dir, "README.md")
    placeholder = f"第{chapter_num:03d}章-xxx.md"
    entry = f"- [第{chapter_num:03d}章]({final_name})"
    if os.path.exists(readme_file):
        with open(readme_file, 'r', encoding='utf-8') as f:
            content = f.read()
        if placeholder in content:
            content = content.replace(f"- [第{chapter_num:03d}章]({placeholder})", entry)
        elif f"第{chapter_num:03d}章" in content:
            print(f"第{chapter_num}章已存在于索引中")
            return True
        else:
            if not content.endswith("\n"):
                content += "\n"
            content += entry + "\n"
        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"已更新 chapters/README.md 索引：{entry}")
    return True


def update_progress(chapter_num):
    """更新项目进度 —— 委托 ProjectCounter 原子生成统计块 + 回写 frontmatter。

    此前本函数用 12 条正则零散拼凑 STATUS.md，同一份文件同时存在互相矛盾的数字
    （38,333 vs 36,111 vs 37,445；43% vs 13%），且不更新各章 frontmatter word_count。
    现统一交给 ProjectCounter：扫描全部正式章节 → 实算字数 → 原子替换两个统计块 →
    回写每章 word_count。任何脚本不得绕过 ProjectCounter 直接 patch STATUS.md。
    """
    from writing.ProjectCounter import count_project, apply_stats

    project_dir = get_project_dir()
    cn, tw, pc, policy, hdr = count_project(project_dir)
    if cn == 0:
        print("未找到章节文件，跳过进度更新。")
        return
    changed = apply_stats(project_dir, cn, tw, pc, policy, hdr, dry_run=False)
    print(f"进度已更新：{cn}章，{tw:,}字，卷完成率{cn/30:.0%}" + (
        f"，前端字回写{len(changed)}章" if changed else ""))


def review():
    """追读/完读复盘"""
    print("追读/完读复盘")
    print("=" * 60)
    print("\n请输入以下数据（从番茄后台获取）：")
    
    data = {
        "完读率": input("完读率（%）："),
        "追读率": input("追读率（%）："),
        "书架比": input("书架比（%）："),
        "次日留存": input("次日留存（%）："),
        "有效阅读": input("日均有效阅读："),
        "收入": input("今日收入（元）："),
    }
    
    # 保存数据
    review_dir = os.path.join(get_project_dir(), "reviews")
    os.makedirs(review_dir, exist_ok=True)
    
    today = datetime.now().strftime("%Y-%m-%d")
    review_file = os.path.join(review_dir, f"{today}.json")
    
    with open(review_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n复盘数据已保存到：{review_file}")
    
    # 分析
    print("\n数据分析：")
    
    # 完读率分析
    completion_rate = float(data["完读率"])
    if completion_rate < 30:
        print("❌ 完读率偏低，检查前3章节奏")
    elif completion_rate < 50:
        print("⚠️ 完读率一般，优化开篇")
    else:
        print("✅ 完读率良好")
    
    # 追读率分析
    follow_rate = float(data["追读率"])
    if follow_rate < 10:
        print("❌ 追读率太低，检查爽点密度")
    elif follow_rate < 15:
        print("⚠️ 追读率一般，加强钩子")
    else:
        print("✅ 追读率良好")
    
    # 改进建议
    print("\n改进建议：")
    if completion_rate < 50:
        print("1. 检查开篇节奏，尽快切入冲突")
        print("2. 每章结尾必须有强钩子")
        print("3. 检查爽点密度（每800字一个小高潮）")
    
    if follow_rate < 15:
        print("1. 增加章节间的连贯性")
        print("2. 强化主角目标")
        print("3. 增加信息差碾压爽点")


def main():
    args = sys.argv[1:]
    
    if not args:
        print("用法：")
        print("  python tools/scripts/创作闭环助手.py --next-chapter")
        print("  python tools/scripts/创作闭环助手.py --template <chapter>")
        print("  python tools/scripts/创作闭环助手.py --self-check <file>")
        print("  python tools/scripts/创作闭环助手.py --remove-ai <file>")
        print("  python tools/scripts/创作闭环助手.py --move-chapter <num>")
        print("  python tools/scripts/创作闭环助手.py --update-progress <num>")
        print("  python tools/scripts/创作闭环助手.py --review")
        return 1
    
    if "--next-chapter" in args:
        outline = get_next_chapter_outline()
        if outline:
            print(f"下一章：第{outline['chapter']}章")
            print("=" * 60)
            print(outline['content'][:500] + "...")
        else:
            print("未找到下一章细纲")
    
    elif "--template" in args:
        idx = args.index("--template")
        if idx + 1 < len(args):
            chapter_num = int(args[idx + 1])
            template = generate_chapter_template(chapter_num)
            if template:
                print(template)
            else:
                print("生成模板失败")
        else:
            print("错误：请指定章节号")
    
    elif "--self-check" in args:
        idx = args.index("--self-check")
        if idx + 1 < len(args):
            file_path = args[idx + 1]
            return self_check(file_path)
        else:
            print("错误：请指定文件路径")
    
    elif "--remove-ai" in args:
        idx = args.index("--remove-ai")
        if idx + 1 < len(args):
            file_path = args[idx + 1]
            remove_ai(file_path)
        else:
            print("错误：请指定文件路径")
    
    elif "--move-chapter" in args:
        idx = args.index("--move-chapter")
        if idx + 1 < len(args):
            chapter_num = int(args[idx + 1])
            ok = move_chapter(chapter_num)
            return 0 if ok else 1
        else:
            print("错误：请指定章节号")
    
    elif "--update-progress" in args:
        idx = args.index("--update-progress")
        if idx + 1 < len(args):
            chapter_num = int(args[idx + 1])
            update_progress(chapter_num)
        else:
            print("错误：请指定章节号")
    
    elif "--review" in args:
        review()
    
    else:
        print("未知命令")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())