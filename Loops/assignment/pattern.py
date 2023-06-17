#Half pyramid using no:s
# r=int(input("enter no of rows"))
#
# for i in range(1,r+1):
#   #  print(i)
#     for j in range(i):
#
#     #    print(j)
#         print(j+1, end = " ")
#     print()


# 3. Full pyramid
n=int(input("enter no of rows"))

for i in range(n): #rows
    for s in range(n-i-1): #space 5-0-1=4
        print(" ",end="")
    for j in range(i+1): #column
        print("*",end=" ")
    print()


# #2. inverted pyramid using no:s

# r=int(input("enter no of rows")) #user input
# for i in range(0,r+1): #row
#     for j in range(r-i,0,-1): # column
#         print(j,end = " ")
#     print()
