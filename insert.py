import mysql.connector

mydb= mysql.connector.connect(
    host= "pncproject.tk",
    user= "root",
    password= "ngoccuong1812",
    database= "mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO bienso (time, soxe) VALUES (%s, %s)"
val = ("10h", "92 A 5 1 2 6 8 8")
mycursor.execute(sql, val)

val1 = ("12h", "92 A 1 6 8 4 2 6")
mycursor.execute(sql, val1)

val2 = ("1h", "43 H 3 6 1 8 5 3")
mycursor.execute(sql, val2)

val2 = ("5h", "43 U 6 4 9 8 6 3")
mycursor.execute(sql, val2)
mydb.commit()

print(mycursor.rowcount, "record inserted.")
