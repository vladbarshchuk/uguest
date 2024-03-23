import sqlite3
import hashlib
conn = sqlite3.connect('users.db')

c = conn.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS users (
    username text,
    password text,
    EMAIL text
    )
          """)
username1, password1 = "mike", hashlib.sha256("mikepassword".encode()).hexdigest()
username2, password2 = "Cevin", hashlib.sha256("Cevin21".encode()).hexdigest()
c.execute("""INSERT INTO users (username, password) VALUES (?,?)""", (username1, password1))
c.execute("""INSERT INTO users (username, password) VALUES (?,?)""", (username2, password2))
conn.commit()

conn.close()
