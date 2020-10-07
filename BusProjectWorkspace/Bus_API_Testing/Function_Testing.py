import json

with open('testFile.txt') as json_file:
    data = json.load(json_file)

print(data)
print(type(data))

# This function does not account for arrays
# finds dictionaries inside dictionaries
def _finditem(obj, key):
    if key in obj: return obj[key]
    for k, v in obj.items():
        if isinstance(v,dict):
            item = _finditem(v, key)
            if item is not None:
                return item


print(_finditem(data, 'ServiceDelivery').get('ResponseTimestamp'))


