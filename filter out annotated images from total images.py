import os
import shutil
directory1 = "D:/Adani_Manglore_Airport/Final_mangalore_dataset/"
directory2 =  "D:/Adani Queue Manager/labels/"
for filename in os.listdir(directory1):
    #if filename.endswith('.txt') and os.path.isfile(directory1+filename[:-4]+'.jpg') :
     #   shutil.move(directory1+filename[:-4]+'.jpg',directory2)
      #  shutil.move(directory1+filename[:-4]+'.txt',directory2)
    if os.path.isfile(directory1+filename[:-4]+'.jpg') and filename.endswith('.txt'):
        shutil.move(directory1+filename[:-4]+'.jpg',directory2)
        shutil.move(directory1+filename[:-4]+'.txt',directory2)
    elif os.path.isfile(directory1+filename[:-4]+'.jpeg') and filename.endswith('.txt'):
        shutil.move(directory1+filename[:-4]+'.jpeg',directory2)
        shutil.move(directory1+filename[:-4]+'.txt',directory2)
    elif os.path.isfile(directory1+filename[:-4]+'.png') and filename.endswith('.txt'):
        shutil.move(directory1+filename[:-4]+'.png',directory2)
        shutil.move(directory1+filename[:-4]+'.txt',directory2)
