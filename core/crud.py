import mysql.connector as c
from create import Create
from read import Read
from update import Update
from delete import Delete

mydb = c.connect(
  host="localhost",
  user="santosh",
  password="Mysql@12",
  database="pythondatabase",
  auth_plugin='mysql_native_password',
)

mycursor = mydb.cursor()


def checkregistration():
    print('Available Options: C=Create, R=Read, U=Update, D=Delete ,E=Exit')
    choice = input('Choose your option = ').upper()
    if choice == 'C':
        t=Create()
        if t==True:
            print("\n","\t","--Please select options--")
            checkregistration()
    elif choice == 'R':
        t=Read()
        if t==True:
            print("\n","\t","--Please select options--")
            checkregistration()
    elif choice == 'U':
        t=Update()
        if t==True:
            print("\n","\t","--Please select options--")
            checkregistration()
    elif choice == 'D':
        t=Delete()
        if t==True:
            print("\n","\t","--Please select options--")
            checkregistration()
    elif choice == 'E':
        return True
    else:
        print('Wrong Entry')
        checkregistration()

checkregistration()      




