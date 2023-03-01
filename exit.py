import cv2
import face_recognition as FR
import os 
import pickle as pk
from datetime import datetime
import time
from db import DBhelper
with open('train.pkl','rb') as f:
    names = pk.load(f)
    knownEncodings = pk.load(f)

obj = DBhelper()
def attendance(name):
    
            obj.exit(name)
            # time_now = datetime.now()
            # tStr = time_now.strftime('%H:%M:%S')
            # dStr = time_now.strftime('%d/%m/%Y')
            # f.writelines(f'\n{name},{tStr},{dStr}')
            # time.sleep(1)
font=cv2.FONT_HERSHEY_SIMPLEX

# cam = cv2.VideoCapture('http://192.168.43.183:4747/video')
cam = cv2.VideoCapture(0) # making camera object
while True:
    ignore , frame = cam.read()
    faceLocations=FR.face_locations(frame)
    unknownEncodings=FR.face_encodings(frame,faceLocations)
    for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
        top,right,bottom,left=faceLocation
        cv2.rectangle(frame,(left+10,top-10),(right,bottom),(255,0,0),3)
        name='Unknown Person'
        matches=FR.compare_faces(knownEncodings,unknownEncoding)
        if True in matches:
            matchIndex=matches.index(True)
            name=names[matchIndex]
            attendance(name)

        cv2.putText(frame,name,(left,top),font,.75,(0,0,255),2)
    
    cv2.imshow('My Faces',frame)
    del(frame)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()

