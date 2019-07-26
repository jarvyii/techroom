import os
import sqlite3
from sqlite3 import Error
# from fibo import *  This is to use function from others .py files


def CheckUser(conn, nameUser, passUser):
   curs = conn.cursor()
   sql = "SELECT * FROM users where  username = ? and password=?"
   val = (nameUser, passUser)
   curs.execute(sql, (nameUser, passUser))
   User = curs. fetchall()

   if not User:
       print("Wrong username or password.")
       return 0
   else:
       return User


def Login(conn):
    Chance = 1
    User = []
    while (Chance <=3) and not User:
        os.system('cls')
        print("\n\n\n Please enter your User information: \n\n")
        nameUser = input("Enter your user Name: ")
        passUser = input("Enter password: ")
        User = CheckUser(conn, nameUser, passUser)
        Chance += 1
    if not User:
        return 0
    else:
        return User
##
