import ast
from datetime import datetime

# Use 2 different longitude and latitude to calculate distance
# preferably distance in meters

# Use distance and time to calculate speed preferably m/s

# m/s -> mph

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

def distance_with_val(s_lat, s_lng, e_lat, e_lng):
    # approximate radius of earth in km
    R = 6373.0
    s_lat = s_lat * np.pi / 180.0
    s_lng = np.deg2rad(s_lng)
    e_lat = np.deg2rad(e_lat)
    e_lng = np.deg2rad(e_lng)

    d = np.sin((e_lat - s_lat) / 2) ** 2 + np.cos(s_lat) * np.cos(e_lat) * np.sin((e_lng - s_lng) / 2) ** 2
    return 2 * R * np.arcsin(np.sqrt(d))

def test():
    file = open('Data/output.txt', 'r')
    line = file.readline()
    file.close()
    dictionary = ast.literal_eval(line)

    # keys = dictionary.keys()
    #
    # for key in keys:
    #     keys_2 = dictionary[key].keys()

    Latitude = dictionary['MTABC_616']['FOREST HILLS UNION TPK via 108 ST']['Latitude']
    Longitude = dictionary['MTABC_616']['FOREST HILLS UNION TPK via 108 ST']['Longitude']
    Time = dictionary['MTABC_616']['FOREST HILLS UNION TPK via 108 ST']['Response Time']

    print(Latitude)
    print(Longitude)
    print(Time)





test()
