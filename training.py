from unicodedata import name
import cv2
import face_recognition as FR
import os
import pickle as pk
import mysql.connector
font=cv2.FONT_HERSHEY_SIMPLEX

def insert_known():
    # connecting to database
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="image_demo"
    )
    # making object of database and fetching the data
    cursor = db.cursor()
    cursor.execute("SELECT * FROM images WHERE 1=1")
    result = cursor.fetchall()
    # pasting data in known folder
    for i in list(result):
        with open("./known/"+str(i[0])+".jpg", "wb") as image_file:
            image_file.write(i[2])

# insert_known()

imgDirs = ('./known')
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
        nm1 = nm1.strip('.png')
        names.append(nm1)
with open('train.pkl','wb') as f:
    pk.dump(names,f)
    pk.dump(knownEncodings,f)










