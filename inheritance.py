# inheritance allows us to pass in an existing
# class into a new class, which means we get to
# inherit the use of the methods already defined within the
# parent class (including the __init__method).
# and this saves us a lot of times.
"""
Let's explore inheritance, including:
    - Creating a Parent Class (Base Class)
    - Creating a Child Class (Derived Class)
    - Using inherited methods
    - Adding new methods
    - Overwriting derived methods
"""
class Person():

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def hello(self):
        print("hello")

    def report(self):
        print(f" I am {self.first_name} {self.last_name}")

class Agent(Person):# I will have inherite all methods
    # Change what report does with an agent.
    # override the inherited method
    # what is I want to override the init methods?

    def __init__(self,first_name,last_name,code_name):
        # if you wanna add new attributes that is not provided
        # for you by the base class
        #inheriting first_name and last_name
        Person.__init__(self,first_name,last_name)
        self.code_name = code_name

    def report(self):
        print(" I am here!!")
    def reveal(self,passcode):
        if passcode ==123:
            print("I am a secret Agent!!")
        else:
            self.report()

# create a person instance
#x = Person("Johny","Raga")
#x.report()

# Person has to assossation with agent
# but Agent will inherite every property or methods
# that was defined with Person class.
x =Agent("Johny","Raga","XXX")
#x.hello()
#x.report()
#x.reveal(123) # prints 'I am a secret agent message'
#x.reveal(1234) # prints ' I am here!! '
#x.report()
print(x.first_name)
print(x.code_name)
# add a new methods and override the new methods.



