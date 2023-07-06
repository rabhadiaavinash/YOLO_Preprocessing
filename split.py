import os
import shutil
import numpy as np


images =r"D:/Adani_Manglore_Airport_Flipped/Final_Flipped_and_normal_images/"
labels =r"D:/Adani_Manglore_Airport_Flipped/Final _Flipped_and_normal_annotations/"


images_train =r"D:/Adani_Manglore_Airport_Flipped/Dataset/images/train/"
images_test = r"D:/Adani_Manglore_Airport_Flipped/Dataset/images/valid/"

labels_train = r"D:/Adani_Manglore_Airport_Flipped/Dataset/labels/train/"
labels_test = r"D:/Adani_Manglore_Airport_Flipped/Dataset/labels/valid/"

print(len(os.listdir(images)))

print(len(os.listdir(labels)))

threshold = len(os.listdir(images)) * 0.2
print(int(threshold))

counter = 0


files1 = os.listdir(images)
files2 = os.listdir(labels)

pointer = (len(os.listdir(labels)) - threshold)
print(int(pointer))


for filename1 in files1:
    for filename2 in files2:
        if filename1[:-4] == filename2[:-4]:
            shutil.move(images + filename1[:-4] + '.jpg', images_train)
            shutil.move(labels + filename2[:-4] + '.txt', labels_train)
            counter += 1
    if counter > pointer:
        break




