# for row in range(6):
#     for col in range(7):
#         if (row==0 and col % 3 !=0)or(row==1 and col %3==0) or(row-col==2) or(row+col==8):
#             print("*",end=" ")
#         else:
#             print(end=" ")
#     print()

num= int(input("Enter a number"))
half = round(num/2)

for i in range(2, half):
    print(" "*(half-i-1)+"*"*(2*i+1)+"  "*(half-i)+"*"*(2*i+1))
for i in range(num,0,-1):
    print(" "*(num-i)+"*"*(2*i-1))
