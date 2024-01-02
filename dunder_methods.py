# Special methods or Dunder Methods
class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    # when every python needs string representation
    # like print formating or literals or
    # print the object itself
    # do not use print inside __str__ methods.

    def __str__(self):
        return f"{self.title} written by {self.author}"

    def __len__(self): # return int
        return self.pages

# create an object
mybook = Book("Python cookbook","John",120)
print(mybook) # print object location
print(len(mybook))
# create our own custom object in order to
# print out