"""
Python Scope:
*************

1. Global Variables:
-Variables that are created outside of a function-

- can be used by everyone, both inside of functions and outside.


"""

# Create a variable outside of a function, and use it inside the function

# x = "awesome"
# def printstring():
#     print("Python is " + x)
# printstring()

"""
Create a variable with the same name inside a function:
- Python will treat them as two separate variables
 - this variable will be local, and can only be used inside the function.
- The global variable with the same name will remain as it was, 
  global and with the original value.

"""
# x = "awesome"
# def printstring():
#     x = "powerful"
#     print("Python is " + x)
# printstring()
# print("Python is " + x)

"""

The global Keyword:
******************

Normally, when create a variable inside a function, that variable is local,
 and can only be used inside that function.

To create a global variable inside a function, we can use the global keyword.

"""

# def printstring():
#     global y
#     y = "powerful"
#     print("Inside Python is " + y)
# printstring()
# print("Outside Python is " + y)

# To change the value of a global variable inside a function,
# refer to the variable by using the global keyword:

# x = "awesome"
#
# def myfunc():
#   global x
#   x = "fantastic"
#
# myfunc()
#
# print("Python is " + x)



"""
2. Local variable:
- A variable created inside a function belongs to the local scope of that 
function, and can only be used inside that function.
"""

# def myfunc():
#   x = 300
#   print(x)
#
# myfunc()

"""
Function Inside Function:
- The local variable can be accessed from a function within the function:
"""
# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
#   myinnerfunc()
#
# myfunc()

