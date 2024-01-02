class Circle():
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    # create a methods
    def area(self):
        return self.radius * self.radius * Circle.pi
    # overriding radius and we can create a new methods.
    def set_radius(self, new_r):
        self.radius = new_r


myc = Circle(3)
# changing the value of the radius
#print(myc.radius)
myc.set_radius(9)
print(myc.area())


