import pymysql
con=pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="sneha123",
    database="diksha"
    
)

# print("connected")
cursor=con.cursor()
# cursor.execute("create database diksha")
# qury="create table student(id int primary key,name varchar(100),email varchar(100))"
# cursor.execute(qury)
# print("connected")

# qury="insert into student values(1,'sneha','sneha@gmail.com')"
# qury="insert into student values(%s,%s,%s)"
# val=(3,"dishu","dishu@gmail.com")
# cursor.execute(qury,val)
# con.commit()
# print("data insert sucessfully")





