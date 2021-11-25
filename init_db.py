import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="flask"
)

cur = mydb.cursor()

cur.execute("DROP TABLE IF EXISTS posts")
cur.execute("CREATE TABLE posts ( id INT PRIMARY KEY AUTO_INCREMENT, created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, title TEXT NOT NULL, content TEXT NOT NULL )")

cur.execute(
    "INSERT INTO posts (title, content) VALUES (%s, %s)",
    ('First Post', 'Content for the first post')
)

cur.execute(
    "INSERT INTO posts (title, content) VALUES (%s, %s)",
    ('Second Post', 'Content for the second post')
)

mydb.commit()
mydb.close()