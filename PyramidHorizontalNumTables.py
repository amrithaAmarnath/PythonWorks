#Pyramid of Horizomntal Number table

n=int(input("enter limit"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()
