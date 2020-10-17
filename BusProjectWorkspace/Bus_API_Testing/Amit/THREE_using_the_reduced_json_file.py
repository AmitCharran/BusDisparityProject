import json

with open('TextFileFolder/reduced_vehicle_monitoring_file.txt') as json_file:
    data = json.load(json_file)

test_data = data[0]['MonitoredVehicleJourney']

print(test_data.keys())


def get_passenger_count(json_data):
    for x in json_data:
        test_data_2 = x['MonitoredVehicleJourney']
        vehicle_ref = test_data_2['VehicleRef']
        line_ref = test_data_2['LineRef']
        if 'MonitoredCall' in test_data_2:
            test_data_3 = test_data_2['MonitoredCall']
            if 'Extensions' in test_data_3:
                test_data_4 = test_data_3['Extensions']
                if 'Capacities' in test_data_4:
                    print(line_ref + "\t" + vehicle_ref + "\t" + str(test_data_4['Capacities']['EstimatedPassengerCount']))







# Need function to get all distinct LineRef and map to bus name
def find_all_distinct_line_ref(json_data):
    distinct_line_ref = []
    for x in range(0, len(json_data)):
        line_ref = json_data[x]['MonitoredVehicleJourney']['LineRef']
        if not (distinct_line_ref.__contains__(line_ref)):
            distinct_line_ref.append(line_ref)
    return distinct_line_ref


all_line_ref = find_all_distinct_line_ref(data)

# Writing to outfile
# with open("TextFileFolder/all_line_ref.txt","w") as outfile:
#     for x in all_line_ref:
#         outfile.write(x)
#         outfile.write("\n")


# Need function to get all distinct OperatorRef
def find_all_distinct_operator_ref(json_data):
    distinct_operator_ref = []
    for x in range(0, len(json_data)):
        operator_ref = json_data[x]['MonitoredVehicleJourney']['OperatorRef']
        if not (distinct_operator_ref.__contains__(operator_ref)):
            distinct_operator_ref.append(operator_ref)
    return distinct_operator_ref

print(find_all_distinct_operator_ref(data))

get_passenger_count(data)






