import mysql.connector

# establish connection to MySQL
mydb = mysql.connector.connect(
  # host="192.168.1.12",
  host="192.168.173.2",
  user="root",
  password="BimsCS@8A",
  database="testing"
)

# create a cursor object
# mycursor = mydb.cursor()

# # execute SQL command to show all tables
# mycursor.execute("SHOW TABLES")

# # fetch all tables
# tables = mycursor.fetchall()

# # print all tables
# for table in tables:
#   print(table)


# Create a cursor
mycursor = mydb.cursor()

# Execute a SELECT statement to retrieve all rows from the table
mycursor.execute("SELECT * FROM attendance_app_attendance")

# mycursor.execute("""INSERT INTO attendance_app_attendance (id, date, entrance_time, exit_time, total_time, employee_id, status) 
#                                               VALUES (4, '2022-04-21', '14:03:22.111000', '18:13:22.314000', '5hr', 1, 'live');""")
# mycursor.execute("""INSERT INTO attendance_app_attendance 
#                 (id, date, entrance_time, exit_time, total_time, employee_id, status) VALUES (%s, %s, %s, %s, %s, %s, %s)""", 
#                 (5, '2022-04-24', '14:03:22.111000', '18:13:22.314000', '5hr', 1, 'live'))


# Fetch all rows from the cursor
rows = mycursor.fetchall()

# Print the rows
for row in rows:
  print(row)
# mydb.commit()
# mycursor.close()
# mydb.close()