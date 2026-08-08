---
id: tool-01941
type: tool
area: 库
status: active
tags: [Kotlin, 协议宽松, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: SafHelper
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/bartwell/safhelper
created: 2026-07-18
updated: 2026-07-18
no: 1941
category: 二、网文 / 长篇 AI 写作系统 库
repo: bartwell/SafHelper
stars: 11
url: https://github.com/bartwell/safhelper
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 4a35a8dba2551f21
  - methods/最强写作方法论_全球最强综合版.md
---

# bartwell/SafHelper

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/bartwell/safhelper
- **Stars**：11
- **语言**：Kotlin
- **License**：Apache-2.0
- **Topics**：—
- **GitHub 描述**：Open source Android library for files writing on SD card
- **本地描述**：Open source Android library for files writing on SD card
- **拉取时间**：2026-07-23 23:35:35

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

SafHelper
============

Open source Android library for files writing on SD card.

## Features

SafHelper using Storage Access Framework (SAF) to retrieve permission, create directories and write files on SD card.

## Integration

Add dependency in build.gradle:
```groovy
compile 'ru.bartwell:safhelper:1.0.0'
```

## Usage
```kotlin
private lateinit var safHelper: SafHelper

private fun onButtonClick() {
    writeFile(true)
}

private fun writeFile(requestPermissions: Boolean) {
    val userFile = File(main_path.text.toString())

    if (userFile.parent == null) {
        showToast("Wrong path")
    } else {
        safHelper = SafHelper(this, userFile.parent)
        if (safHelper.isApplicable()) {
            if (safHelper.isPermissionGranted()) {
                try {
                    if (safHelper.mkdirs(userFile.parent)) {
                        val outputStream = safHelper.createFile(userFile.path)
                        outputStream.use {
                            it.write("Text in the file".toByteArray())
                        }
                        showToast("Success")
                    }
                } catch (e: Exception) {
                    e.printStackTrace()
                    showToast("Error: " + e.message)
                }
            } else {
                if (requestPermissions) {
                    safHelper.requestPermissions(this)
                } else {
                    showToast("Permissions not granted")
                }
            }
        } else {
            showToast("File is not on SD Card or Android version < 5.0")
        }
    }
}

override fun onActivityResult(requestCode: Int, resultCode: Int, resultData: Intent?) {
    if (safHelper.onActivityResult(this, requestCode, resultCode, resultData)) {
        writeFile(false)
    }
}
```

## License

Copyright © 2018 Artem Bazhanov

SafHelper is provided under an Apache 2.0 License.
