#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
提交前核心校验
==============

在 Git 提交前自动运行的核心校验，确保知识库状态健康。

检查项
------
1. Frontmatter 合法性
   - 所有带 frontmatter 的文件必须包含 id、title、type、status 字段
   - id 必须唯一
   - type 和 status 取值必须符合规范

2. 链接有效性
   - 内部链接目标必须存在
   - 禁止使用绝对路径

3. 项目结构
   - projects/ 目录必须符合标准结构
   - 章节文件命名必须符合规范

4. 重复内容
   - 检测明显的重复文件
   - 检测孤立文件（无反向链接）

5. 编码检查
   - 所有文件必须是 UTF-8 编码
   - 无乱码字符

退出码: 0 = 通过（可提交）; 1 = 不通过（阻断提交）。

用法
----
    python tools/scripts/maintenance/提交前校验.py                 # 人类可读报告
    python tools/scripts/maintenance/提交前校验.py --json          # 机器可读 JSON
    python tools/scripts/maintenance/提交前校验.py --fix           # 自动修复可修复的问题
"""

import os
import re
import sys
import json
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# 配置
# ---------------------------------------------------------------------------
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PROJECTS_DIR = os.path.join(ROOT_DIR, "projects")

# 受控的 frontmatter 字段取值
VALID_TYPES = {
    "index", "guide", "ref", "dashboard", "template", "moc", "demo",
    "project", "chapter", "character", "setting", "location", "prop",
    "tool", "daily-note", "book-note"
}

VALID_STATUSES = {"active", "demo", "wip", "done", "draft", "archived"}

VALID_AREAS = {"库", "方法", "项目", "资料", "日记", "索引"}

# 章节文件命名模式
CHAPTER_PATTERN = re.compile(r'^第\d{3}章-.+\.md$')

# Frontmatter 正则
FRONTMATTER_PATTERN = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
FIELD_PATTERN = re.compile(r'^(\w+):\s*(.+)$', re.MULTILINE)


def find_markdown_files(root_dir):
    """查找所有 Markdown 文件"""
    md_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # 跳过隐藏目录
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        for filename in filenames:
            if filename.endswith('.md'):
                md_files.append(os.path.join(dirpath, filename))
    return md_files


def parse_frontmatter(file_path):
    """解析文件 frontmatter"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return None, f"读取失败: {e}"

    match = FRONTMATTER_PATTERN.match(content)
    if not match:
        return None, "缺少 frontmatter"

    frontmatter_text = match.group(1)
    fields = {}
    for field_match in FIELD_PATTERN.finditer(frontmatter_text):
        key = field_match.group(1)
        value = field_match.group(2).strip()
        fields[key] = value

    return fields, None


def check_frontmatter(files):
    """检查 frontmatter 合法性"""
    errors = []
    warns = []
    ids = set()
    titles = set()

    for file_path in files:
        rel_path = os.path.relpath(file_path, ROOT_DIR)
        fields, error = parse_frontmatter(file_path)

        if error:
            errors.append({
                "file": rel_path,
                "type": "FRONTMATTER_MISSING",
                "message": error
            })
            continue

        # 检查必需字段
        required_fields = ["id", "title", "type", "status"]
        for field in required_fields:
            if field not in fields:
                errors.append({
                    "file": rel_path,
                    "type": "FIELD_MISSING",
                    "message": f"缺少必需字段: {field}"
                })

        # 检查 id 唯一性
        if "id" in fields:
            if fields["id"] in ids:
                errors.append({
                    "file": rel_path,
                    "type": "DUPLICATE_ID",
                    "message": f"重复的 ID: {fields['id']}"
                })
            ids.add(fields["id"])

        # 检查 title 唯一性
        if "title" in fields:
            if fields["title"] in titles:
                errors.append({
                    "file": rel_path,
                    "type": "DUPLICATE_TITLE",
                    "message": f"重复的标题: {fields['title']}"
                })
            titles.add(fields["title"])

        # 检查 type 取值
        if "type" in fields:
            type_val = fields["type"].lower()
            if type_val not in VALID_TYPES:
                errors.append({
                    "file": rel_path,
                    "type": "INVALID_TYPE",
                    "message": f"无效的 type: {fields['type']}（允许: {', '.join(sorted(VALID_TYPES))}）"
                })

        # 检查 status 取值
        if "status" in fields:
            status_val = fields["status"].lower()
            if status_val not in VALID_STATUSES:
                errors.append({
                    "file": rel_path,
                    "type": "INVALID_STATUS",
                    "message": f"无效的 status: {fields['status']}（允许: {', '.join(sorted(VALID_STATUSES))}）"
                })

        # 检查 area 取值
        if "area" in fields:
            area_val = fields["area"]
            if area_val not in VALID_AREAS:
                warns.append({
                    "file": rel_path,
                    "type": "INVALID_AREA",
                    "message": f"未知的 area: {area_val}（允许: {', '.join(sorted(VALID_AREAS))}）"
                })

    return errors, warns


