#!/usr/bin/env pwsh
# 每周健康报告生成脚本
# 时间：每周日 21:00

$ErrorActionPreference = "Stop"
$ROOT = "e:\个人知识库"

Set-Location $ROOT

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  每周健康报告" -ForegroundColor Cyan
Write-Host "  时间: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 1. 运行健康报告生成器
Write-Host "📊 生成健康报告..." -ForegroundColor Yellow
python tools/scripts/maintenance/每周健康报告.py

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ 健康报告生成失败" -ForegroundColor Red
    exit 1
}

Write-Host "✅ 健康报告已生成" -ForegroundColor Green
Write-Host ""

# 2. 记录日志
$logEntry = @{
    date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    action = "weekly health report"
    status = "success"
} | ConvertTo-Json -Compress

Add-Content -Path "maintenance\backup-log.jsonl" -Value $logEntry -Encoding UTF8

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  健康报告完成" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan