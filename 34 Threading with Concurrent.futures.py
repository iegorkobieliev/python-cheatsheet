from concurrent.futures import ThreadPoolExecutor


def square(x):
    return x ** 2


with ThreadPoolExecutor() as executor:
    results = executor.map(square, [1, 2, 3, 4, 5])
    print(list(results))
