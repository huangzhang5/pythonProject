# 相关库导入
import xlrd
import openpyxl
import pandas as pd
from pyautocad import Autocad, APoint
from tkinter.filedialog import askopenfilename, asksaveasfilename

# 读取txt文件
addr = askopenfilename(title='选择文件',
                       filetypes=[('文本文件', '*.txt')],
                       initialdir='D:/')
data = pd.read_csv(addr, delimiter=' ')

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

# 打开Excel文件
workbook = openpyxl.load_workbook(filename)

# 选择要操作的工作表
worksheet = workbook.active

# 插入表头
header = ['X坐标', 'Y坐标', 'Z坐标']  # 表头内容，根据实际情况修改
worksheet.insert_rows(1)  # 在第一行之前插入新行
for col_num, col_title in enumerate(header, 1):
    cell = worksheet.cell(row=1, column=col_num)
    cell.value = col_title

# 保存修改后的Excel文件
workbook.save(filename)

# 连接autocad(未打开cad,会自动打开)
acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello! AutoCAD from pyautocad.")
print(acad.doc.Name)

# 读取excel文件
data = xlrd.open_workbook(filename)
# 获取excel文件，第一页数据
table = data.sheets()[0]
# 获取有效行数
loop = table.nrows-1

# for循环插入点，并连线
for i in range(1, loop):
    # 获取第i行数据
    location = table.row_values(i)
    x = location[0]
    y = location[1]
    z = location[2]
    # 展点
    insert_point = APoint(x, y, z)
    # 获取第i+1行数据
    location2 = table.row_values(i+1)
    x2 = location2[0]
    y2 = location2[1]
    z2 = location2[2]
    # 展点
    insert_point2 = APoint(x2, y2, z2)
    # 连接相邻点
    acad.model.AddLine(insert_point, insert_point2)

# for循环给所有点赋名字
for i in range(1, loop+1):
    location = table.row_values(i)
    x = location[0]
    y = location[1]
    z = location[2]
    insert_point = APoint(x, y, z)
    # 赋点名
    text = acad.model.AddText("point %s" % i, insert_point, 5)
