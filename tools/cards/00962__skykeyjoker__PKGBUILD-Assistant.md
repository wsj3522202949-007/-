---
id: tool-00962
type: tool
area: 库
status: active
tags: [C++, 协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: PKGBUILD-Assistant
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/skykeyjoker/pkgbuild-assistant
created: 2026-07-18
updated: 2026-07-18
no: 962
category: 二、网文 / 长篇 AI 写作系统 库
repo: skykeyjoker/PKGBUILD-Assistant
stars: 13
url: https://github.com/skykeyjoker/pkgbuild-assistant
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# skykeyjoker/PKGBUILD-Assistant

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/skykeyjoker/pkgbuild-assistant
- **Stars**：13
- **语言**：C++
- **License**：None
- **Topics**：aur, cpp, pkgbuild, pkgbuildassistant, qt5, qt5-gui
- **GitHub 描述**：An auxiliary tool for writing PKGBUILD files written in Qt5.
- **本地描述**：An auxiliary tool for writing PKGBUILD files written in Qt5.
- **拉取时间**：2026-07-23 23:07:06

---

# PKGBUILD-Assistant English Doc
PKGBUILD-Assistant is an auxiliary tool for writing PKGBUILD files developed using the Qt5 framework.



## Availability

| PLATFORM       | LINK                                                         |
| -------------- | ------------------------------------------------------------ |
| AUR            | [pkgbuild-assistant](https://aur.archlinux.org/packages/pkgbuild-assistant/) |
| Github Release | [PKGBUILD-Assistant](https://github.com/skykeyjoker/PKGBUILD-Assistant/releases) |



## Features

### Basic information editing

PKGBUILD-Assistant provides basic software package information editing functions, such as package name `${pkgname}` and package release version `${pkgver}`.



### Dependencies Query

PKGBUILD-Assistant can scan the lib files in the **specified directory** and call the Shell program `pacman -Fx` to query the software packages corresponding to the lib file.



### Package() Implement

PKGBUILD-Assistant can simulate the operation of `Package()` function in **specified directory**, such as copying files, folders, deleting file folders, etc. PKGBUILD-Assistant `Package()` function implementation block **Real-time** maintains two *virtual directory tree structures* of `${srcdir}` and `${pkgdir}`. By referring to the structure of the virtual directory tree, users can write the contents of the `Package()` function more intuitively.



### PKGBUILD and generated software package validity Check

PKGBUILD-Assistant can call namcap to check the validity of PKGBUILD and generated package. It is worth mentioning that when detecting the generated package, PKGBUILD-Assistant can remind the user whether to delete the dependency marked by namcap as **dependency-not-needed** (unneeded dependency).



## Related Links:

* [Arch Wiki: PKGBUILD](https://wiki.archlinux.org/index.php/PKGBUILD)





***





# PKGBUILD-Assistant 中文文档

PKGBUILD-Assistant是一款使用Qt5框架进行开发的PKGBUILD文件编写辅助工具。



## 获取程序

| 平台           | LINK                                                         |
| -------------- | ---------------------------------------------------------related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
--- |
| AUR            | [pkgbuild-assistant](https://aur.archlinux.org/packages/pkgbuild-assistant/) |
| Github Release | [PKGBUILD-Assistant](https://github.com/skykeyjoker/PKGBUILD-Assistant/releases) |





## 程序功能 

### 基本包信息编辑 

PKGBUILD-Assistant提供了基本的软件包信息编辑功能，如软件包名称`${pkgname}`、软件包发行版本`${pkgver}`等。



### 运行依赖查询

PKGBUILD-Assistant可以通过扫描**指定目录**下的lib文件，调用Shell程序`pacman -Fx`查询lib文件对应的软件包。



### Package()函数实现

PKGBUILD-Assistant可以在**指定目录**模拟`Package()`函数操作，如拷贝文件、文件夹，删除文件文件夹等。PKGBUILD-Assistant `Package()`函数实现版块**实时**维护了`${srcdir}`与`${pkgdir}`两个*虚拟目录树结构*。通过参照虚拟目录树结构，使用者能够比较直观地编写`Package()`函数内容。



### PKGBUILD与生成包合法性检测

PKGBUILD-Assistant可以调用namcap对PKGBUILD和生成包进行合法性检测。值得一提的是，对生成包进行检测时，PKGBUILD-Assistant可提醒用户是否删除被namcap标记为**dependency-not-needed**的依赖（即不需要的依赖）。



## 相关链接

* [Arch Wiki: PKGBUILD](https://wiki.archlinux.org/index.php/PKGBUILD)
