import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ngoccuong1812",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM bienso WHERE soxe = '5 1 G 5 1 9 3 6'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")