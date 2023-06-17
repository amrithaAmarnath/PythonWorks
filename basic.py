class Emp:
    x=100
    def display(self): # function inside class has self argument as first argument
        print("Simple function")

    def sum(self):  # function inside class has self argument as first argument
        print("Sum is ",30+40)
    def sum1(self,a,b):  # function inside class has self argument as first argument
        print("Sum is ",a+b)
    def product(se,a,b):  # function inside class has self argument as first argument
        print("Sum is ",a*b)
    def disp(): #def function without self argument
        print('Without self arguments')

    """
    Self arg to use the varaiables in one method 
    in class in another method in the same class.

    -Usually varaiable without self is private to the function that
     declared it


    """

    def read(self, a, b):
        self.x = a
        self.y = b
        self.a = a
        self.b = b

    def sum2(self):
        print("sum is ",self.x+self.y)

    def difference(self):
        print("difference is ", self.a - self.b)

    def product1(c):
        print("product with self variable is ", c.x * c.y)

obj = Emp()
obj.display()
print('value of x is ',obj.x)
obj.sum()
obj.sum1(30,40)
obj.product(3,4)
obj.read(5,4)
obj.sum2()
obj.product1()
obj.difference()





"""
To call function without self arg in class 
-create an obj using classname without function parameter
-rarely used
"""
obj = Emp
obj.disp()





