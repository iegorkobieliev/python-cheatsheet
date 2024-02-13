class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof!")


my_dog = Dog("Buddy")
my_dog.bark()

print(type(my_dog))
