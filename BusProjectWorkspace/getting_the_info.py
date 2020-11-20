import json
import ast  # convert string into dictionary
import pandas as pd
from datetime import datetime


class generate_my_info:
    def __init__(self, file_input_path, file_output_path):
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
                    avg = (avg + dictionary['Passenger Count']) / 2
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
            if dictionary['Line Ref'] == line_ref and 'null' != dictionary[
                'Passenger Count'] and time_start < current_time < time_end:
                if first:
                    avg = dictionary['Passenger Count']
                    first = False
                else:
                    avg = (avg + dictionary['Passenger Count']) / 2
        return avg

    def get_average_ridership_by_hour(self, line_ref, time_start, time_end):
        lines = self.get_info_from_file()
        first = True
        avg = 0
        time_start_for_comparing = int(time_start.hour * 60) + int(time_start.minute)
        time_end_for_comparing = int(time_end.hour * 60) + int(time_end.minute)
        for line in lines:
            dictionary = ast.literal_eval(line)
            current_time_string = dictionary['Response Time']
            temp = current_time_string[0:current_time_string.rfind('-')]
            current_time = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')
            current_time_for_comparing_hour = int(current_time.hour * 60) + int(current_time.minute)

            if dictionary['Line Ref'] == line_ref and 'null' != dictionary[
                'Passenger Count'] and time_start_for_comparing < current_time_for_comparing_hour < time_end_for_comparing:
                if first:
                    avg = dictionary['Passenger Count']
                    first = False
                else:
                    avg = (avg + dictionary['Passenger Count']) / 2
        # formatted output
        return avg

    def generate_all_bus_disparity_info_separated_by_hour(self):
        dictionary = {}
        lines = self.get_info_from_file()
        hour_hashmap = self.generate_hour_hashmap()
        for line in lines:
            info_from_lines = ast.literal_eval(line)
            published_line_ref = info_from_lines['Published Line Ref']

            if not dictionary.__contains__(published_line_ref):
                self.add_published_line_ref_to_dictionary(dictionary, published_line_ref)

            current_time_string = info_from_lines['Response Time']
            temp = current_time_string[0:current_time_string.rfind('-')]
            current_time = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')
            hour = current_time.hour

            if 'null' != info_from_lines['Passenger Count']:
                if dictionary[published_line_ref][hour_hashmap[hour]] == 0:
                    dictionary[published_line_ref][hour_hashmap[hour]] = info_from_lines['Passenger Count']
                else:
                    dictionary[published_line_ref][hour_hashmap[hour]] = (dictionary[published_line_ref][
                                                                              hour_hashmap[hour]] + info_from_lines[
                                                                              'Passenger Count']) / 2

        return dictionary

    def generate_all_bus_disparity_info_separated_by_hour(self, output_path):
        dictionary = {}
        dictionary_counter = {}
        lines = self.get_info_from_file()
        hour_hashmap = self.generate_hour_hashmap()
        for line in lines:
            info_from_lines = ast.literal_eval(line)
            published_line_ref = info_from_lines['Published Line Ref']

            current_time_string = info_from_lines['Response Time']
            temp = current_time_string[0:current_time_string.rfind('-')]
            current_time = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')
            hour = current_time.hour

            if not dictionary.__contains__(published_line_ref):
                self.add_published_line_ref_to_dictionary(dictionary, published_line_ref)
                self.add_published_line_ref_to_dictionary(dictionary_counter, published_line_ref)

            if 'null' != info_from_lines['Passenger Count']:
                if dictionary[published_line_ref][hour_hashmap[hour]] == 0:
                    dictionary[published_line_ref][hour_hashmap[hour]] = info_from_lines['Passenger Count']
                    dictionary_counter[published_line_ref][hour_hashmap[hour]] = 1
                else:
                    # (size * average + new_value)/ (size + 1)
                    dictionary[published_line_ref][hour_hashmap[hour]] = ((dictionary_counter[published_line_ref][
                                                                               hour_hashmap[hour]] *
                                                                           dictionary[published_line_ref][
                                                                               hour_hashmap[hour]]) + info_from_lines[
                                                                              'Passenger Count']) / (dictionary_counter[
                                                                                                         published_line_ref][
                                                                                                         hour_hashmap[
                                                                                                             hour]] + 1)
                    dictionary[published_line_ref][hour_hashmap[hour]] += 1

        self.write_to_file_disparity_by_hour(dictionary, output_path)

    def generate_all_bus_disparity_info_separated_by_hour(self, output_path_weekday, output_path_weekend):
        dictionary = {}
        dictionary_counter = {}
        dictionary_weekend = {}
        dictionary_weekend_counter = {}
        lines = self.get_info_from_file()
        hour_hashmap = self.generate_hour_hashmap()
        for line in lines:
            info_from_lines = ast.literal_eval(line)
            published_line_ref = info_from_lines['Published Line Ref']

            current_time_string = info_from_lines['Response Time']
            temp = current_time_string[0:current_time_string.rfind('-')]
            current_time = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')
            hour = current_time.hour

            if self.is_weekday(current_time):
                self.add_bus_line_to_dictionary(dictionary, dictionary_counter, published_line_ref)
            else:
                self.add_bus_line_to_dictionary(dictionary_weekend, dictionary_weekend_counter, published_line_ref)

            if self.is_weekday(current_time):
                self.update_average(dictionary, dictionary_counter, hour_hashmap, hour, info_from_lines,
                                    published_line_ref)
            else:
                self.update_average(dictionary_weekend, dictionary_weekend_counter, hour_hashmap, hour, info_from_lines,
                                    published_line_ref)

        self.write_to_file_disparity_by_hour(dictionary, output_path_weekday)
        self.write_to_file_disparity_by_hour(dictionary_weekend, output_path_weekend)

        df = pd.read_table(output_path_weekday, sep=',')
        excel_path = output_path_weekday.replace('txt', 'xlsx')
        df.to_excel(excel_path, 'Weekday', index=False)

        df = pd.read_table(output_path_weekend, sep=',')
        excel_path_2 = output_path_weekend.replace('txt', 'xlsx')
        df.to_excel(excel_path_2, 'Weekend', index=False)



    def update_average(self, dictionary, dictionary_counter, hour_hashmap, hour, info_from_lines, published_line_ref):
        if 'null' != info_from_lines['Passenger Count']:
            if dictionary[published_line_ref][hour_hashmap[hour]] == -1:
                dictionary[published_line_ref][hour_hashmap[hour]] = info_from_lines['Passenger Count']
                dictionary_counter[published_line_ref][hour_hashmap[hour]] = 1
            else:
                # (size * average + new_value)/ (size + 1)
                dictionary[published_line_ref][hour_hashmap[hour]] = ((dictionary_counter[published_line_ref][
                                                                           hour_hashmap[hour]] *
                                                                       dictionary[published_line_ref][
                                                                           hour_hashmap[hour]]) + info_from_lines[
                                                                          'Passenger Count']) / (
                                                                             dictionary_counter[published_line_ref][
                                                                                 hour_hashmap[hour]] + 1)
                dictionary[published_line_ref][hour_hashmap[hour]] += 1

    def add_bus_line_to_dictionary(self, dictionary, dictionary_counter, published_line_ref):
        if not dictionary.__contains__(published_line_ref):
            self.add_published_line_ref_to_dictionary(dictionary, published_line_ref)
            self.add_published_line_ref_to_dictionary(dictionary_counter, published_line_ref)

    def add_published_line_ref_to_dictionary(self, dictionary, published_line_ref):
        dictionary[published_line_ref] = {"0-1": -1, "1-2": -1, "2-3": -1, "3-4": -1,
                                          "4-5": -1, "5-6": -1, "6-7": -1, "7-8": -1,
                                          "8-9": -1, "9-10": -1, "10-11": -1, "11-12": -1,
                                          "12-13": -1, "13-14": -1, "14-15": -1, "15-16": -1,
                                          "16-17": -1, "17-18": -1, "18-19": -1, "19-20": -1,
                                          "20-21": -1, "21-22": -1, "22-23": -1, "23-24": -1}

    def generate_hour_hashmap(self):
        hour = {0: "0-1", 1: "1-2", 2: "2-3", 3: "3-4",
                4: "4-5", 5: "5-6", 6: "6-7", 7: "7-8",
                8: "8-9", 9: "9-10", 10: "10-11", 11: "11-12",
                12: "12-13", 13: "13-14", 14: "14-15", 15: "15-16",
                16: "16-17", 17: "17-18", 18: "18-19", 19: "19-20",
                20: "20-21", 21: "21-22", 22: "22-23", 23: "23-24"}
        return hour

    def write_to_file_disparity_by_hour(self, dictionary, output_path):
        file = open(output_path, "w")
        file.writelines('Buses,0-1,1-2,2-3,3-4,4-5,5-6,6-7,7-8,8-9,9-10,10-11,11-12,12-13,13-14,14-15,15-16,16-17,'
                        '17-18,18-19,19-20,20-21,21-22,22-23,23-24\n')
        for key in dictionary:
            string_output = str(key)
            for key2 in dictionary[key]:
                string_output += "," + str(dictionary[key][key2])
            file.writelines(string_output + "\n")
        file.close()

    def is_weekday(self, current_time):
        if current_time.weekday() < 5:
            return True
        else:
            return False


big_test = generate_my_info("/Users/amitcharran/Desktop/all_info.txt", "output.txt")
# small_test = generate_my_info("info.txt", "output.txt")

big_test.generate_all_bus_disparity_info_separated_by_hour("/Users/amitcharran/Desktop/weekday.txt",
                                                           "/Users/amitcharran/Desktop/weekend.txt")
# small_test.generate_all_bus_disparity_info_separated_by_hour("output.txt")
# df = pd.read_table("/Users/amitcharran/Desktop/output2.txt", sep=',')
# df.to_excel('/Users/amitcharran/Desktop/output2.xlsx', 'Sheet1', index=False)
