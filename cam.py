import cv2
import numpy as np
import tensorflow as tf
import sys
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk,Image

root = Tk()

root.title(' Industrial Meter ')

root.geometry('900x300+100+0')
Label(root,text="Picture",font=('Times New Roman', '35', 'bold'),fg='blue').pack()
f1=LabelFrame(root,bg='blue')
f1.pack()
L1=Label(root,bg='blue')
L1.pack()

f2=LabelFrame(root,bg='blue')
f2.pack()
L2=Label(root,bg='blue')
L2.pack()
cap=cv2.VideoCapture(0)
cap2=cv2.VideoCapture('F:/Basket Ball Analysis/raw2.mp4')
#root.mainloop()
try:
    
    while True:
        ret,img=cap.read()
        resize = cv2.resize(image, (640, 480))
        re,im=cap2.read()
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img=ImageTk.PhotoImage(Image.fromarray(img))
        
        im=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
        im=ImageTk.PhotoImage(Image.fromarray(im))
        L1['image']=img
        L2['image']=im
        root.update()
except:
    pass