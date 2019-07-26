import os
import sqlite3
from database import *
from login import *
from sqlite3 import Error
from modeltechroom import *
 #This is to use function from login.py files
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        print(conn)
        return conn
    except Error as e:
        print(e)

    return None

#To create the connection with SQLite.
#DataBase db/techroom.db
def connectDB():
    database = "db/techroom.db"
    # create a database connection

    conn = create_connection(database)
    if not conn:
       CreateDB()
    curs = conn.cursor()
    #curs.execute("SELECT * FROM status order by idstatus")
    #rows = curs.fetchall()
    #for row in rows:
    #    print(row)
    return conn


##
def Menu():
    Option = '9'
    while (Option not in ('1','2','3','4','5','0')):
          os.system('cls')
          print("\n\nOption Menu\n")
          print("1 - Add new Equipment")
          print("2 - Modify Equipment")
          print("3 - Delete Equipment")
          print("4 - See your Daily Production")
          print("5 - Show your Work")
          print("0 - Quit")
          Option = input("\nPlease select your Option: ")
    return Option

conn = connectDB()
User = Login(conn)
os.system('cls')
if User == 0:
   quit()
flag = True
while flag != '0':
      flag = Menu()
      os.system('cls')
      if flag == '1':
          AddEquipment(conn, User)
      elif flag == '2':
         ModifyEquipment(conn, User)
      elif flag == '3':
        DeleteEquipment(conn, User)
      elif flag == '4':
          GraphInfo(conn, User)
      elif flag == '5':
         ShowWork(conn, User)
