import json

# Convert Python object to JSON
json_data = json.dumps({"name": "John", "age": 25})
print(type(json_data))
# Convert JSON to Python object
python_obj = json.loads(json_data)
print(type(python_obj))
