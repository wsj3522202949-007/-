#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
来源验证.py — 平台指标来源证据完整性校验

校验 platform_metrics.yaml 中每条非 internal 指标的"证据结构"：

  1. source_url 非空
  2. 证据快照文件存在（references/来源证据/<id>_snapshot.html）
  3. 快照非空、非纯 JS 壳（正文长度阈值）
  4. --online 模式：source_url HTTP 可达性实时检查

用法：
  python 来源验证.py                     # 本地证据结构校验（快照存在性+内容）
  python 来源验证.py --online            # 额外做 HTTP 可达性实时检查
  python 来源验证.py --json              # 输出 JSON（供门禁/CI 消费）

退出码：0=全部通过，1=存在缺失/不可达
"""
import os
import sys
import json
import argparse
import urllib.request
import ssl
import re

# 终端编码安全
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # noqa: BLE001
    pass

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
METRICS_FILE = os.path.join(ROOT, "projects", "（已删除项目）", "platform_metrics.yaml")
EVIDENCE_DIR = os.path.join(ROOT, "references", "来源证据")

# 快照文件名约定：<metric_id>_snapshot.html
MIN_TEXT_LEN = 200  # 快照正文（去 HTML 标签后）最小长度，低于视为空壳


def load_metrics():
    import yaml
    with open(METRICS_FILE, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("metrics", [])


def check_local(metric):
    """本地证据结构校验：返回 (issues: list[str], ok: bool)。"""
    issues = []
    mid = metric.get("id", "?")
    stype = metric.get("source_type", "?")
    url = metric.get("source_url")
    # internal 不要求外部证据
    if stype == "internal":
        return issues, True

    if not url:
        issues.append(f"[{mid}] source_url 为空（非 internal 来源必须有 URL）")
    else:
        # 快照文件名：优先用 evidence_file 显式关联，否则回退 <id>_snapshot.html
        snap = metric.get("evidence_file")
        if snap:
            snap = snap if os.path.isabs(snap) else os.path.join(ROOT, snap)
        else:
            snap = os.path.join(EVIDENCE_DIR, f"{mid}_snapshot.html")
        if not os.path.isfile(snap):
            issues.append(f"[{mid}] 证据快照缺失: {os.path.relpath(snap, ROOT)}")
        else:
            with open(snap, encoding="utf-8", errors="replace") as f:
                html = f.read()
            text = re.sub(r"<[^>]+>", " ", html)
            text = re.sub(r"\s+", " ", text).strip()
            if len(text) < MIN_TEXT_LEN:
                issues.append(f"[{mid}] 快照正文过短（{len(text)}<{MIN_TEXT_LEN}），疑似 JS 壳/登录页，需人工复核")
            # 检查是否含 HTML 注释标记（抓取工具写入的时间戳）
            if "抓取时间" not in html:
                issues.append(f"[{mid}] 快照缺少抓取元信息头（非标准快照格式）")
    return issues, len(issues) == 0


def check_online(metric, timeout=15):
    """HTTP 可达性实时检查：返回 (ok: bool, detail: str)。"""
    mid = metric.get("id", "?")
    url = metric.get("source_url")
    if not url:
        return False, "no url"
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            return r.status == 200, f"HTTP {r.status}"
    except Exception as e:  # noqa: BLE001
        return False, f"{type(e).__name__}: {str(e)[:80]}"


def main():
    ap = argparse.ArgumentParser(description="平台指标来源证据校验")
    ap.add_argument("--online", action="store_true", help="额外做 HTTP 可达性检查")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    args = ap.parse_args()

    metrics = load_metrics()
    results = []
    all_ok = True

    for m in metrics:
        issues, local_ok = check_local(m)
        entry = {
            "id": m.get("id"),
            "source_type": m.get("source_type"),
            "source_url": m.get("source_url"),
            "local_ok": local_ok,
            "issues": issues,
        }
        if args.online and m.get("source_type") != "internal":
            ok, detail = check_online(m)
            entry["online_ok"] = ok
            entry["online_detail"] = detail
            if not ok:
                all_ok = False
        if not local_ok:
            all_ok = False
        results.append(entry)

    if args.json:
        print(json.dumps({"overall_pass": all_ok, "results": results}, ensure_ascii=False, indent=2))
    else:
        for r in results:
            status = "✅" if r["local_ok"] else "❌"
            tag = f" | online {r['online_detail']}" if "online_detail" in r else ""
            print(f"{status} [{r['id']}] ({r['source_type']}){tag}")
            for iss in r["issues"]:
                print(f"     ⚠️ {iss}")
        print(f"\n{'✅ 全部证据完整' if all_ok else '❌ 存在证据缺失'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
