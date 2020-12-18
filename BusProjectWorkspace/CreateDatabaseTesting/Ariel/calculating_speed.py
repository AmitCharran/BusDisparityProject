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

# Function to calculate speed
def bus_speed(dist, time):
    dist = ()
    time = (date.second)
    return dist / time

# sec_to_hr = 1/3600 # 3600 seconds in 1 hour
# min_to_hr = 1/60 # 60 minutes in 1 hour
# km_to_miles = 0.62 # 0.62 miles in 1 kilometer
# time_hrs = 1 + (5*min_to_hr)+ (42*sec_to_hr) # Total time in hours
# dist_miles = 10 * km_to_miles # Total time in miles
