#1. Multiply all the numbers in a list using function


# def product_list(lst):
#     p = 1
#     for i in lst:
#         p *= i
#     return p
# lst = [1, 2, 3, 4, 5, 6]
# print(f' product of list items is {product_list(lst)}')










#
#
# #  2.Write a Python program to reverse a string.


# Sample String: "1234abcd"
# Expected Output: "dcba4321"



# def stringRev(st):
#     return st[::-1]
#
# print(stringRev("1234abcd"))








# # 3 Write a Python function to calculate the factorial of a number
# # (a non-negative integer). The function accepts the number as an argument.
#

# def fact(n):
#     if n == 1:
#         return n
#     else:
#         return n*fact(n-1)
#
# n=int(input("enter a number to find factorial"))
# # check if the number is negative
# if n < 0:
#    print("Factorial does not exist for negative numbers")
# elif n == 0:
#    print("The factorial of 0 is 1")
# else:
#    print("The factorial of", n, "is", fact(n))




# # 4. Write a Python function that takes a number as a parameter and check
# # the number is prime or not
#
def prime(n):
    if n == 1:
        return "neither prime nor composite"
    p=""
    for i in range(1, (n // 2)+1):
        if n%i == 0 and i != 1:
             p="is not prime"
             break
        else:
             p="is prime"
    return p

n=int(input("enter a number to check prime"))
print(prime(n))





# 5. Create an inner function to calculate the addition in the following way
# •	Create an outer function that will accept two parameters, a and b
# •	Create an inner function inside an outer function that will calculate
# the addition of a and b
# •	At last, an outer function will add 5 into addition and return it
#


# def outerFn(a,b):
#     def innerFn(a, b):
#         return a+b
#     return 5 + innerFn(a,b)
#
# a= int(input("enter first number "))
# b= int(input("enter second number "))
# print(outerFn(a,b))

#    6. Generate a Python list of all the even numbers between 4 to 30
# Expected o/p:
# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
# [HINT]:
# •	Use the built-in function range() to generate the sequence of numbers between
# the given start number to the stop number with a step = 2 to get even numbers.
# •	pass range() function to a list constructor to create a list

# def create_list(a,b):
#     r = range(a,b,2)
#     return list(r)
#
#
# print(create_list(4, 30))





