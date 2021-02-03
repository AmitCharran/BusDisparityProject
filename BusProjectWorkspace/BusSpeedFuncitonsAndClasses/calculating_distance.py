import ast
from datetime import datetime

# Use 2 different longitude and latitude to calculate distance
# preferably distance in meters

# Use distance and time to calculate speed preferably m/s

# m/s -> mph

import numpy as np
import math

class calculating_speed:
    def __init__(self):
        pass

    def distance(self, dist1, dist2):
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

    def distance_with_val(self, s_lat, s_lng, e_lat, e_lng):
        # approximate radius of earth in km
        R = 6373.0
        s_lat = s_lat * np.pi / 180.0
        s_lng = np.deg2rad(s_lng)
        e_lat = np.deg2rad(e_lat)
        e_lng = np.deg2rad(e_lng)

        d = np.sin((e_lat - s_lat) / 2) ** 2 + np.cos(s_lat) * np.cos(e_lat) * np.sin((e_lng - s_lng) / 2) ** 2
        return 2 * R * np.arcsin(np.sqrt(d))


    def string_to_time(self, string_date):
        temp = string_date[0:string_date.rfind('-')]
        date = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')
        return date


    def time_difference(self, start_time, end_time):
        start = self.string_to_time(start_time)
        end = self.string_to_time(end_time)

        total_seconds = (end - start).total_seconds()
        return total_seconds

    def convert_to_average_speed(self, latitude, longitude, time):
        answer_array = []

        for i in range(0, (len(latitude) - 1)):
            distance_km = self.distance_with_val(latitude[i], longitude[i], latitude[i + 1], longitude[i + 1])
            distance_m = distance_km * 1000
            seconds = self.time_difference(time[i], time[i + 1])
            answer_array.append((distance_m/seconds))

        return answer_array

    def test(self):
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



    def test2(self):
        file = open('Data/output2.txt', 'r')
        line = file.readline()
        file.close()
        dictionary = ast.literal_eval(line)

        answer_dictionary = {}

        for key in dictionary.keys():
            print("Vehicle Ref: " + key)
            for key_2 in dictionary[key].keys():
                print("Destination Name: " + key_2)
                for key_3 in dictionary[key][key_2].keys():
                    print('Journey Pattern Ref: ' + key_3)
                    print(dictionary[key][key_2][key_3]['Latitude']) # use latitude, longitude, & time to calculate speed
                    print(dictionary[key][key_2][key_3]['Longitude'])
                    print(dictionary[key][key_2][key_3]['Response Time'])
                    array = self.convert_to_average_speed(dictionary[key][key_2][key_3]['Latitude'],
                                                          dictionary[key][key_2][key_3]['Longitude'],
                                                          dictionary[key][key_2][key_3]['Response Time'])







test = calculating_speed()
test.test2()