def square_numbers(n):
    for i in range(n):
        yield i ** 2


squares = square_numbers(5)
print(squares)
print(type(squares))
print(list(squares))
