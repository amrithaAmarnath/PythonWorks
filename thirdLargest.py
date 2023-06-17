"""
11.	Write a Python program to find the third largest number from a given list of numbers.
"""
lst=[1,5,4,2,6,25,15,10]

lst.sort()
res=lst[-3:-2]
print("Third largest:",str(res)[1:-1])