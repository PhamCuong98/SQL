import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ngoccuong1812",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS realtime"
mycursor.execute(sql)
sql = "DROP TABLE IF EXISTS data"

mycursor.execute(sql)