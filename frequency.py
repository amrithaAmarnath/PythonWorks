"""
Write a python program to print the frequency of each element in a given list
ex: [1,2,7,7,7,8,2,2,1,1,1]
o/p: frequencies are
  '1': 4 times
  '2': 3 times
  '7': 3 times
  '8':  times
"""

ls=[1,2,7,7,7,8,2,2,1,1,1]
fq={}
for i in ls:
    if i in fq:
        fq[i] += 1
    else:
        fq[i] = 1
print(f' frequencies are: ')
for key,value in fq.items():
    print(f" '{ key}' : {value} times  ")


#another method
# ls=[1,2,7,7,7,8,2,2,1,1,1]
# l=set()
# c=0
# for i in range(len(ls)):
#     c=0
#     for j in range(len(ls)):
#         if ls[i] == ls[j]:
#             c += 1
#     if ls[i] not in l:
#       print(f" '{ ls[i]}' : {c} times  ")
#       l.add(ls[i])


#Another method
# from collections import Counter
#
# lst = [1,2,7,7,7,8,2,2,1,1,1]
#
# count = Counter(lst)
#
# for element, frequency in count.items():
#     print(f"{element}: {frequency}")
