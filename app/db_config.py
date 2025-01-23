import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS usd_exchange")
cursor.execute("USE usd_exchange")