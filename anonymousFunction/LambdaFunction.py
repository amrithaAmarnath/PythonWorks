# x = lambda a: a+10
# print(x(5))
#
# x = lambda a,b: a+b
# print(x(5,15))
#
# def myFunc(n):
#     return lambda a:a*n
#
# mydoubler = myFunc(2)
# print(mydoubler(11))

"""
create a fn takes one arg and that arg will multiply by unknown given number

"""
# a=int(input("enter number"))
# n=int(input("enter another number number"))
# multiplier = myFunc(n)
# print(multiplier(a))

"""
filter a list of even integers using lambda

"""
mylist = [12, 65, 54, 39, 102, 339, 221, 50, 70]
#syntax: filter(function, sequence)
even= list(filter(lambda a:(a % 2 == 0),mylist))
print(even)
odd= list(filter(lambda a:(a % 2 != 0),mylist))
print(odd)

#lambda with if else condition
Max = lambda a,b: a if(a>b) else b
print(Max(10,100))

"""
The map() function in Python takes in a function and 
an iterable (lists, tuples, and strings) as arguments.

The function is called with all the items in the list and a new list is
 returned which contains items returned by that function for each item.
"""
# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)

"""
reduce()
Step 1) Perform the defined operation on the first 2 elements of the sequence.

Step 2) Save this result

Step 3) Perform the operation with the saved result and the next element in the sequence.

Step 4) Repeat until no more elements are left.
"""
# Program that returns the product of all elements in a list with reduce()

from functools import reduce
sequences = [1,2,3,4,5]
product = reduce (lambda x, y: x*y, sequences)
print(product)

# subtract the value of each element in a vector with the values form a
# second vector and introduce all the results in a 3rd vector.

v1=[1, 2, 3, 4]
v2 =[7,2 ,7 ,6]
v3=[lambda x,y: abs(x-y) for x,y in zip(v1,v2)]
print(list(v3))