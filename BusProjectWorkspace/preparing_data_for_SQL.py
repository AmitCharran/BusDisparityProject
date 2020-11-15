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
        for (dirpath, dirnames, filenames) in walk(directory + x):  # getting directyory
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

def add_json_info_into_array():
    array = []
    path_directories = create_list_of_all_paths()
    for paths in path_directories:
        if not paths.__contains__("/.DS_Store"):
            bus_data = access_json_info(paths)
            for info in bus_data:
                array.append(info)

    return array

# Get data for SQL table
def get_passenger_count(data):
    data = data['MonitoredVehicleJourney']
    if 'MonitoredCall' in data:
        data2 = data['MonitoredCall']
        if 'Extensions' in data2:
            data3 = data2['Extensions']
            if 'Capacities' in data3:
                return data3['Capacities']['EstimatedPassengerCount']
    return "NoPassengerCountRecorded"


def get_stop_point_name(data):
    data = data['MonitoredVehicleJourney']
    if 'MonitoredCall' in data:
        return data['MonitoredCall']['StopPointName']
    return "NoStopPointName"

def get_stop_point_ref(data):
    data = data['MonitoredVehicleJourney']
    if 'MonitoredCall' in data:
        return data['MonitoredCall']['StopPointRef']
    return "NoStopPointRef"

def get_destination_name(data):
    if 'DestinationName' in data['MonitoredVehicleJourney']:
        return data['MonitoredVehicleJourney']['DestinationName']
    return "NoDestinationName"

def get_journey_pattern_ref(data):
    if 'JourneyPatternRef'in data['MonitoredVehicleJourney']:
        return data['MonitoredVehicleJourney']['JourneyPatternRef']
    return "NoJourneyPatternRef"


def get_data_for_SQL_table():
    all_bus_info = add_json_info_into_array()
    array_of_info_for_SQL_table = []
    for data in all_bus_info:
        response_time_stamp = data['RecordedAtTime']
        vehicle_ref = data['MonitoredVehicleJourney']['VehicleRef']
        line_ref = data['MonitoredVehicleJourney']['LineRef']
        published_line_name =  data['MonitoredVehicleJourney']['PublishedLineName']

        passenger_count = get_passenger_count(data)

        longitue = data['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        latitude = data['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        destination_name = get_destination_name(data)
        journey_pattern_ref = get_journey_pattern_ref(data)

        stop_point_name = get_stop_point_name(data)
        stop_point_ref = get_stop_point_ref(data)

        string_date = response_time_stamp
        temp = string_date[0:string_date.rfind('-')]
        date = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')

        primary_key = str(date.date()) + str(date.hour) + str(date.minute) + str(vehicle_ref) + str(line_ref)

        array = [primary_key, response_time_stamp, vehicle_ref, line_ref, published_line_name, passenger_count, longitue, latitude, destination_name, journey_pattern_ref, stop_point_name, stop_point_ref]
        array_of_info_for_SQL_table.append(array)

    return array_of_info_for_SQL_table


array = get_data_for_SQL_table()
print(len(array))
# Now information is ready to go into SQLTables