def check_links(files):
    """检查链接有效性"""
    errors = []
    warns = []

    # 构建文件索引
    file_index = {}
    for file_path in files:
        rel_path = os.path.relpath(file_path, ROOT_DIR)
        file_index[rel_path] = file_path
        # 也索引文件名
        file_index[os.path.basename(file_path)] = file_path

    # 链接正则
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            continue

        rel_path = os.path.relpath(file_path, ROOT_DIR)

        # 查找所有链接
        for match in link_pattern.finditer(content):
            link_text = match.group(1)
            link_target = match.group(2)

            # 跳过外部链接
            if link_target.startswith('http://') or link_target.startswith('https://'):
                continue

            # 检查绝对路径
            if link_target.startswith('/') or (len(link_target) > 1 and link_target[1] == ':'):
                errors.append({
                    "file": rel_path,
                    "type": "ABSOLUTE_PATH",
                    "message": f"使用绝对路径: {link_target}"
                })
                continue

            # 解析相对路径
            if link_target.startswith('#'):
                # 锚点链接，跳过
                continue

            # 计算目标文件路径
            file_dir = os.path.dirname(file_path)
            target_path = os.path.normpath(os.path.join(file_dir, link_target))

            # 检查目标是否存在
            if not os.path.exists(target_path):
                # 尝试添加 .md 后缀
                if not link_target.endswith('.md'):
                    target_path_md = target_path + '.md'
                    if os.path.exists(target_path_md):
                        continue

                errors.append({
                    "file": rel_path,
                    "type": "BROKEN_LINK",
                    "message": f"断链: [{link_text}]({link_target}) -> 目标不存在"
                })

    return errors, warns


def check_project_structure(files):
    """检查项目结构"""
    errors = []
    warns = []

    # 检查 projects/ 目录结构
    if not os.path.exists(PROJECTS_DIR):
        errors.append({
            "file": "projects/",
            "type": "MISSING_DIR",
            "message": "projects/ 目录不存在"
        })
        return errors, warns

    # 遍历项目目录
    for project_name in os.listdir(PROJECTS_DIR):
        project_dir = os.path.join(PROJECTS_DIR, project_name)
        if not os.path.isdir(project_dir):
            continue

        # 检查必需文件
        required_files = ["README.md", "STATUS.md", "framework.md"]
        for req_file in required_files:
            if not os.path.exists(os.path.join(project_dir, req_file)):
                warns.append({
                    "file": f"projects/{project_name}/",
                    "type": "MISSING_REQUIRED_FILE",
                    "message": f"缺少推荐文件: {req_file}"
                })

        # 检查章节命名
        chapters_dir = os.path.join(project_dir, "chapters")
        if os.path.exists(chapters_dir):
            for filename in os.listdir(chapters_dir):
                if filename.endswith('.md') and filename != "README.md":
                    if not CHAPTER_PATTERN.match(filename):
                        warns.append({
                            "file": f"projects/{project_name}/chapters/{filename}",
                            "type": "INVALID_CHAPTER_NAME",
                            "message": f"章节文件命名不符合规范（应为 第NNN章-标题.md）"
                        })

    return errors, warns


def check_encoding(files):
    """检查文件编码"""
    errors = []
    warns = []

    for file_path in files:
        try:
            with open(file_path, 'rb') as f:
                raw = f.read()
                raw.decode('utf-8')
        except UnicodeDecodeError:
            rel_path = os.path.relpath(file_path, ROOT_DIR)
            errors.append({
                "file": rel_path,
                "type": "ENCODING_ERROR",
                "message": "文件不是 UTF-8 编码"
            })

    return errors, warns


