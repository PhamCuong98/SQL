import mysql.connector

mydb= mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "Ngoccuong1812",
    database= "mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM bienso WHERE time ='12h'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

sql2= "SELECT * FROM bienso WHERE time LIKE '%h%'"
mycursor.execute(sql2)

myresult2 = mycursor.fetchall()

for y in myresult2:
  print(y)