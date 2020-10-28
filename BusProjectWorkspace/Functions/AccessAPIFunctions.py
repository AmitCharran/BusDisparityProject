import json
import requests

import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="admin",
        password="admin.Fall2020.Fall2020",
        host="localhost",
        port=3306,
        database="Bus_Project"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()


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


# Setter Example (Adding one row)
def add_testingTable_Row(testingTable_PK, name):
    cur.execute("INSERT INTO TestingTable(TestingTable_PK, Name) VALUES (?, ?)",
                (testingTable_PK, name))

#define the function of Accesing Vehicle Monitoring
def accessing_vechicle_monitoring(bus_data):
    time = bus_data['ResponseTimestamp']
    my_name = "";
    my_name += "VM" + time + ".txt"
    #with open(my_name,'w') as outfile:
     #   json.dump(time,outfile)
    add_testingTable_Row(10, my_name)


accessing_vechicle_monitoring(bus_data)

conn.commit()
conn.close()