import ast
from datetime import datetime
import pandas as pd
from os import walk

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
            if seconds != 0:
                answer_array.append((distance_m/seconds))
            else:
                answer_array.append(0)

        return answer_array

    def convert_to_average_speed_with_check(self, latitude, longitude, time, number_gt):
        answer_array = []

        for i in range(0, (len(latitude) - 1)):
            distance_km = self.distance_with_val(latitude[i], longitude[i], latitude[i + 1], longitude[i + 1])
            distance_m = distance_km * 1000
            seconds = self.time_difference(time[i], time[i + 1])
            if seconds != 0:
                if distance_m/seconds >= number_gt:
                    print('distance: ' + str(distance_m))
                    print('seconds: ' + str(seconds))
                    print('Latitude: {} and {}'.format(str(latitude[i]), str(latitude[i+1])))
                    print('Longitude: {} and {}'.format(str(longitude[i]), str(longitude[i + 1])))
                    print('Time: {} and {}'.format(str(time[i]), str(time[i + 1])))
                answer_array.append((distance_m / seconds))
            else:
                answer_array.append(0)

        return answer_array

    def msToMph(self, list):
        ans = []
        for x in list:
            ans.append((x * 2.2369362920544))

        return ans


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
            # print("Vehicle Ref: " + key)
            for key_2 in dictionary[key].keys():
                # print("Destination Name: " + key_2)
                for key_3 in dictionary[key][key_2].keys():
                    # print('Journey Pattern Ref: ' + key_3)
                    print(dictionary[key][key_2][key_3]['Latitude']) # use latitude, longitude, & time to calculate speed
                    print(dictionary[key][key_2][key_3]['Longitude'])
                    print(dictionary[key][key_2][key_3]['Response Time'])
                    array = self.convert_to_average_speed(dictionary[key][key_2][key_3]['Latitude'],
                                                          dictionary[key][key_2][key_3]['Longitude'],
                                                          dictionary[key][key_2][key_3]['Response Time'])
                    print("speed:" + str(self.msToMph(array)))


    def counting_data(self):
        file = open('Data/output3.txt', 'r')
        line = file.readline()
        file.close()
        dictionary = ast.literal_eval(line)

        counter = 0
        for key in dictionary.keys():
            counter = counter + 1
            for key_2 in dictionary[key].keys():
                counter = counter + 1
                for key_3 in dictionary[key][key_2].keys():
                    counter = counter + 1
                    for key_4 in dictionary[key][key_2][key_3].keys():
                        counter = counter + 1
        print(counter)

    def test3(self):
        # this is the one I will use
        file = open('Data/output3.txt', 'r')
        line = file.readline()
        file.close()
        dictionary = ast.literal_eval(line)

        answer_dictionary = {}

        for key in dictionary.keys():
            # published line ref
            if key not in answer_dictionary.keys():
                answer_dictionary[key] = {}
            for key_2 in dictionary[key].keys():
                # Vehicle Ref
                if key_2 not in answer_dictionary[key].keys():
                    answer_dictionary[key][key_2] = {}
                for key_3 in dictionary[key][key_2].keys():
                    # destination ref
                    if key_3 not in answer_dictionary[key][key_2].keys():
                        answer_dictionary[key][key_2][key_3] = {}
                    for key_4 in dictionary[key][key_2][key_3].keys():
                        # journey pattern ref

                        array = self.convert_to_average_speed(dictionary[key][key_2][key_3][key_4]['Latitude'],
                                                              dictionary[key][key_2][key_3][key_4]['Longitude'],
                                                              dictionary[key][key_2][key_3][key_4]['Response Time'])
                        answer_dictionary[key][key_2][key_3][key_4] = array

        f = open('Data/converted_speed_data_2.txt', 'a')
        f.write(str(answer_dictionary))
        f.write('\n')
        f.close()

    def show_values_from_of_a_line_ref(self, published_line_ref, input_file):
        file = open(input_file, 'r')
        line = file.readline()
        file.close()
        dictionary = ast.literal_eval(line)

        p = published_line_ref
        total_counts = 0
        for key in dictionary[p].keys():
            v = key
            for key2 in dictionary[p][v].keys():
                d = key2
                for key3 in dictionary[p][v][d].keys():
                    j = key3
                    latitude = dictionary[p][v][d][j]['Latitude']
                    longitude = dictionary[p][v][d][j]['Longitude']
                    time = dictionary[p][v][d][j]['Response Time']
                    array = self.convert_to_average_speed_with_check(latitude, longitude, time, 30)

                    total_counts = len(array) + total_counts

                    if len(array) > 0 and max(array) >= 30:
                        print(p)
                        print(v)
                        print(d)
                        print(j)

                        for i in range(0, len(longitude) - 1):
                            print('Longitude: {} and {}'.format(longitude[i], longitude[i + 1]))
                            print('Latitude: {} and {}'.format(latitude[i], latitude[i + 1]))
                            print('Time: {} and {}'.format(time[i], time[i + 1]))
                            print('Speed: ' + str(array[i]))
                            print('\n\n')

                        print(longitude)
                        print(latitude)
                        print(time)
                        print('Speed Array: ' + str(array))
        print(total_counts)

    def print_highest_per_line_ref(self, input_file):
        file = open(input_file, 'r') #converted_speed_data
        line = file.readline()
        file.close()
        dictionary = ast.literal_eval(line)

        for key in dictionary.keys():
            p = key
            current_max = 0
            for key2 in dictionary[p].keys():
                v = key2
                for key3 in dictionary[p][v].keys():
                    d = key3
                    for key4 in dictionary[p][v][d].keys():
                        j = key4
                        array = dictionary[p][v][d][j]
                        max_in_array = 0
                        if len(array) > 0:
                            max_in_array = max(array)
                        if max_in_array > current_max:
                            current_max = max_in_array

            print(p + " : " + str(current_max * 2.2369362920544))

    def calculate_average_from_file(self, input_file, output_file = "file.csv"):
        file = open(input_file, 'r')
        line = file.readline()
        file.close()
        dictionary = ast.literal_eval(line)

        df = pd.DataFrame()

        pub_line_ref = []
        averages = []

        for key in dictionary.keys():
            p = key
            arrays = []
            for key2 in dictionary[p].keys():
                v = key2
                for key3 in dictionary[p][v].keys():
                    d = key3
                    for key4 in dictionary[p][v][d].keys():
                        j = key4
                        arrays.append(dictionary[p][v][d][j])
            average = self.average_from_arrays_remove_0s(arrays)
            pub_line_ref.append(p)
            averages.append(average)

        df['Published Line Ref'] = pub_line_ref
        df['Averages'] = averages

        df.to_csv(output_file)
        ## print to file


