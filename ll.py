import cv2 as cv
import cv2
import numpy as np
import math

backSub = cv.bgsegm.createBackgroundSubtractorMOG() 
cap= cv.VideoCapture('F:/Basket Ball Analysis/basket.wmv')
while True:

    ret, frame = cap.read()
    if frame is None:
        break
        cv2.destroyAllWindows()

    kernel=np.ones((5,5),np.float32)/15 #np.ones((5,5),np.float32)/15
    #kernel =np.arange(16).reshape(4,4)/5
    b_frame=cv2.filter2D(frame,-1,kernel)
    b1_frame=cv2.filter2D(b_frame,-1,kernel)
    #fgMask = fgbg.apply(b_frame)
    fgMask = backSub.apply(frame)
    cv2.rectangle(fgMask,(5,5),(100,100),(0,255,255),2)
    a=cv2.line(frame,(460,190),(540,190),(255,255,0),5)
    thresh = cv2.threshold(fgMask,180,25,cv2.THRESH_BINARY)[1]
    contours,hierachy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame,contours,-1,(0,255,0),3)
    cv2.imshow('Imm',frame)
    cv.imshow('FG Mask', fgMask)
    k = cv.waitKey(1) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()