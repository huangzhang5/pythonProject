# 相关库导入
from pyautocad import Autocad, APoint
import xlrd

# 连接autocad(未打开cad,会自动打开)
acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello! AutoCAD from pyautocad.")
print(acad.doc.Name)

# 读取excel文件
data = xlrd.open_workbook("D:/output3.xlsx")
# 获取excel文件，第一页数据
table = data.sheets()[0]
# 获取有效行数
loop = table.nrows-1

# for循环插入点，并连线
for i in range(1, loop):
    # 获取第i行数据
    location = table.row_values(i)
    x = location[1]
    y = location[2]
    z = location[0]
    # 展点
    insert_point = APoint(x, y, z)
    # 获取第i+1行数据
    location2 = table.row_values(i+1)
    x2 = location2[1]
    y2 = location2[2]
    z2 = location2[0]
    # 展点
    insert_point2 = APoint(x2, y2, z2)
    # 连接相邻点
    acad.model.AddLine(insert_point, insert_point2)

# for循环给所有点赋名字
for i in range(1, loop+1):
    location = table.row_values(i)
    x = location[1]
    y = location[2]
    z = location[0]
    insert_point = APoint(x, y, z)
    # 赋点名
    text = acad.model.AddText("point %s" % i, insert_point, 5)