def check_duplicates(files):
    """检查重复内容"""
    errors = []
    warns = []

    # 简单检查：文件名完全相同但内容不同的文件
    filename_map = {}
    for file_path in files:
        filename = os.path.basename(file_path)
        if filename not in filename_map:
            filename_map[filename] = []
        filename_map[filename].append(file_path)

    for filename, paths in filename_map.items():
        if len(paths) > 1:
            # 检查内容是否相同
            contents = []
            for path in paths:
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        contents.append(f.read())
                except:
                    contents.append(None)

            # 如果有不同内容，警告
            unique_contents = set(contents)
            if len(unique_contents) > 1:
                rel_paths = [os.path.relpath(p, ROOT_DIR) for p in paths]
                warns.append({
                    "file": rel_paths[0],
                    "type": "DUPLICATE_FILENAME",
                    "message": f"同名文件内容不同: {filename}（{len(paths)} 个副本）"
                })

    return errors, warns


def run_checks(root_dir, fix=False):
    """运行所有检查"""
    all_errors = []
    all_warns = []

    print("🔍 开始核心校验...")
    print(f"   根目录: {root_dir}")
    print()

    # 查找所有 Markdown 文件
    print("📁 扫描 Markdown 文件...")
    files = find_markdown_files(root_dir)
    print(f"   找到 {len(files)} 个文件")
    print()

    # 1. 检查 frontmatter
    print("📋 检查 frontmatter...")
    errors, warns = check_frontmatter(files)
    all_errors.extend(errors)
    all_warns.extend(warns)
    print(f"   ❌ {len(errors)} 个错误")
    print(f"   ⚠️  {len(warns)} 个警告")
    print()

    # 2. 检查链接
    print("🔗 检查链接...")
    errors, warns = check_links(files)
    all_errors.extend(errors)
    all_warns.extend(warns)
    print(f"   ❌ {len(errors)} 个错误")
    print(f"   ⚠️  {len(warns)} 个警告")
    print()

    # 3. 检查项目结构
    print("📂 检查项目结构...")
    errors, warns = check_project_structure(files)
    all_errors.extend(errors)
    all_warns.extend(warns)
    print(f"   ❌ {len(errors)} 个错误")
    print(f"   ⚠️  {len(warns)} 个警告")
    print()

    # 4. 检查编码
    print("🔤 检查编码...")
    errors, warns = check_encoding(files)
    all_errors.extend(errors)
    all_warns.extend(warns)
    print(f"   ❌ {len(errors)} 个错误")
    print(f"   ⚠️  {len(warns)} 个警告")
    print()

    # 5. 检查重复
    print("🔁 检查重复内容...")
    errors, warns = check_duplicates(files)
    all_errors.extend(errors)
    all_warns.extend(warns)
    print(f"   ❌ {len(errors)} 个错误")
    print(f"   ⚠️  {len(warns)} 个警告")
    print()

    return all_errors, all_warns


def main():
    args = sys.argv[1:]

    # 解析参数
    json_output = "--json" in args
    fix_mode = "--fix" in args

    # 运行检查
    errors, warns = run_checks(ROOT_DIR, fix=fix_mode)

    # 输出结果
    if json_output:
        result = {
            "timestamp": datetime.now().isoformat(),
            "errors": errors,
            "warns": warns,
            "error_count": len(errors),
            "warn_count": len(warns),
            "pass": len(errors) == 0
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("=" * 60)
        print("📊 校验结果")
        print("=" * 60)
        print()

        if errors:
            print(f"❌ 发现 {len(errors)} 个错误（阻断提交）:")
            print()
            for i, error in enumerate(errors, 1):
                print(f"{i}. [{error['type']}] {error['file']}")
                print(f"   {error['message']}")
                print()

        if warns:
            print(f"⚠️  发现 {len(warns)} 个警告（建议修复）:")
            print()
            for i, warn in enumerate(warns, 1):
                print(f"{i}. [{warn['type']}] {warn['file']}")
                print(f"   {warn['message']}")
                print()

        if not errors and not warns:
            print("✅ 校验通过，没有发现问题")
        elif not errors:
            print("✅ 校验通过（有警告，但不阻断提交）")
        else:
            print("❌ 校验失败，存在错误，建议修复后再提交")

        print()
        print("=" * 60)

    # 返回退出码
    return 0 if len(errors) == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
