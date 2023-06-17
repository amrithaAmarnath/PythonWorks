"""
largest number in list without max()

"""
n = int(input("Enter limit : "))

lst = list(map(int, input("Enter the numbers : ").split()))[:n]
l=lst[0]
for i in range(1,len(lst)):
    if(lst[i]>l):
        l=lst[i]
print(l)





