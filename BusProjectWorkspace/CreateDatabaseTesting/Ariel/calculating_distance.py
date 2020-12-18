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


def distance_data(dictionary):
    for x in dictionary:
            test_data_2 = x['Response Time']
            latitude_ref = test_data_2['Latitude']
            longitude_ref = test_data_2['Longitude']

import numpy as np
import math
def distance(dist1, dist2):
 #approximate radius of earth in km
    R = 6373.0
    s_lat = dist1['Latitude']
    s_lng = dist1['Longitude']
    e_lat = dist2['Latitude']
    e_lng = dist2['Longitude']
    s_lat = s_lat * np.pi / 180.0
    s_lng = np.deg2rad(s_lng)
    e_lat = np.deg2rad(e_lat)
    e_lng = np.deg2rad(e_lng)

    d = np.sin((e_lat - s_lat) / 2) ** 2 + np.cos(s_lat) * np.cos(e_lat) * np.sin((e_lng - s_lng) / 2) ** 2

    return 2 * R * np.arcsin(np.sqrt(d))

print(distance(array[0],array[1]))

def recursive_counter(n):
    if n == 0:
        print(n)
    else:
         print(n)
         recursive_counter(n-1)
recursive_counter(10)
