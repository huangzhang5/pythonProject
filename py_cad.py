import pandas as pd
from tkinter.filedialog import askopenfilename, asksaveasfilename
# 读取txt文件
addr = askopenfilename(title='选择文件',
                       filetypes=[('文本文件', '*.txt')],
                       initialdir='D:/')
data = pd.read_csv(addr, delimiter=' ', header=None)

# 指定需要提取的列，假设是第1和第3列
selected_columns = [0, 1, 11]

# 提取指定列
selected_data = data.iloc[:, selected_columns]

# 将结果写入Excel文件
filename = asksaveasfilename(title="另存为",
                            filetypes=[('数据文件', '*.xlsx')],
                            initialdir='D:/', initialfile='output.xlsx',
                            defaultextension='.xlsx')
selected_data.to_excel(filename, index=False)

# # 打开Excel文件
# workbook = openpyxl.load_workbook(filename)
#
# # 选择要操作的工作表
# worksheet = workbook.active
#
# # 插入表头
# header = ['X坐标', 'Y坐标', 'Z坐标']  # 表头内容，根据实际情况修改
# worksheet.insert_rows(1)  # 在第一行之前插入新行
# for col_num, col_title in enumerate(header, 1):
#     cell = worksheet.cell(row=1, column=col_num)
#     cell.value = col_title

# # 保存修改后的Excel文件
# workbook.save(filename)
