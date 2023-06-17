# 1.Write a Python program to access a function inside a function

# def outerfn(a):  # outer function
#
#     def add(b): # inner function add with parameter from outer function ie b=a
#         nonlocal a
#         a += 1
#         return a + b
#
#     return add
#
#
# func = outerfn(5)  # argument passed to fn = 1  this function is provided to inner function
# print(func(2))

# 2. square of numbers from 1 to 30

# def squares():
#     sq = []
#     for i in range(1, 30):
#         sq.append(i ** 2)
#     return sq
#
# print(squares())

# 3 assign new name to function
# def foo(name):
#     print('Hello',name)
#
# new_foo = foo
# new_foo('ammu')


# 4 Generate a Python list of all the even numbers between 4 to 30
# def even():
#     print(list(range(4,30,2)))
# even()

# 5 Python function that accepts two numbers as arguments and returns the sum

# def sum(a,b):
#     return a+b
#
#
# a = int(input("enter first number"))
# b = int(input("enter second number"))
# print(sum(a,b))


# 6. accept different values as parameters and return a list
# def listcreater(a, b):
#     return list(range(a, b))
#
#
# print(listcreater(1, 10))


# 7. Python function that returns a tuple
# def tuplecreater(a, b):
#     return tuple(range(a, b))
#
#
# print(tuplecreater(1, 10))


# 8 Define a function that accepts 2 values and return its sum,
# subtraction and multiplication.

# def calc(a,b):
#     return a+b,a-b,a*b
# s,d,m = calc(4,4)
# print(s,d,m)

# Another method:

# def sum(a, b):
#     return a + b
# def sub(a, b):
#     return a - b
# def mult(a,b):
#     return a*b
#
# def calc(func, a, b):
#     return func(a, b)
#
# result = calc(sum, 4, 4)
# print(f'sum of 4 and 4 ={result}')
# result = calc(sub, 4, 4)
# print(f'subraction of 5 and 3 ={result}')
# result = calc(mult, 4, 4)
# print(f'multiplication of 5 and 3 ={result}')

# 8. Define a function that accepts roll number and returns whether the student
# is present or absent
# def attendence(rollno):
#     present=[1,2,3,5,6,7,8,10,12,13]
#     if rollno in present:
#         return "Present"
#     else:
#         return "Absent"
#
# print(attendence(10))
#

#10.Define a function which counts vowels and consonant in a word

# def counter(word):
#     v = ['a','e','i','o','u','A','E','I','O','U']
#     vow=0
#     cons=0
#     for i in word:
#         if i in v:
#             vow += 1
#         else:
#             cons +=1
#
#     print(f'no of vowels {vow}')
#     print(f'no of consonants {cons}')
#
#
# word = input("enter a word")
# counter(word)

# 11.Define a function that accepts a number and returns whether the number
# is even or odd.



# 12.Define a function in python that accepts 3 values and returns the maximum
# of three numbers

# def maximum(a,b,c):
#     return max(a,b,c)
#
# a=int(input("enter first number"))
# b=int(input("enter second number"))
# c=int(input("enter third number"))
# print(f'maximum ={maximum(a,b,c)}')
