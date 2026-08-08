#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
http_link_validator.py — 工具卡外部链接 HTTP 有效性校验器（v2：语义化判决）

与 link_absolutizer.py 的关系
-----------------------------
本工具是"第二道门禁"：只做真实 HTTP 200/404 校验，不处理文本/语法转换。
第一道门禁 link_absolutizer.py 只做语法转换（相对→绝对、blob/tree 修正）。

判决模型（v2）
-------------
  PASS         : 成功率 ≥ 阈值 且 无新增坏链
  INCONCLUSIVE : 无法判定的链接比例 > 阈值（超时/连接失败太多）
  FAIL         : 出现新增坏链（不在 known_broken_links 基线中）

基线管理
--------
  --update-baseline   将当前坏链写入基线（必须显式指定才能修改基线）
  基线文件: maintenance/state/known_broken_links.json

用法
----
    python tools/scripts/quality/http_link_validator.py              # S,A 级
    python tools/scripts/quality/http_link_validator.py --tiers all
    python tools/scripts/quality/http_link_validator.py --update-baseline
    python tools/scripts/quality/http_link_validator.py --json
    python tools/scripts/quality/http_link_validator.py --json-file report.json

退出码
------
  0 → PASS
  1 → INCONCLUSIVE（非致命，但需关注）
  2 → FAIL（新增坏链，阻断）
