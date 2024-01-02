"""
 Key rules of Python scope
 Python scope Scope follows the LEGB Rule:
  - Local variables
     - Names assigned in any way within a function (def or lambda),
     And not declared global in that functions

  - Enclosing Functions locals
        -Name in the local scope of any and all enclosing functions ( def or
    lambda), from inner to outer.
  - Global variables.
        - Names assigned at the top-level of a module, or declared global
   in a def within the file.
  - Built-in
   - Built-in (python) -Names preassigned in the built-in names module:
   open , range, syntaxError.

"""
 # let's walk through simple experiement.

x = 25
def my_func():
    global x
    x = 50
    return x
"""print(x) # 25
print(my_func()) # 50 """

my_func()
print(x)

