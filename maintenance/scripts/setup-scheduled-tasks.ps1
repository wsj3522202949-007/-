#!/usr/bin/env pwsh
# 知识库自动灾备 · 定时任务注册脚本
# ============================================
# 使用 Register-ScheduledTask（ScheduledTasks 模块）注册 Windows 定时任务
#
# 注册任务：
#   1. KnowledgeBase_DailyBackup   → 每日 23:30
#   2. KnowledgeBase_WeeklyHealth  → 每周日 21:00
#   3. KnowledgeBase_QuarterlyRecovery → 季度（3/6/9/12月 1日 22:00）
#
# 需要管理员权限（以管理员身份运行 PowerShell）

$ErrorActionPreference = "Stop"

# 加载运行时解析器（获取 $Script:Root）
. "$PSScriptRoot\_runtime.ps1"

# -------------------------------------------------------------------
# 自动发现 PowerShell 7 路径
# -------------------------------------------------------------------
$pwshPath = (Get-Command pwsh.exe -ErrorAction SilentlyContinue).Source
if (-not $pwshPath) {
    $pwshPath = "C:\Program Files\PowerShell\7\pwsh.exe"
}
if (-not (Test-Path $pwshPath)) {
    # 回退到 Windows PowerShell
    $pwshPath = "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
    Write-Warning "pwsh.exe 未找到，回退到 Windows PowerShell: $pwshPath"
}
Write-Host "[setup] PowerShell: $pwshPath" -ForegroundColor DarkGray

# 检查管理员权限
$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "⚠️  当前不是以管理员身份运行。" -ForegroundColor Yellow
    Write-Host "   请以管理员身份重新运行此脚本。" -ForegroundColor Yellow
    Write-Host "   右键 PowerShell → 以管理员身份运行 → 再执行此脚本" -ForegroundColor Yellow
    Write-Host ""
    exit 1
}

# 检查 ScheduledTasks 模块
if (-not (Get-Module -ListAvailable -Name ScheduledTasks)) {
    Write-Host "❌ ScheduledTasks 模块不可用，无法注册定时任务" -ForegroundColor Red
    exit 1
}

# -------------------------------------------------------------------
# 任务定义
# -------------------------------------------------------------------
$SCRIPT_DIR = $PSScriptRoot
$TASKS = @(
    @{
        Name = "KnowledgeBase_DailyBackup"
        Description = "知识库每日自动备份：校验→提交→推送"
        ScriptPath = "$SCRIPT_DIR\daily-backup.ps1"
        Trigger = { New-ScheduledTaskTrigger -Daily -At 23:30 }
    },
    @{
        Name = "KnowledgeBase_WeeklyHealth"
        Description = "知识库每周健康报告生成"
        ScriptPath = "$SCRIPT_DIR\weekly-health.ps1"
        Trigger = { New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 21:00 }
    },
    @{
        Name = "KnowledgeBase_QuarterlyRecovery"
        Description = "知识库季度恢复演练：克隆→门禁→报告（脚本含季度月份保护）"
        ScriptPath = "$SCRIPT_DIR\quarterly-recovery.ps1"
        # 注册为每月 1 日 22:00，脚本内 guard 仅在 3/6/9/12 月真正执行
        Trigger = { New-ScheduledTaskTrigger -Monthly -DaysOfMonth 1 -At 22:00 }
    }
)

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  知识库自动灾备 · 定时任务注册" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# 检查脚本文件是否存在
$allExist = $true
foreach ($task in $TASKS) {
    if (-not (Test-Path $task.ScriptPath)) {
        Write-Host "❌ 脚本不存在: $($task.ScriptPath)" -ForegroundColor Red
        $allExist = $false
    }
}
if (-not $allExist) {
    Write-Host "请先创建缺失的脚本文件" -ForegroundColor Red
    exit 1
}

Write-Host ""

# -------------------------------------------------------------------
# 注册任务
# -------------------------------------------------------------------
foreach ($task in $TASKS) {
    Write-Host "📌 注册任务: $($task.Name)" -ForegroundColor Yellow
    Write-Host "   描述: $($task.Description)" -ForegroundColor Gray
    Write-Host "   脚本: $($task.ScriptPath)" -ForegroundColor Gray

    $trigger = & $task.Trigger
    $action = New-ScheduledTaskAction -Execute $pwshPath -Argument "-ExecutionPolicy Bypass -File `"$($task.ScriptPath)`""
    $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Hours 2)
    $principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -RunLevel Highest -LogonType S4U

    try {
        # 先删除旧任务（如果存在）
        Unregister-ScheduledTask -TaskName $task.Name -Confirm:$false -ErrorAction SilentlyContinue | Out-Null

        Register-ScheduledTask -TaskName $task.Name `
            -Action $action `
            -Trigger $trigger `
            -Settings $settings `
            -Principal $principal `
            -Description $task.Description `
            -Force | Out-Null

        Write-Host "   ✅ 注册成功" -ForegroundColor Green
    } catch {
        Write-Host "   ❌ 注册失败: $($_.Exception.Message)" -ForegroundColor Red
    }
    Write-Host ""
}

# -------------------------------------------------------------------
# 验证注册
# -------------------------------------------------------------------
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  验证注册结果" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

$tasks = Get-ScheduledTask -TaskName "KnowledgeBase_*" -ErrorAction SilentlyContinue
if ($tasks) {
    Write-Host "已注册的 KnowledgeBase 任务:" -ForegroundColor Green
    $tasks | Format-Table TaskName, State, @{Name="NextRunTime";Expression={$_.NextRunTime}}, Description -AutoSize
} else {
    Write-Host "⚠️  未找到 KnowledgeBase 任务（可能因权限不足）" -ForegroundColor Yellow
    Write-Host "   请以管理员身份重新运行此脚本" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  注册完成" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "手动触发测试命令：" -ForegroundColor Gray
Write-Host "  Start-ScheduledTask -TaskName KnowledgeBase_DailyBackup" -ForegroundColor Gray
Write-Host "  Start-ScheduledTask -TaskName KnowledgeBase_WeeklyHealth" -ForegroundColor Gray
Write-Host "  Start-ScheduledTask -TaskName KnowledgeBase_QuarterlyRecovery" -ForegroundColor Gray
Write-Host ""
Write-Host "查看任务状态：" -ForegroundColor Gray
Write-Host "  Get-ScheduledTask -TaskName KnowledgeBase_* | Format-Table TaskName,State,LastRunTime,LastTaskResult" -ForegroundColor Gray