from BusDisparityFunctionsAndClasses.getting_json_data import retriving_from_API
from HiddenVariables.hidden_variables import MTA_API_KEY
from HiddenVariables import hidden_variables

from BusDisparityFunctionsAndClasses.preparing_data_for_SQL import format_data
from BusDisparityFunctionsAndClasses.getting_the_info import generate_to_excel
from BusDisparityFunctionsAndClasses.preparing_data_for_SQL import mta_bus_project_sql_tables
from datetime import datetime
#
# test = retriving_from_API(MTA_API_KEY, 'BusDisparityFunctionsAndClasses/output/')
# test.start_calls()
#
#
start_date = datetime(year=2020, month=11, day=8)
start_date = start_date.replace(hour=0, minute= 9)

end_date = datetime(year=2020, month=11, day=9)
end_date = end_date.replace(hour=0, minute=15)
input_path = '/Users/amitcharran/Desktop/Unneeded_Files_for_project/Sample_JSON_Data'
output_path = '/Users/amitcharran/Desktop/Unneeded_Files_for_project/output.txt'
# test_format = format_data(input_path, output_path, start_date, end_date)
# test_format.write_to_sql_from_file_skip_lines2('/Users/amitcharran/Desktop/all_info2.txt', 10000000)
# test_format.count_from_file('/Users/amitcharran/Desktop/all_info2.txt')
# Max 10039122


#
#
#
#
# test_g = retriving_from_API(MTA_API_KEY, "")
# test_g.start_call_and_write_to_SQL()



# test_w = mta_bus_project_sql_tables(hidden_variables.sql_host, hidden_variables.sql_user, hidden_variables.sql_password)
# test_w.generate_avg_for_a_bus("Q6")



#
# test_a = generate_to_excel("", "")
# array = test_a.create_list_of_articulated_buses()

# highest per bus
# smallest per bus

