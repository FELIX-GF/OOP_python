# structure
class NameofClass: # camel case
    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        # perform some action
        print(self.param1)
        print(self.param2)
cl = NameofClass("hello","world")
print(cl.param1)
print(cl.param2)
