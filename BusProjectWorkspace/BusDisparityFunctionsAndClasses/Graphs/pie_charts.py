import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import mysql.connector
import ast
from HiddenVariables import hidden_variables
from BusDisparityFunctionsAndClasses.setting_up_sql_connection import mta_bus_project_sql_tables

class pie_chart:
    def __init__(self):
        pass

    def get_data_as_dictionary(self, path):
        file = open(path, 'r')
        lines = file.readlines()
        file.close()
        line = lines[0]
        dictionary = ast.literal_eval(line)
        return dictionary

    def dictionary_to_pandas_for_bar_chart(self, path):
        dictionary = self.get_data_as_dictionary(path)
        keys = [*dictionary]
        df = pd.DataFrame(columns=['Time', 'Borough', 'Passenger Count'])

        for key in keys:
            keys_2 = [*dictionary[key]]
            for key_2 in keys_2:
                df = df.append({'Time': key,
                           'Borough': key_2,
                           'Passenger Count': dictionary[key][key_2]},
                               ignore_index=True)
        return df

    def create_bar_graph(self, path, title =''):
        df = self.dictionary_to_pandas_for_bar_chart(path)

        # df.to_csv('/Users/amitc/Desktop/BusDisparityProject/BusProjectWorkspace/BusDisparityFunctionsAndClasses/Graphs/CSV_files/passenger_count_every_5_minutes.csv')

        index_name = df[df['Borough'] == 'Total'].index
        df = df.drop(index_name)

        graph = px.scatter(df, x='Borough', y='Passenger Count',
                       animation_frame='Time', color='Borough',
                       title=title_name, range_y=[0, 6000])
        graph.update_xaxes(showgrid=False)
        graph.update_yaxes(showgrid=False)

        graph.update_layout(
            title_font_family="Fantasy",)

        graph.write_html('/Users/amitc/Desktop/BusDisparityProject/BusProjectWorkspace/BusDisparityFunctionsAndClasses/Graphs/HTML_file_links/bar_chart.html')
        # graph.write_json('/Users/amitc/Desktop/BusDisparityProject/BusProjectWorkspace/BusDisparityFunctionsAndClasses/Graphs/HTML_file_links/bar_chart.json')


        graph.show()

test = pie_chart()
path = '/Users/amitc/Desktop/BusDisparityProject/BusProjectWorkspace/BusDisparityFunctionsAndClasses/Data/January_22_data/1_22_pie_chart.txt'
# diction = test.get_data_as_dictionary(path)

title_name = 'Passenger Count by Borough every 5 minutes: Data Recorded on Friday January 22, 2020'

test.create_bar_graph(path, title_name)


# print([*diction])
#
# for key in diction.items():
#     print(key)

# data_canada = px.data.gapminder().query("country == 'Canada'")
# fig = px.bar(data_canada, x='year', y='pop')
#
# print(data_canada)