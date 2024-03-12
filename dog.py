class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print("Woof! My name is", self.name)

my_dog = Dog("Buddy")
my_dog.bark()
