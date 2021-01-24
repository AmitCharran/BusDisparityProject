from datetime import datetime
import ast
import math
import mysql.connector
import mariadb
import sys
from mysql.connector import Error
from HiddenVariables import hidden_variables
from BusDisparityFunctionsAndClasses.getting_the_info import generate_to_excel

class mta_bus_project_sql_tables:
    def __init__(self, sql_host='localhost', sql_user='root', sql_password='', connection='mariadb', sql_port=3306, starting_database='mta_bus_project'):
        if connection == 'mysql':
            self.mydb = mysql.connector.connect(
                host=sql_host,
                user=sql_user,
                password=sql_password
            )
        elif connection == 'mariadb':
            self.mydb = mariadb.connect(
                user=sql_user,
                password=sql_password,
                host=sql_host,
                port=sql_port,
                database=starting_database
            )
        else:
            print('For connection choose either "mysql" or "mariadb"')
            quit()

        self.current_database = starting_database
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute('USE {};'.format(starting_database))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.mycursor.close()
        self.mydb.close()


    def create_main_table(self):
        string = "CREATE TABLE main_table (" \
                 "id varchar(255) NOT NULL," \
                 "response_time varchar(255)," \
                 "vehicle_ref varchar(255)," \
                 "line_ref varchar(255)," \
                 "published_line_ref varchar(255)," \
                 "passenger_count int," \
                 "latitude float," \
                 "longitude float," \
                 "stop_point_name varchar(255)," \
                 "destination_name varchar(255)," \
                 "journey_pattern_ref varchar(255)," \
                 "PRIMARY KEY (id));"
        self.mycursor.execute(string)
        self.mydb.commit()

    def count_current_table(self, table_name='main_table'):
        print("If no argument, table defaults to 'main_table'")
        self.mycursor.execute('SELECT COUNT(*) from {};'.format(table_name))
        for x in self.mycursor:
            print(x)

    def show_by_line_ref(self):
        self.mycursor.execute('SELECT * FROM main_table WHERE published_line_ref=\"Q25\"')

        for x in self.mycursor:
            print(x[0])

    def create_bus_average_table(self):
        # table name = bus_average_table table_columns:
            # id (NOT NULL) auto increment
            # line_ref
            # 0-23 (so 24 other columns)
            # total_avg column
        string = "CREATE TABLE bus_average_table (" \
                 "id int NOT NULL AUTO_INCREMENT," \
                 "published_line_ref varchar(255) NOT NULL," \
                 "0_hour float," \
                 "1_hour float," \
                 "2_hour float," \
                 "3_hour float," \
                 "4_hour float," \
                 "5_hour float," \
                 "6_hour float," \
                 "7_hour float," \
                 "8_hour float," \
                 "9_hour float," \
                 "10_hour float," \
                 "11_hour float," \
                 "12_hour float," \
                 "13_hour float," \
                 "14_hour float," \
                 "15_hour float," \
                 "16_hour float," \
                 "17_hour float," \
                 "18_hour float," \
                 "19_hour float," \
                 "20_hour float," \
                 "21_hour float," \
                 "22_hour float," \
                 "23_hour float," \
                 "total_avg float," \
                 "PRIMARY KEY (id));"
        self.mycursor.execute(string)
        self.mydb.commit()

    def create_bus_table(self):
        string = "CREATE TABLE bus_table (" \
                 "id int NOT NULL AUTO_INCREMENT," \
                 "published_line_ref varchar(255) NOT NULL," \
                 "0_hour int," \
                 "1_hour int," \
                 "2_hour int," \
                 "3_hour int," \
                 "4_hour int," \
                 "5_hour int," \
                 "6_hour int," \
                 "7_hour int," \
                 "8_hour int," \
                 "9_hour int," \
                 "10_hour int," \
                 "11_hour int," \
                 "12_hour int," \
                 "13_hour int," \
                 "14_hour int," \
                 "15_hour int," \
                 "16_hour int," \
                 "17_hour int," \
                 "18_hour int," \
                 "19_hour int," \
                 "20_hour int," \
                 "21_hour int," \
                 "22_hour int," \
                 "23_hour int," \
                 "total int," \
                 "PRIMARY KEY (id));"
        self.mycursor.execute(string)
        self.mydb.commit()

    def create_bus_weekend_table(self):
        string = "CREATE TABLE bus_weekend_table (" \
                 "id int NOT NULL AUTO_INCREMENT," \
                 "published_line_ref varchar(255) NOT NULL," \
                 "0_hour int," \
                 "1_hour int," \
                 "2_hour int," \
                 "3_hour int," \
                 "4_hour int," \
                 "5_hour int," \
                 "6_hour int," \
                 "7_hour int," \
                 "8_hour int," \
                 "9_hour int," \
                 "10_hour int," \
                 "11_hour int," \
                 "12_hour int," \
                 "13_hour int," \
                 "14_hour int," \
                 "15_hour int," \
                 "16_hour int," \
                 "17_hour int," \
                 "18_hour int," \
                 "19_hour int," \
                 "20_hour int," \
                 "21_hour int," \
                 "22_hour int," \
                 "23_hour int," \
                 "total int," \
                 "PRIMARY KEY (id));"
        self.mycursor.execute(string)
        self.mydb.commit()

    def create_bus_weekday_table(self):
        string = "CREATE TABLE bus_weekday_table (" \
                 "id int NOT NULL AUTO_INCREMENT," \
                 "published_line_ref varchar(255) NOT NULL," \
                 "0_hour int," \
                 "1_hour int," \
                 "2_hour int," \
                 "3_hour int," \
                 "4_hour int," \
                 "5_hour int," \
                 "6_hour int," \
                 "7_hour int," \
                 "8_hour int," \
                 "9_hour int," \
                 "10_hour int," \
                 "11_hour int," \
                 "12_hour int," \
                 "13_hour int," \
                 "14_hour int," \
                 "15_hour int," \
                 "16_hour int," \
                 "17_hour int," \
                 "18_hour int," \
                 "19_hour int," \
                 "20_hour int," \
                 "21_hour int," \
                 "22_hour int," \
                 "23_hour int," \
                 "total int," \
                 "PRIMARY KEY (id));"
        self.mycursor.execute(string)
        self.mydb.commit()

    def create_bus_weekday_average_table(self):
        string = "CREATE TABLE bus_weekday_average_table (" \
                 "id int NOT NULL AUTO_INCREMENT," \
                 "published_line_ref varchar(255) NOT NULL," \
                 "0_hour float," \
                 "1_hour float," \
                 "2_hour float," \
                 "3_hour float," \
                 "4_hour float," \
                 "5_hour float," \
                 "6_hour float," \
                 "7_hour float," \
                 "8_hour float," \
                 "9_hour float," \
                 "10_hour float," \
                 "11_hour float," \
                 "12_hour float," \
                 "13_hour float," \
                 "14_hour float," \
                 "15_hour float," \
                 "16_hour float," \
                 "17_hour float," \
                 "18_hour float," \
                 "19_hour float," \
                 "20_hour float," \
                 "21_hour float," \
                 "22_hour float," \
                 "23_hour float," \
                 "total_avg float," \
                 "PRIMARY KEY (id));"
        self.mycursor.execute(string)
        self.mydb.commit()

    def create_bus_weekend_average_table(self):
        string = "CREATE TABLE bus_weekend_average_table (" \
                 "id int NOT NULL AUTO_INCREMENT," \
                 "published_line_ref varchar(255) NOT NULL," \
                 "0_hour float," \
                 "1_hour float," \
                 "2_hour float," \
                 "3_hour float," \
                 "4_hour float," \
                 "5_hour float," \
                 "6_hour float," \
                 "7_hour float," \
                 "8_hour float," \
                 "9_hour float," \
                 "10_hour float," \
                 "11_hour float," \
                 "12_hour float," \
                 "13_hour float," \
                 "14_hour float," \
                 "15_hour float," \
                 "16_hour float," \
                 "17_hour float," \
                 "18_hour float," \
                 "19_hour float," \
                 "20_hour float," \
                 "21_hour float," \
                 "22_hour float," \
                 "23_hour float," \
                 "total_avg float," \
                 "PRIMARY KEY (id));"
        self.mycursor.execute(string)
        self.mydb.commit()

    def create_bus_highest_table(self):
        string = "CREATE TABLE bus_highest_table (" \
                 "id int NOT NULL AUTO_INCREMENT," \
                 "published_line_ref varchar(255) NOT NULL," \
                 "0_hour int," \
                 "1_hour int," \
                 "2_hour int," \
                 "3_hour int," \
                 "4_hour int," \
                 "5_hour int," \
                 "6_hour int," \
                 "7_hour int," \
                 "8_hour int," \
                 "9_hour int," \
                 "10_hour int," \
                 "11_hour int," \
                 "12_hour int," \
                 "13_hour int," \
                 "14_hour int," \
                 "15_hour int," \
                 "16_hour int," \
                 "17_hour int," \
                 "18_hour int," \
                 "19_hour int," \
                 "20_hour int," \
                 "21_hour int," \
                 "22_hour int," \
                 "23_hour int," \
                 "highest_val int," \
                 "PRIMARY KEY (id));"
        self.mycursor.execute(string)
        self.mydb.commit()

    def create_bus_weekday_highest_table(self):
        string = "CREATE TABLE bus_weekday_highest_table (" \
                 "id int NOT NULL AUTO_INCREMENT," \
                 "published_line_ref varchar(255) NOT NULL," \
                 "0_hour int," \
                 "1_hour int," \
                 "2_hour int," \
                 "3_hour int," \
                 "4_hour int," \
                 "5_hour int," \
                 "6_hour int," \
                 "7_hour int," \
                 "8_hour int," \
                 "9_hour int," \
                 "10_hour int," \
                 "11_hour int," \
                 "12_hour int," \
                 "13_hour int," \
                 "14_hour int," \
                 "15_hour int," \
                 "16_hour int," \
                 "17_hour int," \
                 "18_hour int," \
                 "19_hour int," \
                 "20_hour int," \
                 "21_hour int," \
                 "22_hour int," \
                 "23_hour int," \
                 "highest_val int," \
                 "PRIMARY KEY (id));"
        self.mycursor.execute(string)
        self.mydb.commit()

    def create_bus_weekend_highest_table(self):
        string = "CREATE TABLE bus_weekend_highest_table (" \
                 "id int NOT NULL AUTO_INCREMENT," \
                 "published_line_ref varchar(255) NOT NULL," \
                 "0_hour int," \
                 "1_hour int," \
                 "2_hour int," \
                 "3_hour int," \
                 "4_hour int," \
                 "5_hour int," \
                 "6_hour int," \
                 "7_hour int," \
                 "8_hour int," \
                 "9_hour int," \
                 "10_hour int," \
                 "11_hour int," \
                 "12_hour int," \
                 "13_hour int," \
                 "14_hour int," \
                 "15_hour int," \
                 "16_hour int," \
                 "17_hour int," \
                 "18_hour int," \
                 "19_hour int," \
                 "20_hour int," \
                 "21_hour int," \
                 "22_hour int," \
                 "23_hour int," \
                 "highest_val int," \
                 "PRIMARY KEY (id));"
        self.mycursor.execute(string)
        self.mydb.commit()

    def create_bus_articulated_table(self):
        string = "CREATE TABLE bus_articulated_table (" \
                 "id int NOT NULL AUTO_INCREMENT," \
                 "published_line_ref varchar(255) NOT NULL," \
                 "0_hour int," \
                 "1_hour int," \
                 "2_hour int," \
                 "3_hour int," \
                 "4_hour int," \
                 "5_hour int," \
                 "6_hour int," \
                 "7_hour int," \
                 "8_hour int," \
                 "9_hour int," \
                 "10_hour int," \
                 "11_hour int," \
                 "12_hour int," \
                 "13_hour int," \
                 "14_hour int," \
                 "15_hour int," \
                 "16_hour int," \
                 "17_hour int," \
                 "18_hour int," \
                 "19_hour int," \
                 "20_hour int," \
                 "21_hour int," \
                 "22_hour int," \
                 "23_hour int," \
                 "contains int," \
                 "PRIMARY KEY (id));"
        self.mycursor.execute(string)
        self.mydb.commit()

    def create_bus_weekday_articulated_table(self):
        string = "CREATE TABLE bus_weekday_articulated_table (" \
                 "id int NOT NULL AUTO_INCREMENT," \
                 "published_line_ref varchar(255) NOT NULL," \
                 "0_hour int," \
                 "1_hour int," \
                 "2_hour int," \
                 "3_hour int," \
                 "4_hour int," \
                 "5_hour int," \
                 "6_hour int," \
                 "7_hour int," \
                 "8_hour int," \
                 "9_hour int," \
                 "10_hour int," \
                 "11_hour int," \
                 "12_hour int," \
                 "13_hour int," \
                 "14_hour int," \
                 "15_hour int," \
                 "16_hour int," \
                 "17_hour int," \
                 "18_hour int," \
                 "19_hour int," \
                 "20_hour int," \
                 "21_hour int," \
                 "22_hour int," \
                 "23_hour int," \
                 "contains int," \
                 "PRIMARY KEY (id));"
        self.mycursor.execute(string)
        self.mydb.commit()

    def create_bus_weekend_articulated_table(self):
        # table name = bus_average_table table_columns:
        string = "CREATE TABLE bus_weekend_articulated_table (" \
                 "id int NOT NULL AUTO_INCREMENT," \
                 "published_line_ref varchar(255) NOT NULL," \
                 "0_hour int," \
                 "1_hour int," \
                 "2_hour int," \
                 "3_hour int," \
                 "4_hour int," \
                 "5_hour int," \
                 "6_hour int," \
                 "7_hour int," \
                 "8_hour int," \
                 "9_hour int," \
                 "10_hour int," \
                 "11_hour int," \
                 "12_hour int," \
                 "13_hour int," \
                 "14_hour int," \
                 "15_hour int," \
                 "16_hour int," \
                 "17_hour int," \
                 "18_hour int," \
                 "19_hour int," \
                 "20_hour int," \
                 "21_hour int," \
                 "22_hour int," \
                 "23_hour int," \
                 "contains int," \
                 "PRIMARY KEY (id));"
        self.mycursor.execute(string)
        self.mydb.commit()

    def create_bus_weekend_counter_table(self):
        # table name = bus_average_table table_columns:
        string = "CREATE TABLE bus_weekend_counter_table (" \
                 "id int NOT NULL AUTO_INCREMENT," \
                 "published_line_ref varchar(255) NOT NULL," \
                 "0_hour int," \
                 "1_hour int," \
                 "2_hour int," \
                 "3_hour int," \
                 "4_hour int," \
                 "5_hour int," \
                 "6_hour int," \
                 "7_hour int," \
                 "8_hour int," \
                 "9_hour int," \
                 "10_hour int," \
                 "11_hour int," \
                 "12_hour int," \
                 "13_hour int," \
                 "14_hour int," \
                 "15_hour int," \
                 "16_hour int," \
                 "17_hour int," \
                 "18_hour int," \
                 "19_hour int," \
                 "20_hour int," \
                 "21_hour int," \
                 "22_hour int," \
                 "23_hour int," \
                 "total_count int," \
                 "PRIMARY KEY (id));"
        self.mycursor.execute(string)
        self.mydb.commit()

    def create_bus_weekday_counter_table(self):
        # table name = bus_average_table table_columns:
        string = "CREATE TABLE bus_weekday_counter_table (" \
                 "id int NOT NULL AUTO_INCREMENT," \
                 "published_line_ref varchar(255) NOT NULL," \
                 "0_hour int," \
                 "1_hour int," \
                 "2_hour int," \
                 "3_hour int," \
                 "4_hour int," \
                 "5_hour int," \
                 "6_hour int," \
                 "7_hour int," \
                 "8_hour int," \
                 "9_hour int," \
                 "10_hour int," \
                 "11_hour int," \
                 "12_hour int," \
                 "13_hour int," \
                 "14_hour int," \
                 "15_hour int," \
                 "16_hour int," \
                 "17_hour int," \
                 "18_hour int," \
                 "19_hour int," \
                 "20_hour int," \
                 "21_hour int," \
                 "22_hour int," \
                 "23_hour int," \
                 "total_count int," \
                 "PRIMARY KEY (id));"
        self.mycursor.execute(string)
        self.mydb.commit()

    def create_bus_counter_table(self):
        string = "CREATE TABLE bus_counter_table (" \
                 "id int NOT NULL AUTO_INCREMENT," \
                 "published_line_ref varchar(255) NOT NULL," \
                 "0_hour int," \
                 "1_hour int," \
                 "2_hour int," \
                 "3_hour int," \
                 "4_hour int," \
                 "5_hour int," \
                 "6_hour int," \
                 "7_hour int," \
                 "8_hour int," \
                 "9_hour int," \
                 "10_hour int," \
                 "11_hour int," \
                 "12_hour int," \
                 "13_hour int," \
                 "14_hour int," \
                 "15_hour int," \
                 "16_hour int," \
                 "17_hour int," \
                 "18_hour int," \
                 "19_hour int," \
                 "20_hour int," \
                 "21_hour int," \
                 "22_hour int," \
                 "23_hour int," \
                 "total_count int," \
                 "PRIMARY KEY (id));"
        self.mycursor.execute(string)
        self.mydb.commit()

    def generate_values_to_SQL(self, published_line_ref):
        self.mycursor.execute("SELECT COUNT(*) FROM bus_average_table"
                              " WHERE published_line_ref = '{}'".format(published_line_ref))

        ## if count >= 1 return. Already in database, return
        exists = self.mycursor.fetchall()
        if exists[0][0] > 0:
            print(published_line_ref + " is already in database")
            return

        # Variables: total - bus_counter - avg
        total = 0
        bus_counter = 0

        array_weekday = [0] * 24  # this is per hour
        array_counter_weekday = [0] * 24  # this is per hour
        array_highest_val_weekday = [0] * 24
        array_check_art_bus_weekday = [0] * 24  # checking for articulated buses

        array_weekend = [0] * 24
        array_counter_weekend = [0] * 24
        array_highest_val_weekend = [0] * 24
        array_check_art_bus_weekend = [0] * 24

        func = generate_to_excel("", "")
        list_of_articulated_bus = list(func.create_list_of_articulated_buses())

        self.mycursor.execute('SELECT * FROM main_table WHERE published_line_ref="{}"'.format(published_line_ref))
        for x in self.mycursor:
            if x[5]:
                total = total + x[5]
                if self.weekday(x[1]):
                    bus_counter = bus_counter + 1
                    self.add_value_at_time(x, array_weekday, array_counter_weekday)
                    self.highest_val(x, array_highest_val_weekday)
                    self.set_articulated(x, array_check_art_bus_weekday, list_of_articulated_bus)
                    ## bus_lowest_val_counter
                else:
                    bus_counter = bus_counter + 1
                    self.add_value_at_time(x, array_weekend, array_counter_weekend)
                    self.highest_val(x, array_highest_val_weekend)
                    self.set_articulated(x, array_check_art_bus_weekend, list_of_articulated_bus)

        array_total = [0] * 24
        array_counter_total = [0] * 24
        array_articulated_total = [0] * 24
        array_highest_val_total = [0] * 24
        for i in range(24):
            array_total[i] = array_weekday[i] + array_weekend[i]
            array_counter_total[i] = array_counter_weekday[i] + array_counter_weekend[i]
            if array_articulated_total[i] != 1 and (array_check_art_bus_weekday[i] == 1 or array_check_art_bus_weekend[i] == 1):
                array_articulated_total[i] = 1

            if array_highest_val_weekend[i] > array_highest_val_weekday[i]:
                array_highest_val_total[i] = array_highest_val_weekend[i]
            else:
                array_highest_val_total[i] = array_highest_val_weekday[i]



        ## enter into table function for total
        self.enter_total_values_into_table(published_line_ref, array_total, array_counter_total, array_highest_val_total, array_articulated_total)

        ## enter into table for weekend
        self.enter_weekday_values_into_table(published_line_ref, array_weekday, array_counter_weekday, array_highest_val_weekday, array_check_art_bus_weekday)
        ## enter into table for weekday
        self.enter_weekend_values_into_table(published_line_ref, array_weekend, array_counter_weekend, array_highest_val_weekend, array_check_art_bus_weekend)

        print("finished {}".format(published_line_ref))

    def enter_total_values_into_table(self, x, array, array_counter, array_highest, array_articulated):
        array_avg = [0] * 24
        total = 0
        total_counter = 0
        for i in range(24):
            total = total + array[i]
            total_counter = total_counter + array_counter[i]
            if array_counter[i] != 0:
                array_avg[i] = array[i]/array_counter[i]
            else:
                array_avg[i] = 0

        total_avg = 0
        if total_counter != 0:
            total_avg = total / total_counter

        # add to avg table
        highest = max(array_highest)
        articulate = max(array_articulated)
        average_string = self.create_insert_string(x, 'bus_average_table', array_avg, total_avg)
        highest_string = self.create_insert_string_highest(x, 'bus_highest_table', array_highest, highest)
        articulate_string = self.create_insert_string_art(x, 'bus_articulated_table', array_articulated, articulate)

        try:
            self.mycursor.execute(average_string)
            self.mydb.commit()
        except:
            #self.mycursor.execute(average_string)
            print("Problem with {} in adding average_total to table".format(x))

        try:
            self.mycursor.execute(highest_string)
            self.mydb.commit()
        except:
            print("Problem with {} in adding highest_total to table".format(x))

        try:
            self.mycursor.execute(articulate_string)
            self.mydb.commit()
        except:
            print("Problem with {} in adding highest_total to table".format(x))

    def enter_weekday_values_into_table(self, x, array, array_counter, array_highest, array_articulated):
        array_avg = [0] * 24
        total = 0
        total_counter = 0
        for i in range(24):
            total = total + array[i]
            total_counter = total_counter + array_counter[i]
            if array_counter[i] != 0:
                array_avg[i] = array[i] / array_counter[i]
            else:
                array_avg[i] = 0

        total_avg = 0
        if total_counter != 0:
            total_avg = total / total_counter

        # add to avg table
        highest = max(array_highest)
        articulate = max(array_articulated)
        average_string = self.create_insert_string(x, 'bus_weekday_average_table', array_avg, total_avg)
        highest_string = self.create_insert_string_highest(x, 'bus_weekday_highest_table', array_highest, highest)
        articulate_string = self.create_insert_string_art(x, 'bus_weekday_articulated_table', array_articulated, articulate)

        try:
            self.mycursor.execute(average_string)
            self.mydb.commit()
        except:
            print("Problem with {} in adding average_weekday to table".format(x))

        try:
            self.mycursor.execute(highest_string)
            self.mydb.commit()
        except:
            print("Problem with {} in adding highest_weekday to table".format(x))

        try:
            self.mycursor.execute(articulate_string)
            self.mydb.commit()
        except:
            print("Problem with {} in adding highest_weekday to table".format(x))

    def enter_weekend_values_into_table(self, x, array, array_counter, array_highest, array_articulated):
        array_avg = [0] * 24
        total = 0
        total_counter = 0
        for i in range(24):
            total = total + array[i]
            total_counter = total_counter + array_counter[i]
            if array_counter[i] != 0:
                array_avg[i] = array[i] / array_counter[i]
            else:
                array_avg[i] = 0

        total_avg = 0
        if total_counter != 0:
            total_avg = total / total_counter

        # add to avg table
        highest = max(array_highest)
        articulate = max(array_articulated)
        average_string = self.create_insert_string(x, 'bus_weekend_average_table', array_avg, total_avg)
        highest_string = self.create_insert_string_highest(x, 'bus_weekend_highest_table', array_highest, highest)
        articulate_string = self.create_insert_string_art(x, 'bus_weekend_articulated_table', array_articulated, articulate)

        try:
            self.mycursor.execute(average_string)
            self.mydb.commit()
        except:
            print("Problem with {} in adding average_weekend to table".format(x))

        try:
            self.mycursor.execute(highest_string)
            self.mydb.commit()
        except:
            print("Problem with {} in adding highest_weekend to table".format(x))

        try:
            self.mycursor.execute(articulate_string)
            self.mydb.commit()
        except:
            print("Problem with {} in adding highest_weekend to table".format(x))


    def create_insert_string(self,pub_line_ref, table_name, array_avg, total_avg):
        string = "INSERT INTO {} (published_line_ref, 0_hour, " \
                 "1_hour, 2_hour, 3_hour, 4_hour, 5_hour, 6_hour, 7_hour, 8_hour, 9_hour," \
                 "10_hour, 11_hour, 12_hour, 13_hour, 14_hour, 15_hour, 16_hour," \
                 "17_hour, 18_hour, 19_hour, 20_hour, 21_hour, 22_hour, 23_hour, total_avg)" \
                 "VALUES ('{}', {}," \
                 "{}, {}, {}, {}, {}, {}, {}, {}, {}," \
                 "{}, {}, {}, {}, {}, {}, {}," \
                 "{}, {}, {}, {}, {}, {}, {}, {});" \
            .format(table_name, pub_line_ref, array_avg[0],
                    array_avg[1], array_avg[2], array_avg[3], array_avg[4], array_avg[5], array_avg[6], array_avg[7], array_avg[8], array_avg[9],
                    array_avg[10], array_avg[11], array_avg[12], array_avg[13], array_avg[14], array_avg[15], array_avg[16],
                    array_avg[17], array_avg[18], array_avg[19], array_avg[20], array_avg[21], array_avg[22],
                    array_avg[23], total_avg)
        return string

    def create_insert_string_highest(self,pub_line_ref, table_name, array_avg, total_avg):
        string = "INSERT INTO {} (published_line_ref, 0_hour, " \
                 "1_hour, 2_hour, 3_hour, 4_hour, 5_hour, 6_hour, 7_hour, 8_hour, 9_hour," \
                 "10_hour, 11_hour, 12_hour, 13_hour, 14_hour, 15_hour, 16_hour," \
                 "17_hour, 18_hour, 19_hour, 20_hour, 21_hour, 22_hour, 23_hour, highest_val)" \
                 "VALUES ('{}', {}," \
                 "{}, {}, {}, {}, {}, {}, {}, {}, {}," \
                 "{}, {}, {}, {}, {}, {}, {}," \
                 "{}, {}, {}, {}, {}, {}, {}, {});" \
            .format(table_name, pub_line_ref, array_avg[0],
                    array_avg[1], array_avg[2], array_avg[3], array_avg[4], array_avg[5], array_avg[6], array_avg[7],
                    array_avg[8], array_avg[9], array_avg[10],
                    array_avg[11], array_avg[12], array_avg[13], array_avg[14], array_avg[15], array_avg[16],
                    array_avg[17], array_avg[18], array_avg[19], array_avg[20], array_avg[21], array_avg[22],
                    array_avg[23], total_avg)
        return string

    def create_insert_string_art(self,pub_line_ref, table_name, array_avg, total_avg):
        string = "INSERT INTO {} (published_line_ref, 0_hour, " \
                 "1_hour, 2_hour, 3_hour, 4_hour, 5_hour, 6_hour, 7_hour, 8_hour, 9_hour," \
                 "10_hour, 11_hour, 12_hour, 13_hour, 14_hour, 15_hour, 16_hour," \
                 "17_hour, 18_hour, 19_hour, 20_hour, 21_hour, 22_hour, 23_hour, contains)" \
                 "VALUES ('{}', {}," \
                 "{}, {}, {}, {}, {}, {}, {}, {}, {}," \
                 "{}, {}, {}, {}, {}, {}, {}," \
                 "{}, {}, {}, {}, {}, {}, {},{});" \
            .format(table_name, pub_line_ref, array_avg[0],
                    array_avg[1], array_avg[2], array_avg[3], array_avg[4], array_avg[5], array_avg[6], array_avg[7],
                    array_avg[8], array_avg[9], array_avg[10],
                    array_avg[11], array_avg[12], array_avg[13], array_avg[14], array_avg[15], array_avg[16],
                    array_avg[17], array_avg[18], array_avg[19], array_avg[20], array_avg[21], array_avg[22],
                    array_avg[23], total_avg)
        return string

    def highest_val(self, x, array):
        string_date = x[1]
        temp = string_date[0:string_date.rfind('-')]
        date = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')

        if array[date.hour] < x[5]:
            array[date.hour] = x[5]

    def set_articulated(self, x, array_check_art_bus, list_of_articulated_bus):
        string_date = x[1]
        temp = string_date[0:string_date.rfind('-')]
        date = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')

        if array_check_art_bus[date.hour] == 1:
            pass
        else:
            if x[2] in list_of_articulated_bus:
                array_check_art_bus[date.hour] = 1

    def weekday(self, x):
        string_date = x
        temp = string_date[0:string_date.rfind('-')]
        date = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')

        weekno = datetime.weekday(date)

        if weekno < 5:
            return True
        else:  # 5 Sat, 6 Sun
            return False

    def add_value_at_time(self, x, array, array_counter):
        string_date = x[1]
        temp = string_date[0:string_date.rfind('-')]
        date = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')

        array[date.hour] = array[date.hour] + x[5]
        array_counter[date.hour] = array_counter[date.hour] + 1

    def generate_list_of_all_published_line_ref(self):
        array = []
        self.mycursor.execute('SELECT DISTINCT published_line_ref FROM bus_table;')
        for x in self.mycursor:
            array.append(x)
        return array

    def get_array_of_line_ref(self):
        array = []
        self.mycursor.execute('SELECT published_line_ref FROM all_published_line_ref;')
        for x in self.mycursor:
            array.append(x[0])
        return array

    def create_table_of_line_ref(self):
        string = "CREATE TABLE all_published_line_ref (published_line_ref varchar(255) NOT NULL," \
                 "line_ref varchar(255)," \
                 "PRIMARY KEY (published_line_ref));"
        self.mycursor.execute(string)
        self.mydb.commit()

    def insert_values_into_published_line_ref(self):
        array = self.generate_list_of_all_published_line_ref()

        for x in array:
            self.mycursor.execute("INSERT INTO all_published_line_ref"
                                  "(published_line_ref, line_ref)"
                                  "VALUES ('{}', '{}');".format(x[0], x[1]))
        self.mydb.commit()

    def execute_command(self, str):
        self.mycursor.execute(str)
        x = self.mycursor.fetchall()
        return x

    def get_column_names(self):
        self.mycursor.column_names
        x = self.mycursor.fetchall()
        return x

    def get_column_names_tablename(self, table_name):
        string = 'SHOW COLUMNS FROM {};'.format(table_name)
        list = self.execute_command(string)
        ans = []
        for x in list:
            ans.append(x[0])
        return ans


    def execute_command_and_commit(self, str):
        self.mycursor.execute(str)
        self.mydb.commit()

    def show_tables(self):
        self.mycursor.execute('SHOW TABLES;')
        for x in self.mycursor:
            print(x)

    def show_all_in_current_table(self, current_table):
        str = 'SELECT * FROM {};'.format(current_table)
        self.mycursor.execute(str)
        for x in self.mycursor:
            print(x)

    def delete_from_table_by_id(self, table_name, id):
        str = 'DELETE FROM {} WHERE id={};'.format(table_name, id)
        self.mycursor(str)
        self.mydb.commit()

    def show_databases(self):
        self.mycursor.execute('SHOW DATABASES;')
        for x in self.mycursor:
            print(x)

    def get_info_from_file(self, file_input_path):
        file = open(file_input_path, 'r')
        lines = file.readlines()
        file.close()
        return lines

    def reset_tables(self):
        print("are you sure you want to reset")
        answer = input("Yes to proceed")
        if answer != 'Yes':
            return


        array = self.generate_list_of_all_published_line_ref()

        self.create_bus_table()
        self.create_bus_weekday_table()
        self.create_bus_weekend_table()
        self.create_bus_counter_table()
        self.create_bus_weekday_counter_table()
        self.create_bus_weekend_counter_table()

        for x in array:
            self.insert_row_of_blanks_to_table(x[0], 'bus_table')
            self.insert_row_of_blanks_to_table(x[0], 'bus_weekend_table')
            self.insert_row_of_blanks_to_table(x[0], 'bus_weekday_table')
            self.insert_row_of_blanks_to_table_counter(x[0], 'bus_counter_table')
            self.insert_row_of_blanks_to_table_counter(x[0], 'bus_weekday_counter_table')
            self.insert_row_of_blanks_to_table_counter(x[0], 'bus_weekend_counter_table')

    def update_values_from_file(self):
        ## get info as dictionary, line by line
        lines = self.get_info_from_file('/Users/amitcharran/Desktop/all_info2.txt')
        print(len(lines))
        counter = 0
        for line in lines:
            counter = counter + 1
            if (counter % 10000) == 0:
                print(counter)
            dictionary = ast.literal_eval(line)
            self.add_to_sql_from_dictionary(dictionary)

    def update_values_from_file_2(self):
        with open('/home/pi/Desktop/all_info2.txt') as fp:
            line = fp.readline()
            counter = 0
            while line:
                counter = counter + 1
                if (counter % 100000) == 0:
                    print(counter)
                dictionary = ast.literal_eval(line)
                self.add_to_sql_from_dictionary(dictionary)
                line = fp.readline()

        pass

    def update_values_from_main_table(self):
        pass

    def add_to_sql_from_dictionary(self, dictionary):
        if dictionary['Passenger Count'] == 'null':
            return

        string_date = dictionary['Response Time']
        temp = string_date[0:string_date.rfind('-')]
        date = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')

        self.update_value_to_table('bus_table', dictionary)
        self.update_counter_value_to_table('bus_counter_table', dictionary)

        if self.weekday(string_date):
            self.update_value_to_table('bus_weekday_table', dictionary)
            self.update_counter_value_to_table('bus_weekday_counter_table', dictionary)
        else:
            self.update_value_to_table('bus_weekend_table', dictionary)
            self.update_counter_value_to_table('bus_weekend_counter_table', dictionary)

    def update_value_to_table(self, table_name, dictionary):
        string_date = dictionary['Response Time']
        temp = string_date[0:string_date.rfind('-')]
        date = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')
        column = self.convert_hour_to_column_name(date.hour)

        pub_line_ref = dictionary['Published Line Ref']

        get_num = 'select {} from {} where published_line_ref = "{}"'.format(column, table_name, pub_line_ref)
        self.mycursor.execute(get_num)
        num = self.mycursor.fetchall()
        current_number = num[0][0]

        passenger_count = dictionary['Passenger Count']
        adding_num = current_number + passenger_count
        string_update_table = "UPDATE {} SET {} = {} WHERE published_line_ref = '{}'".format(table_name, column, adding_num, pub_line_ref)

        self.mycursor.execute(string_update_table)
        self.mydb.commit()

        get_total_num = 'select total from {} where published_line_ref = "{}"'.format(table_name, pub_line_ref)
        self.mycursor.execute(get_total_num)
        num_total = self.mycursor.fetchall()
        current_total_number = num_total[0][0]
        adding_total_num = current_total_number + passenger_count

        string_update_total_table = "UPDATE {} SET total = {} WHERE published_line_ref = '{}'".format(table_name, adding_total_num, pub_line_ref)
        self.mycursor.execute(string_update_total_table)
        self.mydb.commit()

    def update_counter_value_to_table(self, table_name, dictionary):
        string_date = dictionary['Response Time']
        temp = string_date[0:string_date.rfind('-')]
        date = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')
        column = self.convert_hour_to_column_name(date.hour)

        pub_line_ref = dictionary['Published Line Ref']

        get_num = 'select {} from {} where published_line_ref = "{}"'.format(column, table_name, pub_line_ref)
        self.mycursor.execute(get_num)
        num = self.mycursor.fetchall()
        current_number = num[0][0]
        current_number = current_number + 1

        string_update_table = "UPDATE {} SET {} = {} WHERE published_line_ref = '{}'".format(table_name, column,
                                                                                            current_number, pub_line_ref)
        self.mycursor.execute(string_update_table)
        self.mydb.commit()

        get_total_num = 'select total_count from {} where published_line_ref = "{}"'.format(table_name, pub_line_ref)
        self.mycursor.execute(get_total_num)
        num_total = self.mycursor.fetchall()
        current_total_number = num_total[0][0]
        adding_total_num = current_total_number + 1

        string_update_total_table = "UPDATE {} SET total_count = {} WHERE published_line_ref = '{}'".format(table_name,
                                                                                                      adding_total_num,
                                                                                                      pub_line_ref)
        self.mycursor.execute(string_update_total_table)
        self.mydb.commit()

    def testing(self):
        get_num = 'select {} from bus_table where published_line_ref = "{}"'.format("1_hour", "B1")
        self.mycursor.execute(get_num)
        num = self.mycursor.fetchall()
        print(num)
        print(num[0][0])

    def convert_hour_to_column_name(self, hour):
        return str(hour) + "_hour"

    def switching_from_int_to_big_int(self, table_name):
        for x in range(25):
            if x != 24:
                column_name = self.convert_hour_to_column_name(x)
            else:
                column_name = 'total'
            string = 'ALTER TABLE ' + table_name + ' ALTER COLUMN ' + column_name + ' bigint;'
            self.mycursor.execute(string)
            self.mydb.commit()

    def insert_row_of_blanks_to_table(self, pub_line_ref, table_name):
        array_avg = [0] * 24
        string = "INSERT INTO {} (published_line_ref, 0_hour, " \
                 "1_hour, 2_hour, 3_hour, 4_hour, 5_hour, 6_hour, 7_hour, 8_hour, 9_hour," \
                 "10_hour, 11_hour, 12_hour, 13_hour, 14_hour, 15_hour, 16_hour," \
                 "17_hour, 18_hour, 19_hour, 20_hour, 21_hour, 22_hour, 23_hour, total)" \
                 "VALUES ('{}', {}," \
                 "{}, {}, {}, {}, {}, {}, {}, {}, {}," \
                 "{}, {}, {}, {}, {}, {}, {}," \
                 "{}, {}, {}, {}, {}, {}, {}, {});" \
            .format(table_name, pub_line_ref, array_avg[0],
                    array_avg[1], array_avg[2], array_avg[3], array_avg[4], array_avg[5], array_avg[6], array_avg[7],
                    array_avg[8], array_avg[9], array_avg[10],
                    array_avg[11], array_avg[12], array_avg[13], array_avg[14], array_avg[15], array_avg[16],
                    array_avg[17], array_avg[18], array_avg[19], array_avg[20], array_avg[21], array_avg[22],
                    array_avg[23], 0)
        try:
            self.mycursor.execute(string)
            self.mydb.commit()
        except:
            print(pub_line_ref + " already in")

    def insert_row_of_blanks_to_table_counter(self, pub_line_ref, table_name):
        array_avg = [0] * 24
        string = "INSERT INTO {} (published_line_ref, 0_hour, " \
                 "1_hour, 2_hour, 3_hour, 4_hour, 5_hour, 6_hour, 7_hour, 8_hour, 9_hour," \
                 "10_hour, 11_hour, 12_hour, 13_hour, 14_hour, 15_hour, 16_hour," \
                 "17_hour, 18_hour, 19_hour, 20_hour, 21_hour, 22_hour, 23_hour, total_count)" \
                 "VALUES ('{}', {}," \
                 "{}, {}, {}, {}, {}, {}, {}, {}, {}," \
                 "{}, {}, {}, {}, {}, {}, {}," \
                 "{}, {}, {}, {}, {}, {}, {}, {});" \
            .format(table_name, pub_line_ref, array_avg[0],
                    array_avg[1], array_avg[2], array_avg[3], array_avg[4], array_avg[5], array_avg[6], array_avg[7],
                    array_avg[8], array_avg[9], array_avg[10],
                    array_avg[11], array_avg[12], array_avg[13], array_avg[14], array_avg[15], array_avg[16],
                    array_avg[17], array_avg[18], array_avg[19], array_avg[20], array_avg[21], array_avg[22],
                    array_avg[23], 0)
        try:
            self.mycursor.execute(string)
            self.mydb.commit()
        except:
            print(pub_line_ref + " already in")

    def switch_database(self, database_name):
        self.mycursor.execute('USE ' + database_name + ';')
        self.current_database = database_name

    def insert_into_tables(self, primary_key, response_time, vehicle_ref, line_ref, published_line_ref,
                           passenger_count, latitude, longitude, stop_point_name,
                           destination_name, journey_pattern_ref):
        try:
            self.mycursor.execute("INSERT INTO main_table (id, response_time, vehicle_ref, line_ref,"
                                  "published_line_ref, passenger_count, latitude, longitude,"
                                  "stop_point_name, destination_name, journey_pattern_ref) "
                                  "VALUES ('{}','{}','{}','{}',"
                                  "\"{}\",{}, {}, {},"
                                  "\"{}\",\"{}\",\"{}\");"
                                  .format(primary_key, response_time, vehicle_ref, line_ref,
                                          published_line_ref,passenger_count, latitude, longitude,
                                          stop_point_name, destination_name, journey_pattern_ref))
            self.mydb.commit()
        except:
            # Shows which had a problem with
            self.mycursor = self.mydb.cursor(buffered=True)
            self.mycursor.execute("select count(1) FROM main_table where id='{}';".format(primary_key))
            x = self.mycursor.fetchall()
            if x[0][0] == 0: # shows primary key does not exists
                print("Something went wrong: " + primary_key)

            self.mycursor.execute("select passenger_count from main_table where id='{}'".format(primary_key))
            x = self.mycursor.fetchall()
            if x[0][0] and x[0][0] != passenger_count:
                print("Something went wrong: " + primary_key + " " + str(passenger_count) + " " + str(x[0][0]))

    def generate_output(self, published_line_ref):
        get_value_string = 'SELECT * From bus_table WHERE published_line_ref = "{}"'.format(published_line_ref)
        get_count_string = 'SELECT * From bus_counter_table WHERE published_line_ref = "{}"'.format(published_line_ref)

        self.mycursor.execute(get_value_string)
        values = self.mycursor.fetchall()

        self.mycursor.execute(get_count_string)
        counter = self.mycursor.fetchall()

        print(values)
        print(counter)

        array = []
        for x in range(2, len(values[0])):
            if counter[0][x] != 0:
                array.append(values[0][x] / counter[0][x])
            else:
                array.append(0)

        print(array)

    def add_to_bus_average_tables_from_table(self):
        list = self.generate_list_of_all_published_line_ref()
        array = []
        for x in list:
            array.append(x[0])

        for x in array:
            self.update_average_tables_from_table(x, 'bus_average_table', 'bus_table', 'bus_counter_table')
            self.update_average_tables_from_table(x, 'bus_weekend_average_table', 'bus_weekend_table', 'bus_weekend_counter_table')
            self.update_average_tables_from_table(x, 'bus_weekday_average_table', 'bus_weekday_table', 'bus_weekday_counter_table')

    def update_average_tables_from_table(self, published_line_ref, average_table_name, table_name, table_counter_name):
        string_table = 'SELECT * FROM {} where published_line_ref = "{}"'.format(table_name, published_line_ref)
        string_table_counter = 'SELECT * FROM {} where published_line_ref = "{}"'.format(table_counter_name, published_line_ref)

        self.mycursor.execute(string_table)
        table_call = self.mycursor.fetchall()

        self.mycursor.execute(string_table_counter)
        table_counter_call = self.mycursor.fetchall()

        array_for_average_table = []

        for x in range(2, 27):
            if table_counter_call[0][x] != 0:
                array_for_average_table.append((table_call[0][x] / table_counter_call[0][x]))
            else:
                array_for_average_table.append(0)

        average_table_execute_string = self.create_insert_average_string(average_table_name, published_line_ref, array_for_average_table)
        self.mycursor.execute(average_table_execute_string)
        self.mydb.commit()


    def create_insert_average_string(self, table_name, published_line_ref, array):
        string = "INSERT INTO {} (published_line_ref, 0_hour, " \
                 "1_hour, 2_hour, 3_hour, 4_hour, 5_hour, 6_hour, 7_hour, 8_hour, 9_hour," \
                 "10_hour, 11_hour, 12_hour, 13_hour, 14_hour, 15_hour, 16_hour," \
                 "17_hour, 18_hour, 19_hour, 20_hour, 21_hour, 22_hour, 23_hour, total_avg)" \
                 "VALUES ('{}', {}," \
                 "{}, {}, {}, {}, {}, {}, {}, {}, {}," \
                 "{}, {}, {}, {}, {}, {}, {}," \
                 "{}, {}, {}, {}, {}, {}, {}, {});"\
            .format(table_name, published_line_ref,
                    array[0], array[1], array[2], array[3],
                    array[4], array[5], array[6], array[7], array[8], array[9], array[10],
                    array[11], array[12], array[13], array[14], array[15], array[16], array[17],
                    array[18], array[19], array[20], array[21], array[22], array[23], array[24])
        return string

    def initialize_dictionary_with_published_line_ref(self, dictionary):
        array = self.get_array_of_line_ref()
        for x in array:
            dictionary[x] = [0] * 24

    def highest_val_dictionary(self, dictionary_highest, dictionary):
        string_date = dictionary['Response Time']
        temp = string_date[0:string_date.rfind('-')]
        date = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')

        line_ref = dictionary['Published Line Ref']

        if dictionary_highest[line_ref][date.hour] < dictionary['Passenger Count']:
            dictionary_highest[line_ref][date.hour] = dictionary['Passenger Count']

    def set_articulated_dictionary(self, dictionary_articulated, dictionary, art_list):
        string_date = dictionary['Response Time']
        temp = string_date[0:string_date.rfind('-')]
        date = datetime.strptime(temp, '%Y-%m-%dT%H:%M:%S.%f')

        line_ref = dictionary['Published Line Ref']
        if dictionary_articulated[line_ref][date.hour] == 1:
            return

        if dictionary['Vehicle Ref'] in art_list:
            dictionary_articulated[line_ref][date.hour] = 1

    def update_highest_and_articulated_form_file(self):
        articulated_weekday = {}
        articulated_weekend = {}
        articulated_total = {}
        highest_weekday = {}
        highest_weekend = {}
        highest_total = {}

        func = generate_to_excel("", "")
        list_of_articulated_bus = list(func.create_list_of_articulated_buses())

        self.initialize_dictionary_with_published_line_ref(articulated_weekday)
        self.initialize_dictionary_with_published_line_ref(articulated_weekend)
        self.initialize_dictionary_with_published_line_ref(highest_weekend)
        self.initialize_dictionary_with_published_line_ref(highest_weekday)
        self.initialize_dictionary_with_published_line_ref(highest_total)
        self.initialize_dictionary_with_published_line_ref(articulated_total)

        with open('/home/pi/Desktop/all_info2.txt') as fp:
            line = fp.readline()
            counter = 0
            while line:
                counter = counter + 1
                if (counter % 1000000) == 0:
                    print(counter)
                dictionary = ast.literal_eval(line)
                if dictionary['Passenger Count'] != 'null':
                    self.highest_val_dictionary(highest_total, dictionary)
                    self.set_articulated_dictionary(articulated_total, dictionary, list_of_articulated_bus)
                    if self.weekday(dictionary['Response Time']):
                        self.highest_val_dictionary(highest_weekday, dictionary)
                        self.set_articulated_dictionary(articulated_weekday, dictionary, list_of_articulated_bus)
                    else:
                        self.highest_val_dictionary(highest_weekend, dictionary)
                        self.set_articulated_dictionary(articulated_weekend, dictionary, list_of_articulated_bus)
                line = fp.readline()
        # here
        for x in highest_total:
            total_art_last_col = max(articulated_total[x])
            total_art_string = self.create_insert_string_art(x, 'bus_articulated_table', articulated_total[x], total_art_last_col)

            total_highest_last_col = max(highest_total[x])
            total_highest_string = self.create_insert_string_highest(x, 'bus_highest_table', highest_total[x], total_highest_last_col)

            weekend_art_last_col = max(articulated_weekend[x])
            weekend_art_string = self.create_insert_string_art(x,'bus_weekend_articulated_table', articulated_weekend[x], weekend_art_last_col)

            weekend_highest_last_col = max(highest_weekend[x])
            weekend_highest_string = self.create_insert_string_highest(x, 'bus_weekend_highest_table', highest_weekend[x], weekend_highest_last_col)


            weekday_art_last_col = max(articulated_weekday[x])
            weekday_art_string = self.create_insert_string_art(x,'bus_weekday_articulated_table', articulated_weekday[x], weekday_art_last_col)

            weekday_highest_last_col = max(highest_weekday[x])
            weekday_highest_string = self.create_insert_string_highest(x,'bus_weekday_highest_table', highest_weekday[x], weekday_highest_last_col)

            self.mycursor.execute(total_art_string)
            self.mydb.commit()
            self.mycursor.execute(weekend_art_string)
            self.mydb.commit()
            self.mycursor.execute(weekday_art_string)
            self.mydb.commit()

            self.mycursor.execute(total_highest_string)
            self.mydb.commit()
            self.mycursor.execute(weekend_highest_string)
            self.mydb.commit()
            self.mycursor.execute(weekday_highest_string)
            self.mydb.commit()







    def update_articulated_bus_table(self):
        published_list = self.generate_list_of_all_published_line_ref()

        for published_line_ref in published_list:

            array_highest_val_weekday = [0] * 24
            array_check_art_bus_weekday = [0] * 24

            array_highest_val_weekend = [0] * 24
            array_check_art_bus_weekend = [0] * 24

            func = generate_to_excel("", "")
            list_of_articulated_bus = list(func.create_list_of_articulated_buses())

            self.mycursor.execute('SELECT * FROM main_table WHERE published_line_ref="{}"'.format(published_line_ref))
            for x in self.mycursor:
                if x[5]:
                    if self.weekday(x[1]):
                        self.highest_val(x, array_highest_val_weekday)
                        self.set_articulated(x, array_check_art_bus_weekday, list_of_articulated_bus)
                        ## bus_lowest_val_counter
                    else:
                        self.highest_val(x, array_highest_val_weekend)
                        self.set_articulated(x, array_check_art_bus_weekend, list_of_articulated_bus)

            array_articulated_total = [0] * 24
            array_highest_val_total = [0] * 24

            for i in range(24):
                if array_articulated_total[i] != 1 and (
                        array_check_art_bus_weekday[i] == 1 or array_check_art_bus_weekend[i] == 1):
                    array_articulated_total[i] = 1

                if array_highest_val_weekend[i] > array_highest_val_weekday[i]:
                    array_highest_val_total[i] = array_highest_val_weekend[i]
                else:
                    array_highest_val_total[i] = array_highest_val_weekday[i]


            articulate_string = self.create_insert_string_art(x, 'bus_articulated_table', array_articulated_total, max(array_articulated_total))
            highest_string = self.create_insert_string_highest(x, 'bus_highest_table', array_highest_val_total, max(array_highest_val_total))

            print(array_highest_val_total)
            print(array_articulated_total)

            print(array_highest_val_weekend)
            print(array_highest_val_weekday)

            print('done')






# test = mta_bus_project_sql_tables(connection='mariadb',sql_password='anil6218', sql_user='amit' )
#
# test.update_highest_and_articulated_form_file()