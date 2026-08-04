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

# 项目目录
PROJECTS_DIR = os.path.join(ROOT_DIR, "projects")

# 当前项目
CURRENT_PROJECT = "重生2010万物估值系统"


def get_project_dir():
    """获取当前项目目录"""
    return os.path.join(PROJECTS_DIR, CURRENT_PROJECT)


def get_current_progress():
    """获取当前进度"""
    status_file = os.path.join(get_project_dir(), "STATUS.md")
    if not os.path.exists(status_file):
        return None
    
    with open(status_file, 'r', encoding='utf-8') as f:
        content = f.read()
        match = re.search(r'当前章节\s*\|\s*\*\*(\d+)章\*\*', content)
        if match:
            return int(match.group(1))
    return 0


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
    """生成章节模板"""
    project_dir = get_project_dir()
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

- [ ] 字数达标（2000-4000字）
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
    """正文自检（按写作硬约束：字数 2300-2700、章末钩子、AI 味）"""
    if not os.path.exists(file_path):
        print(f"错误：文件不存在 {file_path}")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # 检查 frontmatter
    if not content.startswith('---'):
        issues.append("❌ 缺少 frontmatter")
    else:
        required_fields = ['id', 'type', 'title', 'chapter', 'volume']
        for field in required_fields:
            if re.search(rf'^{field}\s*:', content[:600], re.MULTILINE) is None:
                issues.append(f"❌ 缺少字段：{field}")
    
    # 正文（去 frontmatter）
    body = content
    fm = re.match(r'^---\n.*?\n---\n', body, re.DOTALL)
    if fm:
        body = body[fm.end():]
    
    # 字数：汉字+字母+数字，不含标点与空白（写作硬约束 §1.2）
    chars = re.findall(r'[\u4e00-\u9fffA-Za-z0-9]', body)
    word_count = len(chars)
    if word_count < 2300:
        issues.append(f"❌ 字数不足：{word_count}字（硬约束 2300-2700）")
    elif word_count > 2700:
        issues.append(f"⚠️ 字数过多：{word_count}字（硬约束 2300-2700）")
    else:
        print(f"✅ 字数达标：{word_count}字")
    
    # 章末钩子：末 400 字含强钩子特征词
    tail = body[-400:]
    hook_kw = ['？', '不知道', '没想到', '原来', '如果', '竟', '却', '突然',
               '终于', '决定', '机会', '考验', '炸弹', '亿', '危险', '秘密', '时代']
    if not any(k in tail for k in hook_kw):
        issues.append("⚠️ 章末钩子可能偏弱（建议强化）")
    else:
        print("✅ 章末钩子特征存在")
    
    # AI 味（14 类禁用表达精简版）
    ai_words = ["值得注意的是", "毫无疑问", "诚然", "综上所述", "归根结底", "本质上",
                "不是 ", "而是 ", "仿佛", "宛若", "眼中闪过一丝", "带着一丝",
                "这意味着", "不得不说"]
    for w in ai_words:
        if w in body:
            issues.append(f"⚠️ 可能包含 AI 味表达：{w}")
    
    if issues:
        print("自检结果：发现问题")
        for issue in issues:
            print(f"  {issue}")
        return False
    else:
        print("自检结果：✅ 通过")
        return True


