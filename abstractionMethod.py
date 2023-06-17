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
 -Abstarct class can be inheritted by the subclass and abstract method gets its
 definition in the subclass
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


from abc import ABC, abstractmethod
#abstract class
class Polygon(ABC): # class poygon inherits built in class ABC
#abstract method
    @abstractmethod
    def sides(self):
        pass

    def display(self):
        print("non abstract method")

class Triangle(Polygon):
    def sides(self):
        print("Triangle has 3 sides")
    def hello(self):
        print("hello Triangle")
t = Triangle()
t.sides()
t.display()
t.hello()


