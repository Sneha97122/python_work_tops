from tkinter import *
import pymysql

con=pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="sneha123",
    database="diksha"
)

cursor=con.cursor()

