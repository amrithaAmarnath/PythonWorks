#1. Diamond pattern
# r = int(input("Enter the number : "))
# #upper part
# for i in range(r+1):
#     for j in range(r-i):
#         print(" ",end = " ")
#     for j in range(i+1):
#         print(" * ",end = " ")
#     print()
# #lower part
# for i in range(r ):
#         for j in range(i+1):
#             print(" ", end=" ")
#         for j in range(r - i):
#             print(" * ", end=" ")
#         print()

# 2. inverted upper part and lower part
# r = int(input("Enter the number : "))
#
# #upper part
#
# for i in range(r):
#     for j in range(i):
#         print(" ",end = "")
#     for j in range(r-i):
#         print("*" , end=" ")
#     print()
#
# #lower part
# for i in range(r):
#     for j in range(r-i-1):
#         print(" ",end = "")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

#3. Hollow Diamond Pattern:
r = int(input("Enter the number: "))
# upper part
for i in range(r+1):
    for j in range(r-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        if j == 1 or j == 2*i-1:
            print("*",end=" ")
        else:
            print(" ",end = " ")
    print()

#lower part

# for i in range(r-1,0,-1):
#     for j in range(1, r-i+1):
#         print(" ", end=" ")
#     for j in range(1, 2*i):
#         if j == 1 or j == 2*i-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


#4. Inverted full pyramid

# r=int(input("enter no of rows"))
#
# for i in range(r+1):
#         print(" "*i+"* "*(r-i))
# print()

#5. Half pyramid using no:s
# r=int(input("enter no of rows"))
#
# for i in range(1,r+1):
#     for j in range(i):
#         print(j+1, end = " ")
#     print()

#6. Reverse pattern from 5 to 1

# r=5
# for i in range(1,r+1):
#     for j in range(r-i+1,0,-1):
#       print(j,end="")
#     print()











