import cv2 
import cv2 as cv
import numpy as np
import math



def ROI_Dynamic():
    global point,circ, point_1,circ_1
    cap= cv2.VideoCapture(0)
    _1,frame=cap.read()
    ROI = cv2.selectROIs("Select Rois",frame,False)
    #counter to save image with different name
    backSub=[]
    a=[]
    for localcount in enumerate(ROI):
        backSub.append(cv.bgsegm.createBackgroundSubtractorMOG())

    def mousePoints(event,x,y,flags,params):
            global point,circ
            if event == cv2.EVENT_LBUTTONDOWN:
                point=(x,y)
                print(point)
            if event ==cv2.EVENT_RBUTTONDOWN:
                circ=(x,y)
                print(circ)
    def mouseP(event,z,v,flags,params):
            global point_1,circ_1
            if event == cv2.EVENT_LBUTTONDOWN:
                point_1=(z,v)
                print(point_1)
            if event ==cv2.EVENT_RBUTTONDOWN:
                circ_1=(z,v)
                print(circ_1)

    point=(0,0) 
    circ=(-1,0)
    point_1=(0,0) 
    circ_1=(-1,0)
    #select ROIs function
    while True:
        o=0
        for i,m in enumerate(ROI):


            _1,frame=cap.read()
            a=crop_it(frame,ROI)
            #ii=funcc_1()
            #yy=funcc()
            cv2.circle(a[0],(circ[0],circ[1]),55,(0,0,0),cv2.FILLED)

            kernel=np.ones((5,5),np.float32)/15 #np.ones((5,5),np.float32)/15
            #print("ROI=",ROI.shape)
            #kernel =np.arange(16).reshape(4,4)/5
            b_frame=cv2.filter2D(a[0],-1,kernel)
            #b1_frame=cv2.filter2D(b_frame,-1,kernel)
            #fgMask = fgbg.apply(b_frame)

            fgMask = backSub[0].apply(b_frame)
            #print("fgmask=",fgMask.shape)
            thresh = cv2.threshold(fgMask,180,25,cv2.THRESH_BINARY)[1]
            contours,hierachy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            #cv2.imshow('nice',a[i])
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

                    cv2.circle(a[0], (cX,cY), 9, (255,0,255), -1)
                    #cv2.circle(frame,(500,350),230,(23,255,255),3)
                    cv2.circle(a[0], (point[0],point[1]), 9, (255,0,255), -1)    
                    diffx=cX-point[0]
                    diffy=cY-point[1]
                    per=math.atan2(diffy,diffx)

                    box=cv2.boxPoints(rec)
                    box=np.int0(box)

                    p=math.degrees(per)
                    cv2.putText(a[0],str(int(p)),(point[0]+20,point[1]+25),cv2.FONT_HERSHEY_COMPLEX,0.7,(23,0,255),2)

                    cv2.drawContours(a[0],[c],-1,(0,255,0),3)


                    ##########################2nd ROI######################################

            cv2.circle(a[1],(circ_1[0],circ_1[1]),55,(0,0,0),cv2.FILLED)

            kernel_1=np.ones((5,5),np.float32)/15 #np.ones((5,5),np.float32)/15
            #print("ROI=",ROI.shape)
            #kernel =np.arange(16).reshape(4,4)/5
            b_frame_1=cv2.filter2D(a[1],-1,kernel_1)
            #b1_frame=cv2.filter2D(b_frame,-1,kernel)
            #fgMask = fgbg.apply(b_frame)

            fgMask_1 = backSub[1].apply(b_frame_1)
            #print("fgmask=",fgMask.shape)
            thresh_1 = cv2.threshold(fgMask_1,180,25,cv2.THRESH_BINARY)[1]
            contours_1,hierachy_1=cv2.findContours(thresh_1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            #cv2.imshow('nice',a[i])
            for cnt_1 in contours_1:

                area_1=cv2.contourArea(cnt_1)
                (z,v,f,g) = cv2.boundingRect(cnt_1)


                if f*g > 1100:

                    rec_1=cv2.minAreaRect(cnt_1)
                    #print(rect)
                    c_1 = max(contours_1, key = cv2.contourArea)
                    #M=cv2.moments(cnt)
                    M_1 = cv2.moments(c_1)
                    #print(M)
                    cX_1 = int(M_1["m10"] / M_1["m00"])
                    cY_1 = int(M_1["m01"] / M_1["m00"])
                    #print(cX,cY)

                    cv2.circle(a[1], (cX_1,cY_1), 9, (255,0,255), -1)
                    #cv2.circle(frame,(500,350),230,(23,255,255),3)
                    cv2.circle(a[1], (point_1[0],point_1[1]), 9, (255,0,255), -1)    
                    diffx_1=cX_1-point_1[0]
                    diffy_1=cY_1-point_1[1]
                    per_1=math.atan2(diffy_1,diffx_1)

                    box_1=cv2.boxPoints(rec_1)
                    box_1=np.int0(box_1)

                    p_1=math.degrees(per_1)
                    cv2.putText(a[1],str(int(p_1)),(point_1[0]+20,point_1[1]+25),cv2.FONT_HERSHEY_COMPLEX,0.7,(23,0,255),2)

                    cv2.drawContours(a[1],[c_1],-1,(0,255,0),3)
            #it=funcc()
            cv2.imshow('ll',a[0])
            cv2.setMouseCallback('ll',mousePoints)

            cv2.imshow('lll',a[1])
            cv2.setMouseCallback('lll',mouseP)
            #imgstack=stackImages(1.0,[a[0],a[1]])
            #cv2.imshow("Good",imgstack)
            #cv2.setMouseCallback('Good',mousePoints)
            #cv2.setMouseCallback('Good',mouseP)
            o+=1
        if cv2.waitKey(1) & 0xFF == ord('q'):      #to break the loop and terminate the program 
            break

    cap.release()
    cv2.destroyAllWindows()    





def crop_it(frame,ROI):
    crop_number=0
    crop_roi=0
    c=[]
    for roicount,rect in enumerate(ROI):
        x1=rect[0]
        y1=rect[1]
        x2=rect[2]
        y2=rect[3]
        ROI=frame[y1:y1+y2,x1:x1+x2]
        cv2.imwrite("F:/crop6"+str(crop_number)+".jpg",ROI)
        img=cv2.imread("F:/crop6"+str(crop_number)+".jpg")
        c.append(img)
        crop_number+=1
    return c

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def ROI_Selection():
    global point,circ
    backSub = cv.createBackgroundSubtractorMOG2() 

    cap_1= cv.VideoCapture('C:/Users/user/Desktop/AARCSOL/Project Cv_meter-20220713T133154Z-001/Project Cv_meter/C_new.wmv')
    ret1,frame=cap_1.read()
    ret1,img=cap_1.read()
    bbox=cv2.selectROI('Meter_1',img,False)
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
    while True:
        global p
        
        ret1, frame = cap_1.read()
        ret1,img=cap_1.read()
        if img is None:
            break
            cv2.destroyAllWindows()
        height,width=img.shape[:2]
        ROI = img[bbox[1]:bbox[1]+bbox[3], bbox[0]:bbox[0]+bbox[2]]
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
                def returnit():
                    global p
                    file=open("C:/address.txt","a")
                    file.write(str(int(p))+"\n")
                    #file.truncate(1)
                    file.close()    
                    return str(p)
                file=open("C:/Users/user/Desktop/AARCSOL/Project Cv_meter-20220713T133154Z-001/Project Cv_meter/Program/address.txt","a")
                file.write(str(int(p))+"\n")

                #file.truncate(1)
                file.close()
                cv2.putText(ROI,str(int(p)),(point[0]+20,point[1]+25),cv2.FONT_HERSHEY_COMPLEX,0.7,(23,0,255),2)
                
                cv2.drawContours(ROI,[c],-1,(0,255,0),3)
                cv2.namedWindow('Imm')
                cv2.imshow('Imm',ROI)
                
                cv2.setMouseCallback('Imm',mousePoints)
        
        #cv2.namedWindow('Imm')
        cv2.setMouseCallback('Imm',mousePoints)
        if ret1:
            cv.imshow('FG Mask', fgMask)
        k = cv.waitKey(90) & 0xff
        if k == 27:
            break
        
    cap_1.release()
    cv2.destroyAllWindows()
    return p


    

def ROI_Selection_2():
    global point,circ
    backSub = cv.bgsegm.createBackgroundSubtractorMOG() 

    cap= cv.VideoCapture('F:/Project Cv_meter/C_new.wmv')
    ret,frame=cap.read()
    ret,img=cap.read()
    bbox=cv2.selectROI('Meter_2',frame,False)
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
                cv2.namedWindow('Image')
                cv2.imshow('Image',ROI)
                a=mousePoints
                cv2.setMouseCallback('Image',mousePoints)
        
        #cv2.namedWindow('Imm')
        cv2.setMouseCallback('Image',mousePoints)
        if ret:
            cv.imshow('FG_Mask_2', fgMask)
        k = cv.waitKey(90) & 0xff
        if k == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()
    return int(p)


def ROI_Selection_3():
    global point,circ
    backSub = cv.bgsegm.createBackgroundSubtractorMOG() 

    cap= cv.VideoCapture('F:/Project Cv_meter/C_new.wmv')
    ret,frame=cap.read()
    ret,img=cap.read()
    bbox=cv2.selectROI('Meter_3',frame,False)
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
                cv2.imshow('Image_0',ROI)
                a=mousePoints
                cv2.setMouseCallback('Image_0',mousePoints)
        
        #cv2.namedWindow('Imm')
        cv2.setMouseCallback('Image_0',mousePoints)
        if ret:

            cv.imshow('FG_Mask_3', fgMask)
        k = cv.waitKey(90) & 0xff
        if k == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()
    return int(p)

 #image_path
def ROI_Selection_4():
    cap= cv2.VideoCapture(0)
    #select ROIs function
    global p
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
                #framea=copy.deepcopy(frame)
                x1=rect[0]
                y1=rect[1]
                x2=rect[2]
                y2=rect[3]

                

                a=[]  #crop roi from original image
                ROI=frame[y1:y1+y2,x1:x1+x2]
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
                    
                #cv2.imshow("crop"+str(crop_number),ROI)
                #cv2.imshow('frame',frame)
                #cv2.imshow("crop1"+str(crop_roi), fgMask)
                #cv2.imshow("imgStack",imgStack)
                #cv2.setMouseCallback('frame',mousePoints)
             #save cropped image
                #cv2.setMouseCallback("crop"+str(crop_number),mousePoints)
             #save cropped image
                #cv2.imwrite("crop"+str(crop_number)+".jpeg",img_crop)
                crop_number+=1
                crop_roi+=1
            back=[]
            for i in enumerate(ROIs):
                back.append(ROI)
                #print(i)
            imgstack=stackImages(1.2,(back))
            cv2.imshow("Result",imgstack)

            cv2.setMouseCallback("Result",mousePoints)
        if cv2.waitKey(1) & 0xFF == ord('q'):      #to break the loop and terminate the program 
                break

    cap.release()
    cv2.destroyAllWindows()
    return str(p)
