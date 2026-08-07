#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
http_link_validator.py — 工具卡外部链接 HTTP 有效性校验器

与 link_absolutizer.py 的关系
-----------------------------
本工具是"第二道门禁"：只做真实 HTTP 200/404 校验，不处理文本/语法转换。
第一道门禁 link_absolutizer.py 只做语法转换（相对→绝对、blob/tree 修正）。

两门禁模型
----------
  门禁1 (link_absolutizer)  → 全量卡片，语法层：URL 格式/路径正确性
  门禁2 (http_link_validator) → S/A 级卡片，HTTP 层：真实可达性

这解决了"假绿"问题：转换器报告全部通过不代表链接真的可访问。

校验范围
--------
默认只校验 S/A 级工具卡（--tiers S,A），因为 HTTP 校验耗时且受 GitHub API 限流影响。
C/D 级卡片只需通过第一道门禁即可。需要全量校验时使用 --tiers all。

用法
----
    python tools/scripts/quality/http_link_validator.py              # 默认 S,A 级
    python tools/scripts/quality/http_link_validator.py --tiers all  # 全部卡片
    python tools/scripts/quality/http_link_validator.py --tiers S,A,B
    python tools/scripts/quality/http_link_validator.py --json       # 机器可读
    python tools/scripts/quality/http_link_validator.py --json-file report.json

