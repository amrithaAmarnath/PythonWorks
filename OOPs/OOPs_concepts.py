"""
#Encapsulation
-Wrapping up of data and functions into a single unit
-Eg: class

inheritance
-To acquire the properties of one class to another class
-Types of Inheritance
   -Simple
   -Multilevel
   -Multiple
   -Hierarchical
   -Hybrid

"""


# class A:
#     def displayA(self):
#         print("Base class")
# class B(A):
#     def displayB(self):
#         print("Derived class")
#
# ob=B()
# ob.displayB()
# ob.displayA()

# read(x,y) method in A and sum() in B

# class A:
#     def read(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class B(A):
#     def sum(self):
#         self.s= self.x + self.y
#         print('sum = ', self.s)


# ob = B()
# ob.read(3,4)
# ob.sum()

# inherit class B to C

# class C(B):
#     def avg(self):
#         print('Average =' , self.s/2)
#
# ob=C()
# ob.read(3,4)
# ob.sum()
# ob.avg()

#Heirarchical Inheritance :

# class A:
#     def read(self):
#         self.x = int(input("enter a number"))
#         self.y = int(input("enter a number"))
#
#
# class B(A):
#     def sum(self):
#         self.s= self.x + self.y
#         print('sum = ', self.s)
#
# class C(A):
#     def avg(self):
#         self.a = self.x + self.y
#         print('Average =' , self.a/2)
#
# class D(A):
#     def product(self):
#         self.p= self.x * self.y
#         print('product = ', self.p)
#
# ob1=B()
# ob1.read()
# ob1.sum()
# ob2=C()
# ob2.read()
# ob2.avg()
# ob3=D()
# ob3.read()
# ob3.product()


#Multiple inheritance

# class A:
#     def Emp(self):
#         self.x = input("enter Employee Name")
#         self.y = int(input("enter age "))
# #
# #
# class B:
#     def salary(self):
#         self.s =int(input("enter salary "))
#         self.d = input("enter designation ")
#
# class C(A,B):
#     def display(self):
#         print('Emplyee name =' , self.x)
#         print('Emplyee age =', self.y)
#         print("Emplyee salary",self.s)
#         print("Emplyee designation", self.d)
#
# ob=C()
# ob.Emp()
# ob.salary()
# ob.display()
#
# class D(A):
#     def product(self):
#         self.p= self.x * self.y
#         print('product = ', self.p)
#
# ob1=B()
# ob1.read()
# ob1.sum()
# ob2=C()
# ob2.read()
# ob2.avg()
# ob3=D()
# ob3.read()
# ob3.product()

"""
#Polymorphism - One_In_Many forms - 
2 types of polymorphism
 - run time Polymorphism  - - late binding -- dynamic binding
    -eg: Function Overriding
    -Function Overriding - different class have different functions with same function name and same signatures
 - compile time Polymorphism --- early binding -- static binding
    -eg: Function Overloading - python not supporting
    -Function Overloading means one class have more than one functions with same 
    function name and different signatures(number,order and type of parameters)

"""
#overloading
# class A:
#     def sum(self,a):
#         print(a+a)
#     def sum(self, a,b):
#         print(a+b)
#
# ob=A()
# ob.sum(10,23)
# #overriding
#
# class rectangle:
#     def Area(self,l,b):
#         print('Area of rectangle :',l*b)
#
# class square(rectangle):
#     def Area(self,l,b):
#         print('Area of rectangle is:', l * b)
#
# ob=square()
# ob.Area(10,20)

#ie derived class method overrides method of base class
#-Difference of overriding and overloading - interview question

"""
super()
"""
"""
#Abstraction is to represent the essential features without
 representing explanation or background details
 - Abstarction is used to hide the internal functionality of the function
 -Adv -- data hiding -- An abstraction is used to hide irrelevant data/class in order 
 to reduce complexity
 
 #Data hiding - cannot create object of abstract class
 -Abstract class - class with one ore more abstract methods
 -Abstract method - do not contain full implementation 
   ie only have declaration
 -Abstarct can be inheritted by the subclass and abstract method gets its definition in the subclass
 -Python provides the abc  module
to use abstarction in Python program
Python does not provide abstract class itself
- need to import abc module, which provides the base for 
defining Abstract Base Classes (ABC).
-ABC works by decorating methods of the base class as abstract
-use @abstractclass as decorator to define an abstract method 
  or if we don't provide the definition of the method ,
  it automatically becomes abstract method
"""

#
# class A:
#     # function def:
#     def display(self):
#         print("haii")
#
#     #function with only  declaration no definition
#     def disp(self): # abstarct method
#         pass


#Example in abtractionmethod.py
#*******



"""
Constructor
-member functions of a class which will automatically executed 
when an object of a class is created
-do not have return value
-in python define constructor by using __init__
class A:
def __init__(self):
  print("non parameterized constructor (default constructor)")
  
-two types
  - non parameterized constructor (default constructor)
  -parameterized constructor
  
"""

# Non Parameterized constructor (default constructor)
# class A:
#     def __init__(self):
#         print("Non parameterized constructor")
#
# ob=A()

# Parameterized constructor
# class A:
#     def __init__(self,name):
#         print("parameterized constructor")
#         self.na=name
#     def display(self):
#         print('Name is ', self.na)
# ob=A('Arun')
# ob.display()


#DEstructors - to delete object
class A:
    def __init__(self,name):
        print("parameterized constructor")
        self.na=name

    # def __del__(self):
    #     print("destructors")

    def display(self):
        print('Name is ', self.na)
ob=A('Arun')
del ob
#ob.display()








