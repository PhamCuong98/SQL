import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ngoccuong1812",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE realtime (time VARCHAR(255), day VARCHAR(255), number VARCHAR(255), ID VARCHAR(255))")
mycursor.execute("CREATE TABLE data (time VARCHAR(255), day VARCHAR(255), number VARCHAR(255), status VARCHAR(255), ID VARCHAR(255))")