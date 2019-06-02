# -*- coding: utf-8 -*-
"""
Created on Fri May 31 23:55:15 2019

@author: Sumit Kumar Singh
"""

import cv2

#colored image


# Create a CascadeClassifier Object
# face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_cascade = cv2.CascadeClassifier('C:\\Users\\USER\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

img = cv2.imread("C:\\Users\\USER\\Pictures\\Aquaman\\Amber1.jpg",1)

# Reading the image as gray scale image
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 

# Search the co-ordintes of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.3, minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),30)
 
resized = cv2.resize(img, (int(img.shape[1]/7),int(img.shape[0]/7)))
cv2.imshow("Gray", resized)
 
cv2.waitKey(0)
 
cv2.destroyAllWindows()
