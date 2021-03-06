import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([36,0,0])
    upper_green = np.array([86,255,255])
    
    
    mask = cv2.inRange(hsv,lower_green,upper_green)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    ##median = cv2.medianBlur(mask,15)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
   ##cv2.imshow('median',median )
    k=cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
