#Edge Detector for segmented images
#Obadah Hammoud
import cv2
import numpy as np
import os
import glob

def seg_to_edge(input_folder,output_folder,thickness,select_object,selected_object=16):
  input_files=glob.glob(input_folder+"*")
  for f in range(len(input_files)):
      file=input_files[f]
      name=os.path.basename(os.path.splitext(file)[0])
      img = cv2.imread(file,cv2.IMREAD_GRAYSCALE)
      width=len(img[0])
      height=len(img)
      _img=np.zeros((len(img),len(img[0])))
      for i in range(len(img)-1):
          for j in range(len(img[0])-1):
              if img[i][j]!=img[i+1][j] and (img[i][j]==selected_object or img[i+1][j]==selected_object or not select_object):
                  x=i+1
                  y=j
                  for k in range(max(0,x-thickness),min(height,x+thickness)):
                      for l in range(max(0,y-thickness),min(width,y+thickness)):
                          _img[k][l]=255
              if img[i][j+1]!=img[i][j] and (img[i][j]==selected_object or img[i][j+1]==selected_object or not select_object):
                  x=i
                  y=j+1
                  for k in range(max(0,x-thickness),min(height,x+thickness)):
                      for l in range(max(0,y-thickness),min(width,y+thickness)):
                          _img[k][l]=255
      cv2.imwrite(output_folder+name+".png",_img)

seg_to_edge("input/","output/",3,False)