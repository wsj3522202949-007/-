# _runtime.ps1 - 运行时路径解析器
# ============================================
# 统一解析 $Script:Root / $Script:Git / $Script:Python
# 消除硬编码路径，避免 WindowsApps 占位程序干扰
#
# 用法：在每个脚本开头 dot-source：
#     . "$PSScriptRoot\_runtime.ps1"
# 之后直接使用 $Script:Root, $Script:Git, $Script:Python

$Script:Root = $null
$Script:Git = $null
$Script:Python = $null

# -------------------------------------------------------------------
# 1. 自动检测项目根目录
#    脚本位于 maintenance/scripts/，根目录为 ../..
# -------------------------------------------------------------------
$Script:Root = Resolve-Path "$PSScriptRoot\..\.." -ErrorAction Stop

# -------------------------------------------------------------------
# 2. 自动发现 Git
# -------------------------------------------------------------------
$gitCandidates = @()
# 2a. 从 PATH 查找
$pathGit = (Get-Command git.exe -ErrorAction SilentlyContinue).Source
if ($pathGit) { $gitCandidates += $pathGit }
# 2b. 已知常用路径
$gitCandidates += @(
    "C:\Program Files\Git\cmd\git.exe"
    "C:\Program Files (x86)\Git\cmd\git.exe"
    "$env:LOCALAPPDATA\Programs\Git\cmd\git.exe"
    "$env:ProgramFiles\Git\cmd\git.exe"
    "${env:ProgramFiles(x86)}\Git\cmd\git.exe"
    "$env:USERPROFILE\.workbuddy\vendor\PortableGit\cmd\git.exe"
    "C:\Users\wsj\.workbuddy\vendor\PortableGit\cmd\git.exe"
)
$Script:Git = $gitCandidates | Where-Object { $_ -and (Test-Path $_) } | Select-Object -First 1

if (-not $Script:Git) {
    Write-Warning "[_runtime] Git 未找到，请安装 Git 或手动设置 `$Script:Git"
}

# -------------------------------------------------------------------
# 3. 自动发现 Python（跳过 WindowsApps 占位程序）
# -------------------------------------------------------------------
$pythonCandidates = @()
# 3a. 从 PATH 查找
$pathPython = (Get-Command python.exe -ErrorAction SilentlyContinue).Source
if ($pathPython) { $pythonCandidates += $pathPython }
$pathPython3 = (Get-Command python3.exe -ErrorAction SilentlyContinue).Source
if ($pathPython3) { $pythonCandidates += $pathPython3 }
# 3b. 已知常用路径
$pythonCandidates += @(
    "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe"
    "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"
    "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe"
    "C:\Python313\python.exe"
    "C:\Python312\python.exe"
    "${env:ProgramFiles}\Python313\python.exe"
    "${env:ProgramFiles}\Python312\python.exe"
    # TRAE / 其他 IDE 内置 Python
    "$env:USERPROFILE\AppData\Roaming\TRAE SOLO CN\ModularData\ai-agent\vm\tools\python\python.exe"
    "$env:USERPROFILE\AppData\Roaming\TRAE SOLO CN\ModularData\ai-agent\vm\tools\bin\python3.exe"
)
# 3b'. WorkBuddy 管理 Python：单一来源 python-candidates.txt
#      （禁止在此硬编码版本路径；与 .githooks/pre-commit 共用同一文件）
$pythonCandFile = Join-Path $PSScriptRoot "python-candidates.txt"
if (Test-Path $pythonCandFile) {
    Get-Content $pythonCandFile | ForEach-Object {
        $l = $_.Trim()
        if ($l -and -not $l.StartsWith("#")) {
            $pythonCandidates += $l.Replace("~", $env:USERPROFILE)
        }
    }
}
$Script:Python = $pythonCandidates | Where-Object {
    $_ -and (Test-Path $_) -and $_ -notmatch 'WindowsApps'
} | Select-Object -First 1

if (-not $Script:Python) {
    Write-Warning "[_runtime] Python 未找到，请安装 Python 或手动设置 `$Script:Python"
}

# -------------------------------------------------------------------
# 4. 验证摘要
# -------------------------------------------------------------------
Write-Host "[_runtime] Root  : $Script:Root" -ForegroundColor DarkGray
Write-Host "[_runtime] Git   : $Script:Git" -ForegroundColor DarkGray
Write-Host "[_runtime] Python: $Script:Python" -ForegroundColor DarkGray