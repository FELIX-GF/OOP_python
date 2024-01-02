# Add more attributes
class Dog():
    def __init__(self,breed,name,age): # we must always use self with the special methods.
        self.breed = breed
        self.name = name
        self.age = age
    def print_detail(self):
        return f"Breed: {self.breed} \nName: {self.name} \nAge: {self.age}"

# instantiate an object

mydog = Dog(breed = "lab", name ="Sammy",age=12)
mydog.print_detail()
