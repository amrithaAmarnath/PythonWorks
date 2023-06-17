#set Datatype
"""
-denoted by {}
-immutable
-unorederd
-unindexed
-not allow dupicates
-can remove or add new items even though set is unchangable
-alllow mixed datatypes

"""




myset = {"apple", "banana", "cherry"}
print(myset)
#empty set
a = set()
print(a)
#myset1 = {1.0,2,4,(33,24),[1,2,3]} # TypeError: unhashable type: 'list'
#myset1 = {1.0,2,4,(33,24)}
myset1 = set(["apple", "banana", "cherry"])
print(myset1)

A = {1,2,3,4,5,6}
B = {5,6,7,8,9,10}
u= A|B
print("Union = ",u)
i = A&B
print("Intersection = ",i)
d= A-B
print("Difference = ", d)
d= B-A
print(d)
sd = A ^ B
print("Symmetric differnce = ",sd)

