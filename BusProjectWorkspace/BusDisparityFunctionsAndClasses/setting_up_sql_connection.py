import mysql.connector
from mysql.connector import Error
from HiddenVariables import hidden_variables

class mta_bus_project_sql_tables:
    def __init__(self,sql_host, sql_user, sql_password):
        self.mydb = mysql.connector.connect(
            host=sql_host,
            user=sql_user,
            password=sql_password
        )
        self.current_database = 'mta_bus_project'
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute('USE mta_bus_project;')
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.mycursor.close()
        self.mydb.close()

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

    def switch_database(self, database_name):
        self.mycursor.execute('USE ' + database_name + ';')
        self.current_database = database_name

    def insert_into_tables(self, primary_key, response_time, vehicle_ref, line_ref, published_line_ref,
                           passenger_count, latitude, longitude, stop_point_name,
                           destination_name, journey_pattern_ref):
        # Make errors if primary_key already exists
        # This is a check for duplicates
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
            if x[0][0] == 0:
                print("Something went wrong: " + primary_key)




test = mta_bus_project_sql_tables(
    hidden_variables.sql_host,
    hidden_variables.sql_user,
    hidden_variables.sql_password)

test.show_all_in_current_table('main_table')