退出码：发现 404 → 1；全部可达 → 0
"""

import os
import re
import sys
import json
import time
import argparse
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path
from collections import defaultdict

# ---- 路径 ----
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = (SCRIPT_DIR / '..' / '..').resolve()
CARDS_DIR = PROJECT_ROOT / 'tools' / 'cards'

# ---- 正则 ----
TIER_FM_RE = re.compile(r'^tier:\s*"([^"]+)"', re.MULTILINE)
REPO_FM_RE = re.compile(r'^repo:\s*(.+)$', re.MULTILINE)
GITHUB_URL_RE = re.compile(
    r'https://github\.com/([^/\s"\')\]]+/[^/\s"\')\]]+)/(?:blob|tree)/([^/\s"\')\]]+)/([^\s"\')\]]+)')
GITHUB_RAW_RE = re.compile(
    r'https://raw\.githubusercontent\.com/([^/\s"\')\]]+/[^/\s"\')\]]+)/([^/\s"\')\]]+)/([^\s"\')\]]+)')
MD_EXT_LINK_RE = re.compile(r'(?<!!)\[([^\]]*)\]\((https?://[^)]+)\)')
MD_IMG_RE = re.compile(r'!\[([^\]]*)\]\((https?://[^)]+)\)')
FENCE_RE = re.compile(r'```[^\n]*\n.*?```', re.DOTALL)
INLINE_CODE_RE = re.compile(r'`[^`\n]*`')

# 占位关键词（这些 URL 中的链接本质是占位符，不参与 HTTP 校验）
PLACEHOLDER_KW = {
    'your-username', 'your-repo', 'your-org', 'your-name', 'your-token',
    'placeholder', 'username/repo', 'example', 'sample',
    '此处', '请替换', '插入',
}


def _is_placeholder_url(url: str) -> bool:
    """检测 URL 是否包含占位内容，不应进行 HTTP 校验。"""
    lower = url.lower()
    for kw in PLACEHOLDER_KW:
        if kw in lower:
            return True
    # 中文路径 → 可能是占位
    decoded = urllib.parse.unquote(url)
    for kw in ('此处', '请替换', '项目Issue地址', '项目地址'):
        if kw in decoded:
            return True
    return False


def extract_urls(content: str) -> list[dict]:
    """从卡片内容中提取所有外部 URL（去重）。"""
    urls = {}
    # 保护代码块
    masked = content
    for pat in (FENCE_RE, INLINE_CODE_RE):
        masked = pat.sub('', masked)

    def _add(url: str, link_type: str):
        if url in urls:
            return
        if not url.startswith('http'):
            return
        if _is_placeholder_url(url):
            urls[url] = {'type': link_type, 'skip': True, 'reason': 'placeholder'}
            return
        urls[url] = {'type': link_type, 'skip': False}

    for m in GITHUB_URL_RE.finditer(masked):
        _add(m.group(0), 'github')
    for m in GITHUB_RAW_RE.finditer(masked):
        _add(m.group(0), 'raw')
    for m in MD_EXT_LINK_RE.finditer(masked):
        _add(m.group(2), 'markdown')
    for m in MD_IMG_RE.finditer(masked):
        _add(m.group(2), 'image')

    return [{'url': url, **info} for url, info in urls.items()]


def check_url(url: str, timeout: int = 8) -> tuple[int | None, str | None]:
    """HTTP HEAD 请求，返回 (status_code, error_message)。"""
    try:
        req = urllib.request.Request(url, method='HEAD',
                                     headers={'User-Agent': 'http-link-validator/1.0'})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return (resp.status, None)
    except urllib.error.HTTPError as e:
        return (e.code, str(e))
    except Exception as e:
        return (None, str(e))


def validate_card(filepath: str) -> dict:
    """校验单张工具卡的所有外部链接。"""
    fname = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    tm = TIER_FM_RE.search(content)
    tier = tm.group(1).upper() if tm else '?'

    urls = extract_urls(content)
    # 只校验非占位链接
    active = [u for u in urls if not u['skip']]
    skipped = [u for u in urls if u['skip']]

    failures = []
    ok_count = 0
    for u in active:
        status, err = check_url(u['url'])
        if status == 404 or status is None:
            failures.append({
                'url': u['url'],
                'type': u['type'],
                'status': status,
                'error': err,
            })
        else:
            ok_count += 1
        time.sleep(0.1)  # 限流

    return {
        'file': fname,
        'tier': tier,
        'total_urls': len(active),
        'ok': ok_count,
        'failed': len(failures),
        'skipped': len(skipped),
        'failures': failures,
    }


def validate_all(cards_dir: str, tiers: set[str]) -> list[dict]:
    """扫描并校验指定等级的工具卡。"""
    results = []
    card_files = sorted([
        f for f in os.listdir(cards_dir)
        if f.endswith('.md') and not f.startswith('_')
    ])

    total = len(card_files)
    validated = 0
    skipped_tier = 0

    for i, fname in enumerate(card_files, 1):
        fp = os.path.join(cards_dir, fname)
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read(2048)  # 只读头部获取 tier
        tm = TIER_FM_RE.search(content)
        tier = tm.group(1).upper() if tm else '?'

        if tiers and tier not in tiers:
            skipped_tier += 1
            continue

        validated += 1
        sys.stdout.write(f'\r[{i}/{total}] 校验 {fname}...')
        sys.stdout.flush()

        r = validate_card(fp)
        results.append(r)

    sys.stdout.write('\r' + ' ' * 60 + '\r')
    sys.stdout.flush()

    # 摘要
    print(f'扫描: {total} 张卡片 | 校验: {validated} ({",".join(sorted(tiers)) if tiers else "all"}级) | 跳过: {skipped_tier}')
    return results


def print_report(results: list[dict]):
    """人类可读报告。"""
    total_ok = sum(r['ok'] for r in results)
    total_failed = sum(r['failed'] for r in results)
    total_skipped = sum(r['skipped'] for r in results)
    total_urls = total_ok + total_failed

    print(f'链接总数: {total_urls} (跳过占位: {total_skipped})')
    print(f'可达: {total_ok}  |  不可达: {total_failed}')
    print('=' * 72)

    # 按 tier 分组
    by_tier: dict[str, list] = defaultdict(list)
    for r in results:
        by_tier[r['tier']].append(r)

    for tier in sorted(by_tier.keys()):
        cards = by_tier[tier]
        t_ok = sum(r['ok'] for r in cards)
        t_failed = sum(r['failed'] for r in cards)
        if t_failed == 0:
            continue
        print(f'\n[{tier} 级] {t_failed} 个不可达链接:')
        for r in cards:
            if not r['failures']:
                continue
            for f in r['failures']:
                icon = '404' if f['status'] == 404 else 'ERR'
                print(f'  [{icon}] {r["file"]}')
                print(f'        {f["url"][:90]}')

    if total_failed == 0:
        print('\n全部校验链接均可达 ✅')


def main():
    ap = argparse.ArgumentParser(
        description='工具卡外部链接 HTTP 有效性校验器（第二道门禁）')
    ap.add_argument('--tiers', default='S,A',
                    help='校验等级，逗号分隔；默认 S,A；all=全部 (default: S,A)')
    ap.add_argument('--dir', default=str(CARDS_DIR),
                    help='工具卡目录 (default: tools/cards)')
    ap.add_argument('--json', action='store_true', help='输出 JSON')
    ap.add_argument('--json-file', help='写入 JSON 报告文件')
    ap.add_argument('--timeout', type=int, default=8,
                    help='单次 HTTP 超时秒数 (default: 8)')
    args = ap.parse_args()

    # 解析 tiers
    tiers_raw = args.tiers.upper().strip()
    if tiers_raw == 'ALL':
        tiers = None  # 全部
    else:
        tiers = set(t.strip() for t in tiers_raw.split(',') if t.strip())

    cards_dir = Path(args.dir)
    if not cards_dir.is_dir():
        print(f'错误: 目录不存在 {cards_dir}', file=sys.stderr)
        sys.exit(1)

    print(f'HTTP 链接有效性校验器 — 门禁2（{",".join(sorted(tiers)) if tiers else "全量"}级）')
    print('=' * 72)

    results = validate_all(str(cards_dir), tiers)
    print_report(results)

    # 统计失效
    total_failed = sum(r['failed'] for r in results)

    if args.json_file:
        with open(args.json_file, 'w', encoding='utf-8') as f:
            json.dump({
                'cards_validated': len(results),
                'total_urls': sum(r['total_urls'] for r in results),
                'total_failed': total_failed,
                'results': results,
            }, f, ensure_ascii=False, indent=2)
        print(f'\nJSON 报告已写入: {args.json_file}')

    if args.json:
        print(json.dumps({
            'cards_validated': len(results),
            'total_failed': total_failed,
            'results': results,
        }, ensure_ascii=False, indent=2))

    return 1 if total_failed > 0 else 0


if __name__ == '__main__':
    sys.exit(main())
