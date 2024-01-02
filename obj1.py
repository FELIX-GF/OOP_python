

# Parameters
# inheritance
# special methods
# module
# packages
# project (your first OOP python project)

class Dog():
    species = "mamals" # class attributes
    def __init__(self, breed, name, age): # we must always use self with the special methods.
        print("Hello Wordl")
        self.breed = breed
        self.name = name
        self.age = age
    def print_detail_info(self):
        print("Breed: " + self.breed, "Name: " + self.name, "Age: "+ str(self.age))

mydog = Dog(breed ="lab", name ="puppy",age=12)
mydog.print_detail_info()
"""print(mydog.species)
print(mydog.breed)
print(mydog.name)
print(mydog.age)"""



