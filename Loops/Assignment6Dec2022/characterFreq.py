str1 = input("enter string")
str1 = "".join(str1.split())
c=0
ls=[]
count=[]
for i in str1:
    if i not in ls:
        c = str1.count(i)
        ls.append(i)
       # count.append(str1.count(i))
        print(f' {i} : {c}')

#print(f' frequency of {ls} is {count}')