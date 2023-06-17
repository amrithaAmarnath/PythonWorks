"""
Recursive Function
-  adefined fn calling itself


"""
# sum of N natural numbers

# def getsum(k):
#     if k <= 0:   #set base condition
#         return 0
#     else:
#         return k + getsum(k-1)
#
#
# print(getsum(6))
#
# # Factorial of a given number
#
# def fact(n):
#     if n == 1:  #set base condition to stop the recursive execution
#         return n
#     else:
#         return n * fact(n-1)
#               # 5*4*3*2*1   # each data is saved in stack. operation of stack is Last in First out
#
# num= int(input("enter a number"))
# if num < 0:
#     print("invalid")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     print(f'Factorial of {num} is {fact(num)}')
#

# Fibonacci series

def fib(n):
    if n <= 1:  #set base condition
        return n
    else:
        return(fib(n-1)+fib(n-2))

limit = 5
for i in range(limit):
       print(fib(i))