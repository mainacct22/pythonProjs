#File parser starting point ...??
#load array of data from 'DemographicSet.csv'

import sys

file1 = '../DemographicSet.csv'

passedValue = sys.argv
demoAray = []
dataAr1 = []

def loadArray(fileName):
  with open(file1, 'r') as f1:
    l1 = f1.readline()
    demoAray.append(l1.split(','))

#load data into array
    for item in f1:
      dataAr1.append(item.split(','))

#print(demoAray)
#print(dataAr1)

#Convert data based off of user input? Based off of file?

#for count in range(len(demoAray)):

def displayArray(passedValue):
  i = int(passedValue[1])
  print(demoAray[0][i])
  for item in dataAr1:
    print(item[i])

if __name__ == '__main__':
  loadArray(file1)
  displayArray(passedValue)
