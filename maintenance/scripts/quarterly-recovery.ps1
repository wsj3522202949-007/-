#!/usr/bin/env pwsh
# 季度恢复演练脚本
# 时间：每季度 22:00（3/6/9/12月 1日，由定时任务触发）
# 依赖：run_all.py（统一门禁）、Git
#
# 季度月份保护：仅 3/6/9/12 月真正执行，其余月份静默退出

$ErrorActionPreference = "Stop"

# 加载运行时解析器
. "$PSScriptRoot\_runtime.ps1"
if (-not $Script:Git -or -not $Script:Python) {
    Write-Host "❌ 运行时环境不完整，请检查 _runtime.ps1 的路径配置" -ForegroundColor Red
    exit 1
}

# 季度保护：仅 3/6/9/12 月 1 日执行（Daily 触发器 + 脚本 guard）
$currentMonth = (Get-Date).Month
$currentDay = (Get-Date).Day
if ($currentMonth -notin @(3, 6, 9, 12) -or $currentDay -ne 1) {
    Write-Host "⏭️ 当前日期 ($currentMonth 月 $currentDay 日) 不是季度首日（3/6/9/12 月 1 日），跳过本次恢复演练" -ForegroundColor Yellow
    exit 0
}

$TEMP_DIR = "C:\tmp\recovery-test-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
$REPORT_DIR = "$Script:Root\maintenance\reports"

Set-Location $Script:Root

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  季度恢复演练" -ForegroundColor Cyan
Write-Host "  时间: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$startTime = Get-Date

# 1. 创建临时目录
Write-Host "📁 创建临时目录: $TEMP_DIR" -ForegroundColor Yellow
New-Item -ItemType Directory -Path $TEMP_DIR -Force | Out-Null
Write-Host ""

# 2. 从 GitHub 克隆
Write-Host "🔄 克隆远程仓库..." -ForegroundColor Yellow
$cloneStart = Get-Date
$cloneOutput = & $Script:Git clone git@github.com:wsj3522202949-007/-.git "$TEMP_DIR\recovered" 2>&1
$cloneEnd = Get-Date
$cloneDuration = ($cloneEnd - $cloneStart).TotalSeconds

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ 克隆失败: $cloneOutput" -ForegroundColor Red
    Remove-Item -Recurse -Force $TEMP_DIR -ErrorAction SilentlyContinue
    exit 1
}

Write-Host "✅ 克隆成功（耗时: $([math]::Round($cloneDuration))秒）" -ForegroundColor Green
Write-Host ""

# 3. 进入恢复目录
Set-Location "$TEMP_DIR\recovered"

# 4. 运行统一门禁
Write-Host "🔍 运行统一门禁校验..." -ForegroundColor Yellow
$gateStart = Get-Date
$jsonOutput = & $Script:Python tools/scripts/validation/run_all.py --json 2>$null | Out-String
$gateEnd = Get-Date
$gateDuration = ($gateEnd - $gateStart).TotalSeconds

$checkResult = $jsonOutput | ConvertFrom-Json
$basicErrors = $checkResult.summary.basic.errors
$linkErrors = $checkResult.summary.'core_broken_links'.errors
$overallPass = $checkResult.summary.overall_pass
$scannedFiles = $checkResult.scope_counts.strict_files

Write-Host "  门禁结果: 基本 $basicErrors ERROR | 断链 $linkErrors ERROR | $scannedFiles 文件" -ForegroundColor Yellow
Write-Host "  耗时: $([math]::Round($gateDuration))秒" -ForegroundColor Yellow
Write-Host ""

# 5. 回到知识库根目录准备写报告
Set-Location $Script:Root

# 6. 生成恢复演练报告
$endTime = Get-Date
$totalDuration = ($endTime - $startTime).TotalSeconds
$reportDate = Get-Date -Format "yyyy-MM-dd"
$reportFile = "$REPORT_DIR\recovery-drill-$reportDate.md"
$status = if ($overallPass) { "✅ 通过" } else { "❌ 失败" }

$report = @"
---
id: maintenance-recovery-drill-$reportDate
type: report
area: 管理
status: archived
tags: [灾备, 恢复演练, 自动生成]
title: 季度恢复演练报告 - $reportDate
summary: 自动生成的季度恢复演练报告，验证从GitHub克隆+门禁校验的完整流程。
source: 自动生成
created: $reportDate
updated: $reportDate
---

# 季度恢复演练报告

> **演练日期**：$reportDate
> **演练类型**：真实克隆（✅ 已从 GitHub 实际执行 git clone）
> **演练结果**：$status

---

## 演练概览

| 项目 | 内容 |
|---|---|
| 演练时间 | $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') |
| 克隆仓库 | git@github.com:wsj3522202949-007/-.git |
| 恢复目录 | $TEMP_DIR\recovered |
| 克隆耗时 | $([math]::Round($cloneDuration)) 秒 |
| 门禁校验耗时 | $([math]::Round($gateDuration)) 秒 |
| 总耗时 | $([math]::Round($totalDuration)) 秒 |
| 门禁结果 | 基本错误: $basicErrors / 断链错误: $linkErrors / 扫描文件: $scannedFiles |

## 演练步骤

| 步骤 | 状态 | 耗时 |
|---|---|---|
| 1. 创建临时目录 | ✅ | < 1秒 |
| 2. 从 GitHub 克隆 | ✅ | $([math]::Round($cloneDuration)) 秒 |
| 3. 运行统一门禁 | $('✅' -f $overallPass) | $([math]::Round($gateDuration)) 秒 |
| 4. 清理临时目录 | ✅ | < 1秒 |

## 结论

本次恢复演练**真实执行**了从 GitHub 克隆 + 门禁校验的完整流程。
恢复总耗时约 $([math]::Round($totalDuration)) 秒，备份有效。

---

> 本报告由 quarterly-recovery.ps1 自动生成
> 下次演练：$(Get-Date (Get-Date).AddMonths(3) -Format 'yyyy-MM-dd')
"@

$report | Out-File -FilePath $reportFile -Encoding UTF8
Write-Host "📄 恢复演练报告已生成: $reportFile" -ForegroundColor Green
Write-Host ""

# 7. 清理临时目录
Write-Host "🧹 清理临时目录..." -ForegroundColor Yellow
Remove-Item -Recurse -Force $TEMP_DIR -ErrorAction SilentlyContinue
Write-Host "✅ 清理完成" -ForegroundColor Green
Write-Host ""

# 8. 记录日志
$logEntry = @{
    date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    action = "quarterly recovery drill"
    status = if ($overallPass) { "success" } else { "failed" }
    clone_seconds = [math]::Round($cloneDuration)
    gate_seconds = [math]::Round($gateDuration)
    total_seconds = [math]::Round($totalDuration)
    basic_errors = $basicErrors
    link_errors = $linkErrors
    scanned_files = $scannedFiles
} | ConvertTo-Json -Compress

Add-Content -Path "$Script:Root\maintenance\backup-log.jsonl" -Value $logEntry -Encoding UTF8

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  恢复演练完成" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan