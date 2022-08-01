from PyQt5 import QtWidgets
from PyQt5 import QtWidgets, QtGui
import sys
import cv2 as cv
import cv2
import numpy as np
import math
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(200,200,500,500)
        self.setWindowTitle("Meter")
        self.setWindowIcon(QtGui.QIcon("F:/0.png"))
        self.VBL = QVBoxLayout()
        


        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)
        self.FeedLabel2 = QLabel()
        self.VBL.addWidget(self.FeedLabel2)

        self.CancelBTN = QPushButton("Cancel")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)
        self.Worker1 = Worker1()
        self.Worker2 = Worker2()

        self.Worker1.start()
        self.Worker2.start()

        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.Worker2.ImageUpdate.connect(self.ImageUpdateSlot1)
        self.setLayout(self.VBL)

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))
    def ImageUpdateSlot1(self, Image):
        self.FeedLabel2.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.Worker1.stop()
        self.Worker2.stop()
        sys.exit()

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()
class Worker2(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())