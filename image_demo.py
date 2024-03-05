import mysql.connector
import os
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="image_demo"
)

cursor = db.cursor()

# cursor.execute("CREATE TABLE images (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), data LONGBLOB)")
# with open("abc.png", "rb") as image_file:
#     image_data = image_file.read()

# cursor.execute("INSERT INTO images (name, data) VALUES (%s, %s)", ("image1.png", image_data))
# db.commit()
# id = 1
# cursor.execute("SELECT name,data FROM images WHERE id = '{}'".format(id))
cursor.execute("SELECT * FROM images WHERE 1=1")
result = cursor.fetchall()
# print(type(result[0]))
# print(len(result))
# print((result[0][0]))
# print((result[0][1]))
for i in list(result):
    # print("testing...")
    with open("./known/"+str(i[0])+".jpg", "wb") as image_file:
        image_file.write(i[2])
    # for id,name,img in list(i):
    #     print(id,name)
# print(result[0])
# with open("./del/axy.jpg", "wb") as image_file:
#     image_file.write(result[1])



# for i in range(10):
#     with open(str(i)+".jpg", "wb") as image_file:
#         image_file.write(result[1])