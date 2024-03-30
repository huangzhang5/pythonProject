from osgeo import gdal
csar_file = "C:/Users/20104/Desktop/2023-286-1012.csar"

# 打开csar文件
dataset = gdal.Open(csar_file)

if dataset is None:
    print("无法打开csar文件")
else:
    # 获取图像的宽度和高度
    width = dataset.RasterXSize
    height = dataset.RasterYSize
    print("图像大小：{} x {}".format(width, height))

    # 获取图像的波段数
    band_count = dataset.RasterCount
    print("波段数：{}".format(band_count))

    # 读取第一个波段的数据
    band = dataset.GetRasterBand(1)
    data = band.ReadAsArray()

    # 关闭数据集
    dataset = None

    # 处理图像数据
    # 在这里可以对图像数据进行进一步处理或分析


