import tkinter
from tkinter import *
import cv2
#import base64
#import numpy as np
#import os
#import webbrowser
#import codecs
  
# open html file
#webbrowser.open("C:\\SMK\\DA\\Python\\Image process\\imagevenv\\upload.html") 

#fileitem = form['filename']
 
# check if the file has been uploaded
#if fileitem.filename:
    # strip the leading path from the file name
 #   fn = os.path.basename(fileitem.filename)
     
   # open read and write the file into the server
 #   open(fn, 'wb').write(fileitem.file.read())

main = Tk()


ourMessage ='Welcome to PhotoEditor'
messageVar = Message(main, text = ourMessage)
messageVar.config(bg='gold')
messageVar.pack()


class Image:
    def __init__(self,img=0,img_scl=0,gi=0):
        self.img = cv2.imread("C:\\SMK\\DA\\Python\\Image process\\pics\\gok.jpg", cv2.IMREAD_COLOR)
        #self.img_scl = img_scl
        #self.gi = gi

    def view(self):
        scl = cv2.resize(self.img, (800, 640), interpolation = cv2.INTER_AREA)
        #self.img_scl= cv2.imread(, cv2.IMREAD_COLOR)
        #self.img_scl = base64.b64encode(scl.read())
        cv2.imshow('image',scl)
        img_scl = cv2.imwrite('C:\\SMK\\DA\\Python\\Image process\\pics\\resize.jpg', scl )
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        #return img_scl
         
    def grey(self):
        sel = cv2.imread('C:\\SMK\\DA\\Python\\Image process\\pics\\resize.jpg', cv2.IMREAD_COLOR)
        gi = cv2.cvtColor(sel, cv2.COLOR_RGB2GRAY)
        #cv2.imread(self.gi)
        cv2.imshow('Grayscale', gi)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()
        #return self.gi

    def gblur(self):
        gblr=cv2.imread('C:\\SMK\\DA\\Python\\Image process\\pics\\resize.jpg',cv2.IMREAD_COLOR)
        Gaussian = cv2.GaussianBlur(gblr, (7, 7), 0)
        cv2.imshow('Gaussian Blurring', Gaussian)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def mblur(self):
        mblr=cv2.imread('C:\\SMK\\DA\\Python\\Image process\\pics\\resize.jpg',cv2.IMREAD_COLOR)
        median = cv2.medianBlur(mblr, 5)
        cv2.imshow('Median Blurring', median)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def bblur(self):
        bblr=cv2.imread('C:\\SMK\\DA\\Python\\Image process\\pics\\resize.jpg',cv2.IMREAD_COLOR)
        bilateral = cv2.bilateralFilter(bblr, 9, 75, 75)
        cv2.imshow('Bilateral Blurring', bilateral)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def hsv(self):
        hhsv=cv2.imread('C:\\SMK\\DA\\Python\\Image process\\pics\\resize.jpg',cv2.IMREAD_COLOR)
        hhvv = cv2.cvtColor(hhsv, cv2.COLOR_BGR2HSV)
        cv2.imshow('HSV', hhvv) 
        cv2.waitKey(0)  
        cv2.destroyAllWindows()

    def edge(self):
        sob = cv2.imread('C:\\SMK\\DA\\Python\\Image process\\pics\\mscl.jpg',cv2.IMREAD_COLOR)
        sobelx = cv2.Sobel(src=sob, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
        sobely = cv2.Sobel(src=sob, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
        sobelxy = cv2.Sobel(src=sob, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
        cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def can(self):
        sobe = cv2.imread('C:\\SMK\\DA\\Python\\Image process\\pics\\mscl.jpg',cv2.IMREAD_COLOR)
        edges = cv2.Canny(image=sobe, threshold1=100, threshold2=200)
        cv2.imshow('Canny Edge Detection', edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        


#path='C:\\SMK\\DA\\Python\\Image process\\pics'
mblr =cv2.imread('C:\\SMK\\DA\\Python\\Image process\\pics\\resize.jpg',cv2.IMREAD_COLOR)
median = cv2.medianBlur(mblr, 5)
#Gaussian = cv2.GaussianBlur(gblr, (7, 7), 0)
m_scl = cv2.imwrite('C:\\SMK\\DA\\Python\\Image process\\pics\\mscl.jpg', median )


a=Image()

frame = Frame(main)
frame.pack()

orgbutton = Button(frame, text = 'Original Photo', fg ='brown',command=a.view)
orgbutton.pack( side =  LEFT)

graybutton = Button(frame, text = 'Gray Scale', fg ='gray',command=a.grey)
graybutton.pack( side = LEFT)

redbutton = Button(frame, text = 'Gaussian Blur', fg='red',command=a.gblur)
redbutton.pack( side = LEFT )

bluebutton = Button(frame, text ='Median Blur', fg ='blue',command=a.mblur)
bluebutton.pack( side = LEFT )

blackbutton = Button(frame, text ='Bilateral Blur', fg ='black',command=a.bblur)
blackbutton.pack( side = LEFT)

orangebutton = Button(frame, text ='HSV color', fg ='orange',command=a.hsv)
orangebutton.pack( side = LEFT)

edgebutton = Button(frame, text ='Edge', fg ='green',command=a.edge)
edgebutton.pack( side = LEFT)

canbutton = Button(frame, text ='Canny', fg ='purple',command=a.can)
canbutton.pack( side = BOTTOM)


main.mainloop()