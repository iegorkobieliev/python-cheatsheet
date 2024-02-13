with open("new_file.txt", "w") as new_file:
    new_file.write("Hello, Python!")

with open("new_file.txt", "r") as file:
    content = file.read()
    print(content)

# Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, Python!')
    print(file)
    print(type(file))

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
