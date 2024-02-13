def decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")

    return wrapper


@decorator
def my_function():
    print("Inside the function")


my_function()
