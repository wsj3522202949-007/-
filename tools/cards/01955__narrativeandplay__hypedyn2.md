---
id: tool-00019
type: tool
area: 库
status: active
tags: [协议未明, 本地优先, 英文文档, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: hypedyn2
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/narrativeandplay/hypedyn2
created: 2026-07-18
updated: 2026-07-18
$11955
category: 二、网文 / 长篇 AI 写作系统 库
repo: narrativeandplay/hypedyn2
stars: 3
language: Scala
license: NOASSERTION
url: https://github.com/narrativeandplay/hypedyn2
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls:
  - "⚠️ 协议未声明，商用/分发前务必到仓库确认授权"
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: ac57611011e5bb5b
  - methods/最强写作方法论_全球最强综合版.md
---

# HypeDyn

HypeDyn (pronounced "hyped in") is a procedural hypertext fiction authoring tool for people who want to create
text-based interactive stories that adapt to reader choice.

This project is split into several modules:

- `api` - The API that the other modules and plugins use to communicate
- `core` - The backend of the system, handling things such as data structure management, serialisation, etc.
- `default-story-viewer` - A plugin that is the default implementation for visualising a HypeDyn story
- `ui` - The UI of the system, including the main entry point into the application

## System Requirements

* Java 8u141 or later
* Gradle >= 4.01
  * If using a local Gradle version and not the included Gradle wrapper

## Installation

The latest stable installers can be found at http://www.narrativeandplay.org/hypedyn/.

[Gradle](http://gradle.org) is used as the build tool for this project; more information about Gradle can be
found at its website.

To run the source version (if you cloned it from this repo), run the following command in a terminal:

```
./gradlew run
```

On Windows, `gradlew` may need to be replaced with `gradlew.bat`.

To execute the tests, run `./gradlew test`.

### Building packages

To build the binary packages, run `./gradlew build` in a terminal.

The Gradle JavaFX plugin used in the project will by default build all appropriate packages for the system it is
being built on. The built packages will be found in `build/distributions`. On all platforms, a base package containing
an executable and all the required files will be built in a `build/distributions/HypeDyn2` folder.

On Windows, if Inno Setup 5 or later is installed and available on the PATH, an installable exe will be created
(details [here](https://bitbucket.org/shemnon/javafx-gradle/issues/20/native-installers-not-create-on-windows) for how
to correctly place the path onto the PATH variable). Also, if the [WiX toolset](http://wixtoolset.org/) is available,
MSI installers will be built.


On OS X, this will also build DMG and pkg files automatically.

On Linux, if the required build tools are present (RPMBuild and/or deb packaging tools), the appropriate package
will be built.

More details on the packaging process can be found [here](http://docs.oracle.com/javafx/2/deployment/self-contained-packaging.htm).


## Contributing

This project follows standard gitflow conventions, with the only deviation from standard conventions being that the
`develop` branch is named `development` instead.

All code contributions must follow the code style as set out in the [style guide](https://github.com/narrativeandplay/hypedyn2/blob/main/style-guide.md)

## License

Copyright &copy; 2015-2019  National University of Singapore

Licensed under the GNU General Public License v3. See LICENSE for details.
