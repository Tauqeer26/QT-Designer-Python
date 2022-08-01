import cv2 as cv
import cv2
import numpy as np
import math

def ROI_Selection():
    backSub = cv.bgsegm.createBackgroundSubtractorMOG() 

    cap= cv.VideoCapture('F:/Project Cv_meter/C_new.wmv')
    ret,frame=cap.read()
    ret,img=cap.read()
    bbox=cv2.selectROI('Tracking',frame,False)
    def mousePoints(event,x,y,flags,params):
        global point,circ
        if event == cv2.EVENT_LBUTTONDOWN:
            point=(x,y)
        if event ==cv2.EVENT_RBUTTONDOWN:
            circ=(x,y)
    point=(0,0) 
    circ=(-1,0)
    while True:
        global p
        
        ret, frame = cap.read()
        ret,img=cap.read()
        if frame is None:
            break
            cv2.destroyAllWindows()
        height,width=frame.shape[:2]
        ROI = frame[bbox[1]:bbox[1]+bbox[3], bbox[0]:bbox[0]+bbox[2]]
        ROI=cv2.circle(ROI,(circ[0],circ[1]),55,(0,0,0),cv2.FILLED)
        kernel=np.ones((5,5),np.float32)/15 #np.ones((5,5),np.float32)/15
        #kernel =np.arange(16).reshape(4,4)/5
        b_frame=cv2.filter2D(ROI,-1,kernel)
        b1_frame=cv2.filter2D(b_frame,-1,kernel)
        #fgMask = fgbg.apply(b_frame)
        fgMask = backSub.apply(b_frame)
        thresh = cv2.threshold(fgMask,180,25,cv2.THRESH_BINARY)[1]
        contours,hierachy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            area=cv2.contourArea(cnt)
            (x,y,w,h) = cv2.boundingRect(cnt)
            
            
            
          
            if w*h > 1100:
               
                rect=cv2.minAreaRect(cnt)
                #print(rect)
                c = max(contours, key = cv2.contourArea)
                M = cv2.moments(c)
                #print(M)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                #print(cX,cY)
                
                cv2.circle(ROI, (cX,cY), 9, (255,0,255), -1)
                #cv2.circle(frame,(500,350),230,(23,255,255),3)
                cv2.circle(ROI, (point[0],point[1]), 9, (255,0,255), -1)    
                diffx=cX-point[0]
                diffy=cY-point[1]
                per=math.atan2(diffy,diffx)

                box=cv2.boxPoints(rect)
                box=np.int0(box)
                
                p=math.degrees(per)
                cv2.putText(ROI,str(int(p)),(point[0]+20,point[1]+25),cv2.FONT_HERSHEY_COMPLEX,0.7,(23,0,255),2)
                
                cv2.drawContours(ROI,[c],-1,(0,255,0),3)
                cv2.imshow('Imm',ROI)
                cv2.setMouseCallback('Imm',mousePoints)
        
        
        
        cv.imshow('FG Mask', fgMask)
        k = cv.waitKey(90) & 0xff
        if k == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()
ROI_Selection()