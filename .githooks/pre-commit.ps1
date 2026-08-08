# pre-commit.ps1 — 知识库质量门禁（PowerShell 版）
# ============================================
# 通过 _runtime.ps1 统一解析 Python 路径，避免 python3 找不到的问题。
# 由 .githooks/pre-commit（bash 包装器）调用。

$ErrorActionPreference = "Stop"

# 加载运行时解析器
$runtimeScript = Join-Path $PSScriptRoot ".." "maintenance" "scripts" "_runtime.ps1"
if (-not (Test-Path $runtimeScript)) {
    Write-Host "[pre-commit] 错误：找不到 _runtime.ps1: $runtimeScript" -ForegroundColor Red
    exit 1
}
. $runtimeScript

if (-not $Script:Python) {
    Write-Host "[pre-commit] 错误：无法找到可用的 Python，门禁无法运行" -ForegroundColor Red
    Write-Host "[pre-commit] 请检查 _runtime.ps1 中的 Python 路径配置" -ForegroundColor Red
    exit 1
}

$repoRoot = $Script:Root
$validator = Join-Path $repoRoot "tools" "scripts" "maintenance" "提交前校验.py"

if (-not (Test-Path $validator)) {
    Write-Host "[pre-commit] 错误：校验脚本不存在: $validator" -ForegroundColor Red
    exit 1
}

Write-Host "[pre-commit] 运行知识库质量门禁（Python: $Script:Python）..." -ForegroundColor Yellow

# 直接调用校验脚本
$proc = Start-Process -FilePath $Script:Python `
    -ArgumentList $validator, "--core-only" `
    -NoNewWindow -Wait -PassThru

if ($proc.ExitCode -eq 0) {
    Write-Host "[pre-commit] 门禁通过" -ForegroundColor Green
} else {
    Write-Host "[pre-commit] 门禁未通过，提交已阻止" -ForegroundColor Red
    Write-Host "[pre-commit] 如需强制提交，请使用: git commit --no-verify" -ForegroundColor Yellow
}

exit $proc.ExitCode
