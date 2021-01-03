from datetime import datetime
from BusDisparityFunctionsAndClasses.setting_up_sql_connection import mta_bus_project_sql_tables
from BusDisparityFunctionsAndClasses.preparing_data_for_SQL import format_data
from HiddenVariables import hidden_variables
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

    def start_call_and_write_to_SQL(self):
        format_json = format_data("","")

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

            print("Request Call Number: " + str(self.counter_calls))
            print(str(self.starttime) + " " + temp)

            ## Here I have to parse SQL info
            json_data = json.loads(response.text)
            reduced_json = format_json.reduce_json(json_data)
            counter = 0
            for x in reduced_json:
                counter = counter + 1
                print(counter, end="\r")
                format_json.write_to_sql_with_json_info(x)

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



