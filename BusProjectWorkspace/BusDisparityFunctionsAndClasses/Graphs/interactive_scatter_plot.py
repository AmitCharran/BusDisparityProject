import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import mysql.connector
from HiddenVariables import hidden_variables
from BusDisparityFunctionsAndClasses.setting_up_sql_connection import mta_bus_project_sql_tables


class scatter_plot:
    def __init__(self):
        self.sql_access = mta_bus_project_sql_tables(hidden_variables.sql_host,
                                                hidden_variables.sql_user,
                                                hidden_variables.sql_password)

    def obtain_values_from_table_as_df(self, table_name):
        value_string = 'SELECT * FROM {};'.format(table_name)
        sql_table = self.sql_access.execute_command(value_string)
        df = pd.DataFrame(sql_table)
        df.columns = self.sql_access.get_column_names()
        return df

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
        val = self.obtain_values_from_table_as_df('bus_average_table')

        #sns.lmplot(data=val.reset_index(), y='total_avg', x='index')
        val = val.sort_values(by='total_avg', ascending=False)

        index_name = val[val['total_avg'] == 0].index
        val = val.drop(index_name)
        sns.scatterplot(data=val, y='total_avg', x='published_line_ref')
        plt.show()

    def interactive_scatter_plot_graph(self):
        val = self.obtain_values_from_table_as_df('bus_average_table')

        array_of_colors = self.add_column_of_colors(val)
        self.add_column_to_df(val, 'Area', array_of_colors)
        val = val.sort_values(by='total_avg', ascending=False)
        index_name = val[val['total_avg'] == 0].index
        val = val.drop(index_name)
        val = val.rename(columns={'published_line_ref': 'Bus Name', 'total_avg': 'Average'})
        graph = px.scatter(data_frame=val.reset_index(), y='Average',  x='Bus Name', color='Area')
        graph.show()


    def add_column_of_colors(self, data_frame):
        array = []
        line_refs = data_frame['published_line_ref'].tolist()

        for bus in line_refs:
            array.append(self.give_color_to_bus_name(bus))
        return array

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




test = scatter_plot()
test.interactive_scatter_plot_graph()









