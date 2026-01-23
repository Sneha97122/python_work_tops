import mysql.connector

con= mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="sneha123"
    
)
print("conncected")
cursor=con.cursor()


