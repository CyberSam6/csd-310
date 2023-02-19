import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="QwEr#45%",
  database="pytest"
)

print(db)
