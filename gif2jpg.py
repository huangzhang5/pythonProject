import os
from PIL import Image

def convert_gif_to_jpg(input_folder, output_folder):
    # 检查输出文件夹是否存在，如果不存在则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith(".gif"):
            gif_path = os.path.join(input_folder, filename)
            jpg_filename = filename[:-4] + ".jpg"  # 修改扩展名为.jpg
            jpg_path = os.path.join(output_folder, jpg_filename)

            # 打开.gif文件并保存为.jpg文件
            try:
                with Image.open(gif_path) as im:
                    im.convert("RGB").save(jpg_path, "JPEG")
                    print(f"成功转换 {gif_path} -> {jpg_path}")
            except Exception as e:
                print(f"转换失败 {gif_path}: {str(e)}")

# 示例用法
input_folder = "D:/研究生/浅剖/0925tu"  # 输入文件夹路径
output_folder = "D:/研究生/浅剖/0925tu1"  # 输出文件夹路径

convert_gif_to_jpg(input_folder, output_folder)
