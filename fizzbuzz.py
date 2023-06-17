"""
A number is reading from a user, if num divisible by 3 only print fizz, if number divisible by 5 only or by 3 and 5
print buzz, if number divisible by 15 only or by 3,5,15 it should print fizzbuzz
"""
num = int(input("enter number"))
if num%15 == 0:
    print("fizzbuzz")

elif num%5 == 0:
    print("buzz")

elif num%3 == 0:
    print("fizz")

else:
    print(num)
