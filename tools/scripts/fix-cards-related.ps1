# tools-cards-fix.ps1 - Add related links to tools/cards/ files
$vaultRoot = "E:\个人知识库"
$cardsDir = "$vaultRoot\tools\cards"

# Category -> related methods files mapping
$categoryMap = @{
    "一、去 AI 味 / Humanizer 库" = @("methods/最强去AI味铁律.md", "methods/改稿润色指令库.md")
    "二、网文 / 长篇 AI 写作系统 库" = @("methods/网文写作最强SOP.md", "methods/最强写作方法论_全球最强综合版.md")
    "画龙补充 / 扩容入库 — 补充源" = @("methods/QUICK_START.md")
    "四、长篇一致性 / RAG / 故事圣经 库" = @("methods/人物思维蒸馏法.md", "methods/模板库.md")
    "五、写作 IDE / 本地优先工作台 库" = @("methods/QUICK_START.md")
    "六、多 Agent 小说生产 / 叙事引擎 库" = @("methods/网文写作最强SOP.md")
    "九、大纲 / 规划 / 结构软件 库" = @("methods/大纲编写规则.md", "methods/模板库.md")
    "十、短剧 / 剧本 / 影视化生成 库" = @("methods/模板库.md")
    "十一、有声书 / 小说转语音 TTS 库" = @("methods/模板库.md")
    "十三、语法 / 风格检查 / 校对 库" = @("methods/改稿润色指令库.md", "methods/自检清单_升级版.md")
    "十四、文风迁移 / 风格微调模型 库" = @("methods/最强去AI味铁律.md")
    "十六、提示词库 / 写作 Agent 工作流 库" = @("methods/QUICK_START.md")
    "十七、AI Dungeon 类 / 互动叙事 / 聊天 Bot 库" = @("methods/网文写作最强SOP.md")
    "十八、Awesome 列表 / 资源聚合 库" = @("methods/QUICK_START.md")
    "十九、其他 AI 写作 / 文本工具 库" = @("methods/QUICK_START.md")
    "十、其他 AI 写作 / 文本工具 库" = @("methods/QUICK_START.md")
    "一、网文 / Claude Skill 生态 写作辅助" = @("methods/QUICK_START.md")
}

$files = Get-ChildItem -Path $cardsDir -File -Filter "*.md"
$updated = 0
$skipped = 0
$errors = 0

foreach ($f in $files) {
    $content = Get-Content $f.FullName -Encoding UTF8 -Raw
    
    # Skip if already has related
    if ($content -match "related:") {
        $skipped++
        continue
    }
    
    # Extract category
    $cat = ""
    if ($content -match "category:\s*(.+)") {
        $cat = $matches[1].Trim()
    }
    
    # Get related files for this category
    $relatedFiles = $categoryMap[$cat]
    if (-not $relatedFiles) {
        $relatedFiles = @("methods/QUICK_START.md")
    }
    
    # Build related YAML
    $relatedYaml = "related:`n"
    foreach ($rf in $relatedFiles) {
        $relatedYaml += "  - $rf`n"
    }
    
    # Insert before closing ---
    # Find the last --- in the file
    $lastDashIndex = $content.LastIndexOf("---")
    if ($lastDashIndex -gt 0) {
        $before = $content.Substring(0, $lastDashIndex)
        $after = $content.Substring($lastDashIndex)
        $newContent = $before + $relatedYaml + $after
        
        [System.IO.File]::WriteAllText($f.FullName, $newContent, [System.Text.Encoding]::UTF8)
        $updated++
    } else {
        $errors++
    }
    
    if ($updated % 500 -eq 0 -and $updated -gt 0) {
        Write-Host "  Processed $updated files..."
    }
}

Write-Host "`nDone!"
Write-Host "Updated: $updated"
Write-Host "Skipped (already had related): $skipped"
Write-Host "Errors: $errors"
