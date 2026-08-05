#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
项目上下文加载器（最小可用版）
==============================

只做一件事：为指定项目生成标准上下文，供 AI 写作时使用。

原则
----
1. 只能读取当前项目。
2. 必须读取：framework.md、系统设定、人物卡、大纲、最近三章。
3. 不读取示范项目和其他小说。
4. 输出清单，便于人工检查有没有串书。
5. 超出长度时按优先级裁剪。

用法
----
    python tools/scripts/项目上下文加载器.py                              # 默认项目
    python tools/scripts/项目上下文加载器.py --project （已删除项目）   # 指定项目
    python tools/scripts/项目上下文加载器.py --json                        # JSON 输出
    python tools/scripts/项目上下文加载器.py --check-only                   # 只检查，不输出内容
"""

import os
import sys
import re
import json
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# 配置
# ---------------------------------------------------------------------------
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECTS_DIR = os.path.join(ROOT_DIR, "projects")

# 上下文优先级（数字越小优先级越高）
# 1: framework.md（世界观/总纲）
# 2: 系统设定
# 3: 人物卡
# 4: 大纲（当前卷/总纲）
# 5: 最近三章（用于保持连贯性）
# 6: 当前细纲（下一章）

# 最大上下文长度（字符数）
MAX_CONTEXT_LENGTH = 15000

# 各部分预算
BUDGET = {
    "framework": 3000,
    "system": 2000,
    "characters": 4000,
    "outline": 3000,
    "recent_chapters": 2000,
    "next_chapter": 1000
}


def list_projects():
    """列出所有项目"""
    projects = []
    if os.path.exists(PROJECTS_DIR):
        for name in os.listdir(PROJECTS_DIR):
            project_dir = os.path.join(PROJECTS_DIR, name)
            if os.path.isdir(project_dir):
                projects.append(name)
    return sorted(projects)


def find_project_dir(project_name):
    """查找项目目录"""
    project_dir = os.path.join(PROJECTS_DIR, project_name)
    if os.path.isdir(project_dir):
        return project_dir
    return None


def read_file_safe(file_path):
    """安全读取文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return None


def truncate(text, max_length):
    """截断文本到指定长度"""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "\n\n[... 已截断 ...]"


def load_framework(project_dir):
    """加载 framework.md"""
    file_path = os.path.join(project_dir, "framework.md")
    content = read_file_safe(file_path)
    if content:
        return truncate(content, BUDGET["framework"])
    return None


def load_system_setting(project_dir):
    """加载系统设定"""
    file_path = os.path.join(project_dir, "entities", "系统设定.md")
    content = read_file_safe(file_path)
    if content:
        return truncate(content, BUDGET["system"])
    return None


