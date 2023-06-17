dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
ascDict = {}
disDict = {}
val = []
val1 = []
key = []
val = list(dict1.values())
val1 = list(dict1.values())
val.sort() # sorted values in ascending order

val1.sort(reverse=True) # sorted values in descending order
key = list(dict1.keys()) # List of keys
for i in val:
    index = list(dict1.values()).index(i)
    ascDict[key[index]] = i

for i in val1:
    index = list(dict1.values()).index(i)
    disDict[key[index]] = i
print("Ascending Dictionary",ascDict.items(), "\n Descending Dictionary",disDict)


#another method
Tup = []
Tupf=[]

Tup= list( dict1.items())
print(Tup)
Tupf = []

for i in Tup:
    print(i)
    Tupf.append(i[::-1])

Tupf.sort()
print(Tupf)




