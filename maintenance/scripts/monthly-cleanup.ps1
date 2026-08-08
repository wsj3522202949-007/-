#!/usr/bin/env pwsh
# 每月清理检查脚本
# 时间：每月 1 日 20:00（Daily 触发器 + 状态守卫）
#
# 状态守卫替代日期判断：追踪本月是否已有成功执行记录。
# StartWhenAvailable 错过 1 日后延迟到 2 日（或更晚）也能正常执行，
# 不会再被硬性日期判断跳过。

$ErrorActionPreference = "Stop"

# 加载运行时解析器
. "$PSScriptRoot\_runtime.ps1"
if (-not $Script:Python) {
    Write-Host "❌ 运行时环境不完整，请检查 _runtime.ps1 的路径配置" -ForegroundColor Red
    exit 1
}

# —— 状态守卫：本月是否已成功执行 ——
$currentMonth = (Get-Date).Month
$currentYear = (Get-Date).Year
$monthKey = "$currentYear-$($currentMonth.ToString('00'))"

$STATE_DIR = "$Script:Root\maintenance\state"
$STATE_FILE = "$STATE_DIR\monthly-cleanup-state.json"
if (-not (Test-Path $STATE_DIR)) { New-Item -ItemType Directory -Path $STATE_DIR -Force | Out-Null }

$cleanupState = $null
if (Test-Path $STATE_FILE) {
    try { $cleanupState = Get-Content $STATE_FILE -Raw | ConvertFrom-Json } catch { $cleanupState = $null }
}
if (-not $cleanupState) {
    $cleanupState = [PSCustomObject]@{ last_successful_month = $null; last_attempt = $null; history = @() }
}

# 本月已成功 → 跳过
if ($cleanupState.last_successful_month -eq $monthKey) {
    Write-Host "⏭️ 本月 ($monthKey) 已有成功的清理检查（$($cleanupState.last_attempt)），跳过本次" -ForegroundColor Yellow
    exit 0
}

# 更新本次尝试时间戳（失败时也记录，避免无限重试但允许后续重试）
$cleanupState.last_attempt = (Get-Date -Format 'yyyy-MM-dd HH:mm:ss')

Set-Location $Script:Root

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  每月清理检查" -ForegroundColor Cyan
Write-Host "  时间: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Cyan
Write-Host "  月份: $monthKey" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 运行清理脚本，保存结果
$reportPath = "$Script:Root\maintenance\state\monthly-cleanup-report.json"
try {
    & $Script:Python tools/scripts/maintenance/每月清理检查.py --json | Out-File -FilePath $reportPath -Encoding UTF8
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "  清理检查完成" -ForegroundColor Cyan
    Write-Host "========================================" -ForegroundColor Cyan

    # 标记本月成功
    $cleanupState.last_successful_month = $monthKey
    $cleanupState.history += @{
        month = $monthKey
        timestamp = $cleanupState.last_attempt
        status = "success"
    }
} catch {
    Write-Host "❌ 清理检查失败：$_" -ForegroundColor Red
    $cleanupState.history += @{
        month = $monthKey
        timestamp = $cleanupState.last_attempt
        status = "failed"
    }
} finally {
    # 保存状态文件
    $cleanupState | ConvertTo-Json -Depth 5 | Out-File -FilePath $STATE_FILE -Encoding UTF8
}
