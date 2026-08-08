#!/usr/bin/env pwsh
# 每日自动备份脚本
# 时间：每日 23:30
# 依赖：run_all.py（统一门禁）、Git
#
# 阶段化执行：gate → commit → push → verify
# 只有全部阶段通过且远端 HEAD 验证一致后，日志才记 success。

$ErrorActionPreference = "Stop"

# 加载运行时解析器
. "$PSScriptRoot\_runtime.ps1"
if (-not $Script:Git -or -not $Script:Python) {
    Write-Host "❌ 运行时环境不完整，请检查 _runtime.ps1 的路径配置" -ForegroundColor Red
    exit 1
}

$LOG_FILE = "$Script:Root\maintenance\state\backup-log.jsonl"

Set-Location $Script:Root

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  每日自动备份" -ForegroundColor Cyan
Write-Host "  时间: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 阶段结果追踪
$stageGate = $null
$stageCommit = $null
$stagePush = $null
$stageVerify = $null
$basicErrors = 0
$linkErrors = 0
$scannedFiles = 0

# ============================================
# 阶段 1: gate — 统一门禁校验
# ============================================
Write-Host "🔍 [阶段 1/4] 统一门禁校验..." -ForegroundColor Yellow
try {
    # 权威判据 = run_all.py 退出码（0=通过，非零=失败），与 ci.yml chapter-gate 一致。
    # 注意：不要用 stdout JSON 解析做成败判据——PowerShell 管道把 python 的
    # UTF-8 中文输出按系统 ANSI(GBK) 解码会污染 JSON（曾致 gate 永远 error、
    # 备份永远假失败）。JSON 仅作统计参考，解析失败不影响成败判定。
    & $Script:Python tools/scripts/validation/run_all.py --json 2>$null | Out-Null
    $gateExit = $LASTEXITCODE
    if ($gateExit -eq 0) {
        Write-Host "   ✅ 门禁通过（exit 0）" -ForegroundColor Green
        $stageGate = "passed"
    } else {
        Write-Host "   ❌ 门禁失败（exit $gateExit）" -ForegroundColor Red
        $stageGate = "failed"
    }
    # 统计字段 best-effort：能解析就带上，解析失败置空不影响成败
    try {
        $jsonOutput = & $Script:Python tools/scripts/validation/run_all.py --json 2>$null | Out-String
        $checkResult = $jsonOutput | ConvertFrom-Json
        $basicErrors = $checkResult.summary.basic.errors
        $linkErrors = $checkResult.summary.'core_broken_links'.errors
        $scannedFiles = $checkResult.scope_counts.strict_files
    } catch {
        $basicErrors = 0
        $linkErrors = 0
        $scannedFiles = 0
    }
} catch {
    Write-Host "   ❌ 门禁执行异常: $_" -ForegroundColor Red
    $stageGate = "error"
}
Write-Host ""

if ($stageGate -ne "passed") {
    Write-Host "⛔ 门禁未通过，终止备份流程" -ForegroundColor Red
    # 仍然记录日志，但标记为 gate_failed
    $logEntry = @{
        date     = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        action   = "daily backup"
        status   = "gate_failed"
        stages   = @{ gate = $stageGate; commit = $null; push = $null; verify = $null }
        basic_errors = $basicErrors
        link_errors  = $linkErrors
        scanned_files = $scannedFiles
    } | ConvertTo-Json -Compress
    Add-Content -Path $LOG_FILE -Value $logEntry -Encoding UTF8
    exit 1
}

# ============================================
# 阶段 2: commit — Git 提交
# ============================================
Write-Host "📦 [阶段 2/4] Git 提交..." -ForegroundColor Yellow
# 只 add 未被忽略的文件
& $Script:Git add -A
if ($LASTEXITCODE -ne 0) {
    Write-Host "   ❌ git add 失败 (exit=$LASTEXITCODE)，无法确保完整备份" -ForegroundColor Red
    $logEntry = @{
        date     = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        action   = "daily backup"
        status   = "add_failed"
        stages   = @{ gate = $stageGate; commit = $null; push = $null; verify = $null }
        basic_errors = $basicErrors
        link_errors  = $linkErrors
        scanned_files = $scannedFiles
    } | ConvertTo-Json -Compress
    Add-Content -Path $LOG_FILE -Value $logEntry -Encoding UTF8
    exit 1
}

$commitMessage = "auto: daily backup $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
$commitStdErr = & $Script:Git commit -m $commitMessage 2>&1
$commitExitCode = $LASTEXITCODE

if ($commitExitCode -eq 0) {
    Write-Host "   ✅ 提交成功" -ForegroundColor Green
    $stageCommit = "committed"
} elseif ($commitStdErr -match 'nothing to commit|nothing added to commit') {
    Write-Host "   ⚠️ 无更改需要提交" -ForegroundColor Yellow
    $stageCommit = "no_changes"
} else {
    Write-Host "   ❌ 提交失败 (exit=$commitExitCode): $commitStdErr" -ForegroundColor Red
    $stageCommit = "failed"
}

Write-Host ""

if ($stageCommit -eq "failed") {
    $logEntry = @{
        date     = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        action   = "daily backup"
        status   = "commit_failed"
        stages   = @{ gate = $stageGate; commit = $stageCommit; push = $null; verify = $null }
        commit_error = ($commitStdErr -join "`n")
        basic_errors = $basicErrors
        link_errors  = $linkErrors
        scanned_files = $scannedFiles
    } | ConvertTo-Json -Compress
    Add-Content -Path $LOG_FILE -Value $logEntry -Encoding UTF8
    exit 1
}

