import cv2
import numpy as np

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
## Drawing and writing on image using cv2
##cv2.line(img,(0,0),(150,150),(255,255,255), 15)
##
##cv2.rectangle(img, (15,25),(200,150),(0,255,0), 5)
##cv2.circle(img,(100,63),55,(0,0,255),-1)
##
##pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
##cv2.polylines(img,[pts],True,(0,255,255),3)
##
##font = cv2.FONT_HERSHEY_SIMPLEX
##cv2.putText(img,'OpenCV Tuts!',(0,130),font,1,(200,255,255),2,cv2.LINE_AA)
##
##
##cv2.imshow('image',imgj)

##getting a pixel and pixel=white to make it white
##px = img[55,55]=[255,355,255]
##px=img[55,55]

##shifting a region
watch_face = img[37:111,107:194]

img[0:74,0:87]=watch_face

cv2.imshow('image',img)

