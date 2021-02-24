import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ngoccuong1812"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
