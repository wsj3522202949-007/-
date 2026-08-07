#!/usr/bin/env pwsh
# 每月清理检查脚本
# 时间：每月第一个周日 20:00

$ErrorActionPreference = "Stop"

# 加载运行时解析器
. "$PSScriptRoot\_runtime.ps1"
if (-not $Script:Python) {
    Write-Host "❌ 运行时环境不完整，请检查 _runtime.ps1 的路径配置" -ForegroundColor Red
    exit 1
}

Set-Location $Script:Root

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  每月清理检查" -ForegroundColor Cyan
Write-Host "  时间: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

& $Script:Python tools/scripts/maintenance/每月清理检查.py --json | Out-File -FilePath "$Script:Root\reports\monthly-cleanup.json" -Encoding UTF8

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  清理检查完成" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan