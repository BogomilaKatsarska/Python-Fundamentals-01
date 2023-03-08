# Each class instance can have attributes attached to it
# Classes can also have methods for modifying its state
# The __init__() method initializes an object's initial attributes
# by giving them default value
# The self parameter is a reference to the current instance of the class
# It is used to access variables that belong to the class
# When defining an instance method, the first paramenter of the method should always be self

class Person:
    species = 'mammal'
    # Constructor below(attributes)
    def __init__(self, name, likes=0):
        self.name = name
        self.likes = likes

    # Method below

    def say_hi(self):
        print(f'Hi, my name is {self.name}')


bogomila = Person("Bogomila Katsarska")
nikolay = Person("Nikolay Mihaylov")

bogomila.say_hi()

# When a parameter is optional, put a default value that it should have
# While instance attributes are specific to each object, class attributes are the same for all instances