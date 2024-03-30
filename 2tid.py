import datetime

# 读取文件
with open('D:/研究生/各种任务/噪声/1227.tid', 'r') as file:
    lines = file.readlines()

# 定义时间格式
time_format = '%Y/%m/%d %H:%M:%S'

# 提取数据
data = []
for line in lines:
    # 跳过空行
    if not line.strip():
        continue

    try:
        # 获取时间字符串和数据值
        time_str, value = line.strip().split('\t')
        time = datetime.datetime.strptime(time_str, time_format)

        # 每五分钟提取一个数据
        if time.minute % 5 == 0 and time.second == 0:
            data.append((time, float(value)))
    except ValueError:
        # 跳过无法解析的行
        continue

# 将提取的数据保存到文件
with open('D:/研究生/各种任务/噪声/output.tid', 'w') as file:
    for item in data:
        file.write(f'{item[0]}\t{item[1]}\n')

print("数据已保存到output.tid文件中")