import json
import requests



API_access = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=f3cd89cf-147d-40bf-8557-5431e990e24f&VehicleRef=MTABC_6242"

response = requests.get(API_access)


data = response.json()

data = response.json()
with open('saved_json_data.txt', 'w') as outfile:
    json.dump(data, outfile)


# All Line References and Published Line Names

# List of all vehicle references

# Getting and Saving Crowding data

# Getting Location Data

#Getting Accessing Vehicle Monitoring
with open('saved_json_data.txt') as json_file:
    data = json.load(json_file)

bus_data = data['Siri']['ServiceDelivery']

# This tells us how many different buses was monitored at this time
print(bus_data['ResponseTimestamp'])

#define the function of Accesing Vehicle Monitoring
def accessing_vechicle_monitoring(bus_data):
    time = bus_data['ResponseTimestamp']
    my_name = "";
    my_name += "VM" + time + ".txt"
    with open(my_name,'w') as outfile:
        json.dump(time,outfile)

accessing_vechicle_monitoring(bus_data)