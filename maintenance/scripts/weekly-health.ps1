#!/usr/bin/env pwsh
# 每周健康报告生成脚本
# 时间：每周日 21:00

$ErrorActionPreference = "Stop"

# 加载运行时解析器
. "$PSScriptRoot\_runtime.ps1"
if (-not $Script:Python) {
    Write-Host "❌ 运行时环境不完整，请检查 _runtime.ps1 的路径配置" -ForegroundColor Red
    exit 1
}

$LOG_FILE = "$Script:Root\maintenance\state\backup-log.jsonl"

Set-Location $Script:Root

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  每周健康报告" -ForegroundColor Cyan
Write-Host "  时间: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 1. 运行健康报告生成器
Write-Host "📊 生成健康报告..." -ForegroundColor Yellow
& $Script:Python tools/scripts/maintenance/每周健康报告.py

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

Add-Content -Path $LOG_FILE -Value $logEntry -Encoding UTF8

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  健康报告完成" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan