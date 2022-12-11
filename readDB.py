import sqlite3
import hashlib
conn = sqlite3.connect("userdata.db")
cur  = conn.cursor()
res = cur.execute("SELECT * FROM userdata")
# res = cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))
# res.fetchall()
print(res.fetchall())
res.close()