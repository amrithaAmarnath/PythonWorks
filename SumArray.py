"""
2.	Find out a pair of elements which form a particular value as sum from a given array?
For eg: arr=[2,3,4,5,6] print elements having sum=9
o/p :   pairs which give sum=9  is (3,6),(4,5)
"""

arr=[2,3,4,5,6]
l=len(arr)
pairs=[]
s=int(input("enter sum"))

[pairs.append((arr[i],arr[j])) for i in range(l) for j in range(i+1,l) if arr[i]+arr[j] == s ]
print(str(pairs)[1:-1])









# for i in range(l):
#     for j in range(i+1,l):
#         if(arr[i]+arr[j] == s):
#             pairs.append((arr[i],arr[j]))
# print(pairs)