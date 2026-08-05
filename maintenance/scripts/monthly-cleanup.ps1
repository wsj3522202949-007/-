#!/usr/bin/env pwsh
# 每月清理检查脚本
# 时间：每月第一个周日 20:00

$ErrorActionPreference = "Stop"

Set-Location "e:\个人知识库"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  每月清理检查" -ForegroundColor Cyan
Write-Host "  时间: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

python tools/scripts/maintenance/每月清理检查.py --json | Out-File -FilePath "reports\monthly-cleanup.json" -Encoding UTF8

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  清理检查完成" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
