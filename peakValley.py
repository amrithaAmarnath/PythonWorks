"""
write a python program to  count elements which are either peak or valley from a given list.
Input : lst = [1, 2, 4, 2, 6, 7, 8, 3]
Output : 3
Input : lst = [1, 2, 4, 5, 3, 2]
Output : 1
"""


def peak_valley(lst):
    c = 0
    for i in range(1, len(lst) - 1):
        if lst[i - 1] < lst[i] > lst[i + 1] or lst[i - 1] > lst[i] < lst[i + 1]:
            c += 1
    return c


ls = [1, 2, 4, 2, 6, 7, 8, 3]
print(f'\n for lst = {ls}, Peak Valley count = {peak_valley(ls)}')
ls1 = [1, 2, 4, 5, 3, 2]
print(f'\n for lst = {ls1}, Peak Valley count = {peak_valley(ls1)}')
