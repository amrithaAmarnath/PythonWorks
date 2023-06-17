SampleData = [{"item": "item1", "amount": 400},
              {"item": "item2", "amount": 300},
              {"item": "item1", "amount": 750}]
print(SampleData)
itemDict = {}

for i in SampleData:
    a = list(i.values())
  #  print(f'a= {a}')
    if a[0] not in itemDict:
        itemDict[a[0]] = a[1]
    else:
        v = itemDict[a[0]]
        itemDict[a[0]] = v+a[1]
print(itemDict)

# method 2

lst = {}
for i in SampleData:
    if i['item'] not in lst:
        lst[i['item']] = i['amount']
    else:
        lst[i['item']] += i['amount']

print(lst)



# another method Need to check
# newDict = {}
# list1 = []
# for d in SampleData:
#     p = list(d.values())  # create list of values
#     list1.append(p[0])
#     list1.append(p[1])  # list1 contains all individual values
# print(list1)
# print(len(list1))
# for i in range(1, len(list1), 2): #take each second item in list1
#     print(i)
#     for list1[i] in newDict:
#         rep = list[i]
#         print(rep)
#         index = list1.index(i)  # find index of repeated variable
#         list1[index+1] = list1[index+1] + list1[i+1]
#         print(list1)
#         newDict[list1[i]] = list1[i+1]  # updating value of repeated values
#     else:
#         newDict.setdefault(list1[i], list[i+1])
#
# #print(newDict)