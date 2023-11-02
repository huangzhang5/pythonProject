import os.path
import os
from PIL import Image
import numpy as np
import cv2
import imageio

def read(input_dir, shape, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    # img = cv2.imread('D:\Installer\\h_1_3_00_2_4_0_0_5_30_01_0_00.raw')

    # type = img.dtype
    w, h, c = shape
    input_dir = os.path.join('D:\\JS17\rawData\\', input_dir)
    list = os.listdir(input_dir)
    for path in list:
        if path.endswith('.xml'):
            continue
        ### 直接传入文件路径，不用加'r'
        imgData = np.fromfile(input_dir + '\\' + path, dtype='uint16')   ### 这里是16bit所以要uint16
        w, h, c = 5120, 4096, 1
        # # imgData = np.fromfile(r'D:\Installer\\h_1_1_0_2_0_4_1_5_38_63_0.raw', dtype='uint16')   # SAR
        # # w, h, c = 2048, 2048, 1
        imgData = imgData.reshape(w, h, c)
        cv2.imwrite(save_dir + path.split('.')[0] + '.png', imgData)
if __name__ == '__main__':
	# 传入raw文件夹；图像的w, h, c；图像的保存路径

    read('SAR', [2048, 2048, 1], 'D:\\JS17\TIFData\SAR\\')

    read('中波红外', [1024, 1280, 1], 'D:\\JS17\TIFData\MiddleHW\\')

    read('可见光', [4096,5120, 1], 'D:\\JS17\TIFData\KJG\\')
