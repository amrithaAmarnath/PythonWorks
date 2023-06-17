"""
Super Function:

-The super() function is used to give access to methods and properties of
 a parent or sibling class.

-The super() function returns an object that represents the parent class.

-The Python super() function returns objects represented in the parent’s class
and is very useful in  multiple and
multilevel inheritances to find which class the child class is extending first.

-syntax : super()
- Return : Return a proxy object which represents the parent’s class.




"""
# How
# Inheritance is working
# without
# super


# code
# class Person:
#
#     # Constructor
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     # To check if this person is an employee
#     def Display(self):
#         print(self.name, self.id)
#
#
# class Emp(Person):
#
#     def __init__(self, name, id):
#         self.name_ = name
#
#     def Print(self):
#         print("Emp class called")
#
#
# Emp_details = Emp("Mayank", 103)
#
# # calling parent class function
# Emp_details.id, Emp_details.name


"""
In above code Emp class is inherits the Person class

Both class has the __init__ constructor
trying to call name & name_ from other class 
But we will encounter the above error
With super implementation in inherent we can solve the problem.
 
 example can found below
"""


class Emp():
    def __init__(self, id, name, Add):
        self.id = id
        self.name = name
        self.Add = Add


# Class freelancer inherits EMP
class Freelance(Emp):
    def __init__(self, id, name, Add, Emails):
        super().__init__(id, name, Add)
        self.Emails = Emails


Emp_1 = Freelance(103, "Suraj kr gupta", "Noida", "KKK@gmails")
print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Address is:', Emp_1.Add)
print('The Emails is:', Emp_1.Emails)


#example:

#Create a class that will inherit all the methods and properties from another class:

# class Parent:
#   def __init__(self, txt):
#     self.message = txt
#
#   def printmessage(self):
#     print(self.message)
#
# class Child(Parent):
#   def __init__(self, txt):
#     super().__init__(txt)
#
# x = Child("Hello, and welcome!")
# #print(x)
# x.printmessage()