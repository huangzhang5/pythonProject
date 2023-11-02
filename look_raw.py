import numpy as np

def get_raw_file_info(file_path):
    # 读取raw文件
    with open(file_path, 'rb') as file:
        data = file.read()

    # 将数据转换为numpy数组
    array = np.frombuffer(data, dtype=np.uint16)

    # 获取数据格式
    data_format = array.dtype.name

    # 获取行数、列数和通道数
    rows = int(len(array) ** 0.5)
    cols = rows
    channels = 1

    # 如果数据是三通道的，则需要计算行数、列数和通道数
    if len(array) % (rows * cols * channels) == 0 and len(array) != rows * cols * channels:
        channels = len(array) // (rows * cols)

    return data_format, rows, cols, channels

# 测试
file_path = 'C:/Users/20104/Desktop/新建文件夹/H11_17092023_023139.raw'
data_format, rows, cols, channels = get_raw_file_info(file_path)
print('数据格式:', data_format)
print('行数:', rows)
print('列数:', cols)
print('通道数:', channels)