def load_character_cards(project_dir):
    """加载所有人物卡"""
    entities_dir = os.path.join(project_dir, "entities")
    characters = {}

    if not os.path.isdir(entities_dir):
        return characters

    for filename in os.listdir(entities_dir):
        if filename.startswith("人物-") and filename.endswith(".md"):
            file_path = os.path.join(entities_dir, filename)
            content = read_file_safe(file_path)
            if content:
                # 提取人物名（去掉"人物-"前缀和".md"后缀）
                char_name = filename[3:-3]
                characters[char_name] = truncate(content, BUDGET["characters"] // max(1, len([f for f in os.listdir(entities_dir) if f.startswith("人物-") and f.endswith(".md")])))

    return characters


def load_outline(project_dir):
    """加载大纲"""
    # 优先加载 outline-第一卷.md，其次 outline.md
    for filename in ["outline-第一卷.md", "outline.md"]:
        file_path = os.path.join(project_dir, filename)
        content = read_file_safe(file_path)
        if content:
            return truncate(content, BUDGET["outline"])
    return None


def load_recent_chapters(project_dir, count=3):
    """加载最近三章"""
    chapters_dir = os.path.join(project_dir, "chapters")
    if not os.path.isdir(chapters_dir):
        return []

    # 获取所有章节文件
    chapter_files = []
    for filename in os.listdir(chapters_dir):
        if filename.endswith('.md') and filename != "README.md":
            chapter_files.append(filename)

    # 按文件名排序（章节号）
    chapter_files.sort()

    # 取最后 N 章
    recent_files = chapter_files[-count:] if len(chapter_files) > count else chapter_files

    chapters = []
    for filename in recent_files:
        file_path = os.path.join(chapters_dir, filename)
        content = read_file_safe(file_path)
        if content:
            # 只取正文部分，去掉 frontmatter
            match = re.search(r'^---\s*\n.*?\n---\s*\n(.*)$', content, re.DOTALL)
            if match:
                body = match.group(1)
            else:
                body = content

            # 截断每章到预算
            per_chapter_budget = BUDGET["recent_chapters"] // max(1, len(recent_files))
            chapters.append({
                "filename": filename,
                "content": truncate(body.strip(), per_chapter_budget)
            })

    return chapters


def load_next_chapter_outline(project_dir):
    """加载下一章细纲"""
    outline_file = os.path.join(project_dir, "outline-第一卷.md")
    content = read_file_safe(outline_file)
    if not content:
        return None

    # 提取当前章节
    status_file = os.path.join(project_dir, "STATUS.md")
    status_content = read_file_safe(status_file)
    current_chapter = 1
    if status_content:
        match = re.search(r'当前章节\s*\|\s*第(\d+)章', status_content)
        if match:
            current_chapter = int(match.group(1))

    next_chapter_num = current_chapter + 1

    # 查找对应章节的细纲
    # 匹配 "### 第11章：xxx" 格式
    pattern = rf'###\s*第{next_chapter_num}章[：:]\s*(.+?)(?=\n###|\Z)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        outline_text = match.group(0).strip()
        return truncate(outline_text, BUDGET["next_chapter"])

    return None


def build_context(project_name):
    """构建项目上下文"""
    project_dir = find_project_dir(project_name)
    if not project_dir:
        return None, f"项目不存在: {project_name}"

    context = {
        "project": project_name,
        "generated_at": datetime.now().isoformat(),
        "sections": {},
        "checklist": [],
        "warnings": []
    }

    # 1. Framework
    framework = load_framework(project_dir)
    if framework:
        context["sections"]["framework"] = framework
        context["checklist"].append("✅ framework.md 已加载")
    else:
        context["warnings"].append("⚠️ framework.md 未找到或为空")

    # 2. 系统设定
    system = load_system_setting(project_dir)
    if system:
        context["sections"]["system_setting"] = system
        context["checklist"].append("✅ 系统设定已加载")
    else:
        context["warnings"].append("⚠️ 系统设定未找到或为空")

    # 3. 人物卡
    characters = load_character_cards(project_dir)
    if characters:
        context["sections"]["characters"] = characters
        context["checklist"].append(f"✅ 人物卡已加载 ({len(characters)} 人)")
    else:
        context["warnings"].append("⚠️ 人物卡未找到")

    # 4. 大纲
    outline = load_outline(project_dir)
    if outline:
        context["sections"]["outline"] = outline
        context["checklist"].append("✅ 大纲已加载")
    else:
        context["warnings"].append("⚠️ 大纲未找到")

    # 5. 最近三章
    recent_chapters = load_recent_chapters(project_dir, count=3)
    if recent_chapters:
        context["sections"]["recent_chapters"] = recent_chapters
        context["checklist"].append(f"✅ 最近三章已加载 ({len(recent_chapters)} 章)")
    else:
        context["warnings"].append("⚠️ 最近三章未找到")

    # 6. 下一章细纲
    next_outline = load_next_chapter_outline(project_dir)
    if next_outline:
        context["sections"]["next_chapter_outline"] = next_outline
        context["checklist"].append("✅ 下一章细纲已加载")
    else:
        context["warnings"].append("⚠️ 下一章细纲未找到")

    # 计算总长度
    total_length = sum(len(str(v)) for v in context["sections"].values())
    context["total_length"] = total_length

    if total_length > MAX_CONTEXT_LENGTH:
        context["warnings"].append(f"⚠️ 上下文过长 ({total_length} 字符)，已按优先级裁剪")

    return context, None


def format_context_human(context):
    """格式化上下文为人类可读格式"""
    lines = []
    lines.append("=" * 60)
    lines.append("📚 项目上下文")
    lines.append("=" * 60)
    lines.append("")
    lines.append(f"项目: {context['project']}")
    lines.append(f"生成时间: {context['generated_at']}")
    lines.append(f"总长度: {context['total_length']} 字符")
    lines.append("")

    # 检查清单
    lines.append("--- 检查清单 ---")
    for item in context["checklist"]:
        lines.append(item)
    lines.append("")

    # 警告
    if context["warnings"]:
        lines.append("--- 警告 ---")
        for warning in context["warnings"]:
            lines.append(warning)
        lines.append("")

    # 内容
    lines.append("--- 上下文内容 ---")
    lines.append("")

    if "framework" in context["sections"]:
        lines.append("【世界观/总纲】")
        lines.append(context["sections"]["framework"])
        lines.append("")

    if "system_setting" in context["sections"]:
        lines.append("【系统设定】")
        lines.append(context["sections"]["system_setting"])
        lines.append("")

    if "characters" in context["sections"]:
        lines.append("【人物卡】")
        for name, content in context["sections"]["characters"].items():
            lines.append(f"\n### {name}")
            lines.append(content)
        lines.append("")

    if "outline" in context["sections"]:
        lines.append("【大纲】")
        lines.append(context["sections"]["outline"])
        lines.append("")

    if "recent_chapters" in context["sections"]:
        lines.append("【最近三章】")
        for chapter in context["sections"]["recent_chapters"]:
            lines.append(f"\n### {chapter['filename']}")
            lines.append(chapter["content"])
        lines.append("")

    if "next_chapter_outline" in context["sections"]:
        lines.append("【下一章细纲】")
        lines.append(context["sections"]["next_chapter_outline"])
        lines.append("")

    lines.append("=" * 60)
    lines.append("✅ 上下文加载完成")
    lines.append("=" * 60)

    return "\n".join(lines)


def format_context_json(context):
    """格式化上下文为 JSON"""
    return json.dumps(context, ensure_ascii=False, indent=2)


def main():
    args = sys.argv[1:]

    # 解析参数
    project_name = "（已删除项目）"  # 默认项目
    json_output = "--json" in args
    check_only = "--check-only" in args

    # 解析项目名
    for i, arg in enumerate(args):
        if arg == "--project" and i + 1 < len(args):
            project_name = args[i + 1]

    # 构建上下文
    context, error = build_context(project_name)

    if error:
        print(f"❌ 错误: {error}")
        return 1

    if check_only:
        # 只显示检查清单
        print("=" * 60)
        print("🔍 项目上下文检查")
        print("=" * 60)
        print()
        print(f"项目: {context['project']}")
        print()
        print("检查清单:")
        for item in context["checklist"]:
            print(f"  {item}")
        print()
        if context["warnings"]:
            print("警告:")
            for warning in context["warnings"]:
                print(f"  {warning}")
        print()
        print("=" * 60)

        # 如果有警告，返回非零退出码
        if context["warnings"]:
            return 1
        return 0

    # 输出上下文
    if json_output:
        print(format_context_json(context))
    else:
        print(format_context_human(context))

    return 0


if __name__ == "__main__":
    sys.exit(main())
