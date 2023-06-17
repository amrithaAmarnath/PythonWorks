r=6
for i in range(0,r):
    for j in range(r-i-1):
        print(" ",end=" ")
    for j in range(1,2*i):
        if j == 1 or j == 2*i-1 or (i == (r // 2) and j < 2*i-1) :
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()
