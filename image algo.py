import cv2
import numpy as np

img1=cv2.imread('3D-Matplotlib.png')
##img2=cv2.imread('mainsvmimage.png')
##add images and show both
##add = img1+img2
##
#### add pixel value (b,g,r)+(b,g,r)
##add = cv2.add(img1,img2)
##weighted adding  60% of img1 and 40 of img 2  ,gamma value =0
##weigh = cv2.addWeighted (img1,0.6,img2,0.4,0)
##cv2.imshow('weigh',weigh)
##bg remove and add to img1
img2=cv2.imread('mainlogo.png')

rows,cols,channels=img2.shape

roi = img1[0:rows,0:cols]##region of image size from img2
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)##graying image
ret,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)

##cv2.imshow('mask',mask)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)

dst = cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols]=dst
cv2.imshow('res',img1)



