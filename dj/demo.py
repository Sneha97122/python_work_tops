import pymysql
con=pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="sneha123"
)

print("connected")
cursor=con.cursor()