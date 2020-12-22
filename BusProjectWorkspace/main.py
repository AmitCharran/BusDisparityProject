from BusDisparityFunctionsAndClasses.getting_json_data import retriving_from_API
from HiddenVariables.hidden_variables import MTA_API_KEY
from BusDisparityFunctionsAndClasses.preparing_data_for_SQL import format_data
from datetime import datetime

# test = retriving_from_API(MTA_API_KEY, 'BusDisparityFunctionsAndClasses/output/')
# test.start_calls()


start_date = datetime(year=2020, month=11, day=8)
start_date = start_date.replace(hour=0, minute= 9)

end_date = datetime(year=2020, month=11, day=9)
end_date = end_date.replace(hour=0, minute=15)
input_path = '/Users/amitcharran/Desktop/Unneeded_Files_for_project/Sample_JSON_Data'
output_path = '/Users/amitcharran/Desktop/Unneeded_Files_for_project/output.txt'
test_format = format_data(input_path, output_path, start_date, end_date)
test_format.create_info_to_output_file()
