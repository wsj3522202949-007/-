# -*- coding: utf-8 -*-
"""验收报告登记器 —— 防止历史报告长期冒充当前事实。

背景：验收报告（门禁 JSON / 周报 / 清理报告等）如果缺少版本元数据，
旧报告会一直以「当前事实」的面貌存在，新结论出现后无人知道哪份有效。
本脚本与 run_all.py 的 JSON 元数据字段（observed_commit / generated_at /
valid_until / superseded_by）配套：

  1. register：扫描 maintenance/reports/ 下全部 .md 报告，读取 frontmatter
     （缺失时从文件 mtime 兜底），写入 maintenance/state/report-registry.json
  2. supersede <file> <commit>：把某份报告标记为被新提交/新报告取代
     （回填 superseded_by），该报告从此视为过期
  3. list：列出登记表，标注 status=active/superseded/expired

用法：
  python 验收报告登记.py register
  python 验收报告登记.py list
  python 验收报告登记.py supersede maintenance/reports/xxx.md <commit-or-id>
"""

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timedelta

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
REPORTS_DIR = os.path.join(ROOT, "maintenance", "reports")
STATE_DIR = os.path.join(ROOT, "maintenance", "state")
REGISTRY = os.path.join(STATE_DIR, "report-registry.json")


def read_frontmatter(path):
    """读取 .md frontmatter 关键字段；无 frontmatter 返回空 dict。"""
    try:
        raw = open(path, encoding="utf-8", errors="replace").read(4000)
    except OSError:
        return {}
    if not raw.startswith("---"):
        return {}
    lines = raw.split("\n")
    end = None
    for i in range(1, min(len(lines), 60)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}
    fm = {}
    for line in lines[1:end]:
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return fm


def file_sha(path, length=12):
    """内容哈希（前 length 位），作为报告内容指纹。"""
    try:
        h = hashlib.sha256()
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()[:length]
    except OSError:
        return None


def mtime_iso(path):
    try:
        return datetime.fromtimestamp(os.path.getmtime(path)).isoformat()
    except OSError:
        return None


def collect():
    entries = {}
    for dirpath, _dirnames, filenames in os.walk(REPORTS_DIR):
        for fname in sorted(filenames):
            if not fname.endswith(".md"):
                continue
            path = os.path.join(dirpath, fname)
            rel = os.path.relpath(path, ROOT).replace("\\", "/")
            fm = read_frontmatter(path)
            generated = fm.get("generated_at") or fm.get("created") \
                or mtime_iso(path)
            observed = fm.get("observed_commit") or "unknown"
            entries[rel] = {
                "file": rel,
                "title": fm.get("title", fname),
                "observed_commit": observed,
                "generated_at": generated,
                "valid_until": fm.get("valid_until")
                or _default_valid_until(generated),
                "superseded_by": fm.get("superseded_by"),
                "content_hash": file_sha(path),
            }
    return entries


def _default_valid_until(generated):
    try:
        return (datetime.fromisoformat(generated)
                + timedelta(days=30)).isoformat()
    except (ValueError, TypeError):
        return None


def load_registry():
    if os.path.isfile(REGISTRY):
        try:
            return json.load(open(REGISTRY, encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def save_registry(reg):
    os.makedirs(STATE_DIR, exist_ok=True)
    with open(REGISTRY, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(reg, fh, ensure_ascii=False, indent=2)


def status_of(entry, now=None):
    now = now or datetime.now()
    if entry.get("superseded_by"):
        return "superseded"
    try:
        valid = datetime.fromisoformat(entry["valid_until"])
        if now > valid:
            return "expired"
    except (ValueError, TypeError, KeyError):
        pass
    return "active"


def main():
    ap = argparse.ArgumentParser(description="验收报告登记器")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("register", help="扫描并登记全部报告")
    sub.add_parser("list", help="列出登记表")
    p3 = sub.add_parser("supersede", help="标记报告被取代")
    p3.add_argument("file", help="报告相对路径，如 maintenance/reports/xxx.md")
    p3.add_argument("by", help="取代它的提交/报告标识")

    args = ap.parse_args()

    if args.cmd == "register":
        entries = collect()
        old = load_registry()
        # 保留既有 superseded_by 回填（collect 只读 frontmatter，不覆盖回填态）
        for rel, e in entries.items():
            if rel in old and old[rel].get("superseded_by"):
                e["superseded_by"] = old[rel]["superseded_by"]
        save_registry(entries)
        active = sum(1 for e in entries.values()
                     if status_of(e) == "active")
        print(f"已登记 {len(entries)} 份报告（active {active}）→ {REGISTRY}")
        return 0

    if args.cmd == "list":
        reg = load_registry()
        if not reg:
            print("登记表为空，先运行 register")
            return 0
        rows = []
        for rel, e in sorted(reg.items()):
            st = status_of(e)
            flag = {"active": "✅", "superseded": "⏭", "expired": "⌛"}.get(st, "?")
            rows.append(f"{flag} [{st:9}] {e['generated_at'][:10] if e['generated_at'] else '?':10} "
                        f"{e['observed_commit'][:8]:8} {rel}")
        print("\n".join(rows))
        return 0

    if args.cmd == "supersede":
        reg = load_registry()
        target = args.file.replace("\\", "/")
        if target not in reg:
            # 容错：允许传入 basename
            hits = [k for k in reg if k.endswith(target.split("/")[-1])]
            if len(hits) == 1:
                target = hits[0]
            else:
                print(f"登记表中未找到 {target}")
                return 1
        reg[target]["superseded_by"] = args.by
        save_registry(reg)
        print(f"已标记 {target} 被 {args.by} 取代（superseded）")
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