if ($stageCommit -eq "no_changes") {
    # 即使无新更改，也要检查是否有尚未推送到远端的旧提交
    $aheadCount = & $Script:Git rev-list --count "origin/main..HEAD" 2>$null
    if ($aheadCount -and [int]$aheadCount -gt 0) {
        Write-Host "   📌 检测到 $aheadCount 个未推送的本地提交，尝试推送到远端..." -ForegroundColor Yellow
        # 更新 localHead（用于后续 verify 阶段）
        $localHead = & $Script:Git rev-parse HEAD 2>$null
        $pushOutput = & $Script:Git push 2>&1
        $pushExitCode = $LASTEXITCODE
        if ($pushExitCode -eq 0) {
            Write-Host "   ✅ 远端推送成功（积压提交已同步）" -ForegroundColor Green
            $stagePush = "pushed"
            # 继续 verify 阶段
        } else {
            Write-Host "   ❌ 推送失败 (exit=$pushExitCode): $pushOutput" -ForegroundColor Red
            $stagePush = "failed"
        }
    } else {
        # 无更改且无积压提交 = 合法 no_changes
        $logEntry = @{
            date     = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
            action   = "daily backup"
            status   = "no_changes"
            stages   = @{ gate = $stageGate; commit = $stageCommit; push = $null; verify = $null }
            basic_errors = $basicErrors
            link_errors  = $linkErrors
            scanned_files = $scannedFiles
        } | ConvertTo-Json -Compress
        Add-Content -Path $LOG_FILE -Value $logEntry -Encoding UTF8
        Write-Host "✅ 备份流程结束（无需提交）" -ForegroundColor Green
        exit 0
    }
}

# ============================================
# 阶段 3: push — Git 推送
# ============================================
Write-Host "🚀 [阶段 3/4] Git 推送..." -ForegroundColor Yellow
# 先获取本地 HEAD 的 commit hash，用于后续 verify
$localHead = & $Script:Git rev-parse HEAD 2>$null

$pushOutput = & $Script:Git push 2>&1
$pushExitCode = $LASTEXITCODE

if ($pushExitCode -eq 0) {
    Write-Host "   ✅ 推送成功" -ForegroundColor Green
    $stagePush = "pushed"
} else {
    Write-Host "   ❌ 推送失败 (exit=$pushExitCode): $pushOutput" -ForegroundColor Red
    $stagePush = "failed"
}
Write-Host ""

if ($stagePush -ne "pushed") {
    $logEntry = @{
        date     = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        action   = "daily backup"
        status   = "push_failed"
        stages   = @{ gate = $stageGate; commit = $stageCommit; push = $stagePush; verify = $null }
        push_error = ($pushOutput -join "`n")
        basic_errors = $basicErrors
        link_errors  = $linkErrors
        scanned_files = $scannedFiles
    } | ConvertTo-Json -Compress
    Add-Content -Path $LOG_FILE -Value $logEntry -Encoding UTF8
    exit 1
}

# ============================================
# 阶段 4: verify — 远端 HEAD 一致性验证
# ============================================
Write-Host "🔬 [阶段 4/4] 远端一致性验证..." -ForegroundColor Yellow
$remoteHead = & $Script:Git ls-remote origin HEAD 2>$null | ForEach-Object { ($_ -split '\s+')[0] }

if ($remoteHead -and $localHead -and ($remoteHead -eq $localHead)) {
    Write-Host "   ✅ 远端 HEAD 与本地一致 ($($localHead.Substring(0,8)))" -ForegroundColor Green
    $stageVerify = "verified"
} elseif ($remoteHead) {
    Write-Host "   ❌ 远端 HEAD ($($remoteHead.Substring(0,8))) 与本地 ($($localHead.Substring(0,8))) 不一致" -ForegroundColor Red
    $stageVerify = "mismatch"
} else {
    Write-Host "   ❌ 无法获取远端 HEAD（网络问题或远程不可达）" -ForegroundColor Red
    $stageVerify = "unreachable"
}
Write-Host ""

# ============================================
# 最终日志：只有全部 passed/committed/pushed/verified 才记 success
# ============================================
$finalStatus = if ($stageGate -eq "passed" -and $stageCommit -eq "committed" -and $stagePush -eq "pushed" -and $stageVerify -eq "verified") {
    "success"
} else {
    "incomplete"
}

$logEntry = @{
    date     = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    action   = "daily backup"
    status   = $finalStatus
    stages   = @{
        gate   = $stageGate
        commit = $stageCommit
        push   = $stagePush
        verify = $stageVerify
    }
    local_head  = $localHead
    remote_head = $remoteHead
    basic_errors = $basicErrors
    link_errors  = $linkErrors
    scanned_files = $scannedFiles
} | ConvertTo-Json -Compress

Add-Content -Path $LOG_FILE -Value $logEntry -Encoding UTF8

Write-Host "========================================" -ForegroundColor Cyan
if ($finalStatus -eq "success") {
    Write-Host "  备份完成 ✅（gate/commit/push/verify 全部通过）" -ForegroundColor Cyan
    exit 0
} else {
    Write-Host "  备份未完全成功（状态: $finalStatus，详情见日志）" -ForegroundColor Yellow
    exit 1
}
