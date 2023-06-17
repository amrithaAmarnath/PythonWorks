"""Write a pyhton program to return a list , having elements whicha are product of all the other elements
except the element in that particular position
if the given list Ex: i/p   lst=[1,2,3] o/p    lst=[6,3,2]
"""


def product(lst1):
    ls = []
    l=len(lst1)
    for i in range(l):
        p=1
        for j in range(l):
            if j!=i:
                p = p * lst1[j]

        ls.append(p)
    return ls

lst = [1, 2, 3]
print(f'original List: {lst}')
l_new = product(lst)
print(f' new list: {l_new}')

    # for i in lst1:
    #     p=1
    #     ind = lst1.index(i)
    #     for j in lst:
    #         if lst1.index(j) != ind:
    #             p = p * j
    #     ls.append(p)
    #return ls
#
# lst = [1, 2, 3]
# print(f'original List: {lst}')
# l_new = product(lst)
# print(f' new list: {l_new}')