"""

import os
import re
import sys
import json
from datetime import datetime
import time
import argparse
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path
from collections import defaultdict

# Windows GBK 终端安全：避免 emoji/中文输出 UnicodeEncodeError
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass

# ---- 默认阈值 ----
DEFAULT_SUCCESS_THRESHOLD = 0.80    # 至少 80% 的链接可访问才算通过
DEFAULT_UNKNOWN_THRESHOLD = 0.50    # 超过 50% 无法判定 → INCONCLUSIVE

# ---- 路径（PROJECT_ROOT 在 main() 中可变）----
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = (SCRIPT_DIR / '..' / '..').resolve()


def _get_paths(root=None):
    """返回 (cards_dir, state_dir, baseline_file)。"""
    r = root or PROJECT_ROOT
    return (
        r / 'tools' / 'cards',
        r / 'maintenance' / 'state',
        r / 'maintenance' / 'state' / 'known_broken_links.json',
    )

# ---- 正则 ----
TIER_FM_RE = re.compile(r'^tier:\s*"([^"]+)"', re.MULTILINE)
GITHUB_URL_RE = re.compile(
    r'https://github\.com/([^/\s"\')\]]+/[^/\s"\')\]]+)/(?:blob|tree)/([^/\s"\')\]]+)/([^\s"\')\]]+)')
GITHUB_RAW_RE = re.compile(
    r'https://raw\.githubusercontent\.com/([^/\s"\')\]]+/[^/\s"\')\]]+)/([^/\s"\')\]]+)/([^\s"\')\]]+)')
MD_EXT_LINK_RE = re.compile(r'(?<!!)\[([^\]]*)\]\((https?://[^)]+)\)')
MD_IMG_RE = re.compile(r'!\[([^\]]*)\]\((https?://[^)]+)\)')
FENCE_RE = re.compile(r'```[^\n]*\n.*?```', re.DOTALL)
INLINE_CODE_RE = re.compile(r'`[^`\n]*`')

PLACEHOLDER_KW = {
    'your-username', 'your-repo', 'your-org', 'your-name', 'your-token',
    'placeholder', 'username/repo', 'example', 'sample',
    '此处', '请替换', '插入',
}


def _is_placeholder_url(url: str) -> bool:
    lower = url.lower()
    for kw in PLACEHOLDER_KW:
        if kw in lower:
            return True
    decoded = urllib.parse.unquote(url)
    for kw in ('此处', '请替换', '项目Issue地址', '项目地址'):
        if kw in decoded:
            return True
    return False


def extract_urls(content: str) -> list[dict]:
    urls = {}
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


def check_url(url: str, timeout: int = 8) -> dict:
    """HTTP HEAD 请求，返回 {status, category, error}。

    category: 'pass' (200-399), 'broken' (404/410/5xx), 'unknown' (timeout/dns/其他)
    """
    try:
        req = urllib.request.Request(url, method='HEAD',
                                     headers={'User-Agent': 'http-link-validator/2.0'})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return {'status': resp.status, 'category': 'pass', 'error': None}
    except urllib.error.HTTPError as e:
        cat = 'broken' if e.code in (404, 410) or e.code >= 500 else 'unknown'
        return {'status': e.code, 'category': cat, 'error': str(e)}
    except urllib.error.URLError as e:
        # 连接失败/超时/DNS → unknown（可能是瞬时网络问题）
        return {'status': None, 'category': 'unknown',
                'error': str(e.reason) if hasattr(e, 'reason') else str(e)}
    except Exception as e:
        return {'status': None, 'category': 'unknown', 'error': str(e)}


def load_baseline(filepath=None):
    """加载已知坏链基线。

    支持两种格式：
      v2（推荐）：{"created_at": ISO时间, "urls": [...]} —— 可判断基线时效
      v1（旧）：纯字符串列表 —— 视为未知时效（调用方警告）
    """
    path = Path(filepath) if filepath else _get_paths()[2]
    if not path.is_file():
        return set()
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return set(data)
        if isinstance(data, dict) and isinstance(data.get('urls'), list):
            return set(data['urls'])
        return set()
    except Exception:
        return set()


def baseline_stale_days(filepath=None):
    """基线文件存在但超过 STALE_DAYS 未更新 → 返回天数；否则 0。"""
    path = Path(filepath) if filepath else _get_paths()[2]
    if not path.is_file():
        return 0
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        created = None
        if isinstance(data, dict):
            created = data.get('created_at')
        elif isinstance(data, list):
            # v1 旧格式：以文件 mtime 兜底
            return 0  # 无法判断，交给调用方提示
        if not created:
            return 0
        created_dt = datetime.fromisoformat(created)
        return (datetime.now() - created_dt).days
    except Exception:
        return 0


def save_baseline(urls: set, filepath=None):
    """保存坏链基线到文件（v2 格式：含 created_at 时间戳）。"""
    path = Path(filepath) if filepath else _get_paths()[2]
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "created_at": datetime.now().isoformat(timespec='seconds'),
        "urls": sorted(urls),
    }
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def validate_card(filepath: str) -> dict:
    fname = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    tm = TIER_FM_RE.search(content)
    tier = tm.group(1).upper() if tm else '?'

    urls = extract_urls(content)
    active = [u for u in urls if not u['skip']]
    skipped = len(urls) - len(active)

    total_pass = 0
    total_broken = 0
    total_unknown = 0
    broken_urls = []
    unknown_urls = []

    for u in active:
        result = check_url(u['url'])
        cat = result['category']
        if cat == 'pass':
            total_pass += 1
        elif cat == 'broken':
            total_broken += 1
            broken_urls.append(u['url'])
        else:
            total_unknown += 1
            unknown_urls.append(u['url'])
        time.sleep(0.1)

    return {
        'file': fname,
        'tier': tier,
        'total_pass': total_pass,
        'total_broken': total_broken,
        'total_unknown': total_unknown,
        'total_skipped': skipped,
        'total_active': len(active),
        'broken_urls': broken_urls,
        'unknown_urls': unknown_urls,
    }


def validate_all(cards_dir: str, tiers: set[str]) -> list[dict]:
    results = []
    card_files = sorted([
        f for f in os.listdir(cards_dir)
        if f.endswith('.md') and not f.startswith('_')
    ])
    total = len(card_files)
    validated = skipped_tier = 0

    for i, fname in enumerate(card_files, 1):
        fp = os.path.join(cards_dir, fname)
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read(2048)
        tm = TIER_FM_RE.search(content)
        tier = tm.group(1).upper() if tm else '?'
        if tiers and tier not in tiers:
            skipped_tier += 1
            continue
        validated += 1
        sys.stdout.write(f'\r[{i}/{total}] 校验 {fname}...')
        sys.stdout.flush()
        results.append(validate_card(fp))

    sys.stdout.write('\r' + ' ' * 60 + '\r')
    sys.stdout.flush()
    tier_label = ",".join(sorted(tiers)) if tiers else "all"
    print(f'扫描: {total} 张卡片 | 校验: {validated} ({tier_label}级) | 跳过: {skipped_tier}')
    return results


def compute_verdict(results: list[dict], baseline: set,
                    success_threshold: float, unknown_threshold: float) -> dict:
    """基于校验结果和基线计算判决。

    返回: {verdict, success_ratio, unknown_ratio, new_broken, ...}
    """
    total_pass = sum(r['total_pass'] for r in results)
    total_broken = sum(r['total_broken'] for r in results)
    total_unknown = sum(r['total_unknown'] for r in results)
    total_active = sum(r['total_active'] for r in results)

    if total_active == 0:
        return {
            'verdict': 'INCONCLUSIVE', 'reason': '没有有效链接',
            'total_pass': 0, 'total_broken': 0, 'total_unknown': 0,
            'success_ratio': 0, 'unknown_ratio': 0, 'new_broken': [],
            'regression': None,
        }

    # 收集当前所有坏链 URL 与不可达 URL（UNKNOWN）
    current_broken = set()
    current_unknown = set()
    for r in results:
        for u in r['broken_urls']:
            current_broken.add(u)
        for u in r.get('unknown_urls', []):
            current_unknown.add(u)

    # 新增坏链 = 当前坏链 - 基线中的已知坏链
    new_broken = sorted(current_broken - baseline)

    # 已修复的坏链（在基线中，本次可达且非 UNKNOWN）
    # 注意：基线中的 URL 若本次返回 UNKNOWN（超时/不可达），不能算"已修复"——
    # 它可能仍然是坏链，只是网络条件不同。只有本次确认可达（不在 broken 也不在
    # unknown）才归入 fixed。
    fixed = sorted(baseline - current_broken - current_unknown)

    success_ratio = total_pass / total_active
    unknown_ratio = total_unknown / total_active

    # 判决逻辑
    if new_broken:
        verdict = 'FAIL'
        reason = f'新增 {len(new_broken)} 个坏链'
    elif unknown_ratio > unknown_threshold:
        verdict = 'INCONCLUSIVE'
        reason = (f'无法判定的链接过多 ({total_unknown}/{total_active}, '
                  f'{unknown_ratio:.0%} > {unknown_threshold:.0%})')
    elif success_ratio < success_threshold:
        verdict = 'INCONCLUSIVE'
        reason = (f'成功率不足 ({total_pass}/{total_active}, '
                  f'{success_ratio:.0%} < {success_threshold:.0%})')
    else:
        verdict = 'PASS'
        reason = (f'成功率 {success_ratio:.0%} ≥ {success_threshold:.0%}，'
                  f'无新增坏链')

    return {
        'verdict': verdict,
        'reason': reason,
        'total_pass': total_pass,
        'total_broken': total_broken,
        'total_unknown': total_unknown,
        'total_active': total_active,
        'success_ratio': round(success_ratio, 4),
        'unknown_ratio': round(unknown_ratio, 4),
        'new_broken': new_broken,
        'regression': {
            'new': len(new_broken),
            'fixed': len(fixed),
            'urls': new_broken,
            'fixed_urls': fixed,
        },
        'baseline_size': len(baseline),
    }


def print_report(results: list[dict], verdict: dict):
    """人类可读报告。"""
    print(f'链接总数: {verdict["total_active"]}'
          f' (跳过占位: {sum(r["total_skipped"] for r in results)})')
    print(f'可达: {verdict["total_pass"]}  |  坏链: {verdict["total_broken"]}'
          f'  |  无法判定: {verdict["total_unknown"]}')
    print(f'成功率: {verdict["success_ratio"]:.0%}'
          f'  |  判定率: {(verdict["total_pass"] + verdict["total_broken"]) / max(verdict["total_active"], 1):.0%}')
    print('=' * 72)

    # 按 tier 分组显示坏链
    by_tier: dict[str, list] = defaultdict(list)
    for r in results:
        by_tier[r['tier']].append(r)

    for tier in sorted(by_tier.keys()):
        cards = by_tier[tier]
        t_broken = sum(r['total_broken'] for r in cards)
        if t_broken == 0:
            continue
        print(f'\n[{tier} 级] {t_broken} 个坏链:')
        for r in cards:
            if not r['broken_urls']:
                continue
            for u in r['broken_urls']:
                print(f'  [BROKEN] {r["file"]}')
                print(f'          {u[:90]}')

    # 判决
    print(f'\n{"=" * 72}')
    labels = {'PASS': '✅ PASS', 'FAIL': '❌ FAIL', 'INCONCLUSIVE': '⚠️ INCONCLUSIVE'}
    label = labels.get(verdict['verdict'], verdict['verdict'])
    print(f'判决: {label}')
    print(f'原因: {verdict["reason"]}')

    if verdict['regression'] and verdict['regression']['new'] > 0:
        print(f'\n新增坏链 ({verdict["regression"]["new"]} 个):')
        for u in verdict['regression']['urls']:
            print(f'  - {u}')

    if verdict['regression'] and verdict['regression']['fixed'] > 0:
        print(f'\n已修复 ({verdict["regression"]["fixed"]} 个):')
        for u in verdict['regression']['fixed_urls']:
            print(f'  + {u}')

    if verdict['baseline_size'] > 0:
        print(f'\n基线：{verdict["baseline_size"]} 个已知坏链')


def main():
    ap = argparse.ArgumentParser(
        description='工具卡外部链接 HTTP 有效性校验器（第二道门禁）')
    ap.add_argument('--tiers', default='S,A',
                    help='校验等级，逗号分隔；默认 S,A；all=全部')
    ap.add_argument('--dir', default=str(_get_paths()[0]), help='工具卡目录')
    ap.add_argument('--json', action='store_true', help='输出 JSON')
    ap.add_argument('--json-file', help='写入 JSON 报告文件')
    ap.add_argument('--timeout', type=int, default=8,
                    help='单次 HTTP 超时秒数 (default: 8)')
    ap.add_argument('--update-baseline', action='store_true',
                    help='将当前坏链写入基线（必须显式指定）')
    ap.add_argument('--success-threshold', type=float,
                    default=DEFAULT_SUCCESS_THRESHOLD,
                    help=f'成功率阈值 (default: {DEFAULT_SUCCESS_THRESHOLD})')
    ap.add_argument('--unknown-threshold', type=float,
                    default=DEFAULT_UNKNOWN_THRESHOLD,
                    help=f'无法判定比例阈值 (default: {DEFAULT_UNKNOWN_THRESHOLD})')
    ap.add_argument('--root', help='仓库根目录（覆盖自动检测）')
    args = ap.parse_args()

    # 分辨率路径（--root 覆盖自动检测）
    root = Path(args.root) if args.root else None
    cards_dir_path, state_dir, baseline_file = _get_paths(root)

    # 解析 tiers
    tiers_raw = args.tiers.upper().strip()
    if tiers_raw == 'ALL':
        tiers = None
    else:
        tiers = set(t.strip() for t in tiers_raw.split(',') if t.strip())

    if args.dir != str(_get_paths()[0]):
        cards_dir_path = Path(args.dir)
    if not cards_dir_path.is_dir():
        print(f'错误: 目录不存在 {cards_dir_path}', file=sys.stderr)
        sys.exit(1)

    # 加载基线
    baseline = load_baseline(baseline_file)

    # 基线时效警告：过期的基线会把旧的坏链当成"已知"，掩盖新增回归
    STALE_DAYS = 30
    stale = baseline_stale_days(baseline_file)
    if baseline and stale >= STALE_DAYS:
        print(f'⚠️ 基线已 {stale} 天未更新（>{STALE_DAYS} 天），可能掩盖新增坏链。'
              f'如卡片内容已大改，请用 --update-baseline 重建基线。', file=sys.stderr)
    if baseline and stale == 0 and baseline_file.is_file():
        # v1 旧格式基线：提醒迁移
        try:
            with open(baseline_file, 'r', encoding='utf-8') as f:
                _d = json.load(f)
            if isinstance(_d, list):
                print('⚠️ 检测到 v1 旧格式基线（无时间戳）。'
                      '建议运行 --update-baseline 升级为 v2 格式。', file=sys.stderr)
        except Exception:
            pass

    tier_label = ",".join(sorted(tiers)) if tiers else "全量"
    print(f'HTTP 链接有效性校验器 — 门禁2（{tier_label}级）')
    print(f'阈值: 成功率≥{args.success_threshold:.0%}  无法判定≤{args.unknown_threshold:.0%}')
    print(f'基线: {len(baseline)} 个已知坏链')
    print('=' * 72)

    results = validate_all(str(cards_dir_path), tiers)
    verdict = compute_verdict(results, baseline,
                              args.success_threshold, args.unknown_threshold)
    print_report(results, verdict)

    # 更新基线
    if args.update_baseline:
        current_broken = set()
        for r in results:
            for u in r['broken_urls']:
                current_broken.add(u)
        save_baseline(current_broken, baseline_file)
        print(f'\n基线已更新: {len(current_broken)} 个坏链 → {baseline_file}')

    # 输出 JSON
    output = {
        'cards_validated': len(results),
        **verdict,
        'results': [
            {k: v for k, v in r.items() if k != 'broken_urls'}
            for r in results
        ],
    }

    if args.json_file:
        os.makedirs(os.path.dirname(args.json_file) or '.', exist_ok=True)
        with open(args.json_file, 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        print(f'\nJSON 报告已写入: {args.json_file}')

    if args.json:
        print(json.dumps(output, ensure_ascii=False, indent=2))

    # 退出码
    if verdict['verdict'] == 'FAIL':
        return 2
    elif verdict['verdict'] == 'INCONCLUSIVE':
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