#####################################
    ### Seems to be most important functions *Also three functions above
    def calculate_average_from_folder(self, folder_path):
        f = []
        for (dirpath, dirnames, filenames) in walk(folder_path):
            f.extend(filenames)
            break

        answer_dictionary = {}

        for filename in f:
            if filename != '.DS_Store':
                file_path = folder_path + '/' + filename
                dictionary = self.calculate_average_from_file_return_dictionary(file_path)

                answer_dictionary = self.average_dictionary_together(answer_dictionary, dictionary)

    def average_dictionary_together(self, answer_dictionary, dictionary):
        pass


    def calculate_average_from_file_return_dictionary(self, input_file):
        file = open(input_file, 'r')
        line = file.readline()
        file.close()
        dictionary = ast.literal_eval(line)

        answer_dictionary = {}

        pub_line_ref = []
        averages = []

        for key in dictionary.keys():
            p = key
            arrays = []
            for key2 in dictionary[p].keys():
                v = key2
                for key3 in dictionary[p][v].keys():
                    d = key3
                    for key4 in dictionary[p][v][d].keys():
                        j = key4
                        arrays.append(dictionary[p][v][d][j])
            average = self.average_from_arrays_remove_0s(arrays)
            pub_line_ref.append(p)
            averages.append(average)

            answer_dictionary[p] = average

        return answer_dictionary


    def average_from_arrays(self, arrays):
        average = 0
        count = 0
        for array in arrays:
            for val in array:
                count = count + 1
                average = average + val

        if count == 0:
            return 0
        else:
            return average/count

    def average_from_arrays_remove_0s(self, arrays):
        average = 0
        count = 0
        for array in arrays:
            for val in array:
                if val >= 0.01:
                    count = count + 1
                    average = average + val

        if count == 0:
            return 0
        else:
            return average / count

    def average_from_arrays_remove_0s_return_count_and_average(self, arrays):
        answer_dictionary = {}
        average = 0
        count = 0
        for array in arrays:
            for val in array:
                if val >= 0.01:
                    count = count + 1
                    average = average + val

        if count == 0:
            answer_dictionary['Average Count'] = 0
            answer_dictionary['Count'] = 0
            return answer_dictionary
        else:
            answer_dictionary['Average Count'] = average
            answer_dictionary['Count'] = count
            return answer_dictionary







# test = calculating_speed()
# test.show_values_from_of_a_line_ref('QM21', input_file='Data/output3.txt')
# test.print_highest_per_line_ref('Data/converted_speed_data_2.txt')
#
# test.show_values_from_of_a_line_ref('M101', 'Data/output3.txt')
# 65mph --> 29.0567

# test.calculate_average_from_folder('Data')
