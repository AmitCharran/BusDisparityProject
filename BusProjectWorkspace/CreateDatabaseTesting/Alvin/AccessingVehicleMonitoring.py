import requests
import json


vehicle_monitoring_url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json"

API_key = 'f3cd89cf-147d-40bf-8557-5431e990e24f'

API_access = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=f3cd89cf-147d-40bf-8557-5431e990e24f&VehicleRef=MTABC_6242"

get_all_info_from_vehicle_monitoring = vehicle_monitoring_url + "?key=" + API_key

response = requests.get(get_all_info_from_vehicle_monitoring)


data = response.json()

# This file will get all the bus data from Vehicle Monitoring and reduce it into something we can use

with open('saved_json_data.txt') as json_file:
    data = json.load(json_file)


# bus_data = data['Siri']['ServiceDelivery']
#
# test_data = data[0]['ServiceDelivery']
#
# print(test_data.keys())
#
#
#
#
#
#
# # This tells us how many different buses was monitored at this time
# print(len(bus_data))

# with open('TextFileFolder/reduced_vehicle_monitoring_file.txt', 'w') as outfile:
#     json.dump(bus_data, outfile)
# def get_passenger_count(json_data):
#     for x in json_data:
#         test_data_2 = x['MonitoredVehicleJourney']
#         vehicle_ref = test_data_2['VehicleRef']
#         line_ref = test_data_2['LineRef']
#         if 'MonitoredCall' in test_data_2:
#             test_data_3 = test_data_2['MonitoredCall']
#             if 'Extensions' in test_data_3:
#                 test_data_4 = test_data_3['Extensions']
#                 if 'Capacities' in test_data_4:
#                     print(line_ref + "\t" + vehicle_ref + "\t" + str(test_data_4['Capacities']['EstimatedPassengerCount']))
#
