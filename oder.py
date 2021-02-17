import mysql.connector

mydb= mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "Ngoccuong1812",
    database= "mydatabase"
)
mycursor = mydb.cursor()
# Xep tu A-Z
sql = "SELECT * FROM bienso ORDER BY time"
# Xep tu Z-A
#sql = "SELECT * FROM bienso ORDER BY time DESC"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)