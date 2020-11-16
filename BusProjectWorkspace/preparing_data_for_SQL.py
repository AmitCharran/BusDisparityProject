from os import walk  # use walk to go through directories
import json
from datetime import datetime

directory = "Sample_JSON_Data/"  # this will be changed later and is used multiple time

# Get the path of all the files dynamically
def get_list_of_directories():
    f = []
    for (dirpath, dirnames, filenames) in walk(directory):  # getting directyory
        f.extend(dirnames)
        break
    return f

def get_file_names_into_array():
    files = []
    f = get_list_of_directories()

    for x in f:
        file_names = []
        for (dirpath, dirnames, filenames) in walk(directory + x):  # getting directory
            file_names.extend(filenames)
            break
        files.append(file_names)

    return files

def create_list_of_all_paths():
    directory_names = get_list_of_directories()
    file_names = get_file_names_into_array()

    f = []

    counter = 0
    for x in directory_names:
        for f_n in file_names[counter]:
            f.append(directory + x + "/" + f_n)
        counter = counter + 1

    return f

# Then put the bus informaion into an array
def access_json_info(file_name):
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
def get_passenger_count(data):
    data = data['MonitoredVehicleJourney']
    if 'MonitoredCall' in data:
        data2 = data['MonitoredCall']
        if 'Extensions' in data2:
            data3 = data2['Extensions']
            if 'Capacities' in data3:
                return data3['Capacities']['EstimatedPassengerCount']
    return "null"

def get_stop_point_name(data):
    data = data['MonitoredVehicleJourney']
    if 'MonitoredCall' in data:
        return data['MonitoredCall']['StopPointName']
    return "null"

def get_stop_point_ref(data):
    data = data['MonitoredVehicleJourney']
    if 'MonitoredCall' in data:
        return data['MonitoredCall']['StopPointRef']
    return "null"

def get_destination_name(data):
    if 'DestinationName' in data['MonitoredVehicleJourney']:
        return data['MonitoredVehicleJourney']['DestinationName']
    return "null"

def get_journey_pattern_ref(data):
    if 'JourneyPatternRef'in data['MonitoredVehicleJourney']:
        return data['MonitoredVehicleJourney']['JourneyPatternRef']
    return "NoJourneyPatternRef"

def get_response_time_stamp(data):
    return data['RecordedAtTime']

def get_vehicle_ref(data):
    return data['MonitoredVehicleJourney']['VehicleRef']

def get_line_ref(data):
    return data['MonitoredVehicleJourney']['LineRef']

def get_published_line_name(data):
    return data['MonitoredVehicleJourney']['PublishedLineName']

def get_longitude(data):
    return data['MonitoredVehicleJourney']['VehicleLocation']['Longitude']

def get_latitude(data):
    return data['MonitoredVehicleJourney']['VehicleLocation']['Latitude']

def get_primary_key(data):
    string_date = get_response_time_stamp(data)
    vehicle_ref = get_vehicle_ref(data)
    line_ref = get_line_ref(data)

    temp = string_date[0:string_date.rfind('-')]
    date = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')
    primary_key = str(date.date()) + str(date.hour) + str(date.minute) + " " + str(vehicle_ref) + " " + str(line_ref)
    return primary_key

def add_json_info_into_SQL():
    array = []
    path_directories = create_list_of_all_paths()
    for paths in path_directories:
        if not paths.__contains__("/.DS_Store"):
            bus_data = access_json_info(paths)
            for data in bus_data:
                    # code to enter things into DB
                    information_for_files(data)
                    pass
    return array


def information_for_files(data):
    dictionary = {"Primary Key": get_primary_key(data),
             "Response Time": get_response_time_stamp(data),
             "Vehicle Ref": get_vehicle_ref(data),
             "Line Ref": get_line_ref(data),
             "Published Line Ref": get_published_line_name(data),
             "Passenger Count": get_passenger_count(data),
             "Latitude": get_latitude(data),
             "Longitude": get_longitude(data),
             "Stop Point Name": get_stop_point_name(data),
             "Stop Point Ref": get_stop_point_ref(data),
             "Destination Name": get_destination_name(data),
             "Journey Pattern Ref": get_journey_pattern_ref(data)}

    file = open("info.txt", "a")
    file.writelines(str(dictionary))
    file.writelines("\n")
    file.close()



add_json_info_into_SQL()

# for each folder
#   for each file
#       for each data
#           insert into sql








