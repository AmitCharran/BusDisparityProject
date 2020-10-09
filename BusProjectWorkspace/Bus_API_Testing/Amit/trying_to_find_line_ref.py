import requests
import json


vehicle_monitoring_url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json"

API_key = 'f3cd89cf-147d-40bf-8557-5431e990e24f'

get_all_info_from_vehicle_monitoring = vehicle_monitoring_url + "?key=" + API_key

response = requests.get(get_all_info_from_vehicle_monitoring)


data = response.json()
with open('saved_json_data.txt', 'w') as outfile:
    json.dump(data, outfile)

with open('vehicle_monitoring.json', 'w') as outfile:
    json.dump(data, outfile)


