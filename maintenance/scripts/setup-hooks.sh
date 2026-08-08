#!/bin/bash
# setup-hooks.sh — 统一安装与自检 Git pre-commit 钩子
# ====================================================
# 用途：
#   1. 设置 core.hooksPath = .githooks（让仓库内钩子生效）
#   2. 校验 Python 候选单一来源文件存在
#   3. 实跑一次门禁，验证钩子链路可用
#
# 用法：
#   bash maintenance/scripts/setup-hooks.sh
#   bash maintenance/scripts/setup-hooks.sh --check   # 只检查不实跑
#
# 说明：Python 候选路径统一由 python-candidates.txt 提供，
#       .githooks/pre-commit（bash）与 _runtime.ps1 均从该文件读取。

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo "$(cd "$(dirname "$0")/../.." && pwd)")"
CAND_FILE="$REPO_ROOT/maintenance/scripts/python-candidates.txt"
HOOKS_DIR=".githooks"

echo "== 钩子安装/自检 =="
echo "仓库根: $REPO_ROOT"

# 1. 设置 core.hooksPath
git config core.hooksPath "$HOOKS_DIR"
echo "✅ core.hooksPath = $(git config core.hooksPath)"

# 2. 校验候选来源
if [ ! -f "$CAND_FILE" ]; then
    echo "❌ python-candidates.txt 不存在: $CAND_FILE" >&2
    exit 1
fi
FOUND=""
while IFS= read -r line; do
    case "$line" in \#*|"") continue ;; esac
    p="${line/\~/$HOME}"
    if [ -f "$p" ]; then FOUND="$p"; break; fi
done < "$CAND_FILE"
if [ -z "$FOUND" ]; then
    echo "⚠️ 候选列表中无可用 Python（将由 PATH 兜底）" >&2
else
    echo "✅ Python: $FOUND"
fi

# 3. 实跑门禁（--check 跳过）
if [ "${1:-}" != "--check" ]; then
    echo "== 实跑 pre-commit 钩子（验证链路）=="
    bash "$REPO_ROOT/.githooks/pre-commit"
    echo "✅ 钩子链路可用（exit 0）"
fi

echo "== 完成 =="
