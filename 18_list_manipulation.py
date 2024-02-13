numbers = [1, 2, 3, 4, 5]

# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# Map
squared = list(map(lambda x: x**2, numbers))
print(squared)

# Reduce (requires functools)
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)