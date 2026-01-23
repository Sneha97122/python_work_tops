import sqlite3

conn=sqlite3.connect("test.db")
cur=conn.cursor()

cur.execute("insert into student values(1,'sneha')")
cur.execute("select * from student")

data=cur.fetchall()
print(data)
conn.commit()
conn.close()
