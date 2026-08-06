#!/usr/bin/env pwsh
# 知识库自动灾备 · 定时任务注册脚本
#
# 注册以下 Windows 定时任务：
#   1. KnowledgeBase_DailyBackup  → 每日 23:30
#   2. KnowledgeBase_WeeklyHealth → 每周日 21:00
#   3. KnowledgeBase_QuarterlyRecovery → 每季度 22:00（3/6/9/12月第一个周日）
#
# 需要管理员权限（以管理员身份运行 PowerShell）

$ErrorActionPreference = "Stop"
$SCHTASKS = "C:\Windows\System32\schtasks.exe"
$PS = "powershell.exe"
$SCRIPT_DIR = "e:\个人知识库\maintenance\scripts"
$TASKS = @(
    @{
        Name = "KnowledgeBase_DailyBackup"
        Desc = "知识库每日自动备份：校验→提交→推送"
        Script = "$SCRIPT_DIR\daily-backup.ps1"
        Schedule = "/sc daily /st 23:30"
    },
    @{
        Name = "KnowledgeBase_WeeklyHealth"
        Desc = "知识库每周健康报告生成"
        Script = "$SCRIPT_DIR\weekly-health.ps1"
        Schedule = "/sc weekly /d SUN /st 21:00"
    },
    @{
        Name = "KnowledgeBase_QuarterlyRecovery"
        Desc = "知识库季度恢复演练：克隆→门禁→报告"
        Script = "$SCRIPT_DIR\quarterly-recovery.ps1"
        # 每月 1 日 22:00（季度=每3个月运行一次，但Windows不支持季度表达式，
        # 实际上每月1日运行也无害，因为门禁很快；如果用"每月1日"太频繁，
        # 改为每季度手动触发。但为简化，每月1日运行，脚本内有前置判断。
        # 更精确：用 /sc monthly /d 1,但是每季度，简化方案直接每月1日。
        # 实际上用 /sc monthly /d 1 即可，每季度手动调整。
        # 改为每月1日运行，季度标志在脚本内判断。
        Schedule = "/sc monthly /d 1 /st 22:00"
    }
)

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  知识库自动灾备 · 定时任务注册" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# 检查管理员权限
$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "⚠️  当前不是以管理员身份运行。" -ForegroundColor Yellow
    Write-Host "   请以管理员身份重新运行此脚本。" -ForegroundColor Yellow
    Write-Host "   右键 PowerShell → 以管理员身份运行 → 再执行此脚本" -ForegroundColor Yellow
    Write-Host ""
    # 不退出，允许用户继续（任务可能注册成功，但建议管理员）
}

# 检查脚本文件是否存在
$allExist = $true
foreach ($task in $TASKS) {
    if (-not (Test-Path $task.Script)) {
        Write-Host "❌ 脚本不存在: $($task.Script)" -ForegroundColor Red
        $allExist = $false
    }
}
if (-not $allExist) {
    Write-Host "请先创建缺失的脚本文件" -ForegroundColor Red
    exit 1
}

Write-Host ""

# 注册每个任务
foreach ($task in $TASKS) {
    Write-Host "📌 注册任务: $($task.Name)" -ForegroundColor Yellow
    Write-Host "   描述: $($task.Desc)" -ForegroundColor Gray
    Write-Host "   脚本: $($task.Script)" -ForegroundColor Gray
    Write-Host "   计划: $($task.Schedule)" -ForegroundColor Gray

    $cmd = "$PS -ExecutionPolicy Bypass -File `"$($task.Script)`""
    $args = @(
        "/create"
        "/tn", $task.Name
        "/tr", $cmd
        "/f"
    )
    $args += $task.Schedule -split " "

    $result = & $SCHTASKS $args 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "   ✅ 注册成功" -ForegroundColor Green
    } else {
        Write-Host "   ❌ 注册失败: $result" -ForegroundColor Red
    }
    Write-Host ""
}

# 验证注册
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  验证注册结果" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

$verify = & $SCHTASKS /query /fo LIST 2>&1 | Select-String "KnowledgeBase"
if ($verify) {
    Write-Host "已注册的 KnowledgeBase 任务:" -ForegroundColor Green
    $verify | ForEach-Object { Write-Host "   $($_)" -ForegroundColor Green }
} else {
    Write-Host "⚠️  未找到 KnowledgeBase 任务（可能因权限不足）" -ForegroundColor Yellow
    Write-Host "   请以管理员身份重新运行此脚本" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  注册完成" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "手动运行测试命令：" -ForegroundColor Gray
Write-Host "  C:\Windows\System32\schtasks.exe /run /tn KnowledgeBase_DailyBackup" -ForegroundColor Gray
Write-Host "  C:\Windows\System32\schtasks.exe /run /tn KnowledgeBase_WeeklyHealth" -ForegroundColor Gray
Write-Host "  C:\Windows\System32\schtasks.exe /run /tn KnowledgeBase_QuarterlyRecovery" -ForegroundColor Gray