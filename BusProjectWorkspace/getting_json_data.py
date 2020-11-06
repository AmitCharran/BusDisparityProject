from datetime import datetime
import os
import requests
import json
import time

vehicle_monitoring_url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json"

API_key = 'f3cd89cf-147d-40bf-8557-5431e990e24f'

get_all_info_from_vehicle_monitoring = vehicle_monitoring_url + "?key=" + API_key

response = requests.get(get_all_info_from_vehicle_monitoring)
data = response.json()
starttime = int(round(time.time() * 1000))

counter_calls = 0
while True:
    counter_calls = counter_calls + 1
    print("Request Call Number: " + str(counter_calls))
    string_date = data['Siri']['ServiceDelivery']['ResponseTimestamp']

    temp = string_date[0:string_date.rfind('-')]

    date = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')

    file_name = str(date.hour) + '_' + str(date.minute) + ".json"
    directory = '/home/pi/PycharmProjects/BusDisparityProject/JSON_Data/' + str(date.date())
    if not os.path.isdir(directory):
        os.mkdir(directory)

    if not os.path.isfile(directory + "/" + file_name):
        with open(directory + '/' + file_name,
              'w') as outfile:
            json.dump(data, outfile)

    currenttime = int(round(time.time() * 1000))
    time.sleep(10 - ((currenttime - starttime)/1000))
    starttime = currenttime
