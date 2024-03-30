def process_dat_file(input_file, output_file):
    with open(input_file, 'r') as file_in:
        with open(output_file, 'w') as file_out:
            for line in file_in:
                line = line.strip()  # 去除行首和行尾的空白字符
                idx = line.find(',')  # 查找第一个逗号的位置
                if idx != -1:  # 如果找到了逗号
                    line = line[:idx] + line[idx+1:]  # 删除逗号
                file_out.write(line + '\n')

# 示例用法
input_file = 'D:/研究生/各种任务/移曲线生数据/F2_distance_202312.dat'
output_file = 'D:/研究生/各种任务/移曲线生数据/output.dat'

process_dat_file(input_file, output_file)
