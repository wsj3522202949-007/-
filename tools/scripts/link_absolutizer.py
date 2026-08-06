#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
GitHub 链接绝对化转换器（可重复执行版）
========================================

将工具卡中的 GitHub 相对链接转换为绝对 URL，并修复已存在的 blob/tree 误用。

处理规则
--------
1. 文件路径 → blob/<default_branch>/
2. 目录路径 → tree/<default_branch>/
3. 图片（![]()）→ raw.githubusercontent.com/<repo>/<default_branch>/path
4. 锚点 → 保留 #anchor
5. 未知目标 → 保留原文，不强制转换
6. 已存在的 blob/tree 链接 → 自动修正误用（目录误用 blob 等）

用法
----
    python tools/scripts/link_absolutizer.py                    # dry-run 报告
    python tools/scripts/link_absolutizer.py --fix              # 实际执行修正
    python tools/scripts/link_absolutizer.py --dry-run          # 同上
    python tools/scripts/link_absolutizer.py --dir tools/cards  # 指定目录
    python tools/scripts/link_absolutizer.py --json             # 机器可读

可重复性保证
------------
- 幂等：多次运行 --fix 结果不变（已绝对的 URL 不会重复转换）
- 无副作用：dry-run 不修改任何文件
- 可配置分支映射：tools/scripts/_branch_map.json（自动生成或手动维护）
"""

import os
import re
import sys
import json
import argparse
from pathlib import Path

# ---------------------------------------------------------------------------
# 常量
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = (SCRIPT_DIR / '..' / '..').resolve()

# 已知文件扩展名 → 判断为文件（blob）
FILE_EXTENSIONS = {
    '.md', '.py', '.js', '.ts', '.jsx', '.tsx', '.ipynb', '.txt', '.csv',
    '.json', '.yaml', '.yml', '.toml', '.ini', '.cfg', '.conf',
    '.html', '.css', '.scss', '.less', '.vue', '.svelte',
    '.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.ico',
    '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
    '.zip', '.tar', '.gz', '.7z', '.rar',
    '.sh', '.bat', '.ps1', '.exe', '.dll', '.so', '.dylib',
    '.c', '.cpp', '.h', '.hpp', '.java', '.go', '.rs', '.rb',
    '.sql', '.xml', '.env', '.gitignore', '.dockerfile',
    '.ttf', '.otf', '.woff', '.woff2', '.mp3', '.wav', '.mp4',
    '.lock', '.mod', '.sum',
}

# 已知的目录名（不包含扩展名且明确是目录的路径段）
KNOWN_DIR_NAMES = {
    'docs', 'src', 'lib', 'bin', 'test', 'tests', 'examples', 'assets',
    'images', 'img', 'css', 'js', 'fonts', 'data', 'config', 'scripts',
    'templates', 'components', 'utils', 'helpers', 'models', 'views',
    'controllers', 'middleware', 'routes', 'api', 'public', 'static',
    'samples', 'demo', 'demos', 'tutorial', 'guide', 'manuals',
    'screenshots', 'icons', 'resources', 'files', 'downloads',
    'screenshot', 'output', 'input', 'build', 'dist', 'node_modules',
    'vendor', 'packages', 'plugins', 'extensions', 'addons',
    'workflows', 'actions', 'github', 'ci', 'cd',
}

# 图片扩展名
IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.ico', '.bmp'}

# 已知的 master 分支仓库（默认分支不是 main 的）
# 可通过 --update-branch-map 自动补充
KNOWN_MASTER_REPOS = {
    'yzhao062/pyod',
    'chrisneagu/FTC-Skystone-Dark-Angels-Romania-2020',
    'ai-maria/neural',
    'ayoisaiah/focus',
    'chinese-poetry/chinese-poetry',
    'chromy/ink-proof',
    'feralcatden/articy3importerforunreal',
    'furkleindustries/inklecate-node',
    'ggml-org/llama.vim',
    'hanmin0822/misakatranslator',
    'hell13cat/wpd',
    'hexgrad/kokoro',
    'hiev/uinv',
    'inkle/ink-unity-integration',
    'jeremyabel/articyimporterforunreal',
    'languagetool-org/languagetool',
    'liuoodh/honglou_graph',
    'liuyuzhangolvz/novel-kg',
    'manjunath5496/computational-narratology-papers',
    'mingdachen/summscreen',
    'morkt/garbro',
    'mshumer/gpt-author',
    'multimokia/vscode-language-renpy',
    'qiaott/ancientpainitng2naturalimage',
    'rimochan/librian',
    'shaido987/novel-dataset',
    'tothebeginning/pulid',
    'videlais/extwee',
    'yale-lily/qmsum',
    'alephpi/24histories',
    'avgjs/avg-core',
    'InfoTechBridge/UserStory',
    'deepakkamboj/artificial-intelligence-resources',
    'ai-khwarizmi/horst.ai',
    'Hamziss/timerr',
    'coroboros/agent-skills',
    'flegac/JStory',
    'daegunkor/sakkanoheya',
    'sassoftware/sas-viya-programming',
    'Id-Dark-Dragon/Disappearing_Text_Tkinter_App',
    'Vishal-Vunnam/essay_helper',
    'BekCodingAddict/PromptSphere',
    'dylanhogg/gptauthor',
    'jovanyoshioka/Code-a-Story',
    'refahy/tesseract',
    'Apoorve8055/Electropy-Framework',
    'Lhagawajaw/11-36-00-PM-Build-ready-to-start-11-36-02-PM-build-image-version-72a309a113b53ef075815b1299536178',
    'martiansideofthemoon/ai-detection-paraphrases',
    'silviomori/udacity-machine-learning-plagiarism-detector',
    'bemisguided/vscode-ink-language-tools',
    'craigtrim/pystylometry',
    'daihaoguang3151/ocr_fusion',
    'inkle/ink-library',
    'kevboh/longform',
    'koboldai/koboldai-client',
    'ropensci/gutenbergr',
    'rucaibox/recsysdatasets',
    'srinivasvssj/ai-detection-paraphrases',
    'ComposioHQ/content-research-writer',
    'rucaibox/recommendersystems-datasets',
    'gearsincorg/ftcvuforiademo',
    'jackeygao/jackeygao.github.io',
    'inkle/ink',
    'google-research/google-research',
    'chenyuntc/pytorch-book',
    'espeak-ng/espeak-ng',
    'hexiangnan/neural_collaborative_filtering',
    'vladmandic/automatic',
}

# 分支映射缓存文件
BRANCH_MAP_FILE = SCRIPT_DIR / '_branch_map.json'

# 从卡片中提取 repo 的正则
REPO_FM_RE = re.compile(r'^repo:\s*(.+)$', re.MULTILINE)

# GitHub 链接正则
GITHUB_BLOB_RE = re.compile(
    r'https://github\.com/([^/]+/[^/]+)/(blob|tree)/(main|master)/([^\s)"\']+)'
)
GITHUB_RAW_RE = re.compile(
    r'https://raw\.githubusercontent\.com/([^/]+/[^/]+)/([^/]+)/([^\s)"\']+)'
)

# Markdown 外部链接（非图片）
MD_LINK_RE = re.compile(r'(?<!!)\[([^\]]*)\]\(([^)]+)\)')

# Markdown 图片链接
MD_IMG_RE = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')

# 相对路径链接（非外部 URL）
RELATIVE_LINK_RE = re.compile(r'(?<!!)\[([^\]]*)\]\(((?![a-zA-Z][a-zA-Z0-9+.-]*:)[^)]+)\)')

# 相对图片链接
RELATIVE_IMG_RE = re.compile(r'!\[([^\]]*)\]\(((?![a-zA-Z][a-zA-Z0-9+.-]*:)[^)]+)\)')

# 代码块保护
FENCE_RE = re.compile(r'```[^\n]*\n.*?```', re.DOTALL)
INLINE_CODE_RE = re.compile(r'`[^`\n]*`')


# ---------------------------------------------------------------------------
# 工具函数
# ---------------------------------------------------------------------------

def is_file_path(path: str) -> bool:
    """判断路径是否指向文件（基于扩展名和路径模式）。"""
    # 去掉锚点
    path = path.split('#')[0].split('?')[0]

    # 以 / 结尾 → 目录
    if path.endswith('/'):
        return False

    # 有扩展名 → 检查是否在已知文件扩展名列表中
    ext = os.path.splitext(path)[1].lower()
    if ext:
        return ext in FILE_EXTENSIONS

    # 没有扩展名 → 检查最后一节是否可能是目录名
    last_segment = path.rstrip('/').split('/')[-1] if '/' in path else path
    if last_segment in KNOWN_DIR_NAMES:
        return False

    # 包含 . 但不是已知扩展名（如 README） → 可能是文件
    if '.' in last_segment:
        return True

    # 无法确定 → 返回 None（需要外部判断）
    return None


def is_image_path(path: str) -> bool:
    """判断路径是否指向图片文件。"""
    path = path.split('#')[0].split('?')[0]
    ext = os.path.splitext(path)[1].lower()
    return ext in IMAGE_EXTENSIONS


def load_branch_map() -> dict:
    """加载分支映射缓存。"""
    if BRANCH_MAP_FILE.exists():
        with open(BRANCH_MAP_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_branch_map(branch_map: dict):
    """保存分支映射缓存。"""
    with open(BRANCH_MAP_FILE, 'w', encoding='utf-8') as f:
        json.dump(branch_map, f, ensure_ascii=False, indent=2)
        f.write('\n')


def get_default_branch(repo: str, branch_map: dict) -> str:
    """获取仓库的默认分支。"""
    # 先查缓存
    if repo in branch_map:
        return branch_map[repo]
    # 再查已知的 master 仓库
    if repo in KNOWN_MASTER_REPOS:
        branch_map[repo] = 'master'
        return 'master'
    # 默认 main
    branch_map[repo] = 'main'
    return 'main'


def update_branch_map_from_cards(cards_dir: str, branch_map: dict) -> dict:
    """从工具卡中已有的 blob/master/tree/master 链接推断 master 分支仓库。"""
    for f in sorted(os.listdir(cards_dir)):
        if not f.endswith('.md'):
            continue
        fp = os.path.join(cards_dir, f)
        with open(fp, 'r', encoding='utf-8') as fh:
            content = fh.read()

        # 提取 repo
        m = REPO_FM_RE.search(content)
        if not m:
            continue
        repo = m.group(1).strip().strip('"').strip("'")

        # 查找 blob/master 或 tree/master 链接
        for m in re.finditer(r'https://github\.com/[^/]+/[^/]+/(?:blob|tree)/master/', content):
            if repo not in branch_map:
                branch_map[repo] = 'master'

    return branch_map


# ---------------------------------------------------------------------------
# 核心转换
# ---------------------------------------------------------------------------

def absolutize_links(content: str, repo: str, branch_map: dict) -> str:
    """将卡片中的相对链接转换为绝对 URL，并修复 blob/tree 误用。"""
    if not repo:
        return content

    default_branch = get_default_branch(repo, branch_map)

    # 保护代码块中的内容不被转换
    masked, replacements = mask_code_blocks(content)

    # 步骤 1: 修复已存在的 blob/tree 链接中的分支和类型误用
    def fix_existing_blob(m):
        r = m.group(1)  # repo
        link_type = m.group(2)  # blob 或 tree
        branch = m.group(3)  # main 或 master
        path = m.group(4)  # 路径

        # 跳过非本卡 repo 的链接
        if r.lower() != repo.lower():
            return m.group(0)

        # 修正分支
        correct_branch = get_default_branch(repo, branch_map)

        # 判断路径类型
        path_type = is_file_path(path)

        # 修正 blob/tree 误用
        if path_type is True and link_type != 'blob':
            link_type = 'blob'
        elif path_type is False and link_type != 'tree':
            link_type = 'tree'
        # path_type is None → 保留原类型

        # 构造新 URL
        if branch == correct_branch and link_type == m.group(2):
            return m.group(0)  # 无变化

        return f'https://github.com/{r}/{link_type}/{correct_branch}/{path}'

    masked = GITHUB_BLOB_RE.sub(fix_existing_blob, masked)

    # 步骤 2: 转换相对路径为绝对 URL
    def absolutize_relative(m, is_image=False):
        display = m.group(1)
        url = m.group(2).strip()

        # 跳过 #anchor 锚点链接
        if url.startswith('#'):
            return m.group(0)

        # 跳过已经绝对的 URL
        if url.startswith(('http://', 'https://', 'mailto:', 'ftp://')):
            return m.group(0)

        # 跳过占位符
        if re.fullmatch(r'[\u4e00-\u9fff]+', url):
            return m.group(0)

        # 图片 → raw.githubusercontent.com
        if is_image and is_image_path(url):
            base_url = f'https://raw.githubusercontent.com/{repo}/{default_branch}/{url}'
        else:
            path_type = is_file_path(url)
            if path_type is True:
                link_type = 'blob'
            elif path_type is False:
                link_type = 'tree'
            else:
                link_type = 'blob'  # 默认 blob
            base_url = f'https://github.com/{repo}/{link_type}/{default_branch}/{url}'

        if is_image:
            return f'![{display}]({base_url})'
        else:
            return f'[{display}]({base_url})'

    # 先处理图片链接
    masked = RELATIVE_IMG_RE.sub(lambda m: absolutize_relative(m, is_image=True), masked)
    # 再处理普通链接
    masked = RELATIVE_LINK_RE.sub(lambda m: absolutize_relative(m, is_image=False), masked)

    return unmask(masked, replacements)


# ---------------------------------------------------------------------------
# 文件处理
# ---------------------------------------------------------------------------

def process_card(filepath: str, fix: bool, branch_map: dict) -> dict:
    """处理单张工具卡，返回统计信息。"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 提取 repo
    m = REPO_FM_RE.search(content)
    if not m:
        return {'file': filepath, 'status': 'skipped', 'reason': 'no repo field', 'changes': 0}

    repo = m.group(1).strip().strip('"').strip("'")

    # 应用转换
    new_content = absolutize_links(content, repo, branch_map)

    if new_content == content:
        return {'file': filepath, 'status': 'unchanged', 'changes': 0}

    # 统计变化
    changes = 0
    for line_orig, line_new in zip(content.split('\n'), new_content.split('\n')):
        if line_orig != line_new:
            changes += 1

    if fix:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return {'file': filepath, 'status': 'fixed' if fix else 'would_fix', 'changes': changes}


