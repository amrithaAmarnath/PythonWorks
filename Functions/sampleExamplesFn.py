"""
organized block of reusable code that can be called whenever required

divide large program into basic building blocks

Re-usability of codes

keyword - def


1. user-defined function
     - created by user to perform specific task
2. Built-in-function
     - predefined function in Python like max(),count() etc
3. Anonymous function


Adv:

avoid rewriting same logic/code again and again in a program -reduce repetition of code
call functions multiply times anywhere in program
re-usablity of code
track program workflow easily

"""


def sample():
    print("Hello world!")


sample()
sample()


# Sum of two numbers

def sum():
    a = 10
    b = 20
    return a + b


c = sum()
print("sum = ", c)


# function call with arguments
# defining the function
def sum(a, b):
    return a + b


# taking values
a = 10
b = 20
# printing the sum of a and b
print("sum = ", sum(a, b))


# Call by reference in Python:

# Example 1 Passing Mutable Object (List)

def change_list(list1):
    list1.append(20)
    list1.append(30)
    print("list inside function = ", list1)


# defining the list
list1 = [10, 30, 40, 50]
# calling the function
change_list(list1)
print("list outside function = ", list1)


# Example 2 Passing Mutable Object (String)
def change_string(str):
    str = str + " Hows you "
    print("printing the string inside function :", str)


string1 = "Hi I am there"
# calling the function
change_string(string1)
print("printing the string outside function :", string1)


# arguments /positional arguments

def myFunc(msg1, msg2):
    print(msg1 + " " + msg2)


myFunc("Hello Dear!!", "How are you?")


# Arbitrary arguments:

def myfunc(*names):
    print("Hi", names[2], "How are you")


myfunc('Jack', 'Jill', 'Jain')

# keyword arguments: can give arguments as key =  value format

def my_func(name1, name2, name3):
    print("Last name is" + name3)


my_func('Jack', 'Jill', 'Jain')
my_func('Jack', name3='Jill', name2='Jain')


# Arbitrary keyword arguments: (**kwargs)

def my_Fnc(**name):
    print("lastname " + name["lname"])


my_Fnc(fname="Amritha", lname="Amarnath")




