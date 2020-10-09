import json

with open('TextFileFolder/reduced_vehicle_monitoring_file.txt') as json_file:
    data = json.load(json_file)


test_data = data[0]['MonitoredVehicleJourney']



# Need function to get all distinct LineRef and map to bus name
def find_all_distinct_line_ref(json_data):
    distinct_line_ref = []
    for x in range(0, len(json_data)):
        line_ref = json_data[x]['MonitoredVehicleJourney']['LineRef']
        if not (distinct_line_ref.__contains__(line_ref)):
            distinct_line_ref.append(line_ref)
    return distinct_line_ref


all_line_ref = find_all_distinct_line_ref(data)
print(len(all_line_ref))
for x in all_line_ref:
    print(x)

# Need function to get all distinct OperatorRef

