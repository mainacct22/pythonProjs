#Insert data/rows/row then delete or update the row to show "completed" in
#some way

import mysql.connector

myDb = mysql.connector
dbCur = ' '

def connectDB ():

  myDbConn = myDb.connect(

    host="18.214.220.93",
    user="webUser",
    passwd="#edCft6",
    database="webPage"

  )
  print 'Connected'
  dbCur = myDbConn.cursor()
#Retrieve field names

#def getAll():
  dbCur.execute("show columns from users") 
  dbRes = dbCur.fetchall()
  print(dbRes)

#Insert data
  dbCur.execute("insert into users(userid, usrfrtnme, usrlstnme, hstParid) values (5, 'test', 'test', 0)")
  dbCur.close()

#Remote data

#main
if __name__ == '__main__':
  connectDB()
