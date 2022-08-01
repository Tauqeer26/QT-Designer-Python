

import cv2
import cv2 as cv
import numpy as np
import math
 #image_path
def ROI_Selection_4():
    cap= cv2.VideoCapture(0)
    #select ROIs function

    _1,frame=cap.read()
    ROIs = cv2.selectROIs("Select Rois",frame,False)
    global point,circ
    #print rectangle points of selected roi
    #Crop selected roi ffrom raw image
    #counter to save image with different name
    backSub=[]
    for localcount in enumerate(ROIs):
        backSub.append(cv.bgsegm.createBackgroundSubtractorMOG())

    def mousePoints(event,x,y,flags,params):
            global point,circ
            if event == cv2.EVENT_LBUTTONDOWN:
                point=(x,y)
                print(point)
            if event ==cv2.EVENT_RBUTTONDOWN:
                circ=(x,y)
                print(circ)

    point=(0,0) 
    circ=(-1,0)
    import copy
    while True:
        _1,frame=cap.read()

        if _1:
            crop_number=0
            crop_roi=0
            for roicount,rect in enumerate(ROIs):
                framea=copy.deepcopy(frame)
                x1=rect[0]
                y1=rect[1]
                x2=rect[2]
                y2=rect[3]

                    #crop roi from original image
                ROI=framea[y1:y1+y2,x1:x1+x2]
                cv2.circle(ROI,(circ[0],circ[1]),55,(0,0,0),cv2.FILLED)

                kernel=np.ones((5,5),np.float32)/15 #np.ones((5,5),np.float32)/15
                print("ROI=",ROI.shape)
                #kernel =np.arange(16).reshape(4,4)/5
                b_frame=cv2.filter2D(ROI,-1,kernel)
                #b1_frame=cv2.filter2D(b_frame,-1,kernel)
                #fgMask = fgbg.apply(b_frame)

                fgMask = backSub[roicount].apply(b_frame)
                print("fgmask=",fgMask.shape)
                thresh = cv2.threshold(fgMask,180,25,cv2.THRESH_BINARY)[1]
                contours,hierachy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                for cnt in contours:
                    area=cv2.contourArea(cnt)
                    (x,y,w,h) = cv2.boundingRect(cnt)


                    if w*h > 1100:

                        rec=cv2.minAreaRect(cnt)
                        #print(rect)
                        c = max(contours, key = cv2.contourArea)
                        #M=cv2.moments(cnt)
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

                        box=cv2.boxPoints(rec)
                        box=np.int0(box)

                        p=math.degrees(per)
                        cv2.putText(ROI,str(int(p)),(point[0]+20,point[1]+25),cv2.FONT_HERSHEY_COMPLEX,0.7,(23,0,255),2)

                        cv2.drawContours(ROI,[c],-1,(0,255,0),3)
                        #cv2.imshow('Imm',ROI)

                    #show cropped image
                cv2.imshow("crop"+str(crop_number),ROI)
                #cv2.imshow('frame',frame)
                cv2.imshow("crop1"+str(crop_roi), fgMask)
                #cv2.setMouseCallback('frame',mousePoints)
             #save cropped image
                cv2.setMouseCallback("crop"+str(crop_number),mousePoints)
             #save cropped image
                #cv2.imwrite("crop"+str(crop_number)+".jpeg",img_crop)
                crop_number+=1
                crop_roi+=1
        if cv2.waitKey(1) & 0xFF == ord('q'):      #to break the loop and terminate the program 
                break

    cap.release()
    cv2.destroyAllWindows()