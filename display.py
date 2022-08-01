
import cv2 as cv
import numpy
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets



def onClick():
    cap=cv.VideoCapture('F:/Basket Ball Analysis/raw2.mp4')
    while True:
        ret,frame=cap.read()
        if ret==True: 
            displayImage(frame,1)
              #cv.imshow("Capturing", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
def onClick_1():
    img=cv.imread('F:/0.png')
    displayImage(img,window=1)
    cv.destroyAllWindows()


def displayImage(img,window=1):
	qformat=QImage.Format_Indexed8
	if len(img.shape)==3:
		if (img.shape[2])==4:
			qformat=QImage.Format_RGBA888

		else:
			qformat=QImage.Format_RGB888

	img=QImage(img,img.shape[1],img.shape[0],qformat)
	img=img.rgbSwapped()
	imgLabel = QLabel()
	imgLabel.setPixmap(QPixmap.fromImage(img))
	imgLabel.setAlignment(QtCore.Qt.AlignHCenter |QtCore.Qt.AlignVCenter )	
		
        

		

    






