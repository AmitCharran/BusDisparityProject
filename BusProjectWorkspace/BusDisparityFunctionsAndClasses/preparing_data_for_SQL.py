from os import walk  # use walk to go through directories
import json
from datetime import datetime
from BusDisparityFunctionsAndClasses.setting_up_sql_connection import mta_bus_project_sql_tables
from HiddenVariables import hidden_variables
import numpy as np

class format_data:
    def __init__(self, input_data_folder_path, output_data_file):
        self.input_folder = input_data_folder_path
        self.output_file = output_data_file
        self.start_time = ""
        self.end_time = ""

    def __init__(self, input_data_folder_path, output_data_file, start_time, end_time):
        self.input_folder = input_data_folder_path
        self.output_file = output_data_file
        self.start_time = start_time
        self.end_time = end_time

    def get_list_of_directories(self):
        f = []
        for (dirpath, dirnames, filenames) in walk(self.input_folder):  # getting directory
            f.extend(dirnames)
            break
        return f

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

# for each folder
#   for each file
#       for each data
#           insert into sql








