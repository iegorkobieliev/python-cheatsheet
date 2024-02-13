# 01Data Types

int_num = 42
float_num = 3.14
string_var = "Hello, Python!"
bool_var = True

# 02Variables and Assignment

x = 10
y = "Python"


my_list = [1, 2, 3, "Python"]
my_tuple = (1, 2, 3, "Tuple")

# 04Dictionaries

my_dict = {'name': 'John', 'age': 25, 'city': 'Pythonville'}

# 05Control Flow

if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
for item in my_list:
    print(item)

count = 0
while count > 0:
    print(count)
    count += 1


# 06Functions

def greet(name="User"):
    return f"Hello, {name}!"


result = greet("John")
