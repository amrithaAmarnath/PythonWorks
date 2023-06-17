r=6
n=26
k=1
for i in range(6): #rows
    for s in range(n-i-1): #space 5-0-1=4
        print(" ",end="")
    for j in range(i+1): #column
        ch = chr(64 + k)
        print(ch,end=" ")
        k += 1
    print()