def remove_ai(file_path):
    """去 AI 味处理（简化版）"""
    if not os.path.exists(file_path):
        print(f"错误：文件不存在 {file_path}")
        return
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 禁用表达替换
    replacements = {
        "值得注意的是": "",
        "毫无疑问": "",
        "诚然": "",
        "综上所述": "",
        "归根结底": "",
        "本质上": "",
        "实现了": "做到了",
        "推动了": "推进了",
        "促进了": "帮助了",
        "彰显了": "显示了",
        "体现了": "表现了",
        "见证了": "看到了",
        "标志着": "意味着",
    }
    
    changes = []
    for old, new in replacements.items():
        if old in content:
            content = content.replace(old, new)
            changes.append(f"{old} -> {new}")
    
    # 保存文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    if changes:
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

    # 从草稿 frontmatter 取标题，决定正式文件名
    with open(draft_path, 'r', encoding='utf-8') as f:
        draft_text = f.read()
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
    """更新项目进度（字数从正式章节文件实算，不写死）"""
    project_dir = get_project_dir()
    status_file = os.path.join(project_dir, "STATUS.md")
    
    if not os.path.exists(status_file):
        print(f"错误：STATUS.md 不存在")
        return
    
    # 实算全部正式章节字数（去 frontmatter、去标点）
    total_words = 0
    chapter_files = sorted(
        glob.glob(os.path.join(project_dir, "chapters", "第*章-*.md")))
    for cf in chapter_files:
        with open(cf, 'r', encoding='utf-8') as f:
            txt = f.read()
        fm = re.match(r'^---\n.*?\n---\n', txt, re.DOTALL)
        if fm:
            txt = txt[fm.end():]
        chars = re.findall(r'[\u4e00-\u9fffA-Za-z0-9]', txt)
        total_words += len(chars)
    
    # 取本章标题（用于进度表）
    this_matches = sorted(
        glob.glob(os.path.join(project_dir, "chapters", f"第{chapter_num:03d}章-*.md")))
    chapter_title = ""
    if this_matches:
        with open(this_matches[0], 'r', encoding='utf-8') as f:
            t = f.read()
        mt = re.search(r'^title:\s*(.+)$', t, re.MULTILINE)
        if mt:
            # 去掉「第011章：」式前缀（兼容零填充）
            chapter_title = re.sub(
                r'^第0*' + str(chapter_num) + r'章[：:]', '', mt.group(1).strip())
    
    with open(status_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 当前章节（含标题）
    content = re.sub(
        r'当前章节\s*\|\s*第\d+章\s*\|[^\n|]+',
        f'当前章节 | 第{chapter_num}章 | {chapter_title or "待命名"}',
        content
    )
    # 下一章节
    content = re.sub(
        r'下一章节\s*\|\s*第\d+章\s*\|[^\n|]+',
        f'下一章节 | 第{chapter_num + 1}章 | 待创作',
        content
    )
    # 存稿字数（实算，含真实均值备注）
    avg = total_words // chapter_num if chapter_num else 0
    content = re.sub(
        r'存稿字数\s*\|[^\n]*',
        f'存稿字数 | ~{total_words:,}字 | {chapter_num}章·均~{avg}字',
        content
    )
    # 完成率：按第一卷 30 万字（300,000 字）目标实算
    completion = int(round(total_words / 300000 * 100)) if total_words else 0
    content = re.sub(r'完成率\s*\|\s*[\d.]+%', f'完成率 | {completion}%', content)
    # 总进度（兼容加粗写法）：原 "**35%** | 10/30万字"
    content = re.sub(
        r'总进度\s*\|\s*\*\*?[\d.]+%\*\*?\s*\|[^\n|]*',
        f'总进度 | **{completion}%** | {chapter_num}/30章',
        content
    )
    # 创作统计：总章节数 / 总字数（含真实均值备注）
    content = re.sub(r'总章节数\s*\|\s*\d+章', f'总章节数 | {chapter_num}章', content)
    content = re.sub(r'总字数\s*\|[^\n]*', f'总字数 | ~{total_words:,}字 | 均~{avg}字/章', content)
    
    # 更新日期
    today = datetime.now().strftime("%Y-%m-%d")
    content = re.sub(r'最后更新时间：\d{4}-\d{2}-\d{2}', f'最后更新时间：{today}', content)
    content = re.sub(r'updated:\s*\d{4}-\d{2}-\d{2}', f'updated: {today}', content)
    
    with open(status_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"已更新 STATUS.md：第{chapter_num}章《{chapter_title}》，存稿约 {total_words:,}字，完成率 {completion}%（第一卷30万字）")


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
            self_check(file_path)
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
            move_chapter(chapter_num)
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