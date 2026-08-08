---
id: tool-00913
type: tool
area: 库
status: active
tags: [MATLAB, 协议宽松, 本地优先, 中文友好, 大纲规划, 多Agent, 本地写作, 灵感创意]
title: matlab-cmg-two-phase-flow-automation-MATLAB-CMG-
summary: 从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）
source: https://github.com/poorphdyj/matlab-cmg-two-phase-flow-automation-matlab-cmg-
created: 2026-07-18
updated: 2026-07-18
no: 913
category: 二、网文 / 长篇 AI 写作系统 库
repo: poorphdyj/matlab-cmg-two-phase-flow-automation-MATLAB-CMG-
stars: 1
url: https://github.com/poorphdyj/matlab-cmg-two-phase-flow-automation-matlab-cmg-
tier: "B"
use_case: "从灵感→大纲→正文的全流程写作辅助（搭框架/续写/多Agent生产）"
pitfalls: []
related:
  - methods/网文写作最强SOP.md
source_kind: distilled
spdx: unknown
fetched_at: 2026-07-18
content_hash: 5d53efc265b08393
  - methods/最强写作方法论_全球最强综合版.md
---

# poorphdyj/matlab-cmg-two-phase-flow-automation-MATLAB-CMG-

- **分类**：二、网文 / 长篇 AI 写作系统 库
- **链接**：https://github.com/poorphdyj/matlab-cmg-two-phase-flow-automation-matlab-cmg-
- **Stars**：1
- **语言**：MATLAB
- **License**：MIT
- **Topics**：capillary-heterogeneity, capillary-pressure, carbon-storage, cmg, cmg-output-extraction, coreflooding, heterogeneity, hydrogen-storage, matlab, matlab-cmg-workflow, numerical-simulation, permeability, petroleum-engineering, porous-media, reservoir-engineering, reservoir-simulation, simulation-automation, subsurface-flow, two-phase-flow, water-saturation
- **GitHub 描述**：A MATLAB workflow for automatically running CMG two-phase flow simulations, writing heterogeneous permeability and capillary pressure input files, and extracting Sw, Pc, and pressure results.
- **本地描述**：A MATLAB workflow for automatically running CMG two-phase flow simulations, writing heterogeneous permeability and capillary pressure input files, and extracting Sw, Pc, and pressure results.
- **拉取时间**：2026-07-23 23:05:40

related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
related:
  - methods/网文写作最强SOP.md
  - methods/最强写作方法论_全球最强综合版.md
---

# MATLAB-CMG Automatic Run and Output Extraction

# MATLAB-CMG Two-Phase Flow Simulation Automation

## 中文简介

本项目提供了一个基于 MATLAB 的自动化工作流，用于调用 CMG 软件运行油藏或岩芯尺度的两相流数值模拟，并自动处理模拟输出结果。

该代码可以从外部生成的渗透率场读取数据，自动生成 CMG 所需的 include 文件，例如 `K.inc` 和 `Pc_max.inc`。其中，`K.inc` 用于定义空间非均质渗透率场，`Pc_max.inc` 用于根据局部渗透率计算并写入非均质最大毛管压力参数。代码随后通过 MATLAB 的 `system` 命令自动调用 CMG 可执行文件运行模拟，并从 CMG 输出文件中提取水饱和度 `Sw`、毛管压力 `Pc` 和压力 `Pressure` 等结果，最终保存为 MATLAB `.mat` 文件，方便后续分析、绘图和反演计算。

该项目适用于需要反复运行 CMG 模型、测试不同渗透率场、考虑毛管压力非均质性，或者批量处理岩芯尺度与油藏尺度两相流模拟结果的研究场景。

## English Introduction

This project provides a MATLAB-based automation workflow for running CMG two-phase flow simulations and extracting simulation results automatically.

The script reads an externally generated permeability field and writes CMG include files such as `K.inc` and `Pc_max.inc`. The file `K.inc` defines the heterogeneous permeability distribution, while `Pc_max.inc` defines the permeability-scaled maximum capillary pressure field. The MATLAB script then calls the CMG executable through the `system` command, runs the reservoir or core-scale two-phase flow model, reads the CMG output file, and extracts water saturation `Sw`, capillary pressure `Pc`, and pressure results. The extracted data are saved as a MATLAB `.mat` file for further analysis, visualization, or inverse modeling.

This workflow is useful for studies involving repeated CMG simulations, heterogeneous permeability fields, capillary pressure heterogeneity, core-scale two-phase flow modeling, reservoir-scale simulations, and automatic post-processing of CMG output files.


The code keeps the original script-style structure. It is intended for users who want to copy, paste, and modify one MATLAB file directly, rather than using a function-based project.

## What this script does

The MATLAB script `run_matlab_cmg_auto.m` does the following:

1. Loads simulation parameters from `parapc2.mat`.
2. Loads an externally generated permeability field from a text file.
3. Generates the CMG include file `K.inc` for permeability.
4. Generates the CMG include file `Pc_max.inc` for maximum capillary pressure.
5. Calls the CMG executable from MATLAB.
6. Reads the CMG `.out` file.
7. Extracts water saturation (`Sw`), pressure (`P`), and capillary pressure (`Pc`).
8. Saves the extracted results into a MATLAB `.mat` file.

