#Multipication table using recursion
def multiplicationTable(n, i):
    if(i>10):
        return
    print(n, "*", i, "=", n*i)
    return multiplicationTable(n, i+1)

print("Enter the Number: ")
num = int(input())
print("\nMultipication Table of", num, "is:")
multiplicationTable(num, 1)

