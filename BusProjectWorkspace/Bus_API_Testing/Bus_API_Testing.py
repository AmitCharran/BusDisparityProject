# requests will let us get information form API
import requests
# to handle json files
import json

# This is our APIkey that we will use to get information from MTA BusTime
# Do not run this file constantly, try and wait 30 seconds before APIkey access
# API key will be invalidated if there are too much requests
API_key = 'f3cd89cf-147d-40bf-8557-5431e990e24f'

# This is the latitude and longitude that we will use as an example to use API Key
# This combination is somewhere in manhattan
latitude = '40.748433'
longitude = '-73.985656'

# This is how we will gather some API data
# For this we will get information on buses near this location
# For now we need to research their website and figure out how to get the information we want
stops_at_location_lat_long = 'http://bustime.mta.info/api/where/stops-for-location.json?' \
                             'lat=' + latitude +\
                             '&lon=' + longitude +\
                             '&latSpan=0.005&lonSpan=0.005&key=' + API_key

# This code grabs the information
response = requests.get(stops_at_location_lat_long)

# They both print the same info, (i think this might be a string)
print(response.content)

# We want this, this is a dictionary, so it is easier to go through
print(response.json())

# Saving .json into a .txt file
data = response.json()
with open('saved_json_data.txt', 'w') as outfile:
    json.dump(data, outfile)

# Go to Bus_API_Testing2.py to see how to load and use 'saved_json_data.txt'


