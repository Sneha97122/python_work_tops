import sqlite3

conn=sqlite3.connect("test.db")
cur=conn.cursor()

cur.execute("create table student(id integer ,name varchar(50))")
conn.commit()
conn.close()