import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ngoccuong1812",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE bienso SET time = '1h' WHERE time = '12h'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")