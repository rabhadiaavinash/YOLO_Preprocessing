from xml.dom import minidom
import os
import glob
import cv2



def convert_coordinates(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)



lut = {}


lut["cane"] = 0
lut["Cane"] = 0
lut["Walker"]=1
lut["walker"]=1
lut["crutch"]=2
lut["Crutch"]=2
lut["carry baby"]=3
lut["Carry baby"]=3
lut["Carry Baby"]=3
lut["CarryBaby"]=3
lut["carrybaby"]=3
lut["baby"]=3
lut["Baby"]=3
lut["unknown"] = 4
lut["Unknown"] = 4
lut["queue_manager"] = 4
# lut["suitcase"] = 4
# lut["handbag_bag"] = 4
lut["trolly"] = 4
# lut["bagpack"] = 4
lut["wheel_chair"] = 4
lut["mop"] = 4
lut["barricade"] = 4
# lut["carry baby_pouch"] = 4
lut["baby_stroller"] = 4
lut["floor_machine"] = 4
lut["Person"] = 5
lut["person"] = 5
# lut["char"]=0
# lut["plate"]=0

# lut["cane"] = 0
# lut["Cane"] = 0
# lut["Walker"]=1
# lut["walker"]=1
# lut["crutch"]=2
# lut["Crutch"]=2
# lut["carry baby"]=3
# lut["Carry baby"]=3
# lut["Carry Baby"]=3
# lut["CarryBaby"]=3
# lut["carrybaby"]=3
# lut["baby"]=3
# lut["Baby"]=3
# lut["unknown"] = 4
# lut["Unknown"] = 4
# lut["queue_manager"] = 6
# lut["Queue_manager"] = 6
# lut["queue manager"] = 6
# lut["Person"] = 5
# lut["person"] = 5
# lut["Fallen"] = 5
# lut["fallen"] = 5
# lut["suitcase"] = 4
# lut["handbag_bag"] = 4
# lut["trolly"] = 4
# lut["bagpack"] = 4
# lut["wheel_chair"] = 4
# lut["mop"] = 4
# lut["barricade"] = 4
# lut["trolly"] = 4

# lut["truck"]=6
# lut["cycle"] = 7
# lut["bike"] = 8

#path_xml=r"D:\Aditi\Yolo2Pascal-annotation-conversion-master\demo\yolo2pascal"

# path_xml ="D:/Adani Queue Manager/Adani_dataset_queue_manager/"
path_xml ="D:/Adani_Manglore_Airport/XML/"
#path_yolo ="C:/Users/aditi.javkar/Desktop/Adani_All_data_ARC_14-09-2022/complete_raw_dataset_XML/Crowdhuman01/"


def convert_xml2yolo(lut):
    for fname in glob.glob(path_xml + "*.xml"):
        #img1=cv2.imread('C:/Users/Aditi.javkar/data_augmentation/test/original.jpg')
        #img2=cv2.imread('C:/Users/Aditi.javkar/data_augmentation/test/flip.jpg')


        xmldoc = minidom.parse(fname)

        fname_out = (fname[:-4] + '.txt')

        with open(fname_out, "w") as f:
            # if os.path.exist(path_yolo+fname_out):
            itemlist = xmldoc.getElementsByTagName('object')
            size = xmldoc.getElementsByTagName('size')[0]
            width = int((size.getElementsByTagName('width')[0]).firstChild.data)
            height = int((size.getElementsByTagName('height')[0]).firstChild.data)



            for item in itemlist:
                # get class label
                classid = (item.getElementsByTagName('name')[0]).firstChild.data
                if classid in lut:
                    label_str = str(lut[classid])
                else:
                    continue
                    #label_str = "-1"
                    print("warning: label '%s' not in look-up table" % classid)

                    # get bbox coordinates
                xmin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmin')[0]).firstChild.data
                ymin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymin')[0]).firstChild.data
                xmax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmax')[0]).firstChild.data
                ymax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymax')[0]).firstChild.data
                b = (float(xmin), float(xmax), float(ymin), float(ymax))
                bb = convert_coordinates((width, height), b)
                # print(bb)
                #previously working code
                # print(xmin,ymin)
                # intXmin=int(width)-int(xmin)
                # intXmax=int(width)-int(xmax)
                # newXmin=intXmax
                # newXmax=intXmin




                b = (float(xmin), float(xmax), float(ymin), float(ymax))
                bb = convert_coordinates((width, height), b)


                f.write(label_str + " " + " ".join([("%.6f" % a) for a in bb]) + '\n')

            print("wrote %s" % fname_out)
        #cv2.rectangle(img1, p1=(xmin, ymin), p2=(xmax, ymax), color=(255, 255, 0), thickness=4)
        #cv2.rectangle(img2, (newXmin, ymin), (newXmax, ymax), (255, 255, 0), 2)
        # cv2.imshow('IMAGE',img1)
        # cv2.imshow('FLIP',img2)
        # cv2.waitKey(0)
        # print("original")
        # print(xmin,ymin)
        # print(xmax,ymax)
        #
        # print("flip")
        # print(newXmin,ymin)
        # print(newXmax,ymax)


if __name__ == '__main__':
    convert_xml2yolo(lut)