import re

pattern = r'\d+'
result = re.findall(pattern, "There are 42 apples and 123 oranges.")
print(result)

# 39 Regular Expressions

# import re
text = "Hello, 123 World!"

# Match numbers
numbers = re.findall(r'\d+', text)
print(numbers)
