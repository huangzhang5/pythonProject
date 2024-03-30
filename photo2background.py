from PIL import Image

# 1. 自己选择照片导入
image_path = input("请输入照片路径: ")
image = Image.open(image_path)

# 2. 自动选择颜色替换照片背景
replace_color = input("请选择要替换的颜色(1为红色，2为蓝色): ")
if replace_color == "1":
    new_image = image.convert("RGB")
    data = new_image.getdata()
    new_data = []
    for item in data:
        # 将红色替换为新颜色（比如白色）
        if item[0] > item[1] and item[0] > item[2]:
            new_data.append((255, 255, 255))
        else:
            new_data.append(item)
    new_image.putdata(new_data)
elif replace_color == "2":
    new_image = image.convert("RGB")
    data = new_image.getdata()
    new_data = []
    for item in data:
        # 将蓝色替换为新颜色（比如黄色）
        if item[2] > item[0] and item[2] > item[1]:
            new_data.append((255, 255, 0))
        else:
            new_data.append(item)
    new_image.putdata(new_data)
else:
    print("无效的选项")

# 3. 导出图片为jpg格式
output_path = input("请输入导出图片的路径: ")
new_image.save(output_path, "JPEG")
