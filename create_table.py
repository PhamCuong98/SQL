import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ngoccuong1812",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE bienso (time VARCHAR(255), day VARCHAR(255), soxe VARCHAR(255))")