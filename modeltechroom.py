import datetime

def AddEquipment(conn, User):
    serial = input("Serial number(Enter to Quit): ")
    if not serial:
        return
    upscode= input("UPS Code: ")
    pack = input("Pack Number: ")
    status = input("Status: ")
    faultcode1 = input("First Fault Code: ")
    partreplace1 = input("First part deplaced: ")
    faultcode2 = input("Second Fault Code: ")
    partreplace2 = input("Second Replaced: ")
    comment = input("Comments: ")
    curs = conn.cursor()
    sql = "INSERT INTO production (iduser, idstatus, serial, upscode, pack,idfaultcode1, idpartreplace1, idfaultcode2, idpartreplace2, comments) values (?,?,?,?,?,?,?,?,?,?) "
    #* FROM users where  username = ? and password=?"
    #val = (User['iduser'], status, serial, upscode, pack, faultcode1, partreplace1, faultcode2, partreplace2, comment)
    curs.execute(sql, (User[0][0], status, serial, upscode, pack, faultcode1, partreplace1, faultcode2, partreplace2, comment))
    conn.commit()
    #User = curs. fetchall()
    if not User:
        print("Wrong username or password.")
        return 0
    else:
        return User

def  ModifyEquipment(conn, User):
     print("Modify Equipment")
     print("********************************")
     serial = input("Serial number(Enter to Quit): ")
     curs = conn.cursor()
     sql ="SELECT * FROM production where serial=? and iduser =? and date=?"
     toDate = datetime.datetime.now()
     curs.execute(sql,(serial, User[0][0], toDate.strftime("%Y-%m-%d")))
     equipment = curs.fetchall()
     upscode= input("UPS Code (Now:{}): ".format(equipment[0][3]))
     pack = input("Pack Number (Now:{}) : ".format(equipment[0][4]))
     status = input("Status (Now:{}): ".format(equipment[0][1]))
     faultcode1 = input("First Fault Code (Now:{}): ".format(equipment[0][5]))
     partreplace1 = input("First part replaced (Now:{}): ".format(equipment[0][6]))
     faultcode2 = input("Second Fault Code (Now:{}): ".format(equipment[0][7]))
     partreplace2 = input("Second Replaced (Now:{}): ".format(equipment[0][8]))
     comment = input("Comments (Now:{}): ".format(equipment[0][9]))
     sql ="UPDATE production set upscode=?, pack=?, idstatus=?, idfaultcode1=?, idpartreplace1=?, idfaultcode2=?, idpartreplace2=?, Comments=? where serial=? and iduser =? and date=?"
     curs.execute(sql,(upscode, pack, status, faultcode1,partreplace1, faultcode2,  partreplace2, comment, serial, User[0][0], toDate.strftime("%Y-%m-%d")))
     conn.commit()
def printReport(Report):
    print("Report for the Day")
    print("\n Serial          UPS Code         Pack            Status           Fault Code       Part Replaced      Comment" )
    print("----------------------------------------------------------------------------------------------------------------------")
    for row in Report:
        arg1 = '{message:{fill}{align}{width}}'.format( message=row[0], fill=' ', align='<',  width=16)
        arg2 = '{message:{fill}{align}{width}}'.format( message=row[1], fill=' ', align='<',  width=16)
        arg3 = '{message:{fill}{align}{width}}'.format( message=row[2], fill=' ', align='<',  width=16)
        arg4 = '{message:{fill}{align}{width}}'.format( message=row[3], fill=' ', align='<',  width=16)
        arg5 = '{message:{fill}{align}{width}}'.format( message=row[4], fill=' ', align='<',  width=16)
        arg6 = '{message:{fill}{align}{width}}'.format( message=row[5], fill=' ', align='<',  width=16)
        #arg7 = '{message:{fill}{align}{width}}'.format( message=row[6], fill=' ', align='<',  width=16)
        print(arg1, arg2, arg3, arg4, arg5, arg6, row[6])
    input("\n\n\nPress any key to continue ... ")


def ShowWork(conn, User):
    curs = conn.cursor()
    toDate = datetime.datetime.now()
    sql ="SELECT serial, upscode, pack, status, faultcode, partreplace, comments FROM production \
          INNER JOIN status on production.idstatus=status.idstatus \
          INNER JOIN faultcode on production.idfaultcode1=faultcode.idfaultcode \
          INNER JOIN partreplace on production.idpartreplace1=partreplace.idpartreplace \
          WHERE iduser =? and date=?"
    curs.execute(sql,( User[0][0], toDate.strftime("%Y-%m-%d")))
    printReport(curs.fetchall())


def GraphInfo(conn, User):
    sql ="SELECT serial, upscode, pack, status, faultcode, partreplace, comments FROM production \
          INNER JOIN status on production.idstatus=status.idstatus \
          INNER JOIN faultcode on production.idfaultcode1=faultcode.idfaultcode \
          INNER JOIN partreplace on production.idpartreplace1=partreplace.idpartreplace \
          WHERE iduser =? and date=?"
    curs.execute(sql,( User[0][0], toDate.strftime("%Y-%m-%d")))     
