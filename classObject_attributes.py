# Class Object Attributes.
# Add more attributes
class Dog():
    # Class Object attributes.
    species = "mammals"

    def __init__(self,breed,name): # we must always use self with the special methods.
        self.breed = breed
        self.name = name

mydog = Dog(breed = "lab", name ="Sammy")
print(mydog.breed)
print(mydog.name)
print(mydog.species)
