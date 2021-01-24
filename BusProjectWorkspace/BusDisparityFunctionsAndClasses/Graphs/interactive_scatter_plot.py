import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import mysql.connector
from HiddenVariables import hidden_variables
from BusDisparityFunctionsAndClasses.setting_up_sql_connection import mta_bus_project_sql_tables

# fbprophet import prophet --> for forecasting data


class scatter_plot:
    def __init__(self):
        pass
        # self.sql_access = mta_bus_project_sql_tables(hidden_variables.sql_host,
        #                                         hidden_variables.sql_user,
        #                                         hidden_variables.sql_password)

    # def obtain_values_from_table_as_df(self, table_name):
    #     value_string = 'SELECT * FROM {};'.format(table_name)
    #     sql_table = self.sql_access.execute_command(value_string)
    #     df = pd.DataFrame(sql_table)
    #     df.columns = self.sql_access.get_column_names()
    #     return df

    def add_column_to_df(self, frame, col_name, col_data_array):
        frame._is_copy = None
        frame[col_name] = col_data_array
        # frame[col_name].tolist()
        # frame = otherFrame[[col_name, col_name2, ...]]

    def create_x_array(self, list):
        new_list = []
        counter = 1
        for i in range(0, len(list)):
            new_list.append(counter)
            counter = counter + 1


    def scatter_plot_graph(self):
        val = pd.read_csv('BusProjectWorkspace/BusDisparityFunctionsAndClasses/Data/bus_average_table1-21-21.csv')

        #sns.lmplot(data=val.reset_index(), y='total_avg', x='index')
        val = val.sort_values(by='total_avg', ascending=False)

        index_name = val[val['total_avg'] == 0].index
        val = val.drop(index_name)
        sns.scatterplot(data=val, y='total_avg', x='published_line_ref')
        plt.show()

    def interactive_scatter_plot_graph(self, csv_path):
        val = pd.read_csv(csv_path)

        array_of_colors = self.add_column_of_colors(val)
        self.add_column_to_df(val, 'Area', array_of_colors)
        val = val.sort_values(by='1_hour', ascending=False)
        index_name = val[val['1_hour'] == 0].index
        val = val.drop(index_name)
        val = val.rename(columns={'published_line_ref': 'Bus Name', '1_hour': 'Average at 1 AM'})
        graph = px.scatter(data_frame=val.reset_index(), y='Average at 1 AM',  x='Bus Name', color='Area')
        graph.show()

    def interactive_scatter_plot_graph_highest(self, csv_path):
        val = pd.read_csv(csv_path)

        array_of_colors = self.add_column_of_colors(val)
        self.add_column_to_df(val, 'Area', array_of_colors)


        val = val.sort_values(by='12_hour', ascending=False)

        # Drops all 0 values
        index_name = val[val['12_hour'] == 0].index
        val = val.drop(index_name)


        val = val.rename(columns={'published_line_ref': 'Bus Name', '12_hour': 'Highest Value at 12 PM'})
        graph = px.scatter(data_frame=val.reset_index(), y='Highest Value at 12 PM',  x='Bus Name', color='Area')
        graph.show()



    def get_data_ready_for_slider_highest(self, dataframe):
        columns = list(dataframe.columns)
        if 'id' in columns:
            columns.remove('id')

        df = pd.DataFrame(columns=['Bus Name', 'Highest Value', 'Hour'])


        hours_number_list = dataframe['highest_val'].tolist()
        string = columns[len(columns) - 1]
        hour_list = [self.replace_x_hour_with_real_time(str(string))] * len(hours_number_list)
        published_list = dataframe[columns[0]].tolist()

        for i in range(0, len(hours_number_list)):
            df = df.append({'Bus Name': published_list[i],
                            'Highest Value': hours_number_list[i],
                            'Hour': hour_list[i]},
                           ignore_index=True)

        for x in columns:
            if x != 'published_line_ref':
                hours_number_list = dataframe[x].tolist()
                published_list = dataframe[columns[0]].tolist()
                hour_list = [self.replace_x_hour_with_real_time(x)] * len(hours_number_list)

                for i in range(0, len(hours_number_list)):
                    df = df.append({'Bus Name': published_list[i],
                                    'Highest Value': hours_number_list[i],
                                    'Hour': hour_list[i]},
                                     ignore_index=True)


        return df

    def get_data_ready_for_slider_average(self, dataframe):
        columns = list(dataframe.columns)
        if 'id' in columns:
            columns.remove('id')


        df = pd.DataFrame(columns=['Bus Name', 'Average', 'Hour'])

        hours_number_list = dataframe['total_avg'].tolist()
        string = columns[len(columns) - 1]
        hour_list = [self.replace_x_hour_with_real_time(str(string))] * len(hours_number_list)
        published_list = dataframe[columns[0]].tolist()

        for i in range(0, len(hours_number_list)):
            df = df.append({'Bus Name': published_list[i],
                            'Average': hours_number_list[i],
                            'Hour': hour_list[i]},
                           ignore_index=True)

        for x in columns:
            if x != 'published_line_ref':
                hours_number_list = dataframe[x].tolist()
                published_list = dataframe[columns[0]].tolist()
                hour_list = [self.replace_x_hour_with_real_time(x)] * len(hours_number_list)
                for i in range(0, len(hours_number_list)):
                    df = df.append({'Bus Name': published_list[i],
                                    'Average': hours_number_list[i],
                                    'Hour': hour_list[i]},
                                     ignore_index=True)
        return df

    def add_column_of_colors(self, data_frame):
        array = []
        line_refs = data_frame['published_line_ref'].tolist()
        for bus in line_refs:
            array.append(self.give_color_to_bus_name(bus))
        return array

    def add_column_of_colors_Bus_Name(self, data_frame):
        array = []
        line_refs = data_frame['Bus Name'].tolist()

        for bus in line_refs:
            array.append(self.give_color_to_bus_name(bus))
        return array

    def interactive_scatter_plot_graph_slider(self, csv_path, title='', annotation_text=''):
        val = pd.read_csv(csv_path)
        val = self.get_data_ready_for_slider_average(val)
        array_of_colors = self.add_column_of_colors_Bus_Name(val)
        self.add_column_to_df(val, 'Area', array_of_colors)
        # val = val.sort_values(by='Average', ascending=False)
        # val = val.sort_values(by='Hour', ascending=)
        # index_name = val[val['Average'] == 0].index
        # val = val.drop(index_name)
        # val = val.rename(columns={'published_line_ref': 'Bus Name', '1_hour': 'Average at 1 AM'})
        graph = px.scatter(data_frame=val.reset_index(), y='Average', x='Bus Name',
                           color='Area', animation_frame='Hour', range_y=[0, 40], title=title)

        graph.add_annotation(text=annotation_text, xref='paper', yref='paper',
                             x=0, y=36,
                             showarrow=False,
                             font=dict(
                                 family="Courier New, monospace",
                                 size=8,
                                 color="#ffffff"
                             ), bordercolor="#c7c7c7",
                             borderwidth=2,
                             borderpad=4,
                             bgcolor="#ff7f0e",
                             opacity=0.8)
        graph.update_xaxes(showgrid=True, zeroline=False)
        graph.update_yaxes(showgrid=False, zeroline=False)

        sliders = [dict(
            pad={"t": 100}
        )]

        graph.update_layout(
            sliders=sliders,
            updatemenus=[dict(
                type="buttons",
                pad={"t": 120}
            )]
        )

        graph.show()

    def interactive_scatter_plot_graph_slider_highest(self, csv_path, title='', annotation_text=''):
        val = pd.read_csv(csv_path)
        val = self.get_data_ready_for_slider_highest(val)
        array_of_colors = self.add_column_of_colors_Bus_Name(val)
        self.add_column_to_df(val, 'Area', array_of_colors)

        # index_name = val[val['Highest Value'] == 0].index
        # val = val.drop(index_name)

        graph = px.scatter(data_frame=val.reset_index(), y='Highest Value', x='Bus Name',
                           color='Area', animation_frame='Hour', range_y=[0, 140], title=title)

        graph.add_annotation(text=annotation_text, xref='paper', yref='paper',
                             x=0, y=136,
                             showarrow=False,
                             font=dict(
                                 family="Courier New, monospace",
                                 size=8,
                                 color="#ffffff"
                             ), bordercolor="#c7c7c7",
                             borderwidth=2,
                             borderpad=4,
                             bgcolor="#ff7f0e",
                             opacity=0.8)
        graph.update_xaxes(showgrid=True, zeroline=False)
        graph.update_yaxes(showgrid=False, zeroline=False)

        sliders = [dict(
            pad={"t": 100}
        )]

        graph.update_layout(
            sliders=sliders,
            updatemenus=[dict(
                type="buttons",
                pad={"t": 120}
            )]
        )

        graph.show()

    def give_color_to_bus_name(self, bus_name):
        if 'Bx' in bus_name:
            return 'Bronx'
        elif 'BM' in bus_name:
            return 'BM buses'
        elif 'QM' in bus_name:
            return 'QM buses'
        elif 'SIM' in bus_name:
            return 'SIM buses'
        elif 'Q' in bus_name:
            return 'Queens'
        elif 'M' in bus_name:
            return 'Manhattan'
        elif 'B' in bus_name:
            return 'Brooklyn'
        elif 'X' in bus_name:
            return 'Express Buses'
        elif 'S' in bus_name:
            return 'Staten Island'
        else:
            return 'Unlabeled'

    def replace_x_hour_with_real_time(self, string):
        if string == '0_hour':
            return '12 AM'
        elif string == '1_hour':
            return '1 AM'
        elif string == '2_hour':
            return '2 AM'
        elif string == '3_hour':
            return '3 AM'
        elif string == '4_hour':
            return '4 AM'
        elif string == '5_hour':
            return '5 AM'
        elif string == '6_hour':
            return '6 AM'
        elif string == '7_hour':
            return '7 AM'
        elif string == '8_hour':
            return '8 AM'
        elif string == '9_hour':
            return '9 AM'
        elif string == '10_hour':
            return '10 AM'
        elif string == '11_hour':
            return '11 AM'
        elif string == '12_hour':
            return '12 AM'
        elif string == '13_hour':
            return '1 PM'
        elif string == '14_hour':
            return '2 PM'
        elif string == '15_hour':
            return '3 PM'
        elif string == '16_hour':
            return '4 PM'
        elif string == '17_hour':
            return '5 PM'
        elif string == '18_hour':
            return '6 PM'
        elif string == '19_hour':
            return '7 PM'
        elif string == '20_hour':
            return '8 PM'
        elif string == '21_hour':
            return '9 PM'
        elif string == '22_hour':
            return '10 PM'
        elif string == '23_hour':
            return '11 PM'
        elif string == 'total_avg':
            return 'All Hours'
        elif string == 'highest_val':
            return 'All Hours'
        else:
            return string





# test = scatter_plot()
#
# recorded_dates = 'Recorded at time:\nOctober 5th - October 10th\nand\nOctober 18th - October 28th'
# test.interactive_scatter_plot_graph_slider('/Users/amitc/Desktop/BusDisparityProject/BusProjectWorkspace/BusDisparityFunctionsAndClasses/Data/bus_average_table1-21-21.csv',
#                                            'Average Bus Ridership, ' + recorded_dates)
#
# test.interactive_scatter_plot_graph_slider_highest('/Users/amitc/Desktop/BusDisparityProject/BusProjectWorkspace/BusDisparityFunctionsAndClasses/Data/bus_highest_table1-21-21.csv',
#                                                    'Highest Recorded Ridership, ' + recorded_dates)
# df = px.data.gapminder()
# print(type(df.columns))
# a= list(df.columns)
# print(a)
#
# a = df['country']
# b = df['year']
# c = pd.concat([a,b], axis=1)
#
# c = c.append({'country': 'Zimbabwe', 'year': 2008}, ignore_index=True)
# print(type(c))
# print(c['country'][0])







