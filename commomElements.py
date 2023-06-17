l1=[3,2,5,7,6,4]
l2=[2,4,7,8,9]
l3=[]
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i] == l2[j]:
            l3.append(l1[i])
if len(l3) == 0:
    print("no common elements")
else :
    print(" common elements ",l3)