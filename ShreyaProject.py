import mysql.connector
db1=None
def connect():
    global db1
    db1=mysql.connector.connect(host="localhost",user="root",password="shreya06062005",database="covid")
def showusers():
    c1=db1.cursor()
    c1.execute("select * from covid")
    res=c1.fetchall()
    #print(res)
    print("list of covid")
    for val in res:
        print("username="+val[0]+"password="+val[1])
        
def login():
    print("-"*50)
    print("\t COVID VACCINATION RECORD")
    print("-"*50)
    print("\t LOGIN")
    un=input("Enter User Name:")
    pw=input("Enter Password:")
    q="select*from covid where username=%s and pass=%s"
    val=(un,pw)
    cursor2=db1.cursor()
    cursor2.execute(q,val)
    result=cursor2.fetchall()
    print("-"*50)
    if len(result)==0:
        print("invalid user name or password")
        print("-"*50)
        return False
    else:
        print("Access Granted!!!")
        print("-"*50)
        return True
    
def addmember():
    ad=input("Enter character:")
    name=input("Enter Name:")
    address=input("Enter Address:")
    phone=input("Enter phone number:")
    email=input("Enter email:")
    age=input("Enter age of member:")
    aadhar=input("Enter Aadhar cardno:")
    cursor1=db1.cursor()
    q="insert into member values(%s,%s,%s,%s,%s,%s,%s)"
    val=(ad,name,address,phone,email,age,aadhar)
    cursor1.execute(q,val)
    db1.commit()
    print("Member Added successfully")
    
def showmembers():
    c1=db1.cursor()
    c1.execute("select * from member")
    res=c1.fetchall()
    #print(res)
    print("List of Members")
    for val in res:
        print("Name ="+val[1]+"Aadhar card="+val[0])
        
def addvaccination():
    ad=input("Enter Aadhar no:")
    name=input("Enter vaccination Name:")
    d=input("Enter 1 for Dose 1: and ")
    dt=input("Enter the date of vaccination:")
    c2=db1.cursor()
    if d=="1":
        q="insert into vaccination values(%s,%s,%s,NULL)"
        val=(ad,name,dt)
        c2.execute(q,val)
        db1.commit()
        print("Vaccination Record Added Successfully")
    elif d=="2":
        q="update vaccination set d=%s where ad=%s"
        val=(dt,ad)
        c2.execute(q,val)
        db1.commit()
        print("Vaccination Record Updated Successfully")
    else:
        print("invalid input,please try again")
        
def showvaccine():
    c1=db1.cursor()
    c1.execute("select*from vaccination,member where vaccination.ad=member.ad")
    res=c1.fetchall()
    #print(res)
    print("List of Vaccinated Members")
    print ("-"*40)
    print("Name\tVaccine\tAadhar No\tDose1\tDose2")
    print ("-"*40)
    for val in res:
        print(val[5],"t",val[1],"\t",val[0],"\t",val[2],"\t",val[3])
              
def shownotvaccined():
    c1=db1.cursor();
    c1.execute("select*from member where ad not in(select ad from vaccination)")
    res=c1.fetchall()
    #print(res)
    print("List of Not Vaccinated Members")
    print ("-"*40)
    print("Name\tAadhar\tphone\tAddress\tEmail")
    print ("-"*40)
    for val in res:
        print(val[1],"t",val[0],"\t",val[3],"\t",val[2],"\t",val[4])
              
def showduevaccine():
    c1=db1.cursor()
    c1.execute("select* from vaccination,member where vaccination.ad=member.ad and d is null")
    res=c1.fetchall()
    #print(res)
    print("List of Members whose Dose2 is due")
    print("-"*40)
    print("Name\tvaccine\tAadhar no\tDose1\tDose 2")
    print ("-"*40)
    for val in res:
        print(val[5],"t",val[1],"\t",val[0],"\t",val[2],"\t",val[3])

    connect()
    print("connected")
    if login():
       while True:
           print("-"*50)
           print("\t CHOOSE AN OPERATION")
           print("-"*50)
           print("Press1-Add a New Society Member")
           print("Press2-Add a Vaccination Record")
           print("Press3-Show all the Members")
           print("Press4-Show all Vaccinated Members")
           print("Press5-Show whose Vaccination is Due")
           print("Press6-Show who are not at all Vaccinated")
           print("Press7-Quit")
           ch=int(input("Enter Your Choice:"))
           if ch==1:
               addmember()
           elif ch==2:
              addvaccination()
           elif ch==3:
              showmembers()
           elif ch==4:
              showvaccine()
           elif ch==5:
              showduevaccine()
           elif ch==6:
              shownotvaccined()
           elif ch==7:
              break           
connect()
showusers()
login()
addmember()
showmembers()
addvaccination()
showvaccine()
showduevaccine()
shownotvaccined()
