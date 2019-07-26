TechRoom System Version 1.0

REQUIREMENTS TO RUN THE PROJECT

I use SQLite Files to store data and you must have the data base in the folder db/tecroom.db.

1- You need to use Python to execute the file. The Main file is Techroom.py

2- You have to Login using one of this users:

  - User: aj   Password: aj
  - User: ja    Password: ja
  You can find more user in the Table User.

  You can create your own User and Password updating the Table User.

This is a dynamic and interactive Aplication. Its designed to be sale and use for differents Tech Rooms  or individual person.

The configuration file has the initial info to use the System.

The purpose is to create one Application where the Technician can update their wrork on real time  they can access to see how is going his work during the day.


The Login Form has to validate the User and Password through my own Python function with the stored info in the Users Table.

The Technician has to update thesystem very time they repaired one equipment. You can verify it using the Report in the menue .

Custom Python Functions:

Login Module:
1-) CheckUser(conn, nameUser, passUser).

2-) Login(conn)

Techroom Module:
1-) create_connection(db_file)
2-) connectDB()
3-) Menu()

Modeltechroom Model:
1-) AddEquipment(conn, User)
2-) ModifyEquipment(conn, User)
3-) printReport(Report)
4-) ShowWork(conn, User)
5-) GraphInfo(conn, User)

Createdb Module:
1-) CreateDB()
