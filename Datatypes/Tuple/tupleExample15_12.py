# print("1. Reverse tuple")
# t= 1,50,25,10
# print(t[::-1])  # reverse
#
# # 2. tup=(1,2,40,30,20) a. access value 20 from tuple
# #  tple = (1,2,40,[10,2,39],(30,20,10)) b. to remove repeated elements from nested tuple
# #
# # a.
# print('\n *****access value 20 from tuple (1,2,40,30,20)***** ')
# tup=(1,2,40,30,20)
# print("tup=(1,2,40,30,20)")
# print(tup[len(tup)-1])
# # b.
# print('\n *****access value 20 from tuple (1,2,40,[10,2,39],(30,20,10),40)***** ')
# tple = (1,2,40,[10,2,39],(30,20,10),40)
# print(tple[len(tple)-2][1])
#
# #c. Remove repeated
# print('\n *****remove repeated items from tuple (1,2,40,[10,2,39],(30,20,10),40)***** ')
# c=[]
# tple = (1,2,40,[10,2,39],(30,20,10),40)
#
# # to remove repeated element 40 and return remaining
# for i in tple:
#     if tple.count(i) == 1:
#         c.append(i)
# print(tuple(c))
#
# # to remove repeated element including that element once
# d=[]
# for i in tple:
#     if i not in d:
#         d.append(i)
# print(tuple(d))


#3 check if all items in the tuple are same
print('\n *****check if all items in the tuple are same***** ')
tup=(1,1,40,30,20)
#tup=(1,1,1,1,1)
# f=1
# for i in tup:
#     for j in range(i,len(tup)-1):
#         if tup[i] != tup[j+1]:
#             f=0
#             break
# if f == 1:
#     print("same")
# else:
#     print("Not same")

#another method
# tup = set(tup)
# if len(tup) == 1:
#     print("same")
# else:
#     print("Not same")

# #4 Copy specific element to one tuple to a new tuple
# print('\n *****Copy specific element to one tuple to a new tuple***** ')
# t=1,2,3,4,"ammu"
# newTple=t[2:5]
# print('newTple =',newTple)
#
#
#
# #5 swap two tuples in Python
# print('\n*****swap two tuples in Python***** ')
tup1=(1,2,40,30,20)
tup2=(1,1,1,1,1)
print(f'Before swap tup1={tup1} and tup2 = {tup2}')
## using temp variable
# temp=tup1
# tup1=tup2
# tup2=temp

## Using tuple of tuple

(tup1,tup2) = (tup2,tup1)

print(f'After swap tup1={tup1} and tup2 = {tup2}')