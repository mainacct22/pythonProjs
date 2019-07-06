import mysql.connector
import sys

file1 = '../DemographicSet.csv'

passedValue = sys.argv
demoAray = []
dataAr1 = []
dbAr1 = []

mydb = mysql.connector.connect(
  host = "18.214.220.93",
  user = "webUser",
  passwd = "#edCft6",
  database = "webPage"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()

for x in myresult:
  dbAr1.append(x)
  print(x)
    
print(dbAr1[0][1])

def loadArray(fileName):
  with open(file1, 'r') as f1:
    l1 = f1.readline()
    demoAray.append(l1.split(','))

    #load data into array
    for item in f1:
      dataAr1.append(item.split(','))

    #load data into mysql DB
    
if __name__ == '__main__':
  loadArray(file1)
