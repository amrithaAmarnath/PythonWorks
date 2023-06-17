#WAP to Print all numbers in a range divisible by a given number
#lower = int(input("Enter lower range limit"))
#upper =
n= int(input("Enter number to be divided by"))
l=[x for x in range(int(input("Enter lower range limit")),int(input("Enter upper range limit"))+1) if x%n == 0]
print(l)