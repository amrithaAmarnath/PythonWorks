num=10
n=num//2
#upper part > 2 full pyramid side by side

for i in range(2,n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    if num %2 == 0:
        for j in range(2*(n-i-1)-1):
            print(" ", end=" ")
    for j in range(2*(n-i-1)-1):
        print(" ", end=" ")
    for j in range(i+1):
        print("* ",end="")
    print()


