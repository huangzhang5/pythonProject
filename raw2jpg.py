from PIL import Image
import numpy as np
import os

# 设置输入和输出文件夹路径
input_folder = 'C:/Users/20104/Desktop/新建文件夹'
output_folder = 'C:/Users/20104/Desktop/新建文件夹'

# 创建输出文件夹（如果不存在）
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有raw文件
for filename in os.listdir(input_folder):
    if filename.endswith('.raw'):
        # 构建输入和输出文件的完整路径
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + '.jpg')

        # 读取raw文件
        data = np.fromfile(input_file, dtype=np.uint8)
        data = data.reshape((5142, 5142))

        # 创建图像对象
        image = Image.fromarray(data, mode='L')

        # 保存为jpg文件
        image.save(output_file)
