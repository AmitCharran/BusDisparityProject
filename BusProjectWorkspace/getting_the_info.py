import json
import ast  # convert string into dictionary
from datetime import datetime


class generate_my_info:
    def __init__(self, file_input_path, file_output_path ):
        self.input_file = file_input_path
        self.output_file = file_output_path

    def generate_line_ref(self):
        array = []
        lines = self.get_info_from_file()
        for line in lines:
            dictionary = ast.literal_eval(line)
            if not array.__contains__(dictionary['Line Ref']):
                array.append(dictionary['Line Ref'])
            if len(array) >= 334:
                break
        return array

    def get_info_from_file(self):
        file = open(self.input_file, 'r')
        lines = file.readlines()
        file.close()
        return lines

    def get_average_bus_ridership(self, line_ref):
        lines = self.get_info_from_file()
        first = True
        avg = 0
        for line in lines:
            dictionary = ast.literal_eval(line)
            if dictionary['Line Ref'] == line_ref and dictionary['Passenger Count'] != 'null':
                if first:
                    avg = dictionary['Passenger Count']
                    first = False
                else:
                    avg = (avg + dictionary['Passenger Count'])/2
        # formatted output
        return avg


    def get_average_ridership_by_time(self, line_ref, time_start, time_end):
        lines = self.get_info_from_file()
        first = True
        avg = 0
        for line in lines:
            dictionary = ast.literal_eval(line)
            current_time_string = dictionary['Response Time']
            temp = current_time_string[0:current_time_string.rfind('-')]
            current_time = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')
            if dictionary['Line Ref'] == line_ref and 'null' != dictionary['Passenger Count'] and time_start < current_time < time_end:
                if first:
                    avg = dictionary['Passenger Count']
                    first = False
                else:
                    avg = (avg + dictionary['Passenger Count']) / 2
        # formatted output
        return avg

    def get_average_ridership_by_hour(self,line_ref, time_start, time_end):
        lines = self.get_info_from_file()
        first = True
        avg = 0
        time_start_for_comparing = int(time_start.hour*60) + int(time_start.minute)
        time_end_for_comparing = int(time_end.hour * 60) + int(time_end.minute)
        for line in lines:
            dictionary = ast.literal_eval(line)
            current_time_string = dictionary['Response Time']
            temp = current_time_string[0:current_time_string.rfind('-')]
            current_time = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')
            current_time_for_comparing_hour =int(current_time.hour *60) + int(current_time.minute)

            if dictionary['Line Ref'] == line_ref and 'null' != dictionary['Passenger Count'] and time_start_for_comparing < current_time_for_comparing_hour < time_end_for_comparing:
                if first:
                    avg = dictionary['Passenger Count']
                    first = False
                else:
                    avg = (avg + dictionary['Passenger Count']) / 2
        # formatted output
        return avg









big_test = generate_my_info("/Users/amitcharran/Desktop/all_info.txt", "output.txt")
small_test = generate_my_info("info.txt", "output.txt")


time_start = datetime(2020, 11, 8, 17, 0)
time_end = datetime(2020, 11, 8, 19, 0)
# print(small_test.get_average_ridership_by_hour('MTABC_Q23', time_start, time_end))
print(big_test.get_average_ridership_by_hour('MTABC_Q23', time_start, time_end))



# big_test.get_average_bus_ridership('MTA NYCT_M86+')

