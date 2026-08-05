#!/usr/bin/env pwsh
# 每周健康报告脚本
# 时间：每周日 21:00

$ErrorActionPreference = "Stop"

Set-Location "e:\个人知识库"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  每周健康报告" -ForegroundColor Cyan
Write-Host "  时间: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

python tools/scripts/maintenance/每周健康报告.py

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  健康报告生成完成" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
