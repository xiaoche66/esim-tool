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
Usage
Download gen_esim.py.

Run the script:

Bash

python gen_esim.py
Follow the prompts to paste your LPA string or enter details manually.

The QR code image will be generated in the same directory.

License
MIT License
