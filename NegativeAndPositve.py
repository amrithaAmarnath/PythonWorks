"""
1.Separate Negative and positive number from list

"""

# number of elements
n = int(input("Enter limits : "))

# Below line read inputs from user using map() function
l = list(map(int, input("Enter the numbers : ").strip().split()))[:n]

print("List is - ", l)
neg=[]
pos=[]
for x in l:
    if x < 0: neg.append(x)
    else: pos.append(x)
print(f'positive numbers : {pos} \nnegative numbers : {neg}')



