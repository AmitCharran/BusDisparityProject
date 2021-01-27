from os import walk  # use walk to go through directories
import json
from datetime import datetime
import time
import sys
from BusDisparityFunctionsAndClasses.setting_up_sql_connection import mta_bus_project_sql_tables
from HiddenVariables import hidden_variables
import ast
import pandas as pd
import numpy as np

class format_data:
    # def __init__(self, input_data_folder_path, output_data_file):
    #     self.input_folder = input_data_folder_path
    #     self.output_file = output_data_file
    #     self.start_time = ""
    #     self.end_time = ""

    def __init__(self, input_data_folder_path ="", output_data_file ="", start_time = "", end_time = ""):
        # self.sql_con = mta_bus_project_sql_tables(connection='mariadb', sql_password=hidden_variables.sql_password, sql_user=hidden_variables.sql_user)
        self.input_folder = input_data_folder_path
        self.output_file = output_data_file
        self.start_time = start_time
        self.end_time = end_time
        # self.sql_con = mta_bus_project_sql_tables(hidden_variables.sql_host,
        #                                      hidden_variables.sql_user,
        #                                      hidden_variables.sql_password)

    def get_list_of_directories(self):
        f = []
        for (dirpath, dirnames, filenames) in walk(self.input_folder):  # getting directory
            f.extend(dirnames)
            break
        return f

    def count_from_file(self, path):
        file = open(path, 'r')
        lines = file.readlines()
        counter = 0
        for line in lines:
            counter = counter + 1
        print(counter)

        file.close()


    def get_file_names_into_array(self):
        files = []
        f = self.get_list_of_directories()

        for x in f:
            file_names = []
            for (dirpath, dirnames, filenames) in walk(self.input_folder +'/'+ x ):  # getting directory
                file_names.extend(filenames)
                break
            files.append(file_names)
        return files

    def create_list_of_all_paths(self):
        directory_names = self.get_list_of_directories()
        file_names = self.get_file_names_into_array()

        f = []
        counter = 0
        for x in directory_names:
            for f_n in file_names[counter]:
                # This is where I change start time/ end time
                current_time = self.create_date_time(x, f_n)
                if (self.start_time == "" or (self.start_time <= current_time <= self.end_time)) and f_n != '.DS_Store':
                    f.append(self.input_folder + '/' + x + "/" + f_n)
            counter = counter + 1
        return f

    def create_date_time(self, direc, file_name):
        if file_name == '.DS_Store':
            current_time = datetime.now()
            current_time = current_time.replace(year=1, month=1, day=1)
            return current_time

        split_directory = direc.split('-')
        split_file_name = file_name.split('_')
        split_file_name[1] = split_file_name[1].replace(".json","")
        current_time = datetime(int(split_directory[0]), int(split_directory[1]), int(split_directory[2]), int(split_file_name[0]), int(split_file_name[1]))
        return current_time

    def get_json_info(self, file_name):
        with open(file_name) as json_file:
            try:
                data = json.load(json_file)
            except json.decoder.JSONDecodeError as e:
                print(str(e) + " " + file_name)
        bus_data = []
        try:
            bus_data = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
        except UnboundLocalError as e:
            pass
        return bus_data

    def reduce_json(self, json_object):
        bus_data = []
        try:
            bus_data = json_object['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
        except UnboundLocalError as e:
            pass
        return bus_data

    # Get data for SQL table
    def get_passenger_count(self, data):
        data = data['MonitoredVehicleJourney']
        if 'MonitoredCall' in data:
            data2 = data['MonitoredCall']
            if 'Extensions' in data2:
                data3 = data2['Extensions']
                if 'Capacities' in data3:
                    return data3['Capacities']['EstimatedPassengerCount']
        return "NULL"

    def get_stop_point_name(self, data):
        data = data['MonitoredVehicleJourney']
        if 'MonitoredCall' in data:
            return data['MonitoredCall']['StopPointName']
        return "NULL"

    def get_stop_point_ref(self, data):
        data = data['MonitoredVehicleJourney']
        if 'MonitoredCall' in data:
            return data['MonitoredCall']['StopPointRef']
        return "NULL"

    def get_destination_name(self, data):
        if 'DestinationName' in data['MonitoredVehicleJourney']:
            return data['MonitoredVehicleJourney']['DestinationName']
        return "NULL"

    def get_journey_pattern_ref(self, data):
        if 'JourneyPatternRef' in data['MonitoredVehicleJourney']:
            return data['MonitoredVehicleJourney']['JourneyPatternRef']
        return "NULL"

    def get_response_time_stamp(self, data):
        return data['RecordedAtTime']

    def get_vehicle_ref(self, data):
        return data['MonitoredVehicleJourney']['VehicleRef']

    def get_line_ref(self, data):
        return data['MonitoredVehicleJourney']['LineRef']

    def get_published_line_name(self, data):
        return data['MonitoredVehicleJourney']['PublishedLineName']

    def get_longitude(self, data):
        return data['MonitoredVehicleJourney']['VehicleLocation']['Longitude']

    def get_latitude(self, data):
        return data['MonitoredVehicleJourney']['VehicleLocation']['Latitude']

    def get_primary_key(self, data):
        string_date = self.get_response_time_stamp(data)
        vehicle_ref = self.get_vehicle_ref(data)
        line_ref = self.get_line_ref(data)

        temp = string_date[0:string_date.rfind('-')]
        date = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')
        primary_key = str(date.date()) + str(date.hour) + str(date.minute) + " " + str(vehicle_ref) + " " + str(
            line_ref)
        return primary_key

    def information_for_files(self, data):
        dictionary = {"Primary Key": self.get_primary_key(data),
             "Response Time": self.get_response_time_stamp(data),
             "Vehicle Ref": self.get_vehicle_ref(data),
             "Line Ref": self.get_line_ref(data),
             "Published Line Ref": self.get_published_line_name(data),
             "Passenger Count": self.get_passenger_count(data),
             "Latitude": self.get_latitude(data),
             "Longitude": self.get_longitude(data),
             "Stop Point Name": self.get_stop_point_name(data),
             "Stop Point Ref": self.get_stop_point_ref(data),
             "Destination Name": self.get_destination_name(data),
             "Journey Pattern Ref": self.get_journey_pattern_ref(data)}
        return dictionary

    def append_to_file(self, dictionary):
        file = open(self.output_file, "a")
        file.writelines(str(dictionary))
        file.writelines("\n")
        file.close()

    def write_to_file(self, dictionary):
        # this might not work because I will constantly rewrite
        file = open(self.output_file, "w")
        file.writelines(str(dictionary))
        file.writelines("\n")
        file.close()

    def create_info_to_output_file(self):
        path_directories = self.create_list_of_all_paths()
        for paths in path_directories:
            bus_data = self.get_json_info(paths)
            for data in bus_data:
                dictionary = self.information_for_files(data)
                self.append_to_file(dictionary)

    def dictionary_to_sql(self, dictionary):
        primary_key = dictionary['Primary Key']
        response_time = dictionary['Response Time']
        vehicle_ref = dictionary['Vehicle Ref']
        line_ref = dictionary['Line Ref']
        published_line_ref = dictionary['Published Line Ref']
        passenger_count = dictionary['Passenger Count']
        if not (passenger_count == "NULL" or passenger_count == 'null'):
            passenger_count = int(passenger_count)
        latitude = float(dictionary['Latitude'])
        longitude = float(dictionary["Longitude"])
        stop_point_name = dictionary['Stop Point Name'].replace("\"", "")
        destination_name = dictionary["Destination Name"].replace("\"", "")
        journey_pattern_ref = dictionary['Journey Pattern Ref'].replace("\"", "")

        self.sql_con.insert_into_tables(primary_key, response_time, vehicle_ref, line_ref,
                                   published_line_ref, passenger_count, latitude,
                                   longitude, stop_point_name, destination_name, journey_pattern_ref)

    def write_to_sql_from_file(self, file_input_path):
        lines = self.get_info_from_file(file_input_path)
        print(len(lines))
        for line in lines:
            dictionary = ast.literal_eval(line)
            self.dictionary_to_sql(dictionary)


    def write_to_sql_from_file_skip_lines(self, file_input_path, skip_lines):
        lines = self.get_info_from_file(file_input_path)
        counter = 0
        print(type(lines))
        print(len(lines))
        start = False
        for line in lines:
            if counter >= skip_lines:
                if not start:
                    print('Starting')
                    start = True
                dictionary = ast.literal_eval(line)
                self.dictionary_to_sql(dictionary)
                counter = counter + 1
            else:
                counter = counter + 1
        print(counter)

    def write_to_sql_from_file_skip_lines2(self, file_input_path, skip_lines):
        counter = 0
        start = False
        with open(file_input_path) as fp:
            line = fp.readline()
            while line:
                if counter >= skip_lines:
                    if not start:
                        print('Starting')
                        start = True
                    dictionary = ast.literal_eval(line)
                    self.dictionary_to_sql(dictionary)
                    # counter = counter + 1
                    line = fp.readline()
                    # if counter >= (skip_lines + 10):
                    #     break
                else:
                    counter = counter + 1
        print(counter)

    def get_info_from_file(self, file_input_path):
        file = open(file_input_path, 'r')
        lines = file.readlines()
        file.close()
        return lines

    def write_to_sql(self):
        path_directories = self.create_list_of_all_paths()
        sql_con = mta_bus_project_sql_tables(hidden_variables.sql_host,
                                             hidden_variables.sql_user,
                                             hidden_variables.sql_password)
        for paths in path_directories:
            bus_data = self.get_json_info(paths)
            for data in bus_data:
                dictionary = self.information_for_files(data)
                primary_key = dictionary['Primary Key']
                response_time = dictionary['Response Time']
                vehicle_ref = dictionary['Vehicle Ref']
                line_ref = dictionary['Line Ref']
                published_line_ref = dictionary['Published Line Ref']
                passenger_count = dictionary['Passenger Count']
                if passenger_count != "NULL":
                    passenger_count = int(passenger_count)
                latitude = float(dictionary['Latitude'])
                longitude = float(dictionary["Longitude"])
                stop_point_name = dictionary['Stop Point Name']
                destination_name = dictionary["Destination Name"]
                journey_pattern_ref = dictionary['Journey Pattern Ref']

                sql_con.insert_into_tables(primary_key, response_time, vehicle_ref, line_ref,
                                           published_line_ref, passenger_count, latitude,
                                           longitude, stop_point_name, destination_name, journey_pattern_ref)

    def write_to_sql_with_json_info(self, data):

        dictionary = self.information_for_files(data)
        ## here is where I add to SQL
        primary_key = dictionary['Primary Key']
        response_time = dictionary['Response Time']
        vehicle_ref = dictionary['Vehicle Ref']
        line_ref = dictionary['Line Ref']
        published_line_ref = dictionary['Published Line Ref']
        passenger_count = dictionary['Passenger Count']
        if passenger_count != "NULL":
            passenger_count = int(passenger_count)
        latitude = float(dictionary['Latitude'])
        longitude = float(dictionary["Longitude"])
        stop_point_name = dictionary['Stop Point Name']
        destination_name = dictionary["Destination Name"]
        journey_pattern_ref = dictionary['Journey Pattern Ref']


        self.sql_con.insert_into_tables(primary_key, response_time, vehicle_ref, line_ref,
                                   published_line_ref, passenger_count, latitude,
                                   longitude, stop_point_name, destination_name, journey_pattern_ref)

    def obtain_values_from_table_as_df(self, table_name):
        value_string = 'SELECT * FROM {};'.format(table_name)
        sql_table = self.sql_con.execute_command(value_string)
        df = pd.DataFrame(sql_table)
        df.columns = self.sql_con.get_column_names_tablename(table_name)
        return df

    def save_table_as_csv_file(self, table_name, file_name, path='Data/'):
        frame = self.obtain_values_from_table_as_df(table_name)
        frame.to_csv((path + file_name), index=False)

    def list_of_tables(self):
        string = 'SHOW tables;'
        list = self.sql_con.execute_command(string)
        ans = []
        for x in list:
            if x[0] != 'main_table':
                ans.append(x[0])
        return ans

    def sort_data_for_pie_charts(self, path, output_path = "name.txt"):
        dictionary = {}
        with open(path) as fp:
            line = fp.readline()
            while line:
                from_file = ast.literal_eval(line)
                time = from_file['Response Time']
                time = self.response_time_to_datetime(time)
                pub_line_ref = from_file['Published Line Ref']

                hour_min = str(time.hour) + ":" + str(time.minute)

                if hour_min not in dictionary:
                    self.add_borough_to_dicitonary(hour_min, dictionary)

                vehicle_ref = []
                while line:
                    from_file = ast.literal_eval(line)
                    pub_line_ref = from_file['Published Line Ref']
                    if from_file['Passenger Count'] != 'NULL':
                        count = from_file['Passenger Count']
                        borough = self.line_ref_to_borough_for_pie_chart(pub_line_ref)
                        if borough == 'Nothing_found':
                            print('problem with: {}'.format(str(from_file)))
                        else:
                            dictionary[hour_min]['Total'] = dictionary[hour_min]['Total'] + count
                            dictionary[hour_min][borough] = dictionary[hour_min][borough] + count

                    if from_file['Vehicle Ref'] in vehicle_ref:
                        break
                    vehicle_ref.append(from_file['Vehicle Ref'])
                    line = fp.readline()
                line = fp.readline()

        file = open(output_path, 'w')
        file.write(str(dictionary))
        file.close()

    def add_borough_to_dicitonary(self, response_time, dictionary):
        dictionary[response_time] = {'Total': 0,
                                     'Brooklyn': 0,
                                     'Bronx': 0,
                                     'Queens': 0,
                                     'Manhattan': 0,
                                     'Staten Island': 0,
                                     'Other': 0}

    def line_ref_to_borough_for_pie_chart(self, published_line_ref):
        if 'QM' in published_line_ref or \
                'BM' in published_line_ref or \
                'SIM' in published_line_ref or \
                'X' in published_line_ref:
            return 'Other'
        elif 'Bx' in published_line_ref:
            return 'Bronx'
        elif 'B' in published_line_ref:
            return 'Brooklyn'
        elif 'M' in published_line_ref:
            return 'Manhattan'
        elif 'Q' in published_line_ref:
            return 'Queens'
        elif 'S' in published_line_ref:
            return 'Staten Island'
        else:
            return 'Nothing_found'

    def response_time_to_datetime(self, string_date):
        temp = string_date[0:string_date.rfind('-')]
        date = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')
        return date
# for each folder
#   for each file
#       for each data
#           insert into sql


# test = format_data()

# test.sort_data_for_pie_charts('/Users/amitc/Desktop/BusDisparityProject/BusProjectWorkspace/BusDisparityFunctionsAndClasses/Data/January_22_data/1_22.txt',
#                               '/Users/amitc/Desktop/BusDisparityProject/BusProjectWorkspace/BusDisparityFunctionsAndClasses/Data/January_22_data/1_22_pie_chart.txt')


# lines = test.get_info_from_file('/Users/amitc/Desktop/BusDisparityProject/BusProjectWorkspace/BusDisparityFunctionsAndClasses/Data/January_22_data/1_22_pie_chart.txt')
#
#
#
# for line in lines:
#     d = ast.literal_eval(line)
#     counter = 0
#     for key in d.items():
#         counter = counter + 1
#         print(key)
#     print(counter)
#
# print('two')





