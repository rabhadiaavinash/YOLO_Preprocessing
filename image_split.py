import os
import shutil
import numpy as np

sourceN =r"D:/Adani Queue Manager/Dataset/labels/"
destN =r"D:/Adani Queue Manager/Dataset/test/"
#destD = r"D:\Aditi\Adani_project_all\Adani_all_unknown_classes\images2"

   #sourceP = base_dir + "\\train\\PNEUMONIA"
   #destP = base_dir + "\\val\\PNEUMONIA"

filesN = os.listdir(sourceN)
   #filesP = os.listdir(sourceP)

for f in filesN:
    if np.random.rand(1) < 0.2:
        shutil.move(sourceN + '\\'+ f, destN + '\\'+ f)

    #elif np.random.rand() >= 0.4:
        #shutil.move(sourceN + '\\'+ f, destN + '\\'+ f)

    #elif np.random.rand() >= 0.7:
        #shutil.move(sourceN + '\\'+ f, destD + '\\'+ f)

   #for i in filesP:
       #if np.random.rand(1) < 0.2:
       #shutil.move(sourceP + '\\'+ i, destP + '\\'+ i)

print(len(os.listdir(sourceN)))
   #print(len(os.listdir(sourceP)))
print(len(os.listdir(destN)))
   #print(len(os.listdir(destP)))
#print(len(os.listdir(destD)))