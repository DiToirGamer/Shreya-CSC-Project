import mysql.connector
try:
    con=mysql.connector.connect(host="localhost",user="root",password="shreya06062005",database="covid")
    cur = con.cursor()
    try:
        cur.execute('CREATE TABLE covid(username varchar(30),pass varchar(30));')
        print('Created covid table')
    except:
        print("Covid Table is already present")
    try:
        cur.execute('CREATE TABLE member(ad varchar(55),name varchar(50),address varchar(50),phone varchar(20),email varchar(60),age int,aadhar varchar(60));')
        print('Created member table')
    except:
        print("Member Table is already present")
    try:
        cur.execute('create table vaccination(aadharno varchar(60),name varchar(50),dt date,dose int);')
        print('Created vaccination table')
    except:
        print("Vaccination Table is already present")
    username = input("Enter new User : ")
    Password = input("Enter New Password: ")
    try:
        cur.execute('INSERT INTO covid VALUES (\'{}\',\'{}\')'.format(username,Password))
        print('created new user')
    except:
        print("Couldnt add new user")
except:
    print("Error connecting to the database")
a= input("press enter to exit")
