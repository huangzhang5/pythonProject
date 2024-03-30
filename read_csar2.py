import geopandas as gpd

# 读取CSAR文件
csar_file = 'C:/Users/20104/Desktop/2023-286-1012.csar' # 替换为实际的CSAR文件路径
data = gpd.read_file(csar_file)

# 打印数据信息
# 打印前几行数据
print(data.head())
# 打印数据维度
print(data.shape)
# 打印数据列名
print(data.columns)
# 输出了数据框的概要信息，包括总行数、列数，每列的名称、非空值数量、数据类型和内存使用情况。
print(data.info())
# 将数据输出到TXT文件
txt_file = 'output.txt' # 输出的TXT文件路径和名称
with open(txt_file, 'w') as f:
    for index, row in data.iterrows():
        line = f"{row['LOD0']}\t{row['LOD1']}\t{row['LOD2']}\t{row['LOD3']}\t{row['LOD4']}\t{row['LOD5']}\t{row['LOD6']}\t{row['LOD6']}\t{row['_key']}\t{row['_private_revision']}\t{row['geometry']}\n"
        f.write(line)