## Project structure

```text
.
├── run_matlab_cmg_auto.m
├── README.md
├── LICENSE
├── .gitignore
├── .gitattributes
├── docs/
│   └── CODE_EXPLANATION.md
├── examples/
│   ├── cmg_include_template.dat
│   └── create_parapc2_example.m
├── data/
│   └── README.md
├── params/
│   └── README.md
└── outputs/
    └── README.md
```

## Required files before running

Before running the MATLAB script, prepare the following files in the working folder.

### 1. MATLAB parameter file

Default file name:

```text
parapc2.mat
```

This file is only used to provide model parameters, such as:

```matlab
kef
Pcmax
```

The script also accepts `pcmax` or `pcma` as alternative names for `Pcmax`.

Important: `parapc2.mat` is not the CMG model file. It is only a MATLAB parameter file.

### 2. External permeability file

Default file name:

```text
K3V05.txt
```

This file contains the externally generated permeability field. The original workflow reshapes this field into a CMG grid with:

```text
52 × 25 × 25 = 32500 grid blocks
```

The internal physical core region is:

```text
50 × 25 × 25 = 31250 grid blocks
```

The first and last I-layers are treated as boundary layers.

### 3. CMG input data file

Default file name in the example script:

```text
gas_3D_10ff_pc2_v1_q4.dat
```

This is the CMG input data file. The name is not fixed. Users can rename it according to their own CMG case naming system.

For example:

```text
case_001.dat
h2_water_core.dat
my_cmg_model.dat
```

If the file name is changed, update the following line in `run_matlab_cmg_auto.m`:

```matlab
cmgInputFile = 'your_model_name.dat';
```

Also update the expected output file name:

```matlab
cmgOutputFile = 'your_model_name.out';
```

### 4. CMG executable and DLL files

The example script calls:

```matlab
mx201710.exe
```

If MATLAB calls the CMG executable directly from the working folder, the following files may also need to be placed in the same folder:

```text
SipLib.dll
SR3SimInterface.dll
binarrayfile.dll
```

These files are part of the local CMG runtime environment. They are not included in this repository and should not be uploaded to GitHub.

If CMG is already installed and available through the Windows system path, users may instead provide the full path to the CMG executable in the script.

Example:

```matlab
cmgExe = 'C:\Program Files\CMG\imex\2017.10\Win_x64\EXE\mx201710.exe';
```

## Required CMG input-file setup

The MATLAB script generates two include files:

```text
K.inc
Pc_max.inc
```

The CMG input data file must include these files under the correct CMG property keywords.

Conceptual example:

```text
** Heterogeneous permeability field generated by MATLAB
[CMG permeability keyword]
*INCLUDE 'K.inc'

** Maximum capillary pressure field generated by MATLAB
[CMG Pcmax keyword]
*INCLUDE 'Pc_max.inc'
```

The exact CMG keywords depend on the user’s own model setup. The key point is that `K.inc` and `Pc_max.inc` only contain grid-indexed values, so the CMG input file must define what property these values represent.

## Capillary pressure scaling

The script computes the local maximum capillary pressure as:

```matlab
Pcmax_local = Pcmax * sqrt(kef / K_local)
```

This means:

- lower permeability gives higher capillary pressure;
- higher permeability gives lower capillary pressure.

The boundary treatment is:

```text
i = 1  : Pcmax
i = 52 : 0
i = 2 to 51 : permeability-scaled Pcmax
```

## How to run

1. Copy the required local files into the same folder as `run_matlab_cmg_auto.m`:

```text
parapc2.mat
K3V05.txt
your_cmg_model.dat
mx201710.exe
SipLib.dll
SR3SimInterface.dll
binarrayfile.dll
```

2. Open MATLAB in this folder.

3. Update the file names at the top of `run_matlab_cmg_auto.m` if needed.

4. Run:

```matlab
run_matlab_cmg_auto
```

5. After the run, check the generated files:

```text
K.inc
Pc_max.inc
your_cmg_model.out
gas_10ff_pc2_v1_q4.mat
```

## Output variables

The saved `.mat` file contains the extracted results.

The main variables are:

```matlab
K   % internal heterogeneous permeability field
Sw  % water saturation table: [I, J, K, value]
P   % pressure table: [I, J, K, value]
Pc  % capillary pressure table: [I, J, K, value]
```

For `Sw` and `Pc`, the boundary layers `i = 1` and `i = 52` are removed after extraction.

For `P`, the boundary layers are kept by default. If pressure should also be restricted to the internal core region, uncomment the optional lines in the script.

## Notes

This script assumes that the CMG `.out` file keeps the same table structure as the original model output. In particular, it searches for the time marker `12.00` in column 3.

If the CMG output format, grid size, or selected output time changes, the output extraction section may need to be updated.

## License

This project is released under the MIT License.
