import glob, os
training_dataset_dir = r"D:/Adani_Manglore_Airport_Flipped/Dataset/images/train/"
destination_folder = r"D:/Adani_Manglore_Airport_Flipped/Dataset/images/"
# file_train = open(destination_folder+'/train.txt', 'w')
file_test = open(destination_folder+'/train.txt', 'w')
# file_test = open(destination_folder+'/valid_adani_mang+ahm_without_person_30jan.txt', 'w')


#./custom_dataset/images/train/01-10-2021_11-37-48frame480.jpg

#"D:\ADANI FINAL DATASET ORIGINAL\yolov7_tiny_dataset\images\vallid"

for filename in os.listdir(training_dataset_dir):
    basename = os.path.basename(filename)
    if basename.endswith(".jpg"):
        #file_test.write("./adani_dataset/images/"+basename[:-4]+".jpg" + "\n")
        file_test.write("./Adani_Manglore_Airport_Flipped/Dataset/images/train/"+basename[:-4]+".jpg" + "\n")
    elif basename.endswith(".jpeg"):
        file_test.write("./Adani_Manglore_Airport_Flipped/Dataset/images/train/"+basename[:-5]+".jpeg" + "\n")
    elif basename.endswith(".png"):
        file_test.write("./Adani_Manglore_Airport_Flipped/Dataset/images/train/"+basename[:-4]+".png" + "\n")


    # if basename.endswith(".jpg"):
    #     file_test.write("./COMPLETE_DATASET/images/train/"+basename[:-4]+".jpg" + "\n")
    # elif basename.endswith(".jpeg"):
    #     file_test.write("./COMPLETE_DATASET/images/train/"+basename[:-5]+".jpeg" + "\n")
    # elif basename.endswith(".png"):
    #     file_test.write("./COMPLETE_DATASET/images/train/"+basename[:-4]+".png" + "\n")

    print(basename)
