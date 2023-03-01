from unicodedata import name
import cv2
import face_recognition as FR
import os
import pickle as pk
font=cv2.FONT_HERSHEY_SIMPLEX

import os 


imgDirs = ('/home/shary/Desktop/AI/paul/face/project/known')
names = []
knownEncodings = []
for root,dirs,filesz in os.walk(imgDirs):
    for nm in filesz:
        objFace=FR.load_image_file(os.path.join(root,nm))
        faceLoc=FR.face_locations(objFace)
        objEncoded = FR.face_encodings(objFace,faceLoc)
        objEncoded = objEncoded[0]
        knownEncodings.append(objEncoded)
        nm1 = nm.strip('.jpg')
        names.append(nm1)
with open('train.pkl','wb') as f:
    pk.dump(names,f)
    pk.dump(knownEncodings,f)