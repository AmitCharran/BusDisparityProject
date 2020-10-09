import json

with open('TextFileFolder/reduced_vehicle_monitoring_file.txt') as json_file:
    data = json.load(json_file)


test_data = data[0]['MonitoredVehicleJourney']
print(test_data.keys())


# Need function to get all distinct LineRef and map to bus name

# Need function to get all distinct OperatorRef

