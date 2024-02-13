squares = [x ** 2 for x in range(5)]
print(squares)


# 32 List Comprehensions

numbers = [1, 2, 3, 4, 5]

# Squares of even numbers
squares = [x**2 for x in numbers if x % 2 == 0]
print(squares)