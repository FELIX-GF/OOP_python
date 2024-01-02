# SPECIAL METHODS
class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Special methods
    def __str__(self):
        return "title:{},Author:{},pages:{}".format(self.title,self.author,self.pages)



    def __len__(self):
        return self.pages


    def __del__(self):
        print("A book is destroyed!!")


b = Book("Python","Jose",200)
del b
print(b)

# when you print b it looks for string representations specifially
# defined the "Python " string representations.
#print(b) # -> <__main__.Book object at 0x000001E0F9CEC210>


