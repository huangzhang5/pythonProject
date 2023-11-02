import pandas as pd

# 读取Excel文件
df = pd.read_excel('C:/Users/20104/Desktop/data.xlsx')

# 创建一个空的数据框，用于存储转换后的数据
new_df = pd.DataFrame()

# 遍历原数据框的每一行
for index, row in df.iterrows():
    expert_id = row['专家编码']
    scores = str(row['原始分']).split(',')  # 将得分字符串按逗号分割成列表

    if expert_id in new_df.columns:
        # 获取该专家的列索引
        expert_col_index = new_df.columns.tolist().index(expert_id)
        # 在对应列上追加该专家的得分数据
        new_df.loc[index, expert_id] = scores
    else:
        # 在新数据框中新增一列，并在对应列上添加该专家的得分数据
        new_df[expert_id] = pd.Series(scores)

# 对NaN值进行填充，将缺失值替换为''
new_df.fillna('', inplace=True)

# 使用pd.concat(axis=1)函数重新整理数据框
new_df = pd.concat([new_df[col].reset_index(drop=True) for col in new_df.columns], axis=1)

# 输出转换后的数据框
new_df.to_excel('C:/Users/20104/Desktop/output_file.xlsx', index=False)
