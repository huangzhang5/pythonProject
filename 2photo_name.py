import os

def batch_rename_tif_to_png(directory):
    """
    批量将指定目录下的.tif文件更改为.png文件。
    :param directory: 包含.tif文件的目录路径
    """
    for filename in os.listdir(directory):
        if filename.endswith(".tif"):
            # 构造原文件的完整路径
            original_file = os.path.join(directory, filename)
            # 构造新文件名（更改扩展名为.png）
            new_filename = filename[:-5] + ".jpeg"
            new_file = os.path.join(directory, new_filename)
            # 重命名文件
            os.rename(original_file, new_file)
            print(f"已将 {original_file} 重命名为 {new_file}")

# 使用示例
# 假设你的.tif文件存储在'C:\path\to\your\directory'目录下
# 请将下方的路径替换为你的实际路径
directory_path = 'D:/1'
batch_rename_tif_to_png(directory_path)