"""

Decorators :
- used to simplify function
- to modify function without changing the actual behaviour of that function
- call with "@" symbol
- Decorators allow us to wrap another function in order to extend the behaviour
 of the wrapped function, without permanently modifying it.

- i.e  allows a user to add new functionality to an existing object without
modifying its structure.
- The outer function is called the decorator, which takes the original
 function as an argument and returns a modified version of it.

- Decorators are usually called before the definition of a function to decorate.

- Function:
  >> everything in Python is an object, even functions are objects.
  A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, …

"""

"""
# Nested Function - created inner() outside outer()
"""


def outer(a):
    print("a",a)
    def inner(b):
        print("a = ",a, " and b= ",b)
        return a+b
    return inner
add_five = outer(5)
print(add_five(6))
"""
Pass Function as Argument to another function in Python?

#the calculate() function takes a function as its argument.
# While calling calculate(), we are passing the add() function as the argument.
# In the calculate() function, arguments: func, x, y become add, 4, and 6
# respectively.
#
# And hence, func(x, y) becomes add(4, 6) which returns 10.

"""


def add(x, y):
    return x + y

def calculate(func, x, y):
    return func(x, y)

result = calculate(add, 4, 6)
print(result)  # prints 10

"""
# Return a Function as a Value >> the return hello statement
# returns the inner hello() function.
# This function is now assigned to the greet variable.
#  So call greet() as a function, we get the output.
"""


def greeting(name):
    print("name>>",name)
    def hello():
        return "Hello, " + name + "!"
    return hello

greet = greeting("Atlantis")
print(greet())  # prints "Hello, Atlantis!"
"""
# Python Decorators >>  A Python decorator is a function that takes in a
# function and returns it by adding some functionality.
# a decorator takes in a function, adds some functionality and returns it.
"""


def make_pretty(func): # takes a function as its argument, make_pretty is the decorator
    def inner(): #  has a nested function named inner()
        print("I got decorated")
        func()
    return inner # and returns the inner function.

# define ordinary function
def ordinary():
    print("I am ordinary")

# decorate the ordinary function
decorated_func = make_pretty(ordinary)

# call the decorated function
decorated_func()  # Here, we are actually calling the inner() function, where we are printing

"""
#@ Symbol With Decorator

"""


def make_pretty(func): # takes a function as its argument, make_pretty is the decorator
    def inner(): #  has a nested function named inner()
        print("I got decorated")
        func()
    return inner # and returns the inner function.

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary() # Here, the ordinary() function is decorated with the make_pretty()
# decorator using the @make_pretty syntax,
# which is equivalent to calling ordinary = make_pretty(ordinary).

"""
Decorating Functions with Parameters
"""


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a,b):
    print(a/b)

divide(4,2)
divide(2,0)
# Here, when we call the divide() function with the arguments (4,2),
# the inner() function defined in the smart_divide() decorator is called instead.
#
# This inner() function calls the original divide() function
# with the arguments 4 and 2 and returns the result, which is 2.0.
#
# Similarly, When we call the divide() function with the arguments (2,0),
# the inner() function checks that b is equal to 0 and
# prints an error message before returning None.


"""
Chaining Decorators in Python
- Multiple decorators can be chained in Python.
- To chain decorators in Python, we can apply multiple decorators to a single 
  function by placing them one after the other, with the most inner decorator
  being applied first.
  
"""

def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("Hello")

#@star
#@percent                                      def printer(msg):
#def printer(msg):      is equivalent to          print(msg)
# print(msg)                                   printer = star(percent(printer))
#

