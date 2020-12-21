from datetime import datetime
import os
import requests
import json
import time


class retriving_from_API:
    def __init__(self, key, output_path):
        self.key = key
        self.vehicle_monitoring_url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json"
        self.get_all_info_from_vehicle_monitoring = self.vehicle_monitoring_url + "?key=" + self.key
        self.starttime = int(round(time.time() * 1000))
        self.output_path = output_path
        self.counter_calls = 0

    def write_to_file_exception(self, e):
        exceptionFile = open((self.output_path + 'exception.txt'), 'a')
        exceptionFile.write(str(self.starttime) + " " + str(e) + "\n")
        exceptionFile.close()

    def start_calls(self):

        while True:
            try:
                response = requests.get(self.get_all_info_from_vehicle_monitoring)
            except requests.ConnectionError as e:
                self.write_to_file_exception(e)
            except requests.exceptions.RequestException as e:
                self.write_to_file_exception(e)
            try:
                data = response.json()
            except json.decoder.JSONDecodeError as e:
                self.write_to_file_exception(e)

            self.counter_calls = self.counter_calls + 1

            string_date = data['Siri']['ServiceDelivery']['ResponseTimestamp']

            temp = string_date[0:string_date.rfind('-')]

            date = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')

            file_name = str(date.hour) + '_' + str(date.minute) + ".json"
            directory = self.output_path + str(date.date())
            if not os.path.isdir(directory):
                os.mkdir(directory)

            # Output
            print("Request Call Number: " + str(self.counter_calls))
            print(str(self.starttime) + " " + file_name)

            if not os.path.isfile(directory + "/" + file_name):
                with open(directory + '/' + file_name,
                          'w') as outfile:
                    json.dump(data, outfile)

            currenttime = int(round(time.time() * 1000))
            # pauseTimeInSecond contains the pause time in seconds
            pauseTimeInSecond = 180
            calculatedTime = pauseTimeInSecond - (
                    (currenttime - self.starttime) / 1000)  # currenttime = 105300  starttime = 105200  c - s = 100ms
            if calculatedTime > 0:
                time.sleep(calculatedTime)
                self.starttime = currenttime + (calculatedTime * 1000)
            else:
                time.sleep(pauseTimeInSecond)
                self.starttime = int(round(time.time() * 1000))


