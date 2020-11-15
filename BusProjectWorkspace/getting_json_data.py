from datetime import datetime
import os
import requests
import json
import time

vehicle_monitoring_url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json"

API_key = 'f3cd89cf-147d-40bf-8557-5431e990e24f'

get_all_info_from_vehicle_monitoring = vehicle_monitoring_url + "?key=" + API_key

starttime = int(round(time.time() * 1000))

counter_calls = 0

def writeToFileException(e):
    exceptionFile = open('/home/pi/PycharmProjects/BusDisparityProject/JSON_Data/exceptions.txt', 'a')
    exceptionFile.write(str(starttime) + " " + str(e) + "\n")
    exceptionFile.close()




while True:

    try:
        response = requests.get(get_all_info_from_vehicle_monitoring)
    except requests.ConnectionError as e:
        writeToFileException(e)
    except requests.exceptions.RequestException as e:
        writeToFileException(e)
    try:
        data = response.json()
    except json.decoder.JSONDecodeError as e:
        writeToFileException(e)

    counter_calls = counter_calls + 1

    string_date = data['Siri']['ServiceDelivery']['ResponseTimestamp']

    temp = string_date[0:string_date.rfind('-')]

    date = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')

    file_name = str(date.hour) + '_' + str(date.minute) + ".json"
    directory = '/home/pi/PycharmProjects/BusDisparityProject/JSON_Data/' + str(date.date())
    if not os.path.isdir(directory):
        os.mkdir(directory)

    # Output
    print("Request Call Number: " + str(counter_calls))
    print(str(starttime) + " " + file_name)

    if not os.path.isfile(directory + "/" + file_name):
        with open(directory + '/' + file_name,
                  'w') as outfile:
            json.dump(data, outfile)

    currenttime = int(round(time.time() * 1000))
    # pauseTimeInSecond contains the pause time in seconds
    pauseTimeInSecond = 180
    calculatedTime = pauseTimeInSecond - ((currenttime - starttime)/1000)  # currenttime = 105300  starttime = 105200  c - s = 100ms
    if calculatedTime>0:
        time.sleep(calculatedTime)
        starttime = currenttime + (calculatedTime * 1000)
    else:
        time.sleep(pauseTimeInSecond)
        starttime = int(round(time.time() * 1000))

