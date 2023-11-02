def calculate_variance(data):
    # 计算数据的平均值
    mean = sum(data) / len(data)

    # 计算每个数据点与平均值的差的平方，并累加求和
    squared_diffs = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diffs) / len(data)

    return variance


data1 = [5,2,22,28,25,98,1,3,11,9,31,45,13,19,47]
data2 = [1
,2
,68
,21
,54
,378
,4
,34
,28
,7
,120
,12
,26
,8
,90
]
variance1 = calculate_variance(data1)
variance2 = calculate_variance(data2)
print("方差:", variance1)
print("方差:", variance2)
