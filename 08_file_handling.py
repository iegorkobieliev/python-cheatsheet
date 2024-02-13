with open("new_file.txt", "w") as new_file:
    new_file.write("Hello, Python!")

with open("new_file.txt", "r") as file:
    content = file.read()
    print(content)
