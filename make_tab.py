import mysql.connector

mydb= mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "Ngoccuong1812",
    database= "mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS bienso")
sql ='''CREATE TABLE bienso(
   time CHAR(20) NOT NULL,
   soxe CHAR(20)
)'''
mycursor.execute(sql)

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)