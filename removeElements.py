#7.	 Write a python program to remove repeated elements from a given list without using built-in methods
lst = [1, 2, 3, 4,5,5,1,2]

l1=[]
[l1.append(i) for i in lst if i not in l1]
print(l1)



# lnew=[]
# for i in lst:
#     if i not in lnew:
#         lnew.append(i)
#
# print(lnew)




