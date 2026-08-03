# ============================================================
# Repair-Encoding.ps1 —— 编码统一修复工具
# 把指定扩展名的文本文件统一转为 UTF-8 without BOM
# 默认: 干跑(仅报告, 不改动). 加 -Apply 才实际转换.
#
# 用法:
#   干跑报告:  .\Repair-Encoding.ps1 -Root 'e:\个人知识库'
#   实际转换:  .\Repair-Encoding.ps1 -Root 'e:\个人知识库' -Apply
#   指定类型:  .\Repair-Encoding.ps1 -Root 'e:\个人知识库' -Extensions .md,.txt -Apply
#   转换并备份:.\\Repair-Encoding.ps1 -Root 'e:\个人知识库' -Apply -Backup
#
# 编码: 本文件为 UTF-8 with BOM (PS5.1 解析中文所需)
# ============================================================
[CmdletBinding()]
param(
    [Parameter(Mandatory)][string]$Root,
    [string[]]$Extensions = @('.md','.txt','.tmpl','.py','.js','.mjs','.json','.sh','.toml','.yml','.css','.svg','.patch'),
    [switch]$Apply,
    [switch]$Backup
)

$utf8Strict = New-Object System.Text.UTF8Encoding($false, $true)   # 校验用: 遇非法字节抛异常

function Get-FileEncoding {
    param([byte[]]$Bytes)
    if ($Bytes.Length -ge 3 -and $Bytes[0] -eq 0xEF -and $Bytes[1] -eq 0xBB -and $Bytes[2] -eq 0xBF) { return 'UTF8-BOM' }
    if ($Bytes.Length -ge 2 -and $Bytes[0] -eq 0xFF -and $Bytes[1] -eq 0xFE) { return 'UTF16LE-BOM' }
    if ($Bytes.Length -ge 2 -and $Bytes[0] -eq 0xFE -and $Bytes[1] -eq 0xFF) { return 'UTF16BE-BOM' }
    try { $null = $utf8Strict.GetString($Bytes); return 'UTF8-NoBOM' } catch { return 'GBK-NoBOM' }
}

# 收集文件(去重)
$files = @()
foreach ($ext in $Extensions) {
    $files += Get-ChildItem -Path $Root -Recurse -File -Filter "*$ext" -ErrorAction SilentlyContinue
}
$files = $files | Sort-Object FullName -Unique

Write-Host "根目录 : $Root"
Write-Host "扩展名 : $($Extensions -join ', ')"
Write-Host "模式   : $(if($Apply){'应用(实际转换)'}else{'干跑(仅报告, 加 -Apply 才转换)'})"
if ($Apply -and $Backup) { Write-Host '备份   : 开启 (原文件复制到 .encoding-backup) ' }
Write-Host ('-' * 56)
Write-Host "待检测 : $($files.Count) 个文件"

$stats = @{}
$convertLog = @()
$i = 0; $conv = 0
$start = Get-Date

foreach ($f in $files) {
    $i++
    try { $bytes = [System.IO.File]::ReadAllBytes($f.FullName) } catch {
        if (-not $stats.ContainsKey('READ-ERROR')) { $stats['READ-ERROR'] = 0 }
        $stats['READ-ERROR']++; continue
    }
    $enc = Get-FileEncoding -Bytes $bytes
    if (-not $stats.ContainsKey($enc)) { $stats[$enc] = 0 }
    $stats[$enc]++
    if ($enc -eq 'UTF8-NoBOM') { continue }   # 已达标, 跳过

    # ---- 需要转换 ----
    if ($Apply) {
        try {
            switch ($enc) {
                'UTF8-BOM'    { $content = [System.Text.Encoding]::UTF8.GetString($bytes, 3, $bytes.Length - 3) }
                'UTF16LE-BOM' { $content = [System.Text.Encoding]::Unicode.GetString($bytes, 2, $bytes.Length - 2) }
                'UTF16BE-BOM' { $content = [System.Text.Encoding]::BigEndianUnicode.GetString($bytes, 2, $bytes.Length - 2) }
                'GBK-NoBOM'   { $gbk = [System.Text.Encoding]::GetEncoding(936); $content = $gbk.GetString($bytes) }
            }
            if ($Backup) {
                $bk = $f.FullName + '.encoding-backup'
                [System.IO.File]::WriteAllBytes($bk, $bytes)
            }
            $out = New-Object System.Text.UTF8Encoding($false)
            [System.IO.File]::WriteAllText($f.FullName, $content, $out)
            $conv++
            $convertLog += [pscustomobject]@{ Path = $f.FullName; From = $enc; To = 'UTF8-NoBOM' }
        } catch {
            $convertLog += [pscustomobject]@{ Path = $f.FullName; From = $enc; To = "FAILED: $($_.Exception.Message)" }
        }
    } else {
        $convertLog += [pscustomobject]@{ Path = $f.FullName; From = $enc; To = '(干跑, 未转换)' }
    }
    if ($i % 1000 -eq 0) { Write-Host "  进度 $i / $($files.Count) ..." }
}

$el = (Get-Date) - $start
Write-Host ('-' * 56)
Write-Host '编码分布:'
$stats.GetEnumerator() | Sort-Object Value -Descending | ForEach-Object {
    $pct = if ($files.Count -gt 0) { [math]::Round($_.Value/$files.Count*100,1) } else { 0 }
    Write-Host ("  {0,-14} {1,6} 个  ({2}%)" -f $_.Key, $_.Value, $pct)
}
Write-Host ('-' * 56)
if ($Apply) {
    Write-Host "已转换: $conv 个文件 -> UTF-8 without BOM"
} else {
    Write-Host "待转换: $($convertLog.Count) 个文件 (加 -Apply 执行)"
}
Write-Host ("耗时: {0:N1} 秒" -f $el.TotalSeconds)

if ($convertLog.Count -gt 0) {
    $csv = Join-Path $PSScriptRoot ('encoding-report-{0:yyyyMMdd-HHmmss}.csv' -f (Get-Date))
    $convertLog | Export-Csv -Path $csv -NoTypeInformation -Encoding UTF8
    Write-Host "明细已导出: $csv"
}
