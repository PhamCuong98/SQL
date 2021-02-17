import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ngoccuong1812",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM bienso WHERE time = '12h'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")