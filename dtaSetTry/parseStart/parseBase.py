#File parser starting point ...??
#load array of data from 'DemographicSet.csv'

file1 = 'DemographicSet.csv'
demoAray = []
dataAr1 = []
with open(file1, 'r') as f1:
  l1 = f1.readline()
  demoAray.append(l1.split(','))

#load data into array
  for item in f1:
    dataAr1.append(item.split(','))

#print(demoAray)
#print(dataAr1)

#Convert data based off of user input? Based off of file?
print(demoAray[0][1])
for data in dataAr1:
  print(data[1])
