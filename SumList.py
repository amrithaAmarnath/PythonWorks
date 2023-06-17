"""
sum of elements in a list
"""
from functools import reduce
n = int(input("Enter limit : "))

# Below line read inputs from user using map() function
lst = list(map(int, input("Enter the numbers : ").split()))[:n]
s=reduce(lambda x,y:x+y , lst)
print('sum= ',s)

