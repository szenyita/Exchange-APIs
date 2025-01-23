import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)

print(conn)