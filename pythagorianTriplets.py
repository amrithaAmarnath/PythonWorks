"""
Write a python progarm to print the count of pythagorian triplets from an array of integers.
Like, an array is given, it should give (a,b,c)'s count if a**2 + b**2 = c**2 if present in the array
"""

def pythagorean_triplets_count(arr):
    sq = [x ** 2 for x in arr]
    count = 0
    for i in range(len(sq)):
        for j in range(i + 1, len(sq)):

            if (sq[i] + sq[j]) in sq:
                count += 1

    return count


lst = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("pythagorean_triplets count is : ",pythagorean_triplets_count(lst))




#Another method
# lst=[1,2,5,3,4,6,8,10]
# def count_pythagorean_triplets(arr):
#     count = 0
#     n = len(arr)
#     for i in range(n):
#         for j in range(i+1, n):
#             for k in range(j+1, n):
#                 if arr[i]**2 + arr[j]**2 == arr[k]**2 or arr[i]**2 + arr[k]**2 == arr[j]**2 or arr[j]**2 + arr[k]**2 == arr[i]**2:
#                     count += 1
#     return count


# lst=[3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15]
# #print(count_pythagorean_triplets(lst))
# sq=[x**2 for x in lst ]
# c=0
# for i in range(len(sq)):
#     for j in range(i+1,len(sq)):
#
#         if (sq[i]+sq[j]) in sq:
#             c += 1
#
# print(c)
#


