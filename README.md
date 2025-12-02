# esim-tool
Generate eSIM QR codes from LPA strings offline. Solves the issue where carriers only provide text activation codes. (离线生成 eSIM 二维码。解决运营商只提供文本激活码的问题。)



# eSIM QR Code Generator (Local & Safe)

A simple Python script to convert eSIM activation codes (`LPA:1$...`) into QR codes locally. 

**Why this tool?**
Some carriers (e.g., Yallo, Lebara) sometimes only provide the text activation code (LPA string) without a QR code image. This tool allows you to generate the QR code offline, making it easier to scan with your phone, ensuring your sensitive eSIM data never leaves your device.

## Features
- 🔒 **100% Local & Safe**: No data is uploaded to any server. Run it offline.
- 🧠 **Smart Input**: Automatically detects if you paste a full LPA string or allows manual entry of SM-DP+ and Activation Code.
- 📂 **No Overwrites**: Automatically renames files (e.g., `esim_qr_1.png`) if a file already exists.

## Requirements
- Python 3.x
- `qrcode` library

## Installation

```bash
pip install qrcode[pil]


这是为你准备的代码仓库（GitHub/Gitee）填写建议。考虑到开源项目的通用性，建议名称使用英文，描述可以中英双语或者英文，这样显得更专业。

1. 仓库名称 (Repository Name)
建议简短、直接，使用连字符分隔。

最推荐 (标准): esim-qr-generator

解释：简单明了，一看就知道是干嘛的。

技术向: lpa-to-qr-converter

解释：强调是从 LPA 激活码转换到 QR 码。

强调安全/本地: offline-esim-qr

解释：强调离线（Offline）特性，吸引在意隐私的用户。

极简: esim-tool 或 esim-helper

2. 仓库描述 (Description)
这是显示在仓库名下方的一行简介，需要包含核心关键词：本地 (Local)、安全 (Safe)、eSIM、LPA。

方案 A：简洁通用（推荐）

A secure, local Python script to convert eSIM activation codes (LPA strings) into QR codes. (一个安全、本地运行的 Python 脚本，用于将 eSIM 激活码转换为二维码。)

方案 B：强调痛点解决

Generate eSIM QR codes from LPA strings offline. Solves the issue where carriers only provide text activation codes. (离线生成 eSIM 二维码。解决运营商只提供文本激活码的问题。)

方案 C：强调功能特性

Offline eSIM QR generator. Supports auto-detection of LPA strings and prevents file overwriting. Secure and simple. (离线 eSIM 二维码生成器。支持自动识别 LPA 字符串及防止文件覆盖。安全且简单。)

3. README.md (项目说明文件)
仓库建好后，你需要一个 README.md 来介绍项目。你可以直接把下面这段 Markdown 代码复制进去：

Markdown

# eSIM QR Code Generator (Local & Safe)

A simple Python script to convert eSIM activation codes (`LPA:1$...`) into QR codes locally. 

**Why this tool?**
Some carriers (e.g., Yallo, Lebara) sometimes only provide the text activation code (LPA string) without a QR code image. This tool allows you to generate the QR code offline, making it easier to scan with your phone, ensuring your sensitive eSIM data never leaves your device.

## Features
- 🔒 **100% Local & Safe**: No data is uploaded to any server. Run it offline.
- 🧠 **Smart Input**: Automatically detects if you paste a full LPA string or allows manual entry of SM-DP+ and Activation Code.
- 📂 **No Overwrites**: Automatically renames files (e.g., `esim_qr_1.png`) if a file already exists.

## Requirements
- Python 3.x
- `qrcode` library

## Installation

```bash
pip install qrcode[pil]
Usage
Download gen_esim.py.

Run the script:

Bash

python gen_esim.py
Follow the prompts to paste your LPA string or enter details manually.

The QR code image will be generated in the same directory.

License
MIT License
