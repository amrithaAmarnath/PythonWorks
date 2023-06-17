# 10.Check if all items in the tuple are the same

tup1=tuple(map(int,input("enter tuple  : ").split()))
res=[x == tup1[0] for x in tup1]
print(all(res))


