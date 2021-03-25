import mysql.connector

mydb= mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "ngoccuong1812",
    database= "mydatabase"
)
myresult= []
mycursor = mydb.cursor()

sql = "SELECT * FROM bienso WHERE soxe ='5 1 G 5 1 9 3 '"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
print(".....")
sql2= "SELECT * FROM bienso WHERE time LIKE '%h%'"
mycursor.execute(sql2)

myresult2 = mycursor.fetchall()

for y in myresult2:
  print(y)