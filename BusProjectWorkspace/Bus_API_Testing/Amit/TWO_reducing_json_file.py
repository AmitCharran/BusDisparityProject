import json

# This file will get all the bus data from Vehicle Monitoring and reduce it into something we can use

with open('TextFileFolder/saved_json_data.txt') as json_file:
    data = json.load(json_file)

bus_data = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

# This tells us how many different buses was monitored at this time
print(len(bus_data))

with open('TextFileFolder/reduced_vehicle_monitoring_file.txt', 'w') as outfile:
    json.dump(bus_data, outfile)


