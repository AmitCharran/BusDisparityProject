from BusSpeedFunctionsAndClasses.calculating_distance import calculating_speed
from BusSpeedFunctionsAndClasses.reading_folders import reading_folder
from BusSpeedFunctionsAndClasses.Converting_bus_data_for_speed_analysis import bus_data_to_matrix

# input the path
def convert_info_from_folder(basepath):
    # first get the array of folderpaths
    read_the_folders = reading_folder(basepath)
    read_the_folders.printfile()
    array_of_file_paths = read_the_folders.answer_array

    ####### we need to create arrays of output
    sample_array_of_output = []
    ##################### function needs to be created above
        # print(array_of_file_paths)

    # Now go through the array and convert data
    convert_files = bus_data_to_matrix()
    for i in range(0, len(array_of_file_paths)):
        convert_files.get_and_convert_data(input_path=array_of_file_paths[i], output_path=sample_array_of_output[i])

    # then go into calculating the buses and generating data
    sample_new_output_for_sample_array_of_output = []
    calculate_speed = calculating_speed()
    for i in range(0, len(sample_array_of_output)):
        calculate_speed.calculate_average_from_file(input_file=sample_array_of_output[i], output_file=sample_new_output_for_sample_array_of_output)







basepath = "/Users/amitc/Desktop/BusDisparityProject/BusProjectWorkspace/BusSpeedFunctionsAndClasses"
convert_info_from_folder(basepath)