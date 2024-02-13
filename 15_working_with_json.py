# import json
#
# # Convert Python object to JSON
# json_data = json.dumps({"name": "John", "age": 25})
# print(type(json_data))
# print(json_data)
# # Convert JSON to Python object
# python_obj = json.loads(json_data)
# print(type(python_obj))
# print(python_obj)

# 45 Working with JSON Files

import json
data = {'name': 'John', 'age': 30}

# Write to JSON file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

# Read from JSON file
with open('data.json', 'r') as json_file:
    loaded_data = json.load(json_file)
    print(loaded_data)
