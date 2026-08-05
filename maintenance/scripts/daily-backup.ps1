#!/usr/bin/env pwsh
# 每日自动备份脚本
# 时间：每日 23:30

$ErrorActionPreference = "Stop"

# 进入知识库目录
Set-Location "e:\个人知识库"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  每日自动备份" -ForegroundColor Cyan
Write-Host "  时间: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 1. 运行提交前校验
Write-Host "🔍 运行提交前校验..." -ForegroundColor Yellow
python tools/scripts/maintenance/提交前校验.py --json | Out-File -FilePath "reports\pre-commit-check.json" -Encoding UTF8

$checkResult = Get-Content "reports\pre-commit-check.json" -Raw | ConvertFrom-Json

if ($checkResult.error_count -gt 0) {
    Write-Host "❌ 校验失败，发现 $($checkResult.error_count) 个错误" -ForegroundColor Red
    Write-Host "   跳过本次提交和推送" -ForegroundColor Red
    exit 1
}

Write-Host "✅ 校验通过" -ForegroundColor Green
Write-Host ""

# 2. Git 提交
Write-Host "📦 Git 提交..." -ForegroundColor Yellow
git add -A
$commitMessage = "auto: daily backup $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
git commit -m $commitMessage

if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  提交失败或无更改需要提交" -ForegroundColor Yellow
} else {
    Write-Host "✅ 提交成功" -ForegroundColor Green
}
Write-Host ""

# 3. Git 推送
Write-Host "🚀 Git 推送..." -ForegroundColor Yellow
git push

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ 推送失败" -ForegroundColor Red
    Write-Host "   可能原因：" -ForegroundColor Yellow
    Write-Host "   - 未配置远程仓库" -ForegroundColor Yellow
    Write-Host "   - 网络连接问题" -ForegroundColor Yellow
    Write-Host "   - 权限问题" -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ 推送成功" -ForegroundColor Green
Write-Host ""

# 4. 记录备份日志
$logEntry = @{
    date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    action = "daily backup"
    status = "success"
    errors = $checkResult.error_count
    warnings = $checkResult.warn_count
} | ConvertTo-Json

Add-Content -Path "maintenance\backup-log.jsonl" -Value $logEntry -Encoding UTF8

Write-Host "📝 备份日志已记录" -ForegroundColor Green
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  备份完成" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
