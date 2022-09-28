import mysql.connector as c
from getpass import getpass

mydb = c.connect(
  host="localhost",
  user="santosh",
  password="Mysql@12",
  database="pythondatabase",
  auth_plugin='mysql_native_password',
)

mycursor = mydb.cursor()
def Read():
    while True:
        print("\t","--Retrieve data--""\n1:Fetch all data\n2:Fetch data by name: ")
        x=input("Enter no: ")
        # flag=0
        if x=='2':
            flag=2
            name=input("Enter your name: ")
            mycursor.execute("SELECT * from crud")
            myresult = mycursor.fetchall()
            # s=set()
            # s2=set()
            for a,b in myresult:
                # print(a,b)
                # s.add(a)
                # s2.add(b)
            # print(s)
            # print(s2)
                if a==name:
                    print(a,b)
                    flag=3
                    break
            else:
                print("There is no such name")
                Read()
            if flag==3:
                x=int(input("1:More user\n2:exit\nSelect option: "))
                if x==2:
                    return True    
        elif x=='1':
            mycursor.execute("SELECT * from crud")
            myresult = mycursor.fetchall()
            flag=0
            for a,b in myresult:
                print(a,b)
                flag=1
            if flag==1:
               x=int(input("1:More user\n2:exit\nSelect option: "))
               if x==2:
                return True
        else:
            print("--Please select correctly--")
            Read()
    # return True
                


