# local
lambda x: x**2 #-> This particular x is local

#ENCLOSING FUNCTION LOCALS
# Nested  functions
name = 'This is a global name!!'

def greet():
    name ="sammy"

    def hello():
        print("hello "+name)
    hello()
greet()


