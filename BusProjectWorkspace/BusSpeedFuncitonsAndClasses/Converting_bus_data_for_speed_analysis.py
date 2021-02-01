from os import walk  # use walk to go through directories
from datetime import datetime
import time
import sys
from HiddenVariables import hidden_variables
import ast
import pandas as pd
import numpy as np

class bus_data_to_matrix:
    def __init__(self, input_path="", output_path=""):
        self.input_path = input_path
        self.output_path = output_path

    def get_and_convert_data_by_line_ref(self, published_line_ref, input_path='None', output_path='None'):
        if input_path == 'None':
            input_path = self.input_path
        if output_path == 'None':
            output_path = self.output_path

        answer_dictionary = {}
        counter = 0
        destin = []
        ref = []
        with open(input_path) as fp:
            line = fp.readline()

            while line:
                dictionary = ast.literal_eval(line)
                if dictionary['Published Line Ref'] == published_line_ref:

                    if dictionary['Vehicle Ref'] not in answer_dictionary.keys():
                        answer_dictionary[dictionary['Vehicle Ref']] = {}

                    if dictionary['Destination Name'] not in answer_dictionary[dictionary['Vehicle Ref']].keys():
                        answer_dictionary[dictionary['Vehicle Ref']][dictionary['Destination Name']] = {}

                    # if dictionary['Destination Name'] not in destin:
                    #     destin.append(dictionary['Destination Name'])
                    #
                    # if dictionary['Vehicle Ref'] not in ref:
                    #     ref.append(dictionary['Vehicle Ref'])


                    if 'Latitude' not in answer_dictionary[dictionary['Vehicle Ref']][dictionary['Destination Name']].keys():
                        answer_dictionary[dictionary['Vehicle Ref']][dictionary['Destination Name']][
                            'Latitude'] = []


                    if 'Longitude' not in answer_dictionary[dictionary['Vehicle Ref']][dictionary['Destination Name']].keys():
                        answer_dictionary[dictionary['Vehicle Ref']][dictionary['Destination Name']][
                            'Longitude'] = []

                    if 'Response Time' not in answer_dictionary[dictionary['Vehicle Ref']][dictionary['Destination Name']].keys():
                        answer_dictionary[dictionary['Vehicle Ref']][dictionary['Destination Name']][
                            'Response Time'] = []

                    answer_dictionary[dictionary['Vehicle Ref']][dictionary['Destination Name']]['Latitude'].append(dictionary['Latitude'])
                    answer_dictionary[dictionary['Vehicle Ref']][dictionary['Destination Name']][
                        'Longitude'].append(dictionary['Longitude'])
                    answer_dictionary[dictionary['Vehicle Ref']][dictionary['Destination Name']][
                        'Response Time'].append(dictionary['Response Time'])


                line = fp.readline()


        print(answer_dictionary.items())
        print(len(answer_dictionary.keys()))

        f = open(output_path, 'a')
        f.write(str(answer_dictionary))
        f.write('\n')
        f.close()





test = bus_data_to_matrix(input_path='/Users/amitc/Desktop/1_27.txt', output_path='Data/output.txt')

test.get_and_convert_data_by_line_ref('Q23')

