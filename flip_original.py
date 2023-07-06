import os
import cv2 as cv
import numpy as np
import random
DirPath="D:/Aditi/Adani dataset(ahm+mang)_03-Jan-2023/Mangalore dataset release wise/Mangalore_23feb/mangalore_annotation_17-02-2023/"
Files= os.listdir(DirPath)
num=0

for File in Files:
    if File.endswith('.jpg'):
        imgPath= os.path.join(DirPath,File)
        image1= cv.imread(imgPath)
        flippedLR= np.fliplr(image1)

        #cv.imwrite(f"E:/Aditi/mask_dataset/complete_mask_dataset_img/{File.split(sep='.')[0]}"+'_Flip_'+str(num)+str(".jpg"),flippedLR)

        cv.imwrite(f"D:/Aditi/Adani dataset(ahm+mang)_03-Jan-2023/Mangalore dataset release wise/Mangalore_23feb/mangalore_annotation_17-02-2023/{File.split(sep='.')[0]}"+'_Flip_'+str(num)+str(".jpg"),flippedLR)
        num+=1

    ##cane_imgs1