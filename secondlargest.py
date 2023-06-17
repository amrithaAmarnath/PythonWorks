"""Write a python program to find the second-largest element from a list without using any built-in functions."""
#Method 1
lst=[5,0,1,5,2,6,6,8,8]
s=set()
for i in lst:
    s.add(i)
if len(lst) > 1:
    print(f'Method 1: second largest number is {list(s)[-2]}')
else:
    print("There is no second largest number.")

# Method2
lst=[5,0,1,5,2,6,6,8,8]
lg=lst[0]
sec_lg = lst[0]
for i in range(len(lst)):
    if lst[i] > lg:
        sec_lg=lg
        lg = lst[i]
    elif lst[i] > sec_lg and lst[i] != lg:
        sec_lg=lst[i]
if len(lst) > 1:
    print(f'Method 2: second largest number is {sec_lg}')
else:
    print("There is no second largest number.")
#Method3
# lst = [5,0,1,5,2,6,6,8,8]
# lst = sorted(set(lst), reverse=True)
# print(lst)
# if len(lst) > 1:
#     print(f"The second largest number is {lst[1]}")
# else:
#     print("There is no second largest number.")
