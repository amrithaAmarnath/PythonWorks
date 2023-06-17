# sum of cube of digits of a number is the number itself
num = int(input("enter a number"))
str1 = str(num)
sum = 0
for i in str1:
   sum = sum + int(i) ** 3

print(sum)
if sum == num:
    print("is Amstrong number")
else:
    print("not an Amstrong number")



