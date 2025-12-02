import qrcode
import sys

def generate_esim_qr():
    print("--- eSIM QR Code Generator (Offline & Safe) ---")
    print("--- eSIM 二维码生成器 (本地离线安全版) ---\n")

    # 1. 获取输入 (Get Input)
    print("请选择输入方式 / Please choose input method:")
    print("1. 粘贴完整的 LPA 字符串 (例如: LPA:1$rsp.hotle.ch$ABCDE...)")
    print("2. 分别输入服务器地址和激活码")
    
    choice = input("\n请输入 1 或 2 (Enter 1 or 2): ").strip()

    final_lpa_string = ""

    if choice == '1':
        raw_input = input("\n请粘贴完整的 LPA 字符串: ").strip()
        # 简单的清理，防止复制时带入多余空格
        final_lpa_string = raw_input
        
        if not final_lpa_string.startswith("LPA:"):
            print("\n[警告] 输入的字符串似乎不是以 'LPA:' 开头，可能无法识别。")
            confirm = input("是否继续生成? (y/n): ")
            if confirm.lower() != 'y':
                sys.exit()

    elif choice == '2':
        sm_dp = input("\n请输入 SM-DP+ 地址 (例如 rsp.yallo.ch): ").strip()
        act_code = input("请输入激活码 (Activation Code): ").strip()
        
        # 自动拼接标准格式
        # Format: LPA:1$<SM-DP+>$<Activation Code>
        final_lpa_string = f"LPA:1${sm_dp}${act_code}"
        print(f"\n已拼接为: {final_lpa_string}")

    else:
        print("无效的选择 / Invalid choice")
        sys.exit()

    if not final_lpa_string:
        print("错误：内容为空！")
        sys.exit()

    # 2. 生成二维码 (Generate QR)
    print("\n正在生成二维码...")
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M, # 使用中等纠错，平衡密度
        box_size=10,
        border=4,
    )
    qr.add_data(final_lpa_string)
    qr.make(fit=True)

    # 3. 保存文件 (Save File)
    filename = "esim_qr.png"
    img = qr.make_image(fill_color="black", back_color="white")
    
    try:
        img.save(filename)
        print(f"\n✅ 成功！二维码已保存为当前目录下的 '{filename}'")
        print("请打开该图片并使用手机扫描。")
    except Exception as e:
        print(f"\n❌ 保存失败: {e}")

if __name__ == "__main__":
    try:
        generate_esim_qr()
    except KeyboardInterrupt:
        print("\n程序已取消。")
