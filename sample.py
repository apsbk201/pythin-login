#!/usr/bin/python3
import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
    )
""")

#username1, password1 = "first", hashlib.sha256("firstpassword".encode()).hexdigest()
#username2, password2 = "second", hashlib.sha256("Song2".encode()).hexdigest()
#username3, password3 = "sam3", hashlib.sha256("three".encode()).hexdigest()
#username4, password4 = "admin", hashlib.sha256("password".encode()).hexdigest()
#
#cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username1, password1))
#cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username2, password2))
#cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username3, password3))
#cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username4, password4))
#
#conn.commit()
