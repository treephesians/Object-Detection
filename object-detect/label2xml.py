from ast import arg
from encodings import utf_8
from textwrap import indent
from tokenize import group
from xml.dom import minidom
import os
import time
from datetime import datetime

from os import listdir
import natsort
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import SubElement, ElementTree, dump
from labelingTemplateXml import indent
import pandas as pd
#import openpyxl 
import numpy as np

import argparse
import glob


if __name__ == '__main__':
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--worker', type=str, help='작업자 이름')
    #parser.add_argument('--imgSize', type=str, help='이미지 사이즈 규격')
    #parser.add_argument('--folder_name', type=str, help='폴더 이름')
    #opt = parser.parse_args()    
    
    dt_now = datetime.now()

    #class, x1, y1, x2, y2,  
    # coding isCrowd,date
    #auto increase //last +1 ==  index,
    # each insert worker,  imgsize
    #data path

    #입력값 받아서 태그에 저장하기

    # path_dir = './rifle/train/'
    # print('./server/server_datasets/')
    # dir_list = os.listdir('./server/server_datasets')

    # #load label data
    # print(dir_list[1])
    # file_list = os.listdir("./server/server_datasets/"+ dir_list[1]+"/")
    datasets_path = f'./data/thermal-human/fail/labels/'
    print(datasets_path)
    file_list = os.listdir(datasets_path)

    #load label data
    #print(dir_list)
    #file_list = os.listdir(f"{datasets_path}{dir_list[1]}")
    fpath = natsort.natsorted(file_list)
    # print(file_list)
    #print(file_list[0]) : get each patient's first .dcm file
    print(fpath)

    for i in range(len(file_list)):

        #txt in split at " " & print for array
        print("-------------------")
        file_name = os.path.splitext(fpath[i])
        print(file_name)
        # fr = open('./server/server_datasets'+ "/" + dir_list[1] + "/" + fpath[i], "r")
        fr = open(f"{datasets_path}/{fpath[i]}", "r")
        # print(fr)
        fsplit=[x.split() for x in fr]
        
        # Create each xml 
        datasets = ET.Element("datasets")
        header = ET.SubElement(datasets, "header")
        imgInfo = ET.SubElement(datasets, "imgInfo")
        ######################################################
        ET.SubElement(header, "nc").text = fsplit[0][0]
        ET.SubElement(header, "date").text = dt_now.strftime('%y%m%d %H%M')
        ET.SubElement(header, "worker").text = "JB"
        ######################################################
        ET.SubElement(imgInfo, "index").text = str(i+1)
        # detect.py 에서 imgsz 를 가져오면 됨.
        ET.SubElement(imgInfo, "imgSize").text = str(640)

        label = ET.SubElement(imgInfo, "label")

        for j in range(len(fsplit)):
            #points realted
            points = ET.SubElement(label, "points")
            ET.SubElement(points, "x1").text = fsplit[j][1]
            ET.SubElement(points, "y1").text = fsplit[j][2]
            ET.SubElement(points, "x2").text = fsplit[j][3]
            ET.SubElement(points, "y2").text = fsplit[j][4]

        ET.SubElement(imgInfo, "isCrowd").text = str(len(fsplit))
        date = dt_now.strftime('%y%m%d %H%M')
        print(date)

        indent(datasets)
        print(indent(datasets))
        
        tree = ET.ElementTree(datasets)
        
        new_dir_path = "./server/" + dt_now.strftime('%y%m%d %H%M')
        
        os.makedirs(new_dir_path, exist_ok=True)
        
        if not os.path.exists(new_dir_path):
            os.makedirs(new_dir_path)

        tempFile =  new_dir_path + "/" + file_name[0] + ".xml"
        #print(tempFile)
        tree.write(tempFile, encoding="UTF-8", xml_declaration=True) # taking time about 4 seconds(29 xml files)=> 1285 : about 20 mins
