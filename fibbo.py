#stack
stack=[]
def IsEmpty():
    if stack == []:
        print("Stack Is Empty")
        return True
    else:
        return False

def view ():
    print("\n\nStack >>")
    viewstack=stack [::-1]
    if not IsEmpty():
        for x in range (len (viewstack) ) :
            print ("\t" + str(viewstack [x]))

def push ():
    item=int (input ("Enter integer value : "))
    stack.append (item)

def pop ():
    if not IsEmpty():
        item=stack.pop (-1)
        print ("Deleted Elemnt : ", item)

def peek ():
    if not IsEmpty():
        item=stack [-1]
        print ("Peeked Element: ", item)

while True:
    print ("\nstack operation")
    print ("********")
    print ("\t1.View")
    print ("\t2.Push")
    print ("\t3.Pop")
    print ("\t4.Peek")
    print ("\t5.Exit")
    choice=int (input ("Enter your choice : "))
    if choice==1:
        view ()
    elif choice==2:
        push ()
    elif choice==3:
        pop ()
    elif choice==4:
        peek ()
    elif choice==5:
        break
    else:
        print ("wrong")
print("\n--Program terminated Peacefully--")
