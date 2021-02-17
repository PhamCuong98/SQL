import mysql.connector

mydb= mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "Ngoccuong1812",
    database= "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM bienso")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.execute("SELECT time FROM bienso")

myresult2 = mycursor.fetchall()

for y in myresult2:
  print(y)
print(myresult2)