# ---------------------------------------------------------------------------
# 代码块保护
# ---------------------------------------------------------------------------

def mask_code_blocks(text: str) -> tuple:
    """保护代码块和 inline code 中的内容不被转换。"""
    replacements = {}
    counter = [0]

    def make_placeholder(m):
        matched = m.group(0) if hasattr(m, 'group') else m
        key = f'\x00PROTECTED_{counter[0]}\x00'
        replacements[key] = matched
        counter[0] += 1
        return key

    # fenced code blocks
    text = FENCE_RE.sub(make_placeholder, text)
    # inline code
    text = INLINE_CODE_RE.sub(make_placeholder, text)

    return text, replacements


def unmask(text: str, replacements: dict) -> str:
    for key, original in replacements.items():
        text = text.replace(key, original)
    return text


# ---------------------------------------------------------------------------
# 主函数
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='GitHub 链接绝对化转换器（可重复执行版）'
    )
    parser.add_argument('--fix', action='store_true', help='实际执行修正（默认 dry-run）')
    parser.add_argument('--dry-run', action='store_true', help='仅报告，不修改')
    parser.add_argument('--dir', default='tools/cards', help='要处理的目录（相对于项目根）')
    parser.add_argument('--json', action='store_true', help='输出 JSON 格式')
    parser.add_argument('--update-branch-map', action='store_true',
                        help='从工具卡中更新分支映射缓存')
    args = parser.parse_args()

    fix = args.fix
    if args.dry_run:
        fix = False

    cards_dir = (PROJECT_ROOT / args.dir).resolve()
    if not cards_dir.is_dir():
        print(f'错误: 目录不存在 {cards_dir}')
        sys.exit(1)

    # 加载分支映射
    branch_map = load_branch_map()

    if args.update_branch_map:
        update_branch_map_from_cards(str(cards_dir), branch_map)
        save_branch_map(branch_map)
        print(f'已更新分支映射缓存: {BRANCH_MAP_FILE}')
        if args.json:
            print(json.dumps({'branch_map': branch_map}, ensure_ascii=False, indent=2))
        return

    # 扫描卡片
    card_files = sorted([
        f for f in os.listdir(str(cards_dir))
        if f.endswith('.md') and not f.startswith('_')
    ])

    results = []
    total_changes = 0
    fixed_count = 0
    unchanged_count = 0
    skipped_count = 0

    for fname in card_files:
        fp = os.path.join(str(cards_dir), fname)
        result = process_card(fp, fix, branch_map)

        if result['status'] == 'skipped':
            skipped_count += 1
        elif result['status'] == 'unchanged':
            unchanged_count += 1
        else:
            fixed_count += 1
            total_changes += result['changes']

        results.append(result)

    # 输出
    mode = 'FIX' if fix else 'DRY-RUN'
    summary = {
        'mode': mode,
        'cards_scanned': len(card_files),
        'cards_fixed': fixed_count,
        'cards_unchanged': unchanged_count,
        'cards_skipped': skipped_count,
        'total_link_changes': total_changes,
        'branch_map_entries': len(branch_map),
        'results': results,
    }

    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f'{"=" * 60}')
        print(f'GitHub 链接绝对化转换器  ·  模式: {mode}')
        print(f'{"=" * 60}')
        print(f'扫描目录: {cards_dir}')
        print(f'卡片总数: {len(card_files)}')
        print(f'需修正:   {fixed_count}')
        print(f'无需修改: {unchanged_count}')
        print(f'跳过:     {skipped_count}')
        print(f'链接变化: {total_changes}')
        print(f'分支映射: {len(branch_map)} 条')
        print(f'{"=" * 60}')

        if fixed_count > 0:
            print(f'\n需修正的卡片（{fixed_count} 张）：')
            for r in results:
                if r['status'] == 'fixed' or r['status'] == 'would_fix':
                    print(f'  {r["changes"]:4d} 处变化  {os.path.basename(r["file"])}')

        if not fix and fixed_count > 0:
            print(f'\n💡 使用 --fix 参数实际执行修正')
        print(f'{"=" * 60}')

    return 0 if fixed_count == 0 else 1


if __name__ == '__main__':
    sys.exit(main())