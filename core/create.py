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
def Create():
  while True:
      print("\n","\t","--Please enter field to store in database--")
      name=input("Enter your name: ")
      city=input("Enter your city: ")
      sql = "INSERT INTO crud (name,city) VALUES (%s, %s)"
      val = (name,city)
      mycursor.execute(sql, val)
      mydb.commit()
      print("\n","--Data saved successfully--")
      x=int(input("1:More user\n2:exit\nSelect option: "))
      if x==2:
        return True
