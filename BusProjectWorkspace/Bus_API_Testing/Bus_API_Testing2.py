# Here I will show you how to load the saved JSON file
import json

# load the file into data as json object
with open('saved_json_data.txt') as json_file:
    data = json.load(json_file)


print(data)
# Accessing specific value in the data object
print(data['data']['stops'][0]['name'])

