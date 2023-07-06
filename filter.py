import os
import shutil
import numpy as np

main_dir = r"D:/Adani_Manglore_Airport/Final_mangalore_dataset/"
directory1 = r"D:/Adani_Manglore_Airport/Dataset/images/"
directory2 = r"D:/Adani_Manglore_Airport/Dataset/labels/"

for filename in os.listdir(main_dir):
    # print(filename)
    if os.path.isfile(main_dir + filename[:-4] + '.jpg') and filename.endswith('.txt'):
        shutil.copy(main_dir + filename[:-4] + '.jpg', directory1)
        shutil.copy(main_dir + filename[:-4] + '.txt', directory2)

    # if os.path.isfile(main_dir + filename[:-4] + '.jpg') and filename.endswith('.txt'):
    #     shutil.copy(directory2 + filename[:-4] + '.txt', directory2)
    # if os.path.isfile(main_dir + filename[:-4] + '.jpg') and filename.endswith('.jpg'):
    #     shutil.copy(directory1 + filename[:-4] + '.jpg', directory1)

