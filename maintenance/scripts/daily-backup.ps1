#!/usr/bin/env pwsh
# 每日自动备份脚本
# 时间：每日 23:30
# 依赖：run_all.py（统一门禁）、Git

$ErrorActionPreference = "Stop"
$GIT = "C:\Users\wsj\.workbuddy\vendor\PortableGit\cmd\git.exe"
$ROOT = "e:\个人知识库"
$RUN_ALL = "python tools/scripts/validation/run_all.py"
$LOG_FILE = "maintenance\backup-log.jsonl"

Set-Location $ROOT

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  每日自动备份" -ForegroundColor Cyan
Write-Host "  时间: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 1. 运行统一门禁校验
Write-Host "🔍 运行统一门禁校验..." -ForegroundColor Yellow
$jsonOutput = & $RUN_ALL --json 2>$null
$checkResult = $jsonOutput | ConvertFrom-Json

$basicErrors = $checkResult.summary.basic.errors
$linkErrors = $checkResult.summary.'core_broken_links'.errors
$overallPass = $checkResult.summary.overall_pass

if (-not $overallPass) {
    Write-Host "❌ 校验失败，基本错误: $basicErrors，断链错误: $linkErrors" -ForegroundColor Red
    Write-Host "   跳过本次提交和推送" -ForegroundColor Red
    exit 1
}

Write-Host "✅ 校验通过（基本: $basicErrors ERROR | 断链: $linkErrors ERROR）" -ForegroundColor Green
Write-Host ""

# 2. Git 提交
Write-Host "📦 Git 提交..." -ForegroundColor Yellow
& $GIT add -A
$commitMessage = "auto: daily backup $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
& $GIT commit -m $commitMessage 2>&1 | Out-Null

if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  无更改需要提交" -ForegroundColor Yellow
} else {
    Write-Host "✅ 提交成功" -ForegroundColor Green
}
Write-Host ""

# 3. Git 推送
Write-Host "🚀 Git 推送..." -ForegroundColor Yellow
& $GIT push 2>&1 | Out-Null

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ 推送失败，网络问题或远程不可达" -ForegroundColor Red
    exit 1
}

Write-Host "✅ 推送成功" -ForegroundColor Green
Write-Host ""

# 4. 记录备份日志
$logEntry = @{
    date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    action = "daily backup"
    status = "success"
    basic_errors = $basicErrors
    link_errors = $linkErrors
    scanned_files = $checkResult.scope_counts.strict_files
} | ConvertTo-Json -Compress

Add-Content -Path $LOG_FILE -Value $logEntry -Encoding UTF8

Write-Host "📝 备份日志已记录" -ForegroundColor Green
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  备份完成" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan