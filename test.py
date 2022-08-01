
from PyQt5 import QtCore, QtGui, QtWidgets
import roi
import sys
import cv2 as cv
import cv2
import numpy as np
import math
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def __init__(self):
        
        
        super().__init__()

    #a=ROI_Selection_2(self)
    
    
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon("F:/l.jpeg"))
        MainWindow.resize(550, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
       
  
        # adding image to label
        #MainWindow.lab.setPixmap(self.pixmap)
  
        # Optional, resize label to image size
        
       




        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 160, 101, 101))

        self.pushButton.clicked.connect(roi.ROI_Selection)
        self.pushButton.setObjectName("pushButton")

        

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 160, 101, 101))
        self.pushButton_2.clicked.connect(roi.ROI_Selection_2)
        self.pushButton_2.setObjectName("pushButton_2")




        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 160, 101, 101))
        self.pushButton_3.clicked.connect(roi.ROI_Selection_3)
        self.pushButton_3.setObjectName("pushButton_3")



        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 50, 361, 61))
        self.label.setObjectName("label")

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(10, 100, 261, 115))
        self.label_1.setObjectName("label_1")



        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(70, 270, 104, 71))
        self.file=open("C:/address.txt","r")
        self.myf=self.file.read() 
        #self.textEdit.setPlainText()
        #for self.line in self.file:

            #self.textEdit.setPlainText(self.line)
          
        #self.ff=self.file.seek(0,0) 
            
        #self.file.truncate()

        self.textEdit.setObjectName("textEdit")


        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(190, 270, 104, 71))
        self.textEdit_2.setObjectName("textEdit_2")
        #b=roi.ROI_Selection_2()
        #self.textEdit_2.setPlainText()


        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(320, 270, 104, 71))
        #c=roi.ROI_Selection_3()
        #self.textEdit_3.setPlainText()
        self.textEdit_3.setObjectName("textEdit_3")


        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 450, 101, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.clicked_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 450, 101, 71))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(roi.ROI_Dynamic)
        #MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 614, 21))
        self.menubar.setObjectName("menubar")


        self.menufILE = QtWidgets.QMenu(self.menubar)
        self.menufILE.setObjectName("menufILE")
        MainWindow.setMenuBar(self.menubar)


        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menufILE.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Meter#1"))
        self.pushButton_2.setText(_translate("MainWindow", "Meter#2"))
        self.pushButton_3.setText(_translate("MainWindow", "Meter#3"))
        self.label.setText(_translate("MainWindow", "INDUSTRIAL CV_METER"))
        self.label.setFont(QFont('Arial', 20))
        self.label.move(100,100)
        self.pixmap = QPixmap("F:/sh.jpeg")
        self.label_1.setPixmap(self.pixmap)
        self.label_1.move(150,0)
        self.pushButton_4.setText(_translate("MainWindow", "QUIT"))
        self.pushButton_5.setText(_translate("MainWindow", "Start_Feed"))
        self.menufILE.setTitle(_translate("MainWindow", "File"))
    def clicked_2(self):
        #self.label.setText("You pressed a button")
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    #print(roi.ROI_Selection())
    #print(roi.ROI_Selection_2())
    #print(roi.ROI_Selection_3())
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
