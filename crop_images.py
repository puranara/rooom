import os
from PIL import Image # 需要安装这个库

# === 配置区域 ===
# 这里的 ./assets 意思是在当前目录下的 assets 文件夹
folder_path = './assets' 

def trim_transparent_pixels(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert("RGBA") # 确保是透明格式
        
        # 获取原来尺寸用于对比
        old_size = img.size
        
        # getbbox() 会自动找到非透明像素的边界 (左, 上, 右, 下)
        bbox = img.getbbox()
        
        if bbox:
            # 按照边界裁剪
            cropped_img = img.crop(bbox)
            # 覆盖保存原文件
            cropped_img.save(image_path)
            
            new_size = cropped_img.size
            print(f"✅ 裁剪成功: {image_path} | 从 {old_size} 变瘦为 -> {new_size}")
        else:
            print(f"⚠️ 跳过（这是一张全透明图）: {image_path}")
            
    except Exception as e:
        print(f"❌ 处理出错 {image_path}: {e}")

# 开始运行
print(f"🚀 开始扫描文件夹: {folder_path} ...")

if not os.path.exists(folder_path):
    print(f"❌ 找不到文件夹: {folder_path}，请确认脚本位置！")
else:
    # 遍历文件夹下所有文件
    for filename in os.listdir(folder_path):
        # 只处理 .png 结尾的图片
        if filename.lower().endswith(".png"):
            full_path = os.path.join(folder_path, filename)
            trim_transparent_pixels(full_path)

    print("\n🎉 全部搞定！所有图片的透明边框都切掉了。")
