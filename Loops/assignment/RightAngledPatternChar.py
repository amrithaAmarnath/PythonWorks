r=6
n=26
k=1
for i in range (r+1):
    for j in range(i):
        ch = chr(64 + k)
        print(ch, end=" ")
        k += 1
    print()



