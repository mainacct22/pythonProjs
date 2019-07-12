#Insert data/rows/row then delete or update the row to show "completed" in
#some way

import sys
sys.path.insert(0, '../../credentials')
from mysqlCreds import *
import mysql.connector

myDb = mysql.connector
dbCur = ' '

print(host)
def connectDB ():

  myDbConn = myDb.connect(

    host=host,
    user=user,
    passwd=passwd,
    database=database

  )
  print 'Connected'
  dbCur = myDbConn.cursor()
#Retrieve field names

#def getAll():
  dbCur.execute("show columns from users") 
  dbRes = dbCur.fetchall()
  print(dbRes)

#Insert data
  dbCur.execute('delete from users')
  for x in range(100):
    for x in range(10):
      dbCur.execute("insert into users(userid, usrfrtnme, usrlstnme, hstParid) values (%d, 'test', 'test', 1)" % (x))
      print 'inserted'
    for i in range(10):
      dbCur.execute("delete from users where userid = %d" % (i))
      print 'deleted'
      myDbConn.commit()
  dbCur.close()

#Remote data

#main
if __name__ == '__main__':
  connectDB()
