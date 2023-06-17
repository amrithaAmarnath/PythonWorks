#1. Adding elements to a list using while loop
# n = int(input(" enter limit"))
# My_list = []
# i=1
# while i <= n:
#     My_list.append(i)
#     i += 1
#
# print(My_list)




#2. Average of 5 numbers using while loop

# n=map(int, input().split())
# list1 = list(n)
# #print(list1[2])
# i=0
# sum=0
# while i < 5:
#     sum = sum + list1[i]
#     i += 1
# Avg= sum / 5
# print(f'Sum of 5 no:s is {sum}' )
# print(f'Average of 5 no:s is {Avg}' )

#3. square of numbers using while loop

# n = map(int, input().split())
# list1 = list(n)
# length = len(list1)
# i=0
# while i < length:
#     print(f' {list1[i]}*{list1[i]}={list1[i] * list1[i]}')
#     i += 1

#4. Reversing number

# n= int(input("enter the number"))
# i = 0
# r=0
# while n > 0:
#     r = r*10 + n % 10
#     n = n // 10
#
#     i += 1
# print(f' reverse is {r}')


#5. Sum of even numbers

# n= int(input("enter the limit"))
# i=1
# sum = 0
# while i <= n:
#     if i % 2 == 0:
#         sum=sum+i
#     i += 1
# print(sum)




#6. prime or not
# n= int(input("enter the number"))
# i=2
# f=1
# while i < n//2:
#     if n % i == 0:
#         f=0
#         break
#     i += 1
# if f == 1:
#     print("is prime")
# else:
#     print("not prime")

#7.print even and odd numbers from 1 to limit
n= int(input("enter the limit"))
i=1
even=[]
odd=[]
while i <=n:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
    i += 1
print(f'even numbers = {even}')
print(f'odd numbers = {odd}')










