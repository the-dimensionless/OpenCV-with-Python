# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 21:39:18 2019

@author: Sumit Kumar Singh
"""

import cv2, time

video = cv2.VideoCapture(0)

frame_width = int(video.get(3))
frame_height = int(video.get(4))


a = 1
fourcc = cv2.VideoWriter_fourcc('M','P','E','G')
out = cv2.VideoWriter('Output.avi',fourcc,10.0,(frame_width,frame_height))

while True:
    a = a+1
    check,frame = video.read()
    
    if check == True:
            #print(frame)
            out.write(frame)
            
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            out.write(gray)
            
            cv2.imshow('Capturing',gray)
            
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
    else:
        break
    

print(a)
video.release()
out.release()
cv2.destroyAllWindows