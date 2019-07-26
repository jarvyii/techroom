import sqlite3
from sqlite3 import Error



def CreateDB():
    db_file="techromm1"
    mydb = sqlite3.connect('techroom.db')
    mycursor = mydb.cursor()
    #mycursor.execute("CREATE DATABASE techromm1")
    sql ="CREATE TABLE IF NOT EXISTS status ( \
                 idstatus INTEGER      NOT NULL PRIMARY KEY AUTOINCREMENT, \
                 `status` VARCHAR(15) NULL)"
    mycursor.execute(sql)
   #sql = "INSERT INTO status (idstatus, status) VALUES (?,?)"
   #val =[ (3, 'Hold'), (3, 'Hold'), (1, 'BER'), (2, 'Completed')];
  # mycursor.execute(sql, val)

    mydb.commit()
