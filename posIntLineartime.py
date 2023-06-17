"""
Given an arry of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.The array can contain duplicates and
negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

"""
lst=[3, 4,4, -1, 1,-2]

mx=max(lst)
count=0

for i in range(1,mx+1):
    count=count+1
    if i not in lst:
        count=count+1
        print(f'lowest positive integer is {i}')
        break
    else:
        count=count+1
        if i == mx:
            count = count + 1
            print(f'lowest positive integer is {i+1}')

count=count+1
print(count)