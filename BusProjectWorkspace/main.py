from BusDisparityFunctionsAndClasses.getting_json_data import retriving_from_API
from HiddenVariables.hidden_variables import MTA_API_KEY
from HiddenVariables import hidden_variables

from BusDisparityFunctionsAndClasses.preparing_data_for_SQL import format_data
from BusDisparityFunctionsAndClasses.getting_the_info import generate_to_excel
from BusDisparityFunctionsAndClasses.preparing_data_for_SQL import mta_bus_project_sql_tables
from datetime import datetime



put_data_into_sql = format_data("", "")
put_data_into_sql.write_to_sql_from_file_skip_lines2('/home/pi/Desktop/all_info2.txt', 10)
