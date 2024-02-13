my_dict = {'a': 1, 'b': 2, 'c': 3}

# Get value with default
value = my_dict.get('d', 0)
print(value)

# Dictionary comprehension
squared_dict = {key: value**2 for key, value in my_dict.items()}
print(squared_dict)