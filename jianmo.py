import pandas as pd
import matplotlib.pyplot as plt


# Step 1: 读取Excel文档
df = pd.read_csv('D:/研究生/数学建模/answer1.csv', index_col=0)

# 打印前5行数据
print(df.head())

# Step 2: 计算专家评审作品的重合度
overlap_scores = df.sum(axis=1) / df.shape[1]
# overlap_score = float(format(overlap_scores, ".3f"))
# 打印每位专家的重合度
print(overlap_scores)
# exp = (0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0)
# Step 3: 画出对应的饼状图
plt.pie(overlap_scores, autopct='%1.1f%%')
plt.title("The degree of overlap of works", fontdict={"family": "serif", "size": "15"})
# plt.
plt.show()
