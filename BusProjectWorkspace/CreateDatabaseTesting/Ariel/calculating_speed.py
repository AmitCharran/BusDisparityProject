import ast
from datetime import datetime

# Use 2 different longitude and latitude to calculate distance
# preferably distance in meters

# Use distance and time to calculate speed preferably m/s

# m/s -> mph

file = open('info.txt', 'r')
lines = file.readlines()

array = []

counter = 0
for line in lines:
    dictionary = ast.literal_eval(line)
    array.append(dictionary)
    counter += 1
    if counter >= 4:
        break

print(array)

string_date = array[0]['Response Time']
temp = string_date[0:string_date.rfind('-')]
date = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')

print(date.date())
print(date.second)
