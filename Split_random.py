import os
import shutil
import numpy as np


images =r"D:/Adani_Manglore_Airport_Flipped/Final_Flipped_and_normal_images/"
labels =r"D:/Adani_Manglore_Airport_Flipped/Final _Flipped_and_normal_annotations/"


images_train =r"D:/Adani_Manglore_Airport_Flipped/Dataset/images/train/"
images_test = r"D:/Adani_Manglore_Airport_Flipped/Dataset/images/valid/"


labels_train = r"D:/Adani_Manglore_Airport_Flipped/Dataset/labels/train/"
labels_test = r"D:/Adani_Manglore_Airport_Flipped/Dataset/labels/valid/"


filesimages = os.listdir(images)
fileslabels = os.listdir(labels)

#d=random.choice(files)


for img in filesimages:
    if np.random.rand(1) < 0.2:
        print(img)

        for label in fileslabels:
            if img[:-4] == label[:-4]:
                shutil.move(images + '\\' + img, images_test + '\\' + img)
                shutil.move(labels + '\\' + label, labels_test + '\\' + label)

