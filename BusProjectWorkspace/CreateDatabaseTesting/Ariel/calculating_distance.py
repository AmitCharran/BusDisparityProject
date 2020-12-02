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

test_data = array[0]['Longitude']



#test_data = array[0]['Response Time']
#def distance_data(test_data):
 #   for x in test_data:
  #          test_data_2 = x['Response Time']
   #         latitude_ref = test_data_2['Latitude']
    #        longitude_ref = test_data_2['Longitude']
    #print(distance_data(test_data))

#import math
#def distance(s_lat, s_lng, e_lat, e_lng):
    # approximate radius of earth in km
 #   R = 6373.0

  #  s_lat = s_lat * np.pi / 180.0
   # s_lng = np.deg2rad(s_lng)
    #e_lat = np.deg2rad(e_lat)
    #e_lng = np.deg2rad(e_lng)

  #  d = np.sin((e_lat - s_lat) / 2) ** 2 + np.cos(s_lat) * np.cos(e_lat) * np.sin((e_lng - s_lng) / 2) ** 2

   # return 2 * R * np.arcsin(np.sqrt(d))