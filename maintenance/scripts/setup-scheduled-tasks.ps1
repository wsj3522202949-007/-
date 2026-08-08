#!/usr/bin/env pwsh
# 知识库自动灾备 · 定时任务注册脚本
# ============================================
# 使用 Register-ScheduledTask（ScheduledTasks 模块）注册 Windows 定时任务
#
# 注册任务：
#   1. KnowledgeBase_DailyBackup      → 每日 23:30（需要网络，Interactive）
#   2. KnowledgeBase_WeeklyHealth     → 每周日 21:00（纯本地，S4U）
#   3. KnowledgeBase_MonthlyCleanup   → 每日 20:00（脚本内守卫限制每月 1 日，纯本地，S4U）
#   4. KnowledgeBase_QuarterlyRecovery → 每日 22:00（脚本内守卫追踪季度演练，需要网络，Interactive）
#
# LogonType 说明：
#   - S4U：无需用户登录即可运行，但无法访问网络资源。
#     仅用于纯本地任务（健康报告、清理检查）。
#   - Interactive：需要用户已登录（有活跃会话）才能运行。
#     用于需要网络的任务（git push/clone）。
#     配合 StartWhenAvailable：如果错过触发时间，任务会在下次登录时补跑。
#   - Password：需要存储密码，可随时运行且能访问网络。
#     如需进一步增强，可手动将任务改为 Password 类型并在任务属性中输入密码。
#
# 无需管理员权限（Register-ScheduledTask 对当前用户注册任务不需要提权）

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

# 检查 ScheduledTasks 模块
if (-not (Get-Module -ListAvailable -Name ScheduledTasks)) {
    Write-Host "❌ ScheduledTasks 模块不可用，无法注册定时任务" -ForegroundColor Red
    exit 1
}

# -------------------------------------------------------------------
# 任务定义
# -------------------------------------------------------------------
$SCRIPT_DIR = $PSScriptRoot
$NETWORK_TASKS = @(
    @{
        Name        = "KnowledgeBase_DailyBackup"
        Description = "知识库每日自动备份：校验 → 提交 → 推送 → 验证远端一致性"
        ScriptPath  = "$SCRIPT_DIR\daily-backup.ps1"
        Trigger     = { New-ScheduledTaskTrigger -Daily -At 23:30 }
        NeedsNetwork = $true
    },
    @{
        Name        = "KnowledgeBase_QuarterlyRecovery"
        Description = "知识库季度恢复演练：克隆 → 门禁 → 报告（脚本内状态文件追踪季度完成情况）"
        ScriptPath  = "$SCRIPT_DIR\quarterly-recovery.ps1"
        Trigger     = { New-ScheduledTaskTrigger -Daily -At 22:00 }
        NeedsNetwork = $true
    }
)

$LOCAL_TASKS = @(
    @{
        Name        = "KnowledgeBase_WeeklyHealth"
        Description = "知识库每周健康报告生成"
        ScriptPath  = "$SCRIPT_DIR\weekly-health.ps1"
        Trigger     = { New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 21:00 }
        NeedsNetwork = $false
    },
    @{
        Name        = "KnowledgeBase_MonthlyCleanup"
        Description = "知识库每月清理检查（脚本内守卫限制仅当月 1 日运行）"
        ScriptPath  = "$SCRIPT_DIR\monthly-cleanup.ps1"
        Trigger     = { New-ScheduledTaskTrigger -Daily -At 20:00 }
        NeedsNetwork = $false
    }
)

$ALL_TASKS = $NETWORK_TASKS + $LOCAL_TASKS

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  知识库自动灾备 · 定时任务注册" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# 检查脚本文件是否存在
$allExist = $true
foreach ($task in $ALL_TASKS) {
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
$successCount = 0
$failCount = 0

foreach ($task in $ALL_TASKS) {
    Write-Host "📌 注册任务: $($task.Name)" -ForegroundColor Yellow
    Write-Host "   描述: $($task.Description)" -ForegroundColor Gray
    Write-Host "   脚本: $($task.ScriptPath)" -ForegroundColor Gray

    $trigger   = & $task.Trigger
    $action    = New-ScheduledTaskAction -Execute $pwshPath -Argument "-ExecutionPolicy Bypass -File `"$($task.ScriptPath)`""
    $settings  = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Hours 2)

    if ($task.NeedsNetwork) {
        # 需要网络的任务 → Interactive（仅用户登录时运行）
        $principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive
        Write-Host "   LogonType: Interactive（需要网络）" -ForegroundColor Gray
    } else {
        # 纯本地任务也使用 Interactive，因为 S4U 在非管理员账户下可能因权限不足注册失败
        # Interactive 的限制：仅用户登录时运行；配合 StartWhenAvailable 可在下次登录时补跑
        $principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive
        Write-Host "   LogonType: Interactive（纯本地，S4U 权限不足回退）" -ForegroundColor Gray
    }

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
        $successCount++
    } catch {
        Write-Host "   ❌ 注册失败: $($_.Exception.Message)" -ForegroundColor Red
        $failCount++
    }
    Write-Host ""
}

# -------------------------------------------------------------------
# 验证注册
# -------------------------------------------------------------------
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  注册结果: $successCount 成功 / $failCount 失败" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

$tasks = Get-ScheduledTask -TaskName "KnowledgeBase_*" -ErrorAction SilentlyContinue
if ($tasks) {
    Write-Host "已注册的 KnowledgeBase 任务:" -ForegroundColor Green
    $tasks | Format-Table TaskName, State, @{Name="NextRunTime";Expression={$_.NextRunTime}}, Description -AutoSize
} else {
    Write-Host "⚠️  未找到 KnowledgeBase 任务" -ForegroundColor Yellow
}

Write-Host ""
if ($failCount -gt 0) {
    Write-Host "============================================" -ForegroundColor Red
    Write-Host "  ⚠️  部分任务注册失败，请检查上方错误详情" -ForegroundColor Red
    Write-Host "============================================" -ForegroundColor Red
} elseif ($successCount -gt 0) {
    Write-Host "============================================" -ForegroundColor Cyan
    Write-Host "  ✅ 全部 $successCount 个任务注册完成" -ForegroundColor Cyan
    Write-Host "============================================" -ForegroundColor Cyan
} else {
    Write-Host "============================================" -ForegroundColor Yellow
    Write-Host "  ⚠️  未注册任何任务（所有任务注册均失败）" -ForegroundColor Yellow
    Write-Host "============================================" -ForegroundColor Yellow
}
Write-Host ""

Write-Host "手动触发测试命令：" -ForegroundColor Gray
foreach ($task in $ALL_TASKS) {
    Write-Host "  Start-ScheduledTask -TaskName $($task.Name)" -ForegroundColor Gray
}
Write-Host ""
Write-Host "查看任务状态：" -ForegroundColor Gray
Write-Host "  Get-ScheduledTask -TaskName KnowledgeBase_* | Format-Table TaskName,State,LastRunTime,LastTaskResult" -ForegroundColor Gray
Write-Host ""
Write-Host "删除所有 KnowledgeBase 任务：" -ForegroundColor Gray
Write-Host "  Get-ScheduledTask -TaskName KnowledgeBase_* | Unregister-ScheduledTask -Confirm:`$false" -ForegroundColor Gray

# 返回退出码：全部成功 → 0，部分失败 → 1
if ($failCount -gt 0) { exit 1 } else { exit 0 }
