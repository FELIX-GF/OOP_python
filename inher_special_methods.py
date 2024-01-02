# INHERITANCE
class Animal():

    def __init__(self):
        print("Animal Created!!")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")

# create another class
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("DOG CREATED!!")
    def bark(self):
        print("WOOF")
    # override eat() defined in parent calss
    """def eat(self):
        print("DOG EATING!")"""

# object instaTIATE
mydog =Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()